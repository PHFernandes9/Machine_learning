import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def learquivo():
    
    df = pd.read_csv('dados\CONSUMO.csv')
    return df

# def grafico(df):


def plota_graficos(df):

    Norte = df[df['Regiao']=='Norte'] 
    y =Norte['Consumo']
    x =Norte['Data']

    plt.bar(x,y)
    plt.show()
    print(Norte)



if __name__=="__main__":

    dados = (learquivo())
    plota_graficos(dados)

