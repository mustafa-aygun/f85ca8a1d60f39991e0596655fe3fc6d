#It is the TcmbApi class file. The Api and its response processing handling here.
import requests
import json
from datetime import datetime

#TcmbApi class is defined and implemented in the same way of XrateApi class. Since Python has dynamic naming, there is no abstract class and method for APIs; however, functions are
#identical for all APIs. 
class TcmbApi():
    #A initial constructor in case of needs of defining payload and headers.
    def __init__(self,payload, headers):
        self.payload = payload
        self.headers = headers
    #process_response function which it should be defined in all API classes with same name. It send request to API and process the result of it. Since every API might return result
    #in different format, this function is the only implementation which is not automized and should be implemented in case of adding a new API.
    def process_response(self,date):
        #url is not definied in constructor and class itself since date format should be processed uniquely according to API format. Since this function is the only function 
        #which is implemented according to APIs, this process is handled here.
        date = datetime.strptime(str(date), "%Y-%m-%d").strftime("%d-%m-%Y")
        url = "https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.USD.A-TP.DK.EUR.A&startDate="+date+"&endDate="+date+"&type=json&key=XXXXXXXXX"
        response = requests.request("GET", url, headers=self.headers, data = self.payload)

        result = response.text
        dict = json.loads(result)
        item = dict["items"][0]
        #Checking if response has a value for exchange rates. In some cases such as weekends, holidays or too old dates, APIs might not have a exchange rate value and return none.
        #In such case function return empty to avoid errors in getCheaper function and continue work with other APIs result.  
        if(item["TP_DK_USD_A"] != None):
            #Return type is list of lists. Every currency append in a main list with its name and rate. 
            usd = []
            usd.append("USD")
            usd.append(item["TP_DK_USD_A"])

            eur = []
            eur.append("EUR")
            eur.append(item["TP_DK_EUR_A"])

            tcmb = []
            tcmb.append(eur)
            tcmb.append(usd)
            #Sorting list according to currency names is crucial before returning it. In case of high number exchange rates and APIs, sorting list will guarantee that we will compare same 
            #exchange rates in getCheaper function and appending order to the list doesn't matter.
            sorted_tcmb= sorted(tcmb, key=lambda tup: tup[0])
            return sorted_tcmb
        else:
            return 