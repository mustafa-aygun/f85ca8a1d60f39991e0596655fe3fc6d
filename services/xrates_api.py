#It is the XratesApi class file. The Api and its response processing handling here.
import requests
import json
#XratesApi class is defined and implemented in the same way of TcmbApi class. Since Python has dynamic naming, there is no abstract class and method for APIs; however, functions are
#identical for all APIs. 
class XratesApi():
    #A initial constructor in case of needs of defining payload and headers. In this case header and key coming from an account. It can be changed easily from the ApiClass.
    def __init__(self,payload, headers):
        self.payload = payload
        self.headers = headers
    #process_response function which it should be defined in all API classes with same name. It send request to API and process the result of it. Since every API might return result
    #in different format, this function is the only implementation which is not automized and should be implemented in case of adding a new API.
    def process_response(self, date):
        #url is not definied in constructor and class itself since date format should be processed uniquely according to API format. Since this function is the only function 
        #which is implemented according to APIs, this process is handled here.

        url = "https://api.apilayer.com/exchangerates_data/"+date+"?symbols=USD%2CEUR&base=TRY"
        response = requests.request("GET", url, headers=self.headers, data = self.payload)
        dict = json.loads(response.text)
        #There is a hard coded response and its own processing implemented below. Since Xrates has an API call limit in a month, for test uses, that response can be used.
        #response = '{ "base": "TRY", "date": "2022-09-04", "rates": {"USD": 0.054943,"EUR": 0.055176},"timestamp": 1662316083}'
        #dict = json.loads(response)

        result= dict["rates"]
        #Checking if response has a value for exchange rates. In some cases such as weekends, holidays or too old dates, APIs might not have a exchange rate value and return none.
        #In such case function return empty to avoid errors in getCheaper function and continue work with other APIs result.  
        if(result["USD"] != None):
            xrate = []
            #The for loop is extracting data from the response and put in the list. Same for loop can be used for more currency type coming from the url.
            for rate in result:
                temp_rate = []
                temp_rate.append(rate)
                temp_rate.append(round(1/result[rate],4))
                xrate.append(temp_rate)
                
            #Sorting list according to currency names is crucial before returning it. In case of high number exchange rates and APIs, sorting list will guarantee that we will compare same 
            #exchange rates in getCheaper function and appending order to the list doesn't matter.
            sorted_xrate= sorted(xrate, key=lambda tup: tup[0])
            return sorted_xrate
        else:
            return