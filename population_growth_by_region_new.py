
# coding: utf-8

# In[5]:

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
from matplotlib import style
import matplotlib.ticker as mticker

style.use('mystylepop')
fig, ax = plt.subplots(1, 1, figsize=(16, 8))

## reading data from csv
population_by_country = '/home/ketka/Git_projects/World_population_1960_2014_graph_by_region_country/datasets/population_by_country_new.csv'
african_countries = '/home/ketka/Git_projects/World_population_1960_2014_graph_by_region_country/datasets/african_countries.csv'
other_countries = '/home/ketka/Git_projects/World_population_1960_2014_graph_by_region_country/datasets/europe_and_others.csv'

years = []
for i in range(1960, 2015):
    years.append(i)
    
pop_by_year = [[]]*len(years)
pp = [[]]*len(years)

for i in range(0,55):
    pp[i] = []

countries_pop = []
africa_c = []

namerica_c = []
samerica_c = []
europe_c = []
nonmuslim_asia_c = []
muslim_c = []

## Reading and appending all the countries and population for every year
## countries_pop - list of all the countries
## pp[i][j] - population by country for a year, where i=year, j=country
with open(population_by_country) as ff:
        reader_ff = csv.reader(ff)
        for i in range(1,6):
            next(reader_ff)
        for row in reader_ff:
            countries_pop.append(str(row[0]))
            for j in range(0, 55):
                pp[j].append(int(row[j+4]))
                
## Reading and appending all african countries         
with open(african_countries) as fafrica:
        reader_fafrica = csv.reader(fafrica)
        for i in range(0,5):
            next(reader_fafrica)
        for row in reader_fafrica:
            africa_c.append(str(row[0]))
            
## Reading and appending all other countries         
with open(other_countries) as fother:
        reader_fother = csv.reader(fother)
        next(reader_fother)
        for row in reader_fother:
            europe_c.append(str(row[0]))
            namerica_c.append(str(row[1]))
            samerica_c.append(str(row[2]))
            nonmuslim_asia_c.append(str(row[3]))
            muslim_c.append(str(row[4]))            
            
        
## Selecting African only countries - their ids            
african_numbers = []
for i in range(0, len(countries_pop)):
    if countries_pop[i] == 'Dem. Rep. Congo' or countries_pop[i] == 'Somaliland' or countries_pop[i] == 'S. Sudan' or countries_pop[i] == 'Eq. Guinea':
        african_numbers.append(i)
    for j in range(0, len(africa_c)):
        if countries_pop[i]== africa_c[j]:
              african_numbers.append(i)
                
## Selecting country ids by defined region
def search_country_number(x_numbers, xregion_c):                
    for i in range(0, len(countries_pop)):
        for j in range(0, len(xregion_c)):
            if countries_pop[i]== xregion_c[j]:
                  x_numbers.append(i)  
                    
## Europe:
european_numbers = []
search_country_number(european_numbers, europe_c) 
                
## North America:  
namerican_numbers = []
search_country_number(namerican_numbers, namerica_c)

## South America:
samerican_numbers = []
search_country_number(samerican_numbers, samerica_c)

## Nonmuslim Asia:
nonmuslim_asia_numbers = []
search_country_number(nonmuslim_asia_numbers, nonmuslim_asia_c)

## Muslim countries (>75% of muslims):
muslim_numbers = []
search_country_number(muslim_numbers, muslim_c)

africa = []
namerica = []
samerica = []
europe = []
india = []
china = []
nonmuslim_asia = []
muslim = []

## appending the sum of population numbers by year by countries in defined region
## where:
## x_numbers - country ids (in countries_pop)
## xregion  - region
def region(x_numbers,xregion):
        x = 0
        for t in range(0, len(x_numbers)):    
            x += pp[k][x_numbers[t]]
        xregion.append(x)

## appending population numbers by year by country or region
for k in range(0, len(years)):
    india.append(pp[k][99])
    china.append(pp[k][38])    
    region(african_numbers,africa)
    region(european_numbers,europe)
    region(namerican_numbers,namerica)
    region(samerican_numbers,samerica)
    region(nonmuslim_asia_numbers,nonmuslim_asia)
    region(muslim_numbers,muslim)

# Limit the range of the plot to only where the data is.
# Avoid unnecessary whitespace.
plt.xlim(1959.5, 2014)
plt.ylim(1.25, 1400000000)

regions = [india, china,  africa, europe, namerica, samerica, nonmuslim_asia, muslim]
colors = ['#edc951', '#eb6841', '#cc2a36', '#4f372d',
          '#00a0b0', '#c71a57', '#1cb6a3', '#269f10']
names = ['India', 'China', 'Africa', 'Europe', 'North America', 
         'South America', 'Nonmuslim Asia', 'Countries with\n>75% of muslims']
y_pos = [1,2,3,4,5,6,7,8]
## setting vertical positions for texts
for l in range(0, len(colors)):
    if regions[l] == namerica: 
        y_pos[l] = (max(regions[l])-95000000)
    if regions[l] == samerica:
        y_pos[l] = (max(regions[l])-90000000)
    if regions[l] == nonmuslim_asia:
        y_pos[l] = (max(regions[l])-75000000)    
    if regions[l] == india:
        y_pos[l] = (max(regions[l])-65000000)
    if regions[l] == africa:
        y_pos[l] = (max(regions[l])-220000000) 
    if regions[l] == muslim:
        y_pos[l] = (max(regions[l])-245000000) 
    if regions[l] == china:
        y_pos[l] = (max(regions[l])-10000000)  
    if regions[l] == europe:
        y_pos[l] = (max(regions[l])+10000000)  
        
## plotting
for u in range(0, len(colors)):
    fig = plt.plot(years, regions[u],colors[u], lw=2.5)
    plt.text(2007, y_pos[u], names[u], fontsize=14, color=colors[u])

## Removing tick marks and tick lines
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='on', left='off', right='off', labelleft='on')    
    
plt.xlabel('Years',fontsize=18, color='#132c41')
plt.locator_params(axis = 'x', nbins = 20)
plt.ylabel('Population', fontsize=18, color='#132c41')
plt.locator_params(axis = 'y', nbins = 20)
plt.ticklabel_format(style='plain')
plt.title('Population growth by country/region', fontsize=20, ha='center', color='#132c41')
plt.show()
#plt.savefig('Population_growth_by_region.png')

