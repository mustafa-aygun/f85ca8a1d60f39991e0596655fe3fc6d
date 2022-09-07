#It is ApiClass file where a class has all APIs inside of it.
from services.tcmb_api import TcmbApi
from services.xrates_api import XratesApi

#ApiClass is working as a kind of Facade pattern. In main application file and functions, only ApiClass will be used a single object and other APIs will stay at back.
#A newly defined API can be added in this class and other functions continue to work same as before. Instead of passing arguments to this API in application, APIs are defined here
#to separate application and APIs as mentioned before. Moreover, in case of any problem in one of the APIs, that API can be removed from the list to maintaince.
class ApiClass():
    tcmb_Api = TcmbApi({},{})
    xrates_Api = XratesApi({},{"apikey": "XXXXXXXXXXXXXXXXXXXXXX"})
    api_list = [tcmb_Api, xrates_Api]

