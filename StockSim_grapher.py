import random
import matplotlib.pyplot as plt
import statistics
import numbers

print('Random Walk와 Monte Carlo 방식을 통한 주식 가격 재현 프로그램')
print('Version 2.1')
print('Made by bcchickadee, Oct 20 2021')
print('=======================================\n')

while True:
    
    PriceList=[]
    while True:
        InitPrice=input('\n초기 주식 가격을 입력해 주십시오. 기본값은 10,000입니다.\n초기 주식 가격 (단위: 원): ')
        if InitPrice=='':
          InitPrice=10000
          break
        else:
          try:
            InitPrice=float(InitPrice)
          except ValueError:
              print('\n오류: 올바른 숫자를 입력해 주십시오.')
          else:    
              if InitPrice<=0:
                  print('\n오류: 초기 주식 가격은 양의 값이어야 합니다.')
              else:
                  break
    while True:
        m=input('\n주식 증가폭의 평균을 입력해 주십시오. 기본값은 0입니다.\n주식 증가폭의 평균 (단위: %): ')
        if m=='':
          m=0
          break
        else:
          try:
            m=float(m)
          except ValueError:
              print('\n오류: 올바른 숫자를 입력해 주십시오.')
          else:
              break
    while True:
        sigma=input('\n주식 변동폭의 표준편차를 입력해 주십시오. 기본값은 1입니다.\n주식 변동폭의 표준편차 (단위: %): ')
        if sigma=='':
          sigma=1
          break
        else:
          try:
            sigma=float(sigma)
          except ValueError:
              print('\n오류: 올바른 숫자를 입력해 주십시오.')
          else:
              if sigma<0:
                  print('\n오류: 주식 변동폭의 표준편차는 0 이상이어야 합니다.')
              else:
                  break
    while True:
        Period=input('\n거래일수를 입력해 주십시오. 기본값은 300거래일입니다.\n거래일수: ')
        if Period=='':
          Period=300
          break
        else:
          try:
            Period=int(Period)
          except ValueError:
              print('\n오류: 올바른 자연수를 입력하여 주십시오.')
          else:
              if Period<=0:
                  print('\n오류: 관측 일수는 자연수여야 합니다.')
              else:
                  break
    
    for Day in range(Period):
        if Day==0:
            PriceList.append(InitPrice)
        else:
            Price=PriceList[-1]*(1+0.01*random.gauss(m, sigma))
            PriceList.append(Price)

    print('\n'+str(Period)+'일 동안 주식 가격의 평균: '+str(statistics.mean(PriceList)))
    print(str(Period)+'일 후의 가격: '+str(PriceList[-1]))
    print(str(Period)+'일 후의 가격의 초기 가격과의 변동폭: '+str(PriceList[-1]-InitPrice))
    print(str(Period)+'일 후의 수익률: '+str(PriceList[-1]/InitPrice*100-100)+'%')
    plt.plot(PriceList, color='red')
    plt.xlim(0, Period)
    plt.title('Stock Price Simulation for '+str(Period)+' Days')
    plt.show()

    print('\n=======================================')
    print('\n프로그램을 다시 시작합니다.')
    del InitPrice
    del m
    del sigma
    del Period
    PriceList.clear()
    print('\n=======================================')
