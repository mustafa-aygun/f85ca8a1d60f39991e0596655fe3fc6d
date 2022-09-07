#This is the main application file where flask routes are defined and processed. 
from flask import Flask, request, render_template, redirect, session, url_for
from datetime import date
from services.base_api import ApiClass
from helpers.pickdate import PickDate
from helpers.functions import *

app = Flask(__name__, template_folder='template')

app.config['SECRET_KEY'] = 'maygun'

#Main page of the application. It shows a date and two buttons to the client. In case of getting a post request from those buttons, it redirects with a date. 
@app.route("/", methods=['GET','POST'])
def main_page():
    form = PickDate() 
    if request.method == 'POST':
        if request.form.get('getLatest') == 'Get Latest Currencies': #Returning the latest exchange rate info with date as today. 
            #Different than returning a selected date, we call the function with today's date.
            return redirect(url_for("getExhchangeRateWithDate",varDate=str(date.today())))
        elif request.form.get('getWithDate') == 'Get Currencies with Date': #Returning exchange rate info according to selected date.
            varDate = form.date.data
            return redirect(url_for("getExhchangeRateWithDate",varDate=str(varDate)))
        else:
            pass
    elif request.method =='GET':
        return render_template('main_page.html', form=form) #It is rendering a main_page.html file
    
    return render_template("main_page.html", form=form)

#It gets date information from the main page and call APIs with that date. 
@app.route('/exchange-rate-info/<varDate>', methods=['GET','POST'])
def getExhchangeRateWithDate(varDate):
    api_list = ApiClass()
    rates = []
    #Creating an object from ApiClass and calling process_response function from the list of APIs. If returning rate is not a None value, append it to the list.
    for api in api_list.api_list:
        rate = api.process_response(varDate)
        if rate is None:
            pass
        else:
            rates.append(rate)
    #Getting cheaper result from the getCheaper function and put them in a data list with the date.
    cheaperCurrencies = getCheaper(rates)
    data = [cheaperCurrencies,varDate]
    #As a design choice, two different html file are prefered for later use and development of design. According to previous dates or today, function render different htmls.
    if varDate != str(date.today()):
        return render_template('exchange_rates_with_date.html',data=data)
    else:
        return render_template('latest_exchange_rates.html',data=data)

if __name__ == '__main__':
    app.run()