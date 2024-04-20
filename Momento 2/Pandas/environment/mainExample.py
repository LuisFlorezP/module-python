import pandas as pd 

variable_series = [1, 2, 3, 4, 5]
series = pd.Series(variable_series) 
print('Series:')
print(series) 

variable_data_frame = {
    'Nombre': ['Yarleyda', 'Yovanny', 'Yesica', 'Ricardo', 'Berta'], 
    'Edad':[40, 43, 47, 72, 69],  
    'Ciudad': ['Medellin','Nueva York','Istmina', 'Medellin', 'Istmina']
} 
data_frame = pd.DataFrame(variable_data_frame) 
print('\nDataFrame:')
print(data_frame) 