import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

country = 'Portugal'
population = 2e6

confirmed_df = pd.read_csv('covid-data/time_series_covid19_confirmed_global.csv')
recovered_df = pd.read_csv('covid-data/time_series_covid19_recovered_global.csv')
deaths_df = pd.read_csv('covid-data/time_series_covid19_deaths_global.csv')

def clean_data(df, country):
    df = df[df['Country/Region']==country]\
            .loc[:, '1/22/20':'3/25/21']

    # Check if this country has multiple regions
    if len(df) > 1:
        df = df.sum()

    df = df.transpose().reset_index(drop=True)

    return df

def draw_plot(confirmed_df, deaths_df, recovered_df, country):

    I_df = clean_data(confirmed_df, country)
    D_df = clean_data(deaths_df, country) #I_df, S_df, D_df
    R_df = clean_data(recovered_df, country)

    # Calculate S_df
    ind = I_df.columns[0] # the column name for this country
    S_lst = [population - I for I in I_df[ind]]
    for i in range(len(D_df)):
        S_lst[i] -= D_df[ind][i]

    ts = [t for t in range(len(I_df))]

    fig, ax = plt.subplots()

    # ax.plot(ts, D_df, label='D')
    ax.plot(ts, S_lst, label='S')
    ax.plot(ts, I_df, label='I')
    ax.plot(ts, R_df, label='R')
    ax.legend()
    ax.set_title(f'SIR of {country} COVID data')
    ax.set_xlabel('Time')
    ax.set_ylabel('Number of People')
    plt.savefig(f'../doc/final/image/var1_SIR of {country} COVID Data')

