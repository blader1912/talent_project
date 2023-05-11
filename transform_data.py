import pandas as pd 

#REQUERIMENTS
main_table = "C:/Users/bkade/OneDrive/Documentos/INGESTION_DATA/Traffic_Flow_Map_Volumes_clean.csv"

#INGEST
def read_data_clean(data):
    data = pd.read_csv(data['raw_data'])
    return {"raw_clean_data": data}


#TRANSFORMATIONS
def medida_total_accidentes(data):
    columns_to_select = [ 'CALLE','AÑO','AVG_NUMERO_VEHICULOS']
    data = data['raw_clean_data']
    trafic_measure = data[columns_to_select].groupby(['AÑO','CALLE']).sum('AVG_NUMERO_VEHICULOS').reset_index()
    return {"dataframe_trafic_measure":trafic_measure} 


def guardado_data_medida(data):
    data = data['dataframe_trafic_measure']
    data.to_csv(r'C:/Users/bkade/OneDrive/Documentos/TRANSFORM_DATA/MEDIDA_TRAFICO.csv', index=False)
    return {"final_data":data}




#RUN PIPELINE
dataframes = {'raw_data':main_table}

functions_list = [
        read_data_clean,
        medida_total_accidentes,
        guardado_data_medida
    ]

for func in functions_list:
    dataframe = func(dataframes)
    print(func)
    dataframes.update(dataframe)


print("LA TRANSFORMACION CORRIO CORRECTAMENTE")