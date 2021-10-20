import random
import matplotlib.pyplot as plt
import statistics
import numbers

print('Random Walk와 Monte Carlo 방식을 통한 주식 가격 재현 프로그램')
print('Made by bcchickadee, Jun 21 2020. Updated Oct 20 2021')
print('=======================================\n')

while True:
    
    PriceList=[]
    while True:
        try:
            InitPrice=float(input('\n초기 주식 가격을 입력해 주십시오. (단위: 원)\n초기 주식 가격: '))
        except ValueError:
            print('\n오류: 올바른 숫자를 입력해 주십시오.')
        else:    
            if InitPrice<=0:
                print('\n오류: 초기 주식 가격은 양의 값이어야 합니다.')
            else:
                break
    while True:
        try:
            m=float(input('\n주식 증가폭의 평균을 입력해 주십시오 (단위: %): '))
        except ValueError:
            print('\n오류: 올바른 숫자를 입력해 주십시오.')
        else:
            break
    while True:
        try:
            sigma=float(input('\n주식 변동폭의 표준편차를 입력해 주십시오 (단위: %): '))
        except ValueError:
            print('\n오류: 올바른 숫자를 입력해 주십시오.')
        else:
            if sigma<0:
                print('\n오류: 주식 변동폭의 표준편차는 0 이상이어야 합니다.')
            else:
                break
    while True:
        try:
            Period=int(input('\n관측 일수를 입력해 주십시오.\n관측 일수: '))
        except ValueError:
            print('\n오류: 올바른 자연수를 입력하여 주십시오.')
        else:
            if Period<=0:
                print('\n오류: 관측 일수는 자연수여야 합니다.')
            else:
                break
    
    for Day in range(int(Period)+1):
        if Day==0:
            PriceList.append(InitPrice)
        elif Day==1:
            Price=InitPrice*(1+0.01*random.gauss(m, sigma))
            PriceList.append(Price)
        else:
            Price=Price*(1+0.01*random.gauss(m, sigma))
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
