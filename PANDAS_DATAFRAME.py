'''

Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.

'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, etiq in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = etiq['country'].upper()


# Print cars
print(cars)

'''

OUTPUT(ANSWER):

     cars_per_cap      ...              COUNTRY
US            809      ...        UNITED STATES
AUS           731      ...            AUSTRALIA
JPN           588      ...                JAPAN
IN             18      ...                INDIA
RU            200      ...               RUSSIA
MOR            70      ...              MOROCCO
EG             45      ...                EGYPT

[7 rows x 4 columns]


'''


'''

ESTA ES LA OTRA MANERA DE MOSTRAR EN MAYUSCULA LA COLUMNA PAISES
EN PANDAS DATFRAME CON LA FUNCION (apply())

'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars["COUNTRY"] = cars["country"].apply(str.upper)
    
print(cars)

'''

Y NOS DA LA MISMA SALIDA QUE QUEREMOS:

     cars_per_cap      ...              COUNTRY
US            809      ...        UNITED STATES
AUS           731      ...            AUSTRALIA
JPN           588      ...                JAPAN
IN             18      ...                INDIA
RU            200      ...               RUSSIA
MOR            70      ...              MOROCCO
EG             45      ...                EGYPT

[7 rows x 4 columns]

'''
