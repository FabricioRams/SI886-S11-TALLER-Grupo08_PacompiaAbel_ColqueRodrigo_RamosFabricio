# Guía de Uso de Recursos y Laboratorio · Taller Semana 11
## Diagnóstico de Gobierno Digital y Tablero de Línea Base
**SI-886 · Planeamiento Estratégico de Tecnologías de la Información**  
**Caso de Aplicación:** Empresa 08 — **EPS AGUAS DEL SUR S.A.**  
**Estudiante / Equipo:** Ramos Fabricio  
**Universidad Privada de Tacna** · Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas  

---

## 1. Propósito de este Repositorio

Este repositorio contiene la solución técnica, programática y analítica del **Taller de Laboratorio de la Semana 11**, aplicando el marco normativo nacional de Gobierno Digital (D.L. 1412, D.S. 029-2021-PCM, R.S.G.D. 005-2018-PCM/SEGDI) a la empresa pública de saneamiento **EPS AGUAS DEL SUR S.A.** (Tacna, Perú).

A través de estos recursos, se evalúa la situación actual del gobierno digital en 8 ejes normativos, se levanta el catálogo de servicios con su nivel de digitalización, se calcula el nivel medio ponderado por volumen, se aplica la prueba del principio de una sola vez, se determinan los indicadores sin línea base y se construye el tablero de inteligencia institucional.

---

## 2. Estructura del Repositorio y Ubicación de Recursos

```text
SI886-S11-TALLER-RamosFabricio/
├── EMPRESA-08-eps-aguas-del-sur/              # Archivos de entrada del banco de casos
│   ├── FICHA.md                              # Ficha técnica institucional de la EPS
│   ├── mesa-de-servicio-y-sla.md             # Registro de atenciones, canales y acuerdos de TI
│   └── cuestionario-diagnostico.md           # Encuesta de diagnóstico institucional aplicada
├── 06_gobierno_digital/                      # Entregables técnicos del PETI (Sección 6.1)
│   ├── GD01_catalogo_servicios.csv           # Catálogo con 9 servicios y niveles de digitalización
│   ├── GD02_analisis_servicios.py            # Script Python de análisis volumétrico y brechas
│   ├── GD03_ejes.csv                         # Matriz de diagnóstico de 8 ejes (18 indicadores)
│   ├── GD04_madurez.py                       # Script Python de cálculo de madurez y radar polar
│   ├── GD05_carga_tablero.py                 # Script de persistencia a PostgreSQL / Metabase
│   └── 6.1_situacion_actual.md               # Redacción completa de la Sección 6.1 del PETI
├── 04_normativa/                             # Insumos normativos y de capacidad complementarios
│   ├── NO03_matriz_cumplimiento.csv          # Matriz de cumplimiento legal (D.L. 1412, SUNASS, etc.)
│   └── MG03_capacidad.csv                    # Capacidad actual vs objetivo de procesos de negocio
├── graficos/                                 # Gráficos generados para el informe y tablero
│   ├── GD_servicios.png                      # Visualización del catálogo y brechas
│   ├── GD_madurez.png                        # Radar polar de madurez en 8 ejes
│   ├── tablero_01_servicios.png              # Card Metabase: Digitalización por servicio
│   ├── tablero_02_kpi_ponderado.png          # Card Metabase: KPI nivel ponderado por volumen
│   ├── tablero_03_madurez_ejes.png           # Card Metabase: Madurez por eje normativo
│   ├── tablero_04_cumplimiento.png           # Card Metabase: Anillo de cumplimiento normativo
│   ├── tablero_05_capacidad.png              # Card Metabase: Capacidad actual vs objetivo
│   ├── tablero_06_sin_linea_base.png         # Card Metabase: Indicadores sin línea base
│   └── tablero_dashboard_completo.png        # Tablero integral Metabase unificado
├── evidencias/S11/                           # Evidencias obligatorias de ejecución
│   ├── salidas/                              # Logs de salida de scripts de terminal
│   │   ├── salida_GD02_servicios.txt         # Evidencia de ejecución de GD02
│   │   └── salida_GD04_madurez.txt           # Evidencia de ejecución de GD04
│   └── tablero_dashboard_completo.png        # Evidencia de captura del tablero
├── 3-TALLER.md                               # Guía oficial del taller y lista de comprobación
├── docker-compose.yml                        # Orquestación de contenedores (PostgreSQL 16 + Metabase)
├── generar_tableros_metabase.py              # Script utilitario para renderizar las vistas del tablero
├── README.md                                 # Esta guía de uso de recursos
└── INFORME_TALLER_S11.md                     # Informe final detallado del proyecto para Google Docs
```

---

## 3. Descripción y Uso de los Archivos de Caso (EMPRESA-08)

1. **`EMPRESA-08-eps-aguas-del-sur/FICHA.md`:**
   - **Contenido:** Contiene la identidad de la empresa (86 000 conexiones, S/ 74.1 millones de presupuesto), gobernanza de TI (6 personas, sin Comité formal ni SGSI), los sistemas de información (Comercial en servidor propio, SCADA compartiendo switches con red administrativa, SIAF, etc.) y los riesgos conocidos.
   - **Uso en el Taller:** Sirve como fuente de hechos verificables para el Paso A (procesos de negocio D y catálogo) y el Paso B (evidencia para los 8 ejes normativos).

2. **`EMPRESA-08-eps-aguas-del-sur/mesa-de-servicio-y-sla.md`:**
   - **Contenido:** Describe los canales de atención de TI, la hoja de cálculo con 2 047 registros de atenciones (102 tickets aún abiertos), los niveles de servicio declarados (no medidos ni reportados) y problemas recurrentes.
   - **Uso en el Taller:** Permite evaluar la madurez de la gestión del servicio (ITIL/ISO 20000), identificar los servicios que TI reconoce y constatar la ausencia de monitoreo formal (SLA).

3. **`EMPRESA-08-eps-aguas-del-sur/cuestionario-diagnostico.md`:**
   - **Contenido:** Encuesta voluntaria interna respondida por solo 22 de 312 trabajadores (7.05% de participación), formulada con sesgos evidentes y preguntas inductivas.
   - **Uso en el Taller:** Permite fundamentar por qué sus datos no constituyen una línea base válida para el diagnóstico estratégico, justificando formalmente declarar «No se mide» en indicadores clave e incorporar proyectos de instrumentación en el PETI.

---

## 4. Guía de Ejecución Paso a Paso

### Requisitos Previos:
- Python 3.10 o superior con las librerías: `pandas`, `matplotlib`, `numpy`.
- (Opcional para persistencia SQL) `SQLAlchemy`, `psycopg2-binary`.
- (Opcional para despliegue de contenedores) Docker Desktop.

### Paso 1: Ejecutar el análisis del catálogo de servicios (`GD02`)
Analiza los 9 servicios catalogados, calcula el promedio simple vs. ponderado, cuantifica documentos redundantes y exporta el gráfico:
```bash
cd 06_gobierno_digital
python GD02_analisis_servicios.py
```
- **Salida esperada:** Consola detallada y gráfico generado en `../graficos/GD_servicios.png`.
- **Log guardado en:** `evidencias/S11/salidas/salida_GD02_servicios.txt`.

### Paso 2: Ejecutar el diagnóstico de madurez por ejes (`GD04`)
Evalúa los 8 ejes normativos, identifica indicadores sin línea base y genera el radar polar:
```bash
cd 06_gobierno_digital
python GD04_madurez.py
```
- **Salida esperada:** Promedio por eje, nivel global (1.12 - Inicial/Reactivo), lista de 3 indicadores sin línea base y gráfico en `../graficos/GD_madurez.png`.
- **Log guardado en:** `evidencias/S11/salidas/salida_GD04_madurez.txt`.

### Paso 3: Renderizar las visualizaciones del Tablero de Línea Base
Para generar los 6 componentes visuales y el dashboard completo estilo Metabase:
```bash
# Desde la raíz del repositorio
python generar_tableros_metabase.py
```
- **Salida esperada:** 6 imágenes de tarjetas (`tablero_01_servicios.png` a `tablero_06_sin_linea_base.png`) y el dashboard consolidado `tablero_dashboard_completo.png` en `graficos/` y `evidencias/S11/`.

### Paso 4: Despliegue del Tablero en Metabase y PostgreSQL con Docker Compose

Para desplegar la infraestructura de BI de manera reproducible y en un solo paso, se provee el archivo `docker-compose.yml` que orquesta PostgreSQL 16 y Metabase en una red privada virtual (`peti_net`) con volúmenes de almacenamiento persistente (`peti_pgdata` y `peti_metabase_data`):

#### 4.1 Iniciar los contenedores:
```bash
# Desde la raíz del repositorio
docker compose up -d
```
* **PostgreSQL (`peti_db`):** Publicado en `127.0.0.1:5433` (mapeado al 5432 interno) con usuario `peti`, base `peti` y contraseña `peti_lab`. Cuenta con healthcheck para asegurar que la base esté lista antes de que Metabase intente conectarse.
* **Metabase (`peti_metabase`):** Publicado en `http://127.0.0.1:3001` (mapeado al 3000 interno), conectado a la red interna y con resolución de host configurada.

#### 4.2 Verificar el estado de los servicios:
```bash
docker compose ps
# Para ver los logs en tiempo real:
docker compose logs -f
```

#### 4.3 Cargar las tablas de datos desde Python a PostgreSQL:
Una vez que los contenedores estén activos:
```bash
cd 06_gobierno_digital
python GD05_carga_tablero.py
```
El script leerá `GD01_catalogo_servicios.csv`, `GD03_ejes.csv`, `NO03_matriz_cumplimiento.csv` y `MG03_capacidad.csv`, poblando automáticamente las tablas `servicios`, `ejes_gd`, `cumplimiento` y `capacidad` en PostgreSQL.

#### 4.4 Configuración inicial en Metabase:
1. Abra su navegador en `http://127.0.0.1:3001`.
2. Complete el asistente de bienvenida (cree la cuenta de administrador local).
3. En **Admin → Databases → Add Database**:
   - **Database type:** PostgreSQL
   - **Host:** `peti_db` (o `host.docker.internal`)
   - **Port:** `5432` (si usa `peti_db`) o `5433` (si usa `host.docker.internal`)
   - **Database name:** `peti`
   - **Database username:** `peti`
   - **Database password:** `peti_lab`
4. Cree las 6 visualizaciones mínimas requeridas.

#### 4.5 Detener o reiniciar la infraestructura:
```bash
# Para detener los contenedores preservando los datos:
docker compose down

# Para reiniciar limpiando los volúmenes (si se desea empezar de cero):
docker compose down -v
```

> **Alternativa sin Compose (comandos individuales de `docker run`):**
> Si prefiere ejecutar los contenedores por separado:
> ```bash
> docker run -d --name peti_db -e POSTGRES_USER=peti -e POSTGRES_PASSWORD=peti_lab \
>   -e POSTGRES_DB=peti -p 127.0.0.1:5433:5432 -v peti_pgdata:/var/lib/postgresql/data postgres:16
>
> docker run -d --name peti_metabase -p 127.0.0.1:3001:3000 \
>   --add-host=host.docker.internal:host-gateway \
>   -e MB_DB_TYPE=postgres -e MB_DB_DBNAME=peti -e MB_DB_PORT=5433 \
>   -e MB_DB_USER=peti -e MB_DB_PASS=peti_lab -e MB_DB_HOST=host.docker.internal \
>   metabase/metabase
> ```

---

## 5. Documentación e Informe para Google Docs

El informe exhaustivo del proyecto se encuentra en el archivo:
- **`INFORME_TALLER_S11.md`**

Dicho documento contiene:
1. Carátula oficial según el formato de la Universidad Privada de Tacna.
2. Desarrollo detallado de los Pasos A, B, C, D, E y F con todas las tablas completas.
3. Lista de comprobación 3.2 con verificación ítem por ítem.
4. Enlace y referencia de todas las figuras obtenidas con el formato requerido:  
   `Figura X: Descripción breve de lo que es la imagen.`
5. Análisis de la pregunta de transferencia de riesgo sobre consecuencias organizacionales reales.
