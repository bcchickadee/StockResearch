import random
import matplotlib.pyplot as plt
import statistics
import numbers

print('Random Walk와 Monte Carlo 방식을 통한 주식 가격 재현 프로그램')
print('Made by bcchickadee, Jun 21 2020')
print('=======================================\n')

while True:
    
    PriceList=[]
    while True:
        try:
            InitPrice=float(input('\n초기 주식 가격을 입력해 주십시오.\n초기 주식 가격: '))
        except ValueError:
            print('\n오류: 올바른 숫자를 입력해 주십시오.')
        else:    
            if InitPrice<=0:
                print('\n오류: 초기 주식 가격은 양의 값이어야 합니다.')
            else:
                break
    while True:
        try:
            MaximumFlux=float(input('\n일일 최대 주식 증가폭(%)을 입력해 주십시오. 예시: 1은 매일 주식이 최대 1% 상승할 수 있다는 것을 의미합니다.\n최대 주식 증가폭: '))
        except ValueError:
            print('\n오류: 올바른 숫자를 입력해 주십시오.')
        else:
            if MaximumFlux<0:
                print('\n오류: 최대 주식 증가폭은 0 이상이어야 합니다.')
            else:
                break
    while True:
        try:
            MinimumFlux=float(input('\n일일 최대 주식 감소폭(%)을 입력해 주십시오. 예시: 1은 매일 주식이 최대 1% 감소할 수 있다는 것을 의미합니다.\n최대 주식 감소폭: '))
        except ValueError:
            print('\n오류: 올바른 숫자를 입력해 주십시오.')
        else:
            if MinimumFlux<0:
                print('\n오류: 최대 주식 감소폭은 0 이상이어야 합니다.')
            else:
                break
    while True:
        try:
            Period=int(input('관측 일수를 입력해 주십시오.\n관측 일수: '))
        except ValueError:
            print('\n오류: 올바른 자연수를 입력하여 주십시오.')
        else:
            if Period<=0:
                print('\n오류: 관측 일수는 자연수여야 합니다.')
    
    for Day in range(int(Period)+1):
        if Day==0:
            PriceList.append(InitPrice)
        elif Day==1:
            Price=InitPrice*random.uniform(1-(MinimumFlux/100), 1+(MaximumFlux/100))
            PriceList.append(Price)
        else:
            Price=Price*random.uniform(1-(MinimumFlux/100), 1+(MaximumFlux/100))
            PriceList.append(Price)

    print('\n'+str(Period)+'일 동안 주식 가격의 평균: '+str(statistics.mean(PriceList)))
    print(str(Period)+'일 후의 가격: '+str(PriceList[-1]))
    print(str(Period)+'일 후의 가격의 초기 가격과의 변동폭: '+str(PriceList[-1]-InitPrice))
    plt.plot(PriceList, color='red')
    plt.xlim(0, Period)
    plt.title('Stock Price Simulation for '+str(Period)+' Days')
    plt.show()

    print('\n=======================================')
    print('\n프로그램을 다시 시작합니다.')
    del InitPrice
    del MaximumFlux
    del MinimumFlux
    del Period
    PriceList.clear()
    print('\n=======================================')
    
    
