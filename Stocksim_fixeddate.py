import random
import matplotlib.pyplot as plt
import statistics
import numbers
import math

print('Random Walk와 Monte Carlo 방식을 통한 주식 가격 재현 프로그램')
print('Made by bcchickadee, Jun 21 2020. Updated Oct 20 2021')
print('이 프로그램은 특정 거래일만큼의 주식 변화를 지정한 만큼 시행하여 그 결과값을 산출합니다.')
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
    while True:
        Attempts=input('\n시행 횟수를 입력해 주십시오. 기본값은 1000번입니다.\n시행 횟수: ')
        if Attempts=='':
          Attempts=1000
          break
        else:
          try:
            Attempts=int(Attempts)
          except ValueError:
              print('\n오류: 올바른 자연수를 입력하여 주십시오.')
          else:
              if Attempts<=0:
                  print('\n오류: 시행 횟수는 자연수여야 합니다.')
              else:
                  break

    for Attempt in range(Attempts):
      for Day in range(Period):
          if Day==0:
              Price=InitPrice
          else:
              Price=Price*(1+0.01*random.gauss(m, sigma))
      PriceList.append(Price)

    print('\n각 시행의 최종 주식 가격의 평균: '+str(statistics.mean(PriceList)))
    print('각 시행의 최종 주식 가격의 표준편차: '+str(statistics.stdev(PriceList)))
    print(str(Attempts)+'번 시행 중 최소 가격: '+str(min(PriceList)))
    print(str(Attempts)+'번 시행 중 최대 가격: '+str(max(PriceList)))
    plt.hist(PriceList, bins=math.floor(Attempts/10))
    plt.title('Stock Price Simulation for '+str(Period)+' Days, '+str(Attempts)+' Tries')
    plt.show()

    print('\n=======================================')
    print('\n프로그램을 다시 시작합니다.')
