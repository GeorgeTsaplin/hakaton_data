import pandas as pd
from pandas import ExcelFile
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

cm = pd.read_excel('Смертность.xlsx')

cm['Год'] =  pd.to_datetime(cm['Год'], format='%Y')
cm.set_index('Год',inplace=True)
cm.sort_index(inplace=True)
#cm.drop(cm.columns[[0]], axis=1, inplace=True)

r1 = cm[['Алтайский край']]
r2 = cm[['Республика Марий Эл']]
decomp_alt = seasonal_decompose(r1, model='additive', freq=3, extrapolate_trend=1)
decomp = seasonal_decompose(r2, model='additive', freq=3, extrapolate_trend=1)

decomp.trend.to_excel(r'/Users/mikek/Downloads/RU-ME_trend.xlsx')

cm_ = cm.interpolate()
clmns = list(cm.columns.values)
cm_ = cm_.dropna()

for col in clmns:
    r = cm_[[col]]
    decomp = seasonal_decompose(r, model='additive', freq=3, extrapolate_trend=1)
    cm_[[col]] = decomp.trend

cm_.to_csv(r'trend.csv')


                        
#df1 = pd.DataFrame(data,columns=['Регион',  'Смертность на 1000 родившихся'])


