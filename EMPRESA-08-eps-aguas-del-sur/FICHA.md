<div align="center">
  <img src="../../../Logos/logo_universidad.png" alt="Universidad Privada de Tacna" height="62">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="../../../Logos/logo_escuela_sistemas.jpeg" alt="Escuela Profesional de Ingeniería de Sistemas" height="62">
</div>

<p align="center">
  <strong>Universidad Privada de Tacna</strong><br>
  Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas
</p>

<h1 align="center">EPS AGUAS DEL SUR S.A.</h1>

<p align="center">
  Banco de casos · <strong>Empresa 08</strong> · Servicio de agua potable y alcantarillado<br>
  <em>Organización ficticia. Cualquier parecido con una empresa real es coincidencia.</em>
</p>

---

## A. Ficha de la organización

| Campo | Contenido |
|---|---|
| **Razón social** | EPS AGUAS DEL SUR S.A. |
| **Sector** | Servicio de agua potable y alcantarillado |
| **Domicilio fiscal** | Tacna |
| **RUC** | 20125XXXXX *(enmascarado; es una organización ficticia)* |
| **Años de operación** | 44 |
| **Personal en planilla** | 312 |
| **Personal adicional** | 58 por servicios |
| **Facturación / presupuesto anual** | S/ 74.1 millones |
| **Mercado o población atendida** | 86 000 conexiones domiciliarias |
| **Naturaleza** | **Entidad pública.** Le aplica el marco de gobierno digital y el control gubernamental. |
| **Entidades que la regulan o supervisan** | SUNASS · OTASS · ANA · Contraloría General · PCM-SGTD · ANPD |

**Objetivo declarado para TI en el periodo.** Segmentar la red industrial y dar trazabilidad al ciclo comercial ante el regulador.

## B. Estructura y gobierno

| | |
|---|---|
| **Personal de TI** | 6 personas |
| **Responsable de TI** | Jefe del Departamento de Tecnologías de la Información, reporta a Gerencia de Administración |
| **Comité de TI o de gobierno digital** | Se reúne, pero no deja actas. |
| **Política de seguridad de la información** | No existe. |
| **Presupuesto de TI del periodo** | S/ 1 080 000 · 1.46 % de la facturación |

> **Marco de gobierno digital.** Por ser entidad pública, le son exigibles el Decreto Legislativo 1412, el D. S. 029-2021-PCM y la designación del Comité y del Líder de Gobierno Digital (R.M. 119-2018-PCM). Verificar el estado real de cada obligación es parte del diagnóstico.

## C. Sistemas de información

| Sistema | Descripción | Dónde corre | Desde | ¿Tiene soporte vigente? |
|---|---|---|---|---|
| **Sistema comercial** | **Producto del sector saneamiento.** Catastro, facturación y cobranza | Servidor propio | 2014 | Sí |
| **SCADA de plantas y reservorios** | Sistema del proveedor de automatización | Red industrial separada | 2019 | Sí |
| **Micromedición y lectura** | Terminales portátiles del proveedor | Mixto | 2018 | Sí |
| **SIAF y patrimonio** | Sistemas del MEF | Cliente local | 2010 | MEF |
| **Atención de reclamos** | Formulario web y hoja de cálculo | Hosting propio | 2021 | No |

**El problema que la organización reconoce.** La red del SCADA de plantas comparte switches con la red administrativa desde una ampliación hecha en 2023, pese a que el diseño original las separaba.

## D. Procesos de negocio

| N.º | Proceso | ¿Qué sistema lo soporta? |
|---|---|---|
| 1 | Catastro comercial de usuarios | Sistema comercial |
| 2 | Lectura de medidores y facturación | Micromedición y lectura |
| 3 | Cobranza y corte/reconexión | Sistema comercial |
| 4 | Atención de reclamos comerciales | Atención de reclamos |
| 5 | Operación de plantas y redes | SCADA de plantas y reservorios |
| 6 | Contrataciones y presupuesto público | SIAF y patrimonio |

## E. Instrumentos de planeamiento existentes

| Instrumento | ¿Existe? | Vigencia | Estado real |
|---|---|---|---|
| Plan Estratégico Institucional (PEI) | Sí | 2023–2027 | Aprobado, pero no se ha revisado desde su aprobación. |
| Plan Operativo Institucional (POI) | Sí | 2025 | Se formula cada año para efectos presupuestales. |
| Plan Estratégico de Tecnologías de la Información (PETI) | **No** | — | **Nunca se ha formulado.** |
| Plan de Gobierno Digital | **No** | — | **Exigible por el D. Leg. 1412 y la R.S.G.D. 005-2018-PCM/SEGDI. No existe.** |
| Política de seguridad de la información | No | — | No existe. |
| Plan de continuidad del negocio | No | — | No existe. El BIA de `datos/bia.csv` es un borrador incompleto elaborado por un practicante. |
| Inventario de servicios digitales | Parcial | — | Sin responsable asignado. |
| Comité de Gobierno Digital y Líder de Gobierno Digital | **No** | — | **Exigible por la R.M. 119-2018-PCM. No se ha designado.** |

## F. Situación de TI — hechos verificables para el diagnóstico

Son los hechos que la organización admite y que pueden darse por ciertos. Todo lo demás se pregunta en la entrevista.

| Aspecto | Situación verificada |
|---|---|
| **Inventario de activos de TI** | No existe. |
| **Capacitación en seguridad** | Se hizo una charla de una hora en la inducción, hace tres años. |
| **Gestión de cambios** | Hay un formato de cambio que se llena después de aplicar el cambio. |
| **Registro de incidentes** | Se lleva por correo electrónico, sin clasificación ni tiempos. |
| **Contratos con proveedores de TI** | Dos de los cinco contratos están vencidos y el servicio continúa. |
| **Segundo factor de autenticación** | Está disponible en el sistema principal pero no se activó para evitar resistencia de los usuarios. |
| **Respaldos** | Se ejecutan a disco local y nunca se ha probado una restauración completa. |
| **Contraseñas** | No hay política escrita. La longitud mínima del sistema principal es de seis caracteres. |

## G. El incidente del periodo

**Reclamo masivo por facturación estimada**

Un fallo en la carga de lecturas dejó tres ciclos de facturación estimados para 11 200 conexiones. SUNASS abrió procedimiento. No se pudo determinar qué lote de lecturas falló porque el sistema no conserva el archivo de carga original.

## H. Riesgos que la organización ya conoce y no ha tratado

| N.º | Riesgo conocido | ¿Tratado? |
|---|---|---|
| 1 | Red industrial (SCADA) sin segmentación efectiva | No |
| 2 | Sin trazabilidad del proceso de carga de lecturas | No |
| 3 | **Doble marco.** Gobierno digital y regulación sectorial, ninguno cubierto por completo | No |

## I. Datos entregados

Los siete archivos de `datos/` corresponden al periodo del 1 de enero al 31 de diciembre de 2025. Fueron generados con la semilla de esta empresa. **No coinciden con los de ningún otro equipo**.

| Archivo | Qué contiene | Registros |
|---|---|---|
| `pagos.csv` | Población de pagos del periodo — comprobante, fecha, proveedor, concepto, monto, quién registró y quién aprobó | 19 281 |
| `proveedores.csv` | Maestro de proveedores con su contacto y documento de identidad | 156 |
| `empleados.csv` | Planilla del periodo, con fechas de ingreso y cese | 312 |
| `usuarios_erp.csv` | Usuarios del ERP con su perfil, último acceso y estado | 192 |
| `bia.csv` | Análisis de impacto al negocio por proceso, con RTO, RPO y fecha de la última prueba | 6 |
| `presupuesto_ti.csv` | Presupuesto de TI del periodo por partida, planificado contra ejecutado | 7 |
| `inversiones_cerradas.csv` | Tres inversiones cerradas con su beneficio declarado y si se midió | 3 |

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
