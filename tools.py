
from data import get_data
import scipy  as sc #type:ignore
import pandas as pd


#* debug code
data = get_data()
print(data.columns)#type:ignore
'''
Index(['Close', 'High', 'Low', 'Open', 'Volume', 'returns',
       'returns_shift(next_day_returns)'],
      dtype='str')
      '''
#* real things
def hypothesis_testing (coloum_a,coloum_b):


    corelation,p_value= sc.stats.pearsonr(coloum_a,coloum_b) #p_value = trust level that is this just luck or patern
    

    



    return corelation,f"{p_value:.25f}"


# print(f'Yesterday high mean today high?\n  {hypothesis_testing(data['returns_shift(next_day_returns)'],data['returns'])}\n')#type:ignore
# print(f' today high volume mean next day reterns high?\n  {hypothesis_testing(data['Volume'],data['returns_shift(next_day_returns)'])}')#type:ignore


def regress(coloum_a,coloum_b):

    output = sc.stats.linregress(coloum_a,coloum_b)
    """
    i add this for my understanding:
    
    r value → correlation, how strongly they move together
    p value → is it luck or real
    slope → how much B changes per +1 in A
    intercept → where the line starts if A were 0 (mostly just scaffolding, not an insight)
    stderr → how confident/stable the slope guess is
    """


    return output


# a=regress(data['Volume'],data['returns_shift(next_day_returns)'])#type:ignore
# print(a)

pairs = [[data['Volume'],data['returns_shift(next_day_returns)']],#type:ignore
         [data['returns'],data['returns_shift(next_day_returns)']],#type:ignore
         [data['High'],data['returns_shift(next_day_returns)']],#type:ignore
         [data['Low'],data['returns_shift(next_day_returns)']],#type:ignore
         [data['Open'],data['returns_shift(next_day_returns)']],#type:ignore
         [data['Close'],data['returns_shift(next_day_returns)']]#type:ignore
         ]

# def employee():
#     while True:
