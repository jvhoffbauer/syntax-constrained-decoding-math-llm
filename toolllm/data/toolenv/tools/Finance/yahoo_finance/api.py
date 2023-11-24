import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def stock_v2_get_financials(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Income Statement data in  Financials section
		* If you want to get Quarterly data, you need to use .../stock/v2/get-timeseries endpoint instead."
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_statistics_deprecating(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Statistics section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_newsfeed_deprecated(category: str, start_uuid: str=None, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		Get general latest newsfeed or specific newsfeed by symbol"
    category: Pass "generalnews" to get general latest newsfeed or a specific symbol
        start_uuid: The uuid of first newsfeed in a list (max 10 newsfeed per request), pass empty to load the first 10 latest newsfeed.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-newsfeed"
    querystring = {'category': category, }
    if start_uuid:
        querystring['start_uuid'] = start_uuid
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_histories_deprecated(symbol: str, is_from: str, events: str, to: str, interval: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		Get stock histories to draw chart"
    symbol: The value of symbol field returned in .../auto-complete endpoint
        from: Epoch timestamp in seconds, must be different from 'to', and the value must be starting of a day to get whole data in day.
        events: Pass this param multiple times to get more related events (div|split|earn), such as : &events=div&events=split&events=earn
        to: Epoch timestamp in seconds, must be different from 'from', and the value must be starting of the later day to get whole data all previous days.
        interval: Allowed values are (1d|5d|1mo|3mo|6mo|1y|2y|5y|max)
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"
    querystring = {'symbol': symbol, 'from': is_from, 'events': events, 'to': to, 'interval': interval, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_fees_and_expenses(symbol: str, lang: str='en-US', region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get fees and expenses related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-fees-and-expenses"
    querystring = {'symbol': symbol, }
    if lang:
        querystring['lang'] = lang
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_top_holdings(symbol: str, straddle: bool=None, lang: str='en-US', region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get top holdings related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-top-holdings"
    querystring = {'symbol': symbol, }
    if straddle:
        querystring['straddle'] = straddle
    if lang:
        querystring['lang'] = lang
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v3_get_holders(symbol: str, straddle: bool=None, region: str='US', lang: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get holders related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-holders"
    querystring = {'symbol': symbol, }
    if straddle:
        querystring['straddle'] = straddle
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_balance_sheet(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Balance Sheet tab in Financials section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-balance-sheet"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v4_get_statistics(symbol: str, lang: str='en-US', region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get statistics related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v4/get-statistics"
    querystring = {'symbol': symbol, }
    if lang:
        querystring['lang'] = lang
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_upgrades_downgrades(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get upgrades and downgrades data"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-upgrades-downgrades"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_summary(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Summary section"
    symbol: The value of symbol field returned in .../auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v3_get_insights(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get brief reports relating to a symbol"
    symbol: The value of symbol field returned in .../auto-complete endpoint
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-insights"
    querystring = {'symbol': symbol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_timeseries(symbol: str, period1: int, period2: str, region: str='US', type: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get more data in Financials section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        period1: Epoch timestamp in seconds (ex : 493578000), must be different from period2, and the value must be starting of a day to get whole data in day.
        period2: Epoch timestamp in seconds (ex : 1571590800), must be different from period1, and the value must be starting of next day to get whole data in previous day.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        type: Specify returned fields, one of the following is allowed (Separated by comma for multiple values, ex : ...&type=quarterlyEbitda,trailingEbitda,quarterlyWeighteAverageShare,...) : annualAdjustedGeographySegmentData|annualAmortizationCashFlow|annualAmortizationOfIntangibles|annualAmortizationOfSecurities|annualAssetImpairmentCharge|annualBeginningCashPosition|annualCapitalExpenditure|annualCapitalExpenditureReported|annualCashDividendsPaid|annualCashFlowFromContinuingFinancingActivities|annualCashFlowFromContinuingInvestingActivities|annualCashFlowFromContinuingOperatingActivities|annualCashFlowFromDiscontinuedOperation|annualCashFlowsfromusedinOperatingActivitiesDirect|annualCashFromDiscontinuedFinancingActivities|annualCashFromDiscontinuedInvestingActivities|annualCashFromDiscontinuedOperatingActivities|annualChangeInAccountPayable|annualChangeInAccruedExpense|annualChangeInDividendPayable|annualChangeInIncomeTaxPayable|annualChangeInInterestPayable|annualChangeInInventory|annualChangeInOtherCurrentAssets|annualChangeInOtherCurrentLiabilities|annualChangeInOtherWorkingCapital|annualChangeInPayable|annualChangeInPayablesAndAccruedExpense|annualChangeInPrepaidAssets|annualChangeInReceivables|annualChangeInTaxPayable|annualChangeInWorkingCapital|annualChangesInAccountReceivables|annualChangesInCash|annualClassesofCashPayments|annualClassesofCashReceiptsfromOperatingActivities|annualCommonStockDividendPaid|annualCommonStockIssuance|annualCommonStockPayments|annualDeferredIncomeTax|annualDeferredTax|annualDepletion|annualDepreciation|annualDepreciationAmortizationDepletion|annualDepreciationAndAmortization|annualDividendPaidCFO|annualDividendReceivedCFO|annualDividendsPaidDirect|annualDividendsReceivedCFI|annualDividendsReceivedDirect|annualDomesticSales|annualEarningsLossesFromEquityInvestments|annualEffectOfExchangeRateChanges|annualEndCashPosition|annualExcessTaxBenefitFromStockBasedCompensation|annualFinancingCashFlow|annualForeignSales|annualFreeCashFlow|annualGainLossOnInvestmentSecurities|annualGainLossOnSaleOfBusiness|annualGainLossOnSaleOfPPE|annualIncomeTaxPaidSupplementalData|annualInterestPaidCFF|annualInterestPaidCFO|annualInterestPaidDirect|annualInterestPaidSupplementalData|annualInterestReceivedCFI|annualInterestReceivedCFO|annualInterestReceivedDirect|annualInvestingCashFlow|annualIssuanceOfCapitalStock|annualIssuanceOfDebt|annualLongTermDebtIssuance|annualLongTermDebtPayments|annualNetBusinessPurchaseAndSale|annualNetCommonStockIssuance|annualNetForeignCurrencyExchangeGainLoss|annualNetIncomeFromContinuingOperations|annualNetIntangiblesPurchaseAndSale|annualNetInvestmentPropertiesPurchaseAndSale|annualNetInvestmentPurchaseAndSale|annualNetIssuancePaymentsOfDebt|annualNetLongTermDebtIssuance|annualNetOtherFinancingCharges|annualNetOtherInvestingChanges|annualNetPPEPurchaseAndSale|annualNetPreferredStockIssuance|annualNetShortTermDebtIssuance|annualOperatingCashFlow|annualOperatingGainsLosses|annualOtherCashAdjustmentInsideChangeinCash|annualOtherCashAdjustmentOutsideChangeinCash|annualOtherCashPaymentsfromOperatingActivities|annualOtherCashReceiptsfromOperatingActivities|annualOtherNonCashItems|annualPaymentsonBehalfofEmployees|annualPaymentstoSuppliersforGoodsandServices|annualPensionAndEmployeeBenefitExpense|annualPreferredStockDividendPaid|annualPreferredStockIssuance|annualPreferredStockPayments|annualProceedsFromStockOptionExercised|annualProvisionandWriteOffofAssets|annualPurchaseOfBusiness|annualPurchaseOfIntangibles|annualPurchaseOfInvestment|annualPurchaseOfInvestmentProperties|annualPurchaseOfPPE|annualReceiptsfromCustomers|annualReceiptsfromGovernmentGrants|annualRepaymentOfDebt|annualRepurchaseOfCapitalStock|annualSaleOfBusiness|annualSaleOfIntangibles|annualSaleOfInvestment|annualSaleOfInvestmentProperties|annualSaleOfPPE|annualShortTermDebtIssuance|annualShortTermDebtPayments|annualStockBasedCompensation|annualTaxesRefundPaid|annualTaxesRefundPaidDirect|annualUnrealizedGainLossOnInvestmentSecurities|quarterlyAccountsPayable|quarterlyAccountsReceivable|quarterlyAccumulatedDepreciation|quarterlyAmortization|quarterlyAmortizationOfIntangiblesIncomeStatement|quarterlyAverageDilutionEarnings|quarterlyBasicAccountingChange|quarterlyBasicAverageShares|quarterlyBasicContinuousOperations|quarterlyBasicDiscontinuousOperations|quarterlyBasicEPS|quarterlyBasicEPSOtherGainsLosses|quarterlyBasicExtraordinary|quarterlyBeginningCashPosition|quarterlyCapitalExpenditure|quarterlyCapitalStock|quarterlyCashAndCashEquivalents|quarterlyCashCashEquivalentsAndShortTermInvestments|quarterlyCashDividendsPaid|quarterlyCashFlowFromContinuingFinancingActivities|quarterlyChangeInAccountPayable|quarterlyChangeInCashSupplementalAsReported|quarterlyChangeInInventory|quarterlyChangeInWorkingCapital|quarterlyChangesInAccountReceivables|quarterlyCommonStockIssuance|quarterlyContinuingAndDiscontinuedBasicEPS|quarterlyContinuingAndDiscontinuedDilutedEPS|quarterlyCostOfRevenue|quarterlyCurrentAccruedExpenses|quarterlyCurrentAssets|quarterlyCurrentDebt|quarterlyCurrentDeferredRevenue|quarterlyCurrentLiabilities|quarterlyDeferredIncomeTax|quarterlyDepletionIncomeStatement|quarterlyDepreciationAmortizationDepletionIncomeStatement|quarterlyDepreciationAndAmortization|quarterlyDepreciationAndAmortizationInIncomeStatement|quarterlyDepreciationIncomeStatement|quarterlyDilutedAccountingChange|quarterlyDilutedAverageShares|quarterlyDilutedContinuousOperations|quarterlyDilutedDiscontinuousOperations|quarterlyDilutedEPS|quarterlyDilutedEPSOtherGainsLosses|quarterlyDilutedExtraordinary|quarterlyDilutedNIAvailtoComStockholders|quarterlyDividendPerShare|quarterlyEarningsFromEquityInterest|quarterlyEarningsFromEquityInterestNetOfTax|quarterlyearningsPerShare|quarterlyEBIT|quarterlyEbitda|quarterlyEndCashPosition|quarterlyExciseTaxes|quarterlyFreeCashFlow|quarterlyGainOnSaleOfBusiness|quarterlyGainOnSaleOfPPE|quarterlyGainOnSaleOfSecurity|quarterlyGainsLossesNotAffectingRetainedEarnings|quarterlyGeneralAndAdministrativeExpense|quarterlyGoodwill|quarterlyGrossPPE|quarterlyGrossProfit|quarterlyImpairmentOfCapitalAssets|quarterlyIncomeTaxPayable|quarterlyInsuranceAndClaims|quarterlyInterestExpense|quarterlyInterestExpenseNonOperating|quarterlyInterestIncome|quarterlyInterestIncomeNonOperating|quarterlyInventory|quarterlyInvestingCashFlow|quarterlyInvestmentsAndAdvances|quarterlyLongTermDebt|quarterlyMinorityInterests|quarterlyNetIncome|quarterlyNetIncomeCommonStockholders|quarterlyNetIncomeContinuousOperations|quarterlyNetIncomeDiscontinuousOperations|quarterlyNetIncomeExtraordinary|quarterlyNetIncomeFromContinuingAndDiscontinuedOperation|quarterlyNetIncomeFromContinuingOperationNetMinorityInterest|quarterlyNetIncomeFromTaxLossCarryforward|quarterlyNetIncomeIncludingNoncontrollingInterests|quarterlyNetInterestIncome|quarterlyNetNonOperatingInterestIncomeExpense|quarterlyNetOtherInvestingChanges|quarterlyNetPPE|quarterlyNonCurrentDeferredRevenue|quarterlyNonCurrentDeferredTaxesLiabilities|quarterlyNormalizedBasicEPS|quarterlyNormalizedDilutedEPS|quarterlyNormalizedEBITDA|quarterlyNormalizedIncome|quarterlyOperatingCashFlow|quarterlyOperatingExpense|quarterlyOperatingIncome|quarterlyOperatingRevenue|quarterlyOtherCurrentAssets|quarterlyOtherCurrentLiabilities|quarterlyOtherGandA|quarterlyOtherIncomeExpense|quarterlyOtherIntangibleAssets|quarterlyOtherNonCashItems|quarterlyOtherNonCurrentAssets|quarterlyOtherNonCurrentLiabilities|quarterlyOtherNonOperatingIncomeExpenses|quarterlyOtherOperatingExpenses|quarterlyOtherShortTermInvestments|quarterlyOtherSpecialCharges|quarterlyOtherTaxes|quarterlyOtherunderPreferredStockDividend|quarterlyPreferredStockDividends|quarterlyPretaxIncome|quarterlyProvisionForDoubtfulAccounts|quarterlyPurchaseOfBusiness|quarterlyPurchaseOfInvestment|quarterlyReconciledCostOfRevenue|quarterlyReconciledDepreciation|quarterlyRentAndLandingFees|quarterlyRentExpenseSupplemental|quarterlyRepaymentOfDebt|quarterlyReportedNormalizedBasicEPS|quarterlyReportedNormalizedDilutedEPS|quarterlyRepurchaseOfCapitalStock|quarterlyResearchAndDevelopment|quarterlyRestructuringAndMergernAcquisition|quarterlyRetainedEarnings|quarterlySalariesAndWages|quarterlySaleOfInvestment|quarterlySecuritiesAmortization|quarterlySellingAndMarketingExpense|quarterlySellingGeneralAndAdministration|quarterlySpecialIncomeCharges|quarterlyStockBasedCompensation|quarterlyStockholdersEquity|quarterlyTaxEffectOfUnusualItems|quarterlyTaxLossCarryforwardBasicEPS|quarterlyTaxLossCarryforwardDilutedEPS|quarterlyTaxProvision|quarterlyTaxRateForCalcs|quarterlyTotalAssets|quarterlyTotalExpenses|quarterlyTotalLiabilitiesNetMinorityInterest|quarterlyTotalNonCurrentAssets|quarterlyTotalNonCurrentLiabilitiesNetMinorityInterest|quarterlyTotalOperatingIncomeAsReported|quarterlyTotalOtherFinanceCost|quarterlyTotalRevenue|quarterlyTotalUnusualItems|quarterlyTotalUnusualItemsExcludingGoodwill|quarterlyWeighteAverageShare|quarterlyWriteOff|timestamp|trailingAccountsPayable|trailingAccountsReceivable|trailingAccumulatedDepreciation|trailingAdjustedGeographySegmentData|trailingAmortization|trailingAmortizationCashFlow|trailingAmortizationOfIntangibles|trailingAmortizationOfIntangiblesIncomeStatement|trailingAmortizationOfSecurities|trailingAssetImpairmentCharge|trailingAverageDilutionEarnings|trailingBasicAccountingChange|trailingBasicAverageShares|trailingBasicContinuousOperations|trailingBasicDiscontinuousOperations|trailingBasicEPS|trailingBasicEPSOtherGainsLosses|trailingBasicExtraordinary|trailingBeginningCashPosition|trailingCapitalExpenditure|trailingCapitalExpenditureReported|trailingCapitalStock|trailingCashAndCashEquivalents|trailingCashCashEquivalentsAndShortTermInvestments|trailingCashDividendsPaid|trailingCashFlowFromContinuingFinancingActivities|trailingCashFlowFromContinuingInvestingActivities|trailingCashFlowFromContinuingOperatingActivities|trailingCashFlowFromDiscontinuedOperation|trailingCashFlowsfromusedinOperatingActivitiesDirect|trailingCashFromDiscontinuedFinancingActivities|trailingCashFromDiscontinuedInvestingActivities|trailingCashFromDiscontinuedOperatingActivities|trailingChangeInAccountPayable|trailingChangeInAccruedExpense|trailingChangeInCashSupplementalAsReported|trailingChangeInDividendPayable|trailingChangeInIncomeTaxPayable|trailingChangeInInterestPayable|trailingChangeInInventory|trailingChangeInOtherCurrentAssets|trailingChangeInOtherCurrentLiabilities|trailingChangeInOtherWorkingCapital|trailingChangeInPayable|trailingChangeInPayablesAndAccruedExpense|trailingChangeInPrepaidAssets|trailingChangeInReceivables|trailingChangeInTaxPayable|trailingChangeInWorkingCapital|trailingChangesInAccountReceivables|trailingChangesInCash|trailingClassesofCashPayments|trailingClassesofCashReceiptsfromOperatingActivities|trailingCommonStockDividendPaid|trailingCommonStockIssuance|trailingCommonStockPayments|trailingContinuingAndDiscontinuedBasicEPS|trailingContinuingAndDiscontinuedDilutedEPS|trailingCostOfRevenue|trailingCurrentAccruedExpenses|trailingCurrentAssets|trailingCurrentDebt|trailingCurrentDeferredRevenue|trailingCurrentLiabilities|trailingDeferredIncomeTax|trailingDeferredTax|trailingDepletion|trailingDepletionIncomeStatement|trailingDepreciation|trailingDepreciationAmortizationDepletion|trailingDepreciationAmortizationDepletionIncomeStatement|trailingDepreciationAndAmortization|trailingDepreciationAndAmortizationInIncomeStatement|trailingDepreciationIncomeStatement|trailingDilutedAccountingChange|trailingDilutedAverageShares|trailingDilutedContinuousOperations|trailingDilutedDiscontinuousOperations|trailingDilutedEPS|trailingDilutedEPSOtherGainsLosses|trailingDilutedExtraordinary|trailingDilutedNIAvailtoComStockholders|trailingDividendPaidCFO|trailingDividendPerShare|trailingDividendReceivedCFO|trailingDividendsPaidDirect|trailingDividendsReceivedCFI|trailingDividendsReceivedDirect|trailingDomesticSales|trailingEarningsFromEquityInterest|trailingEarningsFromEquityInterestNetOfTax|trailingEarningsLossesFromEquityInvestments|trailingearningsPerShare|trailingEBIT|trailingEbitda|trailingEffectOfExchangeRateChanges|trailingEndCashPosition|trailingExcessTaxBenefitFromStockBasedCompensation|trailingExciseTaxes|trailingFinancingCashFlow|trailingForeignSales|trailingFreeCashFlow|trailingGainLossOnInvestmentSecurities|trailingGainLossOnSaleOfBusiness|trailingGainLossOnSaleOfPPE|trailingGainOnSaleOfBusiness|trailingGainOnSaleOfPPE|trailingGainOnSaleOfSecurity|trailingGainsLossesNotAffectingRetainedEarnings|trailingGeneralAndAdministrativeExpense|trailingGoodwill|trailingGrossPPE|trailingGrossProfit|trailingImpairmentOfCapitalAssets|trailingIncomeTaxPaidSupplementalData|trailingIncomeTaxPayable|trailingInsuranceAndClaims|trailingInterestExpense|trailingInterestExpenseNonOperating|trailingInterestIncome|trailingInterestIncomeNonOperating|trailingInterestPaidCFF|trailingInterestPaidCFO|trailingInterestPaidDirect|trailingInterestPaidSupplementalData|trailingInterestReceivedCFI|trailingInterestReceivedCFO|trailingInterestReceivedDirect|trailingInventory|trailingInvestingCashFlow|trailingInvestmentsAndAdvances|trailingIssuanceOfCapitalStock|trailingIssuanceOfDebt|trailingLongTermDebt|trailingLongTermDebtIssuance|trailingLongTermDebtPayments|trailingMinorityInterests|trailingNetBusinessPurchaseAndSale|trailingNetCommonStockIssuance|trailingNetForeignCurrencyExchangeGainLoss|trailingNetIncome|trailingNetIncomeCommonStockholders|trailingNetIncomeContinuousOperations|trailingNetIncomeDiscontinuousOperations|trailingNetIncomeExtraordinary|trailingNetIncomeFromContinuingAndDiscontinuedOperation|trailingNetIncomeFromContinuingOperationNetMinorityInterest|trailingNetIncomeFromContinuingOperations|trailingNetIncomeFromTaxLossCarryforward|trailingNetIncomeIncludingNoncontrollingInterests|trailingNetIntangiblesPurchaseAndSale|trailingNetInterestIncome|trailingNetInvestmentPropertiesPurchaseAndSale|trailingNetInvestmentPurchaseAndSale|trailingNetIssuancePaymentsOfDebt|trailingNetLongTermDebtIssuance|trailingNetNonOperatingInterestIncomeExpense|trailingNetOtherFinancingCharges|trailingNetOtherInvestingChanges|trailingNetPPE|trailingNetPPEPurchaseAndSale|trailingNetPreferredStockIssuance|trailingNetShortTermDebtIssuance|trailingNonCurrentDeferredRevenue|trailingNonCurrentDeferredTaxesLiabilities|trailingNormalizedBasicEPS|trailingNormalizedDilutedEPS|trailingNormalizedEBITDA|trailingNormalizedIncome|trailingOperatingCashFlow|trailingOperatingExpense|trailingOperatingGainsLosses|trailingOperatingIncome|trailingOperatingRevenue|trailingOtherCashAdjustmentInsideChangeinCash|trailingOtherCashAdjustmentOutsideChangeinCash|trailingOtherCashPaymentsfromOperatingActivities|trailingOtherCashReceiptsfromOperatingActivities|trailingOtherCurrentAssets|trailingOtherCurrentLiabilities|trailingOtherGandA|trailingOtherIncomeExpense|trailingOtherIntangibleAssets|trailingOtherNonCashItems|trailingOtherNonCurrentAssets|trailingOtherNonCurrentLiabilities|trailingOtherNonOperatingIncomeExpenses|trailingOtherOperatingExpenses|trailingOtherShortTermInvestments|trailingOtherSpecialCharges|trailingOtherTaxes|trailingOtherunderPreferredStockDividend|trailingPaymentsonBehalfofEmployees|trailingPaymentstoSuppliersforGoodsandServices|trailingPensionAndEmployeeBenefitExpense|trailingPreferredStockDividendPaid|trailingPreferredStockDividends|trailingPreferredStockIssuance|trailingPreferredStockPayments|trailingPretaxIncome|trailingProceedsFromStockOptionExercised|trailingProvisionandWriteOffofAssets|trailingProvisionForDoubtfulAccounts|trailingPurchaseOfBusiness|trailingPurchaseOfIntangibles|trailingPurchaseOfInvestment|trailingPurchaseOfInvestmentProperties|trailingPurchaseOfPPE|trailingReceiptsfromCustomers|trailingReceiptsfromGovernmentGrants|trailingReconciledCostOfRevenue|trailingReconciledDepreciation|trailingRentAndLandingFees|trailingRentExpenseSupplemental|trailingRepaymentOfDebt|trailingReportedNormalizedBasicEPS|trailingReportedNormalizedDilutedEPS|trailingRepurchaseOfCapitalStock|trailingResearchAndDevelopment|trailingRestructuringAndMergernAcquisition|trailingRetainedEarnings|trailingSalariesAndWages|trailingSaleOfBusiness|trailingSaleOfIntangibles|trailingSaleOfInvestment|trailingSaleOfInvestmentProperties|trailingSaleOfPPE|trailingSecuritiesAmortization|trailingSellingAndMarketingExpense|trailingSellingGeneralAndAdministration|trailingShortTermDebtIssuance|trailingShortTermDebtPayments|trailingSpecialIncomeCharges|trailingStockBasedCompensation|trailingStockholdersEquity|trailingTaxEffectOfUnusualItems|trailingTaxesRefundPaid|trailingTaxesRefundPaidDirect|trailingTaxLossCarryforwardBasicEPS|trailingTaxLossCarryforwardDilutedEPS|trailingTaxProvision|trailingTaxRateForCalcs|trailingTotalAssets|trailingTotalExpenses|trailingTotalLiabilitiesNetMinorityInterest|trailingTotalNonCurrentAssets|trailingTotalNonCurrentLiabilitiesNetMinorityInterest|trailingTotalOperatingIncomeAsReported|trailingTotalOtherFinanceCost|trailingTotalRevenue|trailingTotalUnusualItems|trailingTotalUnusualItemsExcludingGoodwill|trailingUnrealizedGainLossOnInvestmentSecurities|trailingWeighteAverageShare|trailingWriteOff
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-timeseries"
    querystring = {'symbol': symbol, 'period1': period1, 'period2': period2, }
    if region:
        querystring['region'] = region
    if type:
        querystring['type'] = type
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_profile_deprecating(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Profile section"
    symbol: The value of symbol field returned in .../auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v3_get_chart(interval: str, symbol: str, range: str, events: str='capitalGain,div,split', period1: int=None, period2: int=None, region: str='US', includeadjustedclose: bool=None, comparisons: str=None, useyfid: bool=None, includeprepost: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data to draw full screen chart"
    interval: One of the following is allowed 1m|2m|5m|15m|30m|60m|1d|1wk|1mo
        symbol: The value of symbol field returned in .../auto-complete endpoint.
        range: One of the following is allowed 1d|5d|1mo|3mo|6mo|1y|2y|5y|10y|ytd|max. Do not use together with period1 and period2.
        events: One of the followings : capitalGain|div|split|earn|history. Separated by comma for multiple events. Ex : capitalGain,split
        period1: Epoch timestamp in seconds, such as 1556816400, must be different from period2, and the value must be starting of a day to get whole data in day. Don't use together with range parameter.
        period2: Epoch timestamp in seconds, such as 1562170150, must be different from period1, and the value must be starting of the next day to get whole data in previous day. Don't use together with range parameter.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        includeadjustedclose: Whether or not including adjusted Close
        comparisons: The symbols for comparison separated by comma. Ex : ^GDAXI,^FCHI
        useyfid: Whether or not using Yfid
        includeprepost: Whether or not including pre post
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-chart"
    querystring = {'interval': interval, 'symbol': symbol, 'range': range, }
    if events:
        querystring['events'] = events
    if period1:
        querystring['period1'] = period1
    if period2:
        querystring['period2'] = period2
    if region:
        querystring['region'] = region
    if includeadjustedclose:
        querystring['includeAdjustedClose'] = includeadjustedclose
    if comparisons:
        querystring['comparisons'] = comparisons
    if useyfid:
        querystring['useYfid'] = useyfid
    if includeprepost:
        querystring['includePrePost'] = includeprepost
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_recommendations(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get similar symbols relating to specified one"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations"
    querystring = {'symbol': symbol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_esg_scores(symbol: str, lang: str='en-US', region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get scores related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-esg-scores"
    querystring = {'symbol': symbol, }
    if lang:
        querystring['lang'] = lang
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_historical_data_deprecated(period1: int, period2: int, symbol: str, frequency: str='1d', filter: str='history', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		Get data in Historical Data section"
    period1: Epoch timestamp in seconds, must be different from 'period2', and the value must be starting of a day to get whole data in day.
        period2: Epoch timestamp in seconds, must be different from 'period1', and the value must be starting of the later day to get whole data in all previous days.
        symbol: The value of symbol field returned in .../auto-complete endpoint.
        frequency: Allow one of following : 1d|1wk|1mo
        filter: Allow one of following : history|div|split
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"
    querystring = {'period1': period1, 'period2': period2, 'symbol': symbol, }
    if frequency:
        querystring['frequency'] = frequency
    if filter:
        querystring['filter'] = filter
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_insider_roster(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Insider Roster tab in Holders section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-insider-roster"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_insider_transactions(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Insider Transactions tab in Holders section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-insider-transactions"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_insights(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get brief reports relating to a symbol"
    symbol: The value of symbol field returned in .../auto-complete endpoint
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-insights"
    querystring = {'symbol': symbol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v3_get_statistics_deprecating(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Statistics section"
    symbol: The value of symbol field returned in …/auto-complete endpoint.
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-statistics"
    querystring = {'symbol': symbol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_chart(range: str, interval: str, symbol: str, region: str='US', period2: int=None, period1: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data to draw full screen chart"
    range: One of the following is allowed 1d|5d|1mo|3mo|6mo|1y|2y|5y|10y|ytd|max. Do not use together with period1 and period2.
        interval: One of the following is allowed 1m|2m|5m|15m|60m|1d
        symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        period2: Epoch timestamp in seconds, such as 1562170150, must be different from period1, and the value must be starting of the next day to get whole data in previous day. Don't use together with range parameter.
        period1: Epoch timestamp in seconds, such as 1556816400, must be different from period2, and the value must be starting of a day to get whole data in day. Don't use together with range parameter.
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"
    querystring = {'range': range, 'interval': interval, 'symbol': symbol, }
    if region:
        querystring['region'] = region
    if period2:
        querystring['period2'] = period2
    if period1:
        querystring['period1'] = period1
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v3_get_historical_data(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Historical Data section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_charts_deprecated(symbol: str, range: str, interval: str, region: str='US', comparisons: str='^GDAXI,^FCHI', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data to draw chart for a specific symbol and its comparisons"
    symbol: The value of symbol field returned in .../auto-complete endpoint
        range: Allowed values are (1d | 5d | 3mo | 6mo | 1y | 5y | max)
        interval: Allowed values are (5m | 15m | 1d | 1wk | 1mo)
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        comparisons: The symbols for comparison separated by comma
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"
    querystring = {'symbol': symbol, 'range': range, 'interval': interval, }
    if region:
        querystring['region'] = region
    if comparisons:
        querystring['comparisons'] = comparisons
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_movers_deprecated(region: str='US', lang: str='en-US', start: int=0, count: int=6, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		The live day gainers / losers / actives in specific region"
    region: One of the following is allowed ASIA | EU | US | AU | BR | CA | FR | DE | HK | IT | ES | GB | IN | SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        start: The offset to start to get quotes for paging purpose
        count: The number of quotes to display in day gainers / losers / activies (max 6)
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-movers"
    querystring = {}
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    if start:
        querystring['start'] = start
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_summary_deprecated(region: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		Get live summary information of market by region"
    region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary"
    querystring = {'region': region, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_watchlist_detail(userid: str, pfid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get detail information of specific watchlist"
    userid: The value of userId field returned in .../market/get-popular-watchlists endpoint.
        pfid: The value of pfId field returned in .../market/get-popular-watchlists endpoint.
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-watchlist-detail"
    querystring = {'userId': userid, 'pfId': pfid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_popular_watchlists(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get popular watchlists in the market"
    
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-popular-watchlists"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_v2_get_movers(start: str='0', region: str='US', lang: str='en-US', count: int=6, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The live day gainers / losers / actives in specific region"
    start: The starting offset for paging purpose
        region: One of the following is allowed ASIA | EU | US | AU | BR | CA | FR | DE | HK | IT | ES | GB | IN | SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        count: The number of items per response for paging purpose (max 25)
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-movers"
    querystring = {}
    if start:
        querystring['start'] = start
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_v2_get_summary(region: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get live summary information of market by region"
    region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-summary"
    querystring = {'region': region, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_v2_get_quotes(symbols: str, region: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The quotes by symbols"
    symbols: The value of symbol field returned in .../auto-complete endpoint. Separated by comma for multiple entities.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
    querystring = {'symbols': symbols, 'region': region, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def screeners_get_filters(region: str='US', quotetype: str='mutualfund', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get optional filters for later use in .../screeners/list endpoint"
    region: One of the following : US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        quotetype: One of the following : equity | etf | mutualfund | future
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/screeners/get-filters"
    querystring = {}
    if region:
        querystring['region'] = region
    if quotetype:
        querystring['quoteType'] = quotetype
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def screeners_get_symbols_by_predefined(scrids: str, start: int=0, count: int=100, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get symbols related to a predefined screener"
    scrids: The value of canonicalName field returned in …/screeners/list-by-ticker endpoint OR one of the following : MOST&#95;ACTIVES|DAY&#95;GAINERS|DAY&#95;LOSERS|AUTO&#95;MANUFACTURERS|MS&#95;CONSUMER&#95;CYCLICAL|MOST&#95;WATCHED&#95;TICKERS|all&#95;cryptocurrencies&#95;us
        start: The offset for paging purpose
        count: The number of items per response for paging purpose
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/screeners/get-symbols-by-predefined"
    querystring = {'scrIds': scrids, }
    if start:
        querystring['start'] = start
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def screeners_list_by_ticker(ticker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get screener IDs related to a ticker"
    ticker: The value of symbol field returned in …/auto-complete endpoint
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/screeners/list-by-ticker"
    querystring = {'ticker': ticker, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_recommendation_trend(symbol: str, region: str='US', lang: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get recommended trending information"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-recommendation-trend"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_company_outlook(symbol: str, region: str='US', lang: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get company outlook"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-company-outlook"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_futures_chain(symbol: str, region: str='US', lang: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get futures chain"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-futures-chain"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_sec_filings(symbol: str, region: str='US', lang: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get sec filings related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-sec-filings"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_recent_updates(symbol: str, region: str='US', lang: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get recent updates related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-recent-updates"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_earnings(symbol: str, region: str='US', lang: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get earnings related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-earnings"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v3_get_options(symbol: str, lang: str='en-US', region: str='US', straddle: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get option prices"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-options"
    querystring = {'symbol': symbol, }
    if lang:
        querystring['lang'] = lang
    if region:
        querystring['region'] = region
    if straddle:
        querystring['straddle'] = straddle
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v3_get_upgrades_downgrades(symbol: str, region: str='US', lang: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get upgrades downgrades histories related to a symbol"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-upgrades-downgrades"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v3_get_profile(symbol: str, lang: str='en-US', region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get ticker's profile"
    symbol: The value of symbol field returned in …/auto-complete endpoint
        lang: One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-profile"
    querystring = {'symbol': symbol, }
    if lang:
        querystring['lang'] = lang
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_tickers_by_quote_type(lang: str='en-US', region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get tickers grouped by quote types"
    lang: The value of symbol field returned in .../auto-complete endpoint. Separated by comma for multiple entities.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-tickers-by-quote-type"
    querystring = {}
    if lang:
        querystring['lang'] = lang
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_earnings(enddate: int, startdate: int, region: str, size: int=10, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get recent earnings in the market"
    enddate: End date - unix timestamps in milliseconds (ex : 1589475600000), the value must be different from startDate, and the value must be starting of the later day to get whole data in all previous days. (Interval between start & end date is up to 14 days)
        startdate: Start date - unix timestamps in milliseconds (ex : 1585155600000), the value must be different from endDate, and the value must be starting of a day to get whole data in day. (Interval between start & end date is up to 14 days)
        region: The main region to get summary information from (AU | CA | FR | DE | HK | US | IT | ES | GB | IN)
        size: Number of items returned (up to 100)
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-earnings"
    querystring = {'endDate': enddate, 'startDate': startdate, 'region': region, }
    if size:
        querystring['size'] = size
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_auto_complete_deprecated(query: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		Get auto complete suggestion by term or phrase"
    query: Any familiar term or phrase to get auto complete suggestions
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/auto-complete"
    querystring = {'query': query, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_quotes_deprecated(region: str, symbols: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		Get real time quotes"
    region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        symbols: The value of symbol field returned in .../auto-complete endpoint. Separated by comma for multiple entities.
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"
    querystring = {'region': region, 'symbols': symbols, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_watchlist_performance(userid: str, pfid: str, symbols: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get performance information of specific watchlist"
    userid: The value of userId field returned in .../market/get-popular-watchlists endpoint.
        pfid: The value of pfId field returned in .../market/get-popular-watchlists endpoint.
        symbols: The value of symbol field returned in .../auto-complete endpoint. Separated by comma for multiple entities.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-watchlist-performance"
    querystring = {'userId': userid, 'pfId': pfid, 'symbols': symbols, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_trending_tickers(region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get latest trending tickers in the market"
    region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-trending-tickers"
    querystring = {}
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_news_deprecated(category: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		Get latest news related to a symbol, the result may be empty if there is no news in that region"
    category: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-news"
    querystring = {'category': category, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_get_detail_deprecated(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get detail information of stock quote, index, exchange, etc..."
    symbol: The value of symbol field returned in .../auto-complete endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_holders(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Major Holders tab in  Holders section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holders"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_options(symbol: str, date: int, straddle: bool=None, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Options section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        date: Epoch timestamp in seconds,  the value must be starting of a day to get whole data
        straddle: View as List or Straddle
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-options"
    querystring = {'symbol': symbol, 'date': date, }
    if straddle:
        querystring['straddle'] = straddle
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_analysis(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Analysis section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_cash_flow(symbol: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get cash flow tab information in Financials section"
    symbol: The value of symbol field returned in .../auto-complete endpoint.
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-cash-flow"
    querystring = {'symbol': symbol, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def market_get_spark(symbols: str, range: str='1d', interval: str='1m', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Used with .../market/get-trending-tickers endpoint together to draw brief chart."
    symbols: The symbol to get data, separated by comma to get data for multiple symbols.
        range: Allowed values are (1d | 5d | 3mo | 6mo | 1y | 5y | max)
        interval: Allowed values are (5m | 15m | 1d | 1wk | 1mo)
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-spark"
    querystring = {'symbols': symbols, }
    if range:
        querystring['range'] = range
    if interval:
        querystring['interval'] = interval
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def auto_complete(q: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get auto complete suggestions by term or phrase"
    q: Any familiar term or phrase to get auto complete suggestions
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"
    querystring = {'q': q, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def news_get_details_deprecated(uuid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		Read the specific news in details"
    uuid: The value of uuid field returned in .../news/list endpoint. Ex : 375879c0-08f3-32fb-8aaf-523c93ff8792
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/get-details"
    querystring = {'uuid': uuid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def news_v2_get_details(uuid: str, region: str='US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Read the specific news in details"
    uuid: The value of id field returned in .../news/v2/list endpoint. Ex : 375879c0-08f3-32fb-8aaf-523c93ff8792
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"
    querystring = {'uuid': uuid, }
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def news_list_deprecated(region: str, category: str, start_uuid: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "*This endpoint is deprecating
		List latest general news or video feeds or news relating to a symbol, the result may be empty if there is no news in that region"
    region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        category: One of the following : generalnews or videofeed or symbol (only one at a time)
        start_uuid: Get suitable value of more/result/uuid returned right in this endpoint to load news in the next page
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list"
    querystring = {'region': region, 'category': category, }
    if start_uuid:
        querystring['start_uuid'] = start_uuid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def conversations_list(symbol: str, messageboardid: str, region: str='US', useractivity: bool=None, sortby: str='createdAt', off: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List conversations relating to a symbol"
    symbol: The value of symbol field returned in .../auto-complete endpoint
        messageboardid: The value of messageBoardId field returned in .../market/get-quotes endpoint
        region: One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG
        useractivity: Whether or not return current number of interacting users 
        sortby: One of the following createdAt | popular
        off: The offset to start loading messages. It is fixed at 10 messages returned per response. Ex : 0 -> 9 -> 19 -> 29 -> 39 -> ...
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/conversations/list"
    querystring = {'symbol': symbol, 'messageBoardId': messageboardid, }
    if region:
        querystring['region'] = region
    if useractivity:
        querystring['userActivity'] = useractivity
    if sortby:
        querystring['sortBy'] = sortby
    if off:
        querystring['off'] = off
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_v2_get_holdings(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data in Holdings tab (it must be Mutual fun stock to have this tab displayed)"
    symbol: The value of symbol field returned in …/auto-complete endpoint.
        
    """
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holdings"
    querystring = {'symbol': symbol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

