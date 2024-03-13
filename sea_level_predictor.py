import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level',s=40, marker="+")
    # Create scatter plot
    # Create first line of best fit

    reg=linregress(x=df.Year, y=df['CSIRO Adjusted Sea Level'])
    a=reg.slope
    b=reg.intercept
    years=pd.array(range(1880, 2051))
    rise=years*a + b
    plt.plot(years, rise,'r')
    
    # Create second line of best fit
    reg=linregress(x=df[df['Year'] > 1999 ]['Year'], y=df[df['Year'] > 1999 ]['CSIRO Adjusted Sea Level'])
    a=reg.slope
    b=reg.intercept
    years=pd.array(range(2000, 2051))
    rise=years*a + b
    plt.plot(years, rise,'g')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
