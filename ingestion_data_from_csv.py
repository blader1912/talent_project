import pandas as pd 

path = "C:/Users/bkade/OneDrive/Documentos/DATA/Traffic_Flow_Map_Volumes.csv"
data = pd.read_csv(path)

#DATA STANDARDIZATION
data.rename(columns = {'OBJECTID':'ID',
                            'STNAME':'CALLE',
                            'COUNT_LOCATION':'DESCR_LOCACION',
                            'YEAR':'AÑO',
                            'SEGKEY':'ID_SEGMENTO',
                            'AAWDT':'AVG_NUMERO_VEHICULOS',
                            'INPUT_STUDY_ID':'ID_ESTUDIO_TRAFICO'}, inplace = True)

data.to_csv(r'C:/Users\bkade/OneDrive/Documentos/INGESTION_DATA/Traffic_Flow_Map_Volumes_clean.csv', index=False)
print("Se ha estandarizado la data y se ha guardado correctamente en la capa de limpieza")