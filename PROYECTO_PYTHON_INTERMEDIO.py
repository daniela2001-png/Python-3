'''

The dataset we'll use was scraped and polished from Wikipedia.
It is made up of three CSV files, one with game data, one with TV data,
and one with halftime musician data for all 52 Super Bowls through 2018.
Let's take a look, using display() instead of print() since its output is much prettier in Jupyter Notebooks.

'''


# Import pandas
import pandas as pd

# Load the CSV data into DataFrames
super_bowls = pd.read_csv('datasets/super_bowls.csv')
tv = pd.read_csv('datasets/tv.csv')
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')

# Display the first five rows of each DataFrame
display(super_bowls.head())
display(tv.head())
display(halftime_musicians.head())

'''

2. Taking note of dataset issues
For the Super Bowl game data, we can see the dataset appears whole except for missing values in the backup
quarterback columns (qb_winner_2 and qb_loser_2), which make sense given most starting QBs
in the Super Bowl (qb_winner_1 and qb_loser_1) play the entire game.
From the visual inspection of TV and halftime musicians data, there is only one missing value displayed,
but I've got a hunch there are more. The Super Bowl goes all the way back to 1967, and the more granular columns
(e.g. the number of songs for halftime musicians) probably weren't tracked reliably over time.
Wikipedia is great but not perfect.

An inspection of the .info() output for tv and halftime_musicians shows us that there are multiple columns with null values.

'''

# Summary of the TV data to inspect
tv.info()

print('\n')

# Summary of the halftime musician data to inspect
halftime_musicians.info()

'''

OUTPUT: Here i USED THE METHOD .info():Print a concise summary of a DataFrame.

This method prints information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 53 entries, 0 to 52
Data columns (total 9 columns):
super_bowl          53 non-null int64
network             53 non-null object
avg_us_viewers      53 non-null int64
total_us_viewers    15 non-null float64
rating_household    53 non-null float64
share_household     53 non-null int64
rating_18_49        15 non-null float64
share_18_49         6 non-null float64
ad_cost             53 non-null int64
dtypes: float64(4), int64(4), object(1)
memory usage: 3.8+ KB


<class 'pandas.core.frame.DataFrame'>
RangeIndex: 134 entries, 0 to 133
Data columns (total 3 columns):
super_bowl    134 non-null int64
musician      134 non-null object
num_songs     88 non-null float64
dtypes: float64(1), int64(1), object(1)
memory usage: 3.2+ KB

'''

'''

3. Combined points distribution
For the TV data, the following columns have missing values and a lot of them:

total_us_viewers (amount of U.S. viewers who watched at least some part of the broadcast)
rating_18_49 (average % of U.S. adults 18-49 who live in a household with a TV that were watching for the entire broadcast)
share_18_49 (average % of U.S. adults 18-49 who live in a household with a TV in use that were watching for the entire broadcast)
For the halftime musician data, there are missing numbers of songs performed (num_songs) for about a third of the performances.

There are a lot of potential reasons for these missing values. Was the data ever tracked? Was it lost in history? Is the research effort to make this data whole worth it? Maybe. Watching every Super Bowl halftime show to get song counts would be pretty fun. But we don't have the time to do that kind of stuff now! Let's take note of where the dataset isn't perfect and start uncovering some insights.

Let's start by looking at combined points for each Super Bowl by visualizing the distribution. Let's also pinpoint the Super Bowls with the highest and lowest scores.

Task 3: Instructions
Plot a histogram of combined points then display the rows with the most extreme combined point outcomes.

From matplotlib, import the pyplot module under the alias plt.
Create a histogram of the combined_pts column from the super_bowls DataFrame.
Select the Super Bowl(s) where the combined score was less than 25.
%matplotlib inline is a magic Jupyter Notebook command that allows you to display your graphs without plt.show(). You only need to use plt.show()
in this notebook if you want to display the plot before other outputs (which you do in this task).

'''

# Import matplotlib and set plotting style
from matplotlib import pyplot as plt
%matplotlib inline
plt.style.use('seaborn')

# Plot a histogram of combined points
plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
display(super_bowls[super_bowls['combined_pts'] > 70])
display(super_bowls[super_bowls['combined_pts'] < 25])

'''

4. Distribución de diferencia de puntos 
La mayoría de los puntajes combinados son alrededor de 40-50 puntos,
con los extremos a una distancia aproximadamente igual en direcciones opuestas.
Subiendo a los puntajes combinados más altos en 74 y 75, encontramos dos juegos
con actuaciones dominantes de mariscal de campo. Uno incluso sucedió recientemente en el Super Bowl LII de 2018,
donde los Patriots de Tom Brady perdieron ante el perdedor Eagles 41-33 de Nick Foles para un puntaje combinado de 74.

Bajando a los puntajes combinados más bajos, tenemos el Super Bowl III y VII, que contó con defensas duras que dominaron.
También tenemos el Super Bowl IX en Nueva Orleans en 1975, cuyo puntaje de 16-6 se puede atribuir al mal tiempo.
El campo estaba resbaladizo por la lluvia de la noche a la mañana, y hacía frío a 46 ° F (8 ° C)
lo que dificultaba mucho a los Steelers y Vikings hacer mucha ofensiva. Este fue el segundo Super Bowl
más frío de la historia y el último que se jugó en condiciones climáticas adversas durante más de 30 años.
La NFL se dio cuenta de que a la gente le gustan los puntos, supongo.

ACTUALIZACIÓN: En el Super Bowl LIII en 2019, los Patriots y los Rams rompieron
el récord del Super Bowl con la puntuación más baja con una puntuación combinada de 16 puntos (13-3 para los Patriots).

Echemos un vistazo a la diferencia de puntos ahora.

'''

# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
display(super_bowls[super_bowls['difference_pts'] == 1])
display(super_bowls[super_bowls['difference_pts'] >= 35])

'''

Task 5: Instructions
Import seaborn and plot household share vs. point difference.

Import the seaborn module under the alias sns.
Fill in the x argument of sns.regplot() with the point difference column
Fill in the y argument of sns.regplot() with the household share column.
Remember column names are represented as strings!

seaborn's regplot() is like scatter plot except more specialized for visualizing linear relationships.
It draws a scatterplot, then fits a regression model and plots the resulting regression line and a 95%
confidence interval for that regression.

'''

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Import seaborn
import seaborn as sns

# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts' , y='share_household', data=games_tv)

'''

6. Viewership and the ad industry over time
The downward sloping regression line and the 95% confidence interval for that regression suggest that bailing on the game
if it is a blowout is common. Though it matches our intuition, we must take it with a grain of salt because the linear
relationship in the data is weak due to our small sample size of 52 games.

Regardless of the score though, I bet most people stick it out for the halftime show,
which is good news for the TV networks and advertisers. A 30-second spot costs a pretty $5 million now
, but has it always been that way? And how have number of viewers and household ratings trended alongside ad cost?
We can find out using line plots that share a "Super Bowl" x-axis.

Task 6: Instructions
Create three line plots using the tv DataFrame to compare viewers, rating, and ad cost.

For the first plot, plot super_bowl on the x-axis, avg_us_viewers on the y-axis, and set the line color to '#648FFF'.
For the second plot, plot super_bowl on the x-axis, rating_household on the y-axis, and set the line color to '#DC267F'.
For the third plot, plot super_bowl on the x-axis, ad_cost on the y-axis, and set the line color to '#FFB000'.

'''
# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF') #accedo como tv.super_bowl ya que tv es el dataframe de data game tv
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improve the spacing between subplots
plt.tight_layout() # deja espacios entre cada plot

'''

Task 7: Instructions
Filter and display the musicians for halftime shows up to and including Super Bowl XXVII.

Using halftime_musicians, select the musicians that performed in halftime shows up to and including Super Bowl XXVII (27)
(i.e. Michael Jackson's performance).
The last line of code in a Jupyter Notebook cell automatically gets it output displayed so you don't need to use display()
here.

'''
# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
halftime_musicians[halftime_musicians.super_bowl <= 27]

'''

Tarea 8 : Instrucciones
Seleccione y muestre a los músicos con más de un espectáculo de medio tiempo.

El nuevo halftime_appearances DataFrame tiene dos columnas musiciany super_bowl, donde super_bowl
ahora contiene los recuentos de espectáculos de medio tiempo para cada músico.
Seleccione los músicos que han aparecido en más de un espectáculo de medio tiempo.
El halftime_appearancescódigo está precargado porque no estaba cubierto en el requisito previo para este proyecto,
Intermediate Python for Data Science . La agrupación y la reorganización de datos
están cubiertas en Manipulación de marcos de datos con pandas .

'''
# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians with more than one halftime show appearance
halftime_appearances[halftime_appearances['super_bowl'] > 1]

'''

Tarea 9 : Instrucciones
Modifique el histograma de la cantidad de canciones interpretadas para músicos que no pertenecen a la banda.

En la plt.hist()función, establezca el número de argumentos de bins igual a most_songs
(el mayor número de canciones interpretadas en un espectáculo de medio tiempo por un solo músico).
Agregue una etiqueta x con 'Number of Songs Per Halftime Show Performance'.
No se puede filtrar "Band" porque Bruce Springsteen y E Street Band se presentaron en el Super Bowl XLIII.

El no_bands código está precargado porque no estaba cubierto en Python intermedio para ciencia de datos .
El .str.contains()método está cubierto en Limpieza de datos en Python .

9. ¿Quién interpretó más canciones en un espectáculo de medio tiempo? 
La mundialmente famosa Banda Marchante de Tigres de la Universidad Estatal de Grambling se lleva la corona
con seis apariciones. Beyoncé, Justin Timberlake, Nelly y Bruno Mars son los únicos músicos post-Y2K
con múltiples apariciones (dos cada uno).

De nuestras inspecciones anteriores, la num_songscolumna tiene muchos valores faltantes:

Muchas de las bandas de música no tienen num_songsentradas.
Para las bandas que no marchan, los datos faltantes comienzan a ocurrir en el Super Bowl XX.
Filtremos las bandas de música filtrando a los músicos con la palabra "Marchando" en ellos y la palabra "Espíritu"
(una convención de nomenclatura común para las bandas de música es "Espíritu de [algo]"). 
Luego, filtraremos para Super Bowls después del Super Bowl XX para abordar el problema de datos faltantes,
luego veamos quién tiene la mayor cantidad de canciones.

'''

# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
# ...and display the top 15
display(no_bands.head(15))

'''

10. Conclusión 
Entonces, la mayoría de los músicos que no pertenecen a la banda hacen 1-3 canciones por espectáculo de medio tiempo.
Es importante tener en cuenta que la duración del espectáculo de medio tiempo es fija (aproximadamente 12 minutos),
por lo que las canciones por actuación son más una medida de cuántas canciones exitosas tienes. JT se fue en 2018, wow.
11 canciones! Diana Ross ocupa el segundo lugar con 10 en su popurrí en 1996.

En este cuaderno, cargamos, limpiamos y luego exploramos los datos del juego del Super Bowl
la televisión y el espectáculo de medio tiempo. Visualizamos las distribuciones de puntos combinados,
diferencias de puntos y presentaciones de medio tiempo usando histogramas. Utilizamos gráficos de líneas para ver
cómo los aumentos en el costo de los anuncios van a la zaga de los aumentos de audiencia.
Y descubrimos que los reventones parecen provocar una caída en los espectadores.

El Big Game de este año estará aquí antes de que te des cuenta. ¿Quién crees que ganará el Super Bowl LIII?


aqui termine apostando 

'''

# 2018-2019 conference champions
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = patriots
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)

