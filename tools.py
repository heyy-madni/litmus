from data import get_data
import scipy  as sc #type:ignore
import pandas as pd


#* debug code
data = get_data()
# print(data.columns)#type:ignore

def test():
    a=[1,2,3,8]
    b=[1,2,3,0.5559814]
    c=sc.stats.pearsonr(a,b)
    return c

#! a,b = test()
#! print(a,b)
a=[1,2,3,8]
b=[1,2,3,0.5559814]

#! real things
def hypothesis_testing (coloum_a,coloum_b):


    corelation,p_value= sc.stats.pearsonr(coloum_a,coloum_b) #p_value = trust level that is this just luck or patern
    

    



    return corelation,f"{p_value:.25f}"





print(f'Yesterday high mean today high?\n  {hypothesis_testing(data['returns_shift(next_day_returns)'],data['returns'])}\n')#type:ignore

print(f' today high volume mean next day reterns high?\n  {hypothesis_testing(data['Volume'],data['returns_shift(next_day_returns)'])}')#type:ignore



