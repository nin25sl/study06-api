import requests
import urllib
import pandas as pd


def get_api(url):
    result = requests.get(url)
    return result.json()

def rank_api_out(keyword):
    #ランキングのtop3をpdfに出力
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}%8B&genreId=555086&hits=3&applicationId=1084281404186677141".format(keyword)
    req_res = get_api(url)
    item_list = []
    temp_key_list = ["mediumImageUrls","pointRate","shopOfTheYearFlag","affiliateRate","shipOverseasFlag","asurakuFlag","endTime","taxFlag","startTime","itemCaption","catchcopy","tagIds","smallImageUrls","asurakuClosingTime","imageFlag","availability","shopAffiliateUrl","itemCode","postageFlag","itemName","itemPrice","pointRateEndTime","shopCode","affiliateUrl","giftFlag","shopName","reviewCount","asurakuArea","shopUrl","creditCardFlag","reviewAverage","shipOverseasArea","genreId","pointRateStartTime","itemUrl"]
    dict_key_list = ["itemName", "shopName" ,"itemPrice","reviewAverage", "itemUrl", "mediumImageUrls"]

    for i in range(0, len(req_res['Items'])):
        tmp_item = {}
        item = req_res['Items'][i]['Item']
        #各要素のキーkeyと値valueの両方に対してforループ処理を行いたい場合は、items()メソッドを使う。
        # for key, value in item.items():
        #     for i in range(0 ,len(key)):
        #         if dict_key_list[i] in key:
        #             tmp_item[key] = value
        #リスト順に結果を取得
        for key in dict_key_list:
            if key in item.keys():
                tmp_item[key] = item[key]

        item_list.append(tmp_item)

    df = pd.DataFrame(item_list)
    df.to_csv('./proc.csv')

def main():
    keyword = input("調べたい単語を入力してください>>> ")
    #url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(keyword)
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&keyword={}&minPrice=1&maxPrice=1&applicationId=1084281404186677141".format(keyword)
    rank_api_out(keyword)
    #print(get_api(url))

main()
