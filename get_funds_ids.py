import requests
import json
import pandas as pd
import asyncio


def get_funds_ids(category_id):
    page = 1
    print("getting a list of funds for: " + category_id)
    list_of_funds = []
    funds_url = 'https://lt.morningstar.com/api/rest.svc/klr5zyak8x/security/screener?page=' + str(page) + \
                 '&pageSize=50&sortOrder=LegalName%20asc&outputType=json&version=1&languageId=en-GB&currencyId=GBP'+\
                 '&universeIds=FOGBR%24%24ALL&securityDataPoints=SecId%7CName%7CPriceCurrency%7CTenforeId%7CLegalName'+ \
                 '%7CClosePrice%7CStarRatingM255%7CSustainabilityRank%7CQuantitativeRating%7CAnalystRatingScale%7'+ \
                 'CCategoryName%7CYield_M12%7CGBRReturnD1%7CGBRReturnW1%7CGBRReturnM1%7CGBRReturnM3%7CGBRReturnM6%7CGBR'+\
                 'ReturnM0%7CGBRReturnM12%7CGBRReturnM36%7CGBRReturnM60%7CGBRReturnM120%7CMaxFrontEndLoad%7COngoingCostActual'+\
                 '%7CPerformanceFeeActual%7CTransactionFeeActual%7CMaximumExitCostAcquired%7CFeeLevel%7CManagerTenure%7CMax'+\
                 'DeferredLoad%7CInitialPurchase%7CFundTNAV%7CEquityStyleBox%7CBondStyleBox%7CAverageMarketCapital%7CAverage'+\
                 'CreditQualityCode%7CEffectiveDuration%7CMorningstarRiskM255%7CAlphaM36%7CBetaM36%7CR2M36%7CStandardDeviati'+\
                 'onM36%7CSharpeM36%7CInvestorTypeRetail%7CInvestorTypeProfessional%7CInvestorTypeEligibleCounterparty%7CE'+\
                 'xpertiseBasic%7CExpertiseAdvanced%7CExpertiseInformed%7CReturnProfilePreservation%7CReturnProfileGrowth%'+\
                 '7CReturnProfileIncome%7CReturnProfileHedging%7CReturnProfileOther%7CTrackRecordExtension&filters=Categ'+\
                 'oryId%3AIN%3A' + category_id + '%7CStarRatingM255%3AIN%3A4%3A5&term=&subUniverseId='

    page_list_funds = requests.get(funds_url)
    page_list_funds_json = page_list_funds.json()
    number_of_loops = page_list_funds_json['total'] // page_list_funds_json['pageSize'] + 1
    for row in page_list_funds_json['rows']:
        if type(row) is list:
            for subrow in row:
                list_of_funds.append({"id": subrow['SecId'], "name": subrow['Name']})
        else:
            list_of_funds.append({"id": row['SecId'], "name": row['Name']})

    for i in range(2, number_of_loops+1):
        page = i
        funds_url = 'https://lt.morningstar.com/api/rest.svc/klr5zyak8x/security/screener?page=' + str(page) + \
                    '&pageSize=50&sortOrder=LegalName%20asc&outputType=json&version=1&languageId=en-GB&currencyId=GBP' + \
                    '&universeIds=FOGBR%24%24ALL&securityDataPoints=SecId%7CName%7CPriceCurrency%7CTenforeId%7CLegalName' + \
                    '%7CClosePrice%7CStarRatingM255%7CSustainabilityRank%7CQuantitativeRating%7CAnalystRatingScale%7' + \
                    'CCategoryName%7CYield_M12%7CGBRReturnD1%7CGBRReturnW1%7CGBRReturnM1%7CGBRReturnM3%7CGBRReturnM6%7CGBR' + \
                    'ReturnM0%7CGBRReturnM12%7CGBRReturnM36%7CGBRReturnM60%7CGBRReturnM120%7CMaxFrontEndLoad%7COngoingCostActual' + \
                    '%7CPerformanceFeeActual%7CTransactionFeeActual%7CMaximumExitCostAcquired%7CFeeLevel%7CManagerTenure%7CMax' + \
                    'DeferredLoad%7CInitialPurchase%7CFundTNAV%7CEquityStyleBox%7CBondStyleBox%7CAverageMarketCapital%7CAverage' + \
                    'CreditQualityCode%7CEffectiveDuration%7CMorningstarRiskM255%7CAlphaM36%7CBetaM36%7CR2M36%7CStandardDeviati' + \
                    'onM36%7CSharpeM36%7CInvestorTypeRetail%7CInvestorTypeProfessional%7CInvestorTypeEligibleCounterparty%7CE' + \
                    'xpertiseBasic%7CExpertiseAdvanced%7CExpertiseInformed%7CReturnProfilePreservation%7CReturnProfileGrowth%' + \
                    '7CReturnProfileIncome%7CReturnProfileHedging%7CReturnProfileOther%7CTrackRecordExtension&filters=Categ' + \
                    'oryId%3AIN%3A' + category_id + '%7CStarRatingM255%3AIN%3A4%3A5&term=&subUniverseId='
        page_list_funds = requests.get(funds_url)
        page_list_funds_json = page_list_funds.json()
        for row in page_list_funds_json['rows']:
            if type(row) is list:
                for subrow in row:
                    list_of_funds.append({"id": subrow['SecId'], "name": subrow['Name']})
            else:
                list_of_funds.append({"id": row['SecId'], "name": row['Name']})

    df = pd.DataFrame(list_of_funds)
    df.to_csv("./fundsByCategory/cat"+category_id)
    return list_of_funds


