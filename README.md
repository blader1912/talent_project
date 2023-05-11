# RETO DATA ENGINEER
REPOSITORIO PARA PRUEBA TECNICA 

Este repositorio consta de 4 archivos:
1) ingestion_data_from_csv.py se encarga de la lectura del archivo CSV en un folder especifico y le asigna una estructura en español a las columnas. El dataset final es enviado a la capa de ingesta 
2) transform_data.py se encarga de la transformacion y obtención de la medida. El dataset es enviado a la capa de transformacion
3) data_storage.py permite el guardado del dataset final en la carpeta CLEAN_DATA
4) DAG.py contiene todo lo referente a la estructura del DAG en Airflow donde hace el llamado a 3 scripts
5) docker-compose.yaml Es la imagen necesaria para correr Airflow

La solución fue desarollada pensando en un flujo regular de datos con capas de INGESTA, TRANSFORMACION Y CLEAN que permita operar uno tras de otro con buenas practicas de coding. Para poder correr los archivos asegurese de tener rutas correspondientes a su equipo local editando los archivos. 

Las carpetas DATA (Donde debe estar el csv original),INGESTION_DATA, TRANSFORM_DATA y CLEAN_DATA fueron creadas previamente y los scripts se encargan de mover los datos para un mejor versionamiento de la informacion.

El pipeline en airflow fue configurado para ser ejecutado todos los dias a las 7 AM y queda estructurado de esta manera
![pipeline](https://github.com/blader1912/talent_project/assets/90916311/f4a11576-c03e-495e-80b1-a65a88924b69)
