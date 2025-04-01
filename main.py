
import pandas as pd
import numpy as np



def learquivo():
    
    df = pd.read_csv('dados\CONSUMO.csv')
    return df



if __name__=="__main__":

    print(learquivo()['Consumo'])


