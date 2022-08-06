from coinbase.wallet.client import Client
from time import sleep
from termcolor import cprint
import os
import LoginInfo
clear = lambda: os.system('cls')

ApiKey=LoginInfo.ApiKey
ApiSec=LoginInfo.ApiKey
client=Client(ApiKey,ApiSec)
refreshtime=14

#Search by Manraf
def search():
    symbol = input("Enter your currency: ")
    pair = symbol.upper() + "-EUR"

    coinprice=client.get_buy_price(currency_pair=pair).amount
    print(pair,"price:",coinprice,)


    print("1)Search again\n2)Main Menu")
    choice1=input("Select an option:")
    if choice1=="1":
        search()
    else:
        main()

def getprices(ethprice,btcprice,usdtprice,solprice,dotprice,avaxprice,adaprice):

    #New Price
    prices=[
        client.get_buy_price(currency_pair="ETH-EUR").amount,#ETH
        client.get_buy_price(currency_pair="BTC-EUR").amount,#BTC
        client.get_buy_price(currency_pair="USDT-EUR").amount,#USDT
        client.get_buy_price(currency_pair="SOL-EUR").amount,#SOL
        client.get_buy_price(currency_pair="DOT-EUR").amount,#DOT
        client.get_buy_price(currency_pair="AVAX-EUR").amount,#AVAX
        client.get_buy_price(currency_pair="ADA-EUR").amount,#ADA
    ]

    #Prev price
    Cprices=[
        ethprice,
        btcprice,
        usdtprice,
        solprice,
        dotprice,
        avaxprice,
        adaprice

    ]
    #Coin names
    Cname=[
        "ETH price:",
        "BTC price:",
        "USDT price:",
        "SOL price:",
        "DOT price:",
        "AVAX price:",
        "ADA price:",

    ]

    #print coin names and their prices
    clear()
    cprint("----------------------","yellow")
    for i in range(len(prices)):
        if prices[i]>Cprices[i]:
            cprint(f"{Cname[i]} {prices[i]}€ (+{round((float(prices[i])-float(Cprices[i]))/float(prices[i])*100,3)}%) (+{round(float(prices[i])-float(Cprices[i]),2)}€)","green")
            Cprices[i]=prices[i]
        elif prices[i]<Cprices[i]:
            cprint(f"{Cname[i]} {prices[i]}€ ({round((float(prices[i])-float(Cprices[i]))/float(prices[i])*100,3)}%) ({round(float(prices[i])-float(Cprices[i]),2)}€)","red")
        else:
            cprint(f"{Cname[i]} {prices[i]}€ ({round((float(prices[i])-float(Cprices[i]))/float(prices[i])*100,3)}%) ({round(float(prices[i])-float(Cprices[i]),2)}€)","white")
    cprint("----------------------","yellow")

    #update prev prices to new prices
    ethprice=client.get_buy_price(currency_pair="ETH-EUR").amount
    btcprice=client.get_buy_price(currency_pair="BTC-EUR").amount
    usdtprice=client.get_buy_price(currency_pair="USDT-EUR").amount
    solprice=client.get_buy_price(currency_pair="SOL-EUR").amount
    dotprice=client.get_buy_price(currency_pair="DOT-EUR").amount
    avaxprice=client.get_buy_price(currency_pair="AVAX-EUR").amount
    adaprice=client.get_buy_price(currency_pair="ADA-EUR").amount


    sleep(refreshtime)

    getprices(ethprice,btcprice,usdtprice,solprice,dotprice,avaxprice,adaprice)

def main():
    clear()
    print("1) Live Coin Price List\n2) Search Specific Coin")
    choice=input("Please choose an option >> ")

    if (choice=="1"):
        
        ethprice=client.get_buy_price(currency_pair="ETH-EUR").amount
        btcprice=client.get_buy_price(currency_pair="BTC-EUR").amount
        usdtprice=client.get_buy_price(currency_pair="USDT-EUR").amount
        solprice=client.get_buy_price(currency_pair="SOL-EUR").amount
        dotprice=client.get_buy_price(currency_pair="DOT-EUR").amount
        avaxprice=client.get_buy_price(currency_pair="AVAX-EUR").amount
        adaprice=client.get_buy_price(currency_pair="ADA-EUR").amount

        
        getprices(ethprice,btcprice,usdtprice,solprice,dotprice,avaxprice,adaprice)

    elif (choice=="2"):
        search()
    else:
        main()

main()