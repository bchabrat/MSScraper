from get_funds_ids import *
from scrapingtop10 import *
from proxy import get_proxies
import time

with open('category_ids') as json_file:
    categories = json.load(json_file)

list_proxies = "52.175.120.142:8080"

for category in categories:
    if "Income" in category['name']:
        print("working on category: " + category['name'])
        if(category['id']!="EUCA000876"):
            funds = get_funds_ids(category['id'])
            scrapingtop10(category['id'], list_proxies, funds)


#
#
# def get_text(bsObject):
#     return bsObject.get_text()
#
#
# with open('data.txt') as json_file:
#     funds_list = json.load(json_file)
#
# names = []
# ids = []
# for fund in funds_list:
#     if type(fund) is list:
#         for subfund in fund:
#             ids.append(subfund['SecId'])
#             names.append(subfund['Name'])
#     else:
#         ids.append(fund['SecId'])
#         names.append(fund['Name'])
#
# funds_ids = dict(zip(ids, names))
# final_data = pd.DataFrame(columns=['fund', 'stock', 'percentage'])
# i = 0
# for fund_id, fund_name in funds_ids.items():
#     page = requests.get('https://www.morningstar.co.uk/uk/funds/snapshot/snapshot.aspx?id=' + fund_id)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     try:
#         print("working on " + fund_name + ". Loop number: " + str(i))
#         topHoldingTable = soup.find(class_="snapshotTextColor snapshotTextFontStyle snapshotTable overviewTopHoldingsTable")
#         top5Holdings_stocks = map(get_text, list(topHoldingTable.find_all(class_="holdingLink")))
#         top5Holdings_percentage = map(get_text, list(topHoldingTable.find_all(class_="col3 value number")))
#         top5Holdings = dict(zip(top5Holdings_stocks, top5Holdings_percentage))
#         print(fund_name + ". Loop number: " + str(i) + "done!")
#         print('......')
#     except AttributeError as err:
#         print("Runtime error occured: ",err)
#     for stock, percentage in top5Holdings.items():
#         final_data.loc[i] = [fund_name, stock, percentage]
#         i += 1
#     time.sleep(10)
#
# final_data.to_csv("final_data.csv")
