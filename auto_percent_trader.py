# WIP

import random
import matplotlib.pyplot as plt
import statistics
import math

# Variable Creation Function
def VarCreater(var_type, default_value, description):
  if var_type=='int+':
    while True:
      var=input('\n'+description+' The default value is '+str(default_value)+'.\nValue: ')
      if var=='':
        var=default_value
        return var
        break
      else:
        try:
          var=int(var)
        except ValueError:
          print('\nError: Type an integer larger than 0\n')
        else:
          if var<=0:
            print('\nError: Type an integer larger than 0\n')
          else:
            return var
            break
  elif var_type=='int+-':
    while True:
      var=input('\n'+description+' The default value is '+str(default_value)+'.\nValue: ')
      if var=='':
        var=default_value
        return var
        break
      else:
        try:
          var=int(var)
        except ValueError:
          print('\nError: Type a valid integer\n')
        else:
          return var
          break
  elif var_type=='float+':
    while True:
      var=input('\n'+description+' The default value is '+str(default_value)+'.\nValue: ')
      if var=='':
        var=default_value
        return var
        break
      else:
        try:
          var=float(var)
        except ValueError:
          print('\nError: Type a valid number larger than 0\n')
        else:
          if var<=0:
            print('\nError: Type a valid number larger than 0\n')
          else:
            return var
            break
  elif var_type=='float+-':
    while True:
      var=input('\n'+description+' The default value is '+str(default_value)+'.\nValue: ')
      if var=='':
        var=default_value
        return var
        break
      else:
        try:
          var=float(var)
        except ValueError:
          print('\nError: Type a valid Number\n')
        else:
          return var
          break
  elif var_type=='str':
    var=input('\n'+description+'.\nValue: ')
    return var
  else:
    raise TypeError('Data type not available. Check for errors in var_type argument\n')

# Variation Creation
InitPrice=VarCreater('float+', 10000, 'Enter Initial Price of stock.')
m=VarCreater('float+-', 0, 'Enter average fluctuation rate, by percent(%).')
sigma=VarCreater('float+', 1, 'Enter standard deviation of fluctuation rate, by percent(%).')
Period=VarCreater('int+', 300, 'Enter number of exchange days.')
InitShares=VarCreater('int+', 100, 'Enter inital number of shares to purchase.')
BuySignal=VarCreater('int+', 5, 'Enter number of days to buy.\nThe algorithm buys shares with the money in the account as many as possible, when share prices drop consecutively for a specific number of days.')
SellSignal=VarCreater('int+', 5, 'Enter number of days to sell.\nThe algorithm sells all shares when prices increase consecutively for a specific number of days.')

Cash=0 # Our 'bank account.' Initially we used all of our money in buying shares
Shares=InitShares # The number of shares we possess
TransactionList=[[0, 'Bought', InitShares, InitPrice]] # An element will be appended every purchase. Format: [Day, Bought/Sold, Number of Shares, Price]
PriceList=[InitPrice] # List of share prices according to day.

# Create Prices based on Random Walk. Price fluctuation follows a Gaussian distribution.
for Day in range(Period):
  Price=PriceList[-1]*(1+0.01*random.gauss(m, sigma))
  PriceList.append(Price)

# Function for returning list of prices of latest days
def return_day_prices(Signal):
  return PriceList[-1-Signal:-1]

# Function for checking overall trend of prices in list.
# If strictly increasing: returns True (required to sell), if strictly decreasing: returns False (required to buy).
def check_trend(PartialList):
  TrendList=[]
  for i in range(len(PartialList)-1):
    if PartialList[i]>PartialList[i+1]:
      TrendList.append(True)
    elif PartialList[i]<PartialList[i+1]:
      TrendList.append(False)
  if set(TrendList)==[True]:
    return True
  elif set(TrendList)==[False]:
    return False

# Automatic transaction algorithm
for Day in range(Period):
  if BuySignal<SellSignal: # We do not need to consider the days before the SellSignal, because there is no cash
    if Day>=SellSignal:
      if check_trend(return_day_prices(SellSignal))==True:
        TransactionList.append([Day, 'Sold', Shares, Price])
        Cash=Cash+Shares*Price
        Shares=0
      elif check_trend(return_day_prices(BuySignal))==False:
        TransactionList.append([Day, 'Bought', math.gauss(Cash/Price), Price])
        Shares=math.gauss(Cash/Price)
        Cash=Cash-Shares*Price
  elif BuySignal==SellSignal:
    if Day>=BuySignal:
      if check_trend(return_day_prices(SellSignal))==True:
        TransactionList.append([Day, 'Sold', Shares, Price])
        Cash=Cash+Shares*Price
        Shares=0
      elif check_trend(return_day_prices(BuySignal))==False:
        TransactionList.append([Day, 'Bought', math.gauss(Cash/Price), Price])
        Shares=math.gauss(Cash/Price)
        Cash=Cash-Shares*Price
  else:
    if SellSignal>=Day>BuySignal:
      if check_trend(return_day_prices(SellSignal))==True:
        TransactionList.append([Day, 'Sold', Shares, Price])
        Cash=Cash+Shares*Price
        Shares=0
    elif Day>=BuySignal:
      if check_trend(return_day_prices(SellSignal))==True:
        TransactionList.append([Day, 'Sold', Shares, Price])
        Cash=Cash+Shares*Price
        Shares=0
      elif check_trend(return_day_prices(BuySignal))==False:
        TransactionList.append([Day, 'Bought', Shares, Price])
        Shares=math.gauss(Cash/Price)
        Cash=Cash-Shares*Price

# Sell all shares in the last day
TransactionList.append([Day, 'Sold', Shares, Price])
Cash=Cash+Shares*Price
Shares=0

# Print Data
print(TransactionList)
print(Cash)
print('Yield of Transaction: '+str(Cash/(InitShares*InitPrice)*100-100)+'%')

# Show price fluctuation in Graph
print('\nAverage stock price during '+str(Period)+' days: '+str(statistics.mean(PriceList)))
print('Stock price after '+str(Period)+' days: '+str(PriceList[-1]))
print('Difference between initial stock price and stock price after '+str(Period)+' days: '+str(PriceList[-1]-InitPrice))
print('Stock price change after '+str(Period)+' days: '+str(PriceList[-1]/InitPrice*100-100)+'%')
plt.plot(PriceList, color='red')
plt.xlim(0, Period)
plt.title('Stock Price Simulation for '+str(Period)+' days')
plt.show()


# INOP: does not automatically transact. WIP
