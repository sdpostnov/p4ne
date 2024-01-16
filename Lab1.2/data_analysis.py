from matplotlib import pyplot
from openpyxl import load_workbook
def getvalue(x): return x.value
wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']
#list как map? Какая то встроенная команда? Спросить что есть кроме list.
years=list(map(getvalue,sheet['A'][1:]))
temperature=list(map(getvalue,sheet['C'][1:]))
sun=list(map(getvalue,sheet['D'][1:]))
pyplot.plot(years,temperature,label='Температура')
pyplot.plot(years,sun,label='Активность солнца')
pyplot.show()