# 06_gobierno_digital/GD05_carga_tablero.py
import sys
import pandas as pd

# Manejo flexible de sqlalchemy
try:
    from sqlalchemy import create_engine
    has_sqlalchemy = True
except ImportError:
    has_sqlalchemy = False

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("================================================================")
print("  EPS AGUAS DEL SUR S.A. - CARGA DE TABLERO DE LÍNEA BASE (METABASE)")
print("================================================================")

if not has_sqlalchemy:
    print("Aviso: 'sqlalchemy' no se encuentra instalado en este entorno de Python.")
    print("Para instalar las dependencias requeridas:")
    print("  pip install sqlalchemy psycopg2-binary pandas")
    print("\nComandos Docker para desplegar PostgreSQL y Metabase:")
    print("  docker run -d --name peti_db -e POSTGRES_USER=peti -e POSTGRES_PASSWORD=peti_lab -e POSTGRES_DB=peti -p 127.0.0.1:5433:5432 postgres:16")
    print("  docker run -d --name peti_metabase -p 127.0.0.1:3001:3000 --add-host=host.docker.internal:host-gateway -e MB_DB_TYPE=postgres -e MB_DB_DBNAME=peti -e MB_DB_PORT=5433 -e MB_DB_USER=peti -e MB_DB_PASS=peti_lab -e MB_DB_HOST=host.docker.internal metabase/metabase")
    sys.exit(0)

eng = create_engine("postgresql://peti:peti_lab@127.0.0.1:5433/peti")

try:
    print("Cargando GD01_catalogo_servicios.csv -> tabla 'servicios'...")
    pd.read_csv("GD01_catalogo_servicios.csv").to_sql("servicios", eng, if_exists="replace", index=False)

    print("Cargando GD03_ejes.csv -> tabla 'ejes_gd'...")
    pd.read_csv("GD03_ejes.csv").to_sql("ejes_gd", eng, if_exists="replace", index=False)

    print("Cargando NO03_matriz_cumplimiento.csv -> tabla 'cumplimiento'...")
    pd.read_csv("../04_normativa/NO03_matriz_cumplimiento.csv").to_sql("cumplimiento", eng, if_exists="replace", index=False)

    print("Cargando MG03_capacidad.csv -> tabla 'capacidad'...")
    pd.read_csv("../04_normativa/MG03_capacidad.csv").to_sql("capacidad", eng, if_exists="replace", index=False)

    print("\n[OK] Datos cargados exitosamente en PostgreSQL.")
    print("Acceda a Metabase para armar las visualizaciones: http://127.0.0.1:3001")
except Exception as ex:
    print(f"\n[AVISO] No se pudo conectar a la base de datos PostgreSQL local: {ex}")
    print("Verifique que el contenedor Docker 'peti_db' se encuentre en ejecución en el puerto 5433.")
