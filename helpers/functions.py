#It is a function file where helper functions are located. Single helper functions to operations will locate here.

#getCheaper function is implemented to compare different rates to find minimum ones. Function is designed as work with more than two rates where any other rates can also be added to 
#APIs such as Sterlin or Japanese Yen. Function is implemented with a for loop; however, in case of high number of APIs and rates, same results can be extracted with numpy to
#provide faster operation.
def getCheaper(rates):
    cheaperCurrencies = rates[0] #The first rate given to the list as starting values.
    for rate in rates:
        for i in range(len(rate)): #Every different type of currency will be compared with the cheaperCurrencies list.
            if(float(rate[i][1]) < float(cheaperCurrencies[i][1])):
                cheaperCurrencies[i][1]=rate[i][1]
    return cheaperCurrencies #Return the resulting list.