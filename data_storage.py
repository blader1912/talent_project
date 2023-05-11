import pandas as pd 

path = "C:/Users/bkade/OneDrive/Documentos/TRANSFORM_DATA/MEDIDA_TRAFICO.csv"



def guardado_data_medida(data):
    data = pd.read_csv(path)
    data.to_csv(r'C:/Users/bkade/OneDrive/Documentos/CLEAN_DATA/MEDIDA_TRAFICO_CLEAN.csv', index=False)
    return print("El guardado se ejecuto con exito")


guardado_data_medida(path)