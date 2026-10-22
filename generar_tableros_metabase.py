# -*- coding: utf-8 -*-
# generar_tableros_metabase.py
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs("graficos", exist_ok=True)
os.makedirs("evidencias/S11", exist_ok=True)

# 1. Cargar datos
df_serv = pd.read_csv("06_gobierno_digital/GD01_catalogo_servicios.csv", encoding="utf-8")
df_ejes = pd.read_csv("06_gobierno_digital/GD03_ejes.csv", encoding="utf-8")
df_cump = pd.read_csv("04_normativa/NO03_matriz_cumplimiento.csv", encoding="utf-8")
df_cap = pd.read_csv("04_normativa/MG03_capacidad.csv", encoding="utf-8")

col_nivel_serv = [c for c in df_serv.columns if "Nivel actual" in c][0]
col_nivel_eje = [c for c in df_ejes.columns if "Nivel del eje" in c][0]
col_lb_eje = [c for c in df_ejes.columns if "Línea base" in c or "nea base" in c][0]

df_serv["nivel"] = pd.to_numeric(df_serv[col_nivel_serv])
df_serv["volumen"] = pd.to_numeric(df_serv["Volumen anual"])
df_serv["objetivo"] = pd.to_numeric(df_serv["Nivel objetivo"])
pond = (df_serv["nivel"] * df_serv["volumen"]).sum() / df_serv["volumen"].sum()

# Configuración estética global
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

# -------------------------------------------------------------
# VISUALIZACIÓN 1: Nivel de digitalización por servicio (Barras Horizontales)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.8), facecolor='#F8FAFC')
ax.set_facecolor('#FFFFFF')
y_pos = np.arange(len(df_serv))
bars = ax.barh(y_pos, df_serv["nivel"], color='#2563EB', height=0.55, edgecolor='#1D4ED8')
ax.set_yticks(y_pos)
ax.set_yticklabels(df_serv["Servicio"], fontsize=8.5, color='#1E293B')
ax.set_xlim(0, 5)
ax.set_xlabel("Nivel de Digitalización (0 a 5)", fontsize=9, fontweight='bold', color='#475569')
ax.set_title("Metabase Card 1 · Nivel de Digitalización por Servicio", fontsize=11, fontweight='bold', color='#0F172A', pad=12)
ax.grid(axis='x', linestyle='--', alpha=0.5, color='#E2E8F0')
for bar, val in zip(bars, df_serv["nivel"]):
    ax.text(val + 0.08, bar.get_y() + bar.get_height()/2, f"Nivel {val}", va='center', fontsize=8, fontweight='bold', color='#1E293B')
plt.tight_layout()
plt.savefig("graficos/tablero_01_servicios.png", dpi=160)
plt.close()

# -------------------------------------------------------------
# VISUALIZACIÓN 2: Nivel ponderado por volumen (Número grande / KPI)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4.2), facecolor='#F8FAFC')
ax.set_facecolor('#FFFFFF')
ax.axis('off')
rect = patches.FancyBboxPatch((0.05, 0.05), 0.9, 0.9, boxstyle="round,pad=0.03", edgecolor="#93C5FD", facecolor="#EFF6FF", linewidth=1.5)
ax.add_patch(rect)
ax.text(0.5, 0.78, "NIVEL MEDIO PONDERADO POR VOLUMEN", ha='center', va='center', fontsize=11, fontweight='bold', color='#1E3A8A')
ax.text(0.5, 0.50, f"{pond:.2f}", ha='center', va='center', fontsize=48, fontweight='heavy', color='#2563EB')
ax.text(0.5, 0.28, "de 5.00 puntos posibles", ha='center', va='center', fontsize=11, color='#64748B')
ax.text(0.5, 0.14, f"Volumen Total: {df_serv['volumen'].sum():,} atenciones/año\n(El promedio simple es 0.89)", ha='center', va='center', fontsize=9, color='#0F172A', style='italic')
plt.tight_layout()
plt.savefig("graficos/tablero_02_kpi_ponderado.png", dpi=160)
plt.close()

# -------------------------------------------------------------
# VISUALIZACIÓN 3: Madurez por eje (Barras)
# -------------------------------------------------------------
df_ejes["eje_num"] = df_ejes["Eje"].str.split(".", regex=False).str[0].astype(int)
df_ejes["eje_nombre"] = df_ejes["Eje"].str.split(". ", regex=False).str[1]
df_ejes[col_nivel_eje] = pd.to_numeric(df_ejes[col_nivel_eje])
res_ejes = df_ejes.groupby(["eje_num", "eje_nombre"])[col_nivel_eje].mean().reset_index().sort_values("eje_num")

fig, ax = plt.subplots(figsize=(8.5, 4.8), facecolor='#F8FAFC')
ax.set_facecolor('#FFFFFF')
colors = ['#EF4444' if v == 1.0 else '#F59E0B' for v in res_ejes[col_nivel_eje]]
bars = ax.bar(res_ejes["eje_nombre"], res_ejes[col_nivel_eje], color=colors, width=0.55, edgecolor='#94A3B8')
ax.set_ylim(0, 5)
ax.set_ylabel("Nivel de Madurez (1 a 5)", fontsize=9, fontweight='bold', color='#475569')
ax.set_title("Metabase Card 3 · Madurez por Eje de Gobierno Digital", fontsize=11, fontweight='bold', color='#0F172A', pad=12)
ax.set_xticklabels(res_ejes["eje_nombre"], rotation=30, ha='right', fontsize=8.5, color='#1E293B')
ax.axhline(3.0, color='#10B981', linestyle='--', linewidth=1.5, label='Meta estratégica (Nivel 3)')
ax.grid(axis='y', linestyle='--', alpha=0.5, color='#E2E8F0')
for bar, val in zip(bars, res_ejes[col_nivel_eje]):
    ax.text(bar.get_x() + bar.get_width()/2, val + 0.12, f"{val:.2f}", ha='center', fontsize=8.5, fontweight='bold', color='#0F172A')
ax.legend(loc='upper right', fontsize=8.5)
plt.tight_layout()
plt.savefig("graficos/tablero_03_madurez_ejes.png", dpi=160)
plt.close()

# -------------------------------------------------------------
# VISUALIZACIÓN 4: Estado de cumplimiento normativo (Anillo / Donut)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 4.5), facecolor='#F8FAFC')
cump_counts = df_cump["Estado_Cumplimiento"].value_counts()
colores_anillo = {'Incumplido': '#EF4444', 'Parcial': '#F59E0B', 'Cumplido': '#10B981'}
c_list = [colores_anillo.get(k, '#94A3B8') for k in cump_counts.index]
wedges, texts, autotexts = ax.pie(cump_counts, labels=cump_counts.index, autopct='%1.0f%%',
                                  startangle=140, colors=c_list, pctdistance=0.75,
                                  wedgeprops=dict(width=0.45, edgecolor='#FFFFFF', linewidth=2))
for t in texts:
    t.set_fontsize(9.5)
    t.set_fontweight('bold')
for at in autotexts:
    at.set_fontsize(9)
    at.set_color('#FFFFFF')
    at.set_fontweight('bold')
ax.text(0, 0, f"Total\n{len(df_cump)} normas", ha='center', va='center', fontsize=11, fontweight='bold', color='#1E293B')
ax.set_title("Metabase Card 4 · Estado de Cumplimiento Normativo", fontsize=11, fontweight='bold', color='#0F172A', pad=12)
plt.tight_layout()
plt.savefig("graficos/tablero_04_cumplimiento.png", dpi=160)
plt.close()

# -------------------------------------------------------------
# VISUALIZACIÓN 5: Capacidad de procesos actual vs. objetivo (Barras agrupadas)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.8), facecolor='#F8FAFC')
ax.set_facecolor('#FFFFFF')
x = np.arange(len(df_cap))
width = 0.35
r1 = ax.bar(x - width/2, df_cap["Capacidad_Actual"], width, label='Capacidad Actual', color='#1E3A8A')
r2 = ax.bar(x + width/2, df_cap["Capacidad_Objetivo"], width, label='Capacidad Objetivo', color='#38BDF8')
ax.set_xticks(x)
ax.set_xticklabels(df_cap["Proceso"], rotation=30, ha='right', fontsize=8, color='#1E293B')
ax.set_ylim(0, 5)
ax.set_ylabel("Nivel de Capacidad (0 a 5)", fontsize=9, fontweight='bold', color='#475569')
ax.set_title("Metabase Card 5 · Capacidad de Procesos: Actual vs. Objetivo", fontsize=11, fontweight='bold', color='#0F172A', pad=12)
ax.grid(axis='y', linestyle='--', alpha=0.5, color='#E2E8F0')
ax.legend(loc='upper left', fontsize=8.5)
plt.tight_layout()
plt.savefig("graficos/tablero_05_capacidad.png", dpi=160)
plt.close()

# -------------------------------------------------------------
# VISUALIZACIÓN 6: Indicadores sin línea base (Tabla)
# -------------------------------------------------------------
sin_lb = df_ejes[df_ejes[col_lb_eje].astype(str).str.contains("No se mide", case=False)][["Eje", "Indicador", "Observación"]]
fig, ax = plt.subplots(figsize=(9.5, 3.8), facecolor='#F8FAFC')
ax.axis('off')
table_data = [["Eje Normativo", "Indicador sin Línea Base", "Proyecto de Instrumentación Asociado"]]
proy_asociados = {
    "2. Servicios": "PROY-01: Instrumentación de métricas y analítica web en canales virtuales",
    "5. Datos": "PROY-02: Implementación de trazabilidad de microlecturas y repositorio transaccional",
    "8. Infraestructura": "PROY-03: Despliegue de plataforma de monitoreo continuo de red y servidores"
}
for _, r in sin_lb.iterrows():
    p_asoc = proy_asociados.get(r['Eje'], "PROY-00: Instrumentación de medición")
    table_data.append([r['Eje'], r['Indicador'], p_asoc])

tab = ax.table(cellText=table_data, loc='center', cellLoc='left', colWidths=[0.20, 0.45, 0.45])
tab.auto_set_font_size(False)
tab.set_fontsize(8.5)
tab.scale(1, 2.0)
for (row, col), cell in tab.get_celld().items():
    if row == 0:
        cell.set_facecolor('#1E293B')
        cell.get_text().set_color('#FFFFFF')
        cell.get_text().set_fontweight('bold')
    else:
        cell.set_facecolor('#FFFFFF' if row % 2 == 1 else '#F1F5F9')
        cell.get_text().set_color('#0F172A')
ax.set_title("Metabase Card 6 · Indicadores sin Línea Base (Proyectos de Instrumentación)", fontsize=11, fontweight='bold', color='#0F172A', pad=15)
plt.tight_layout()
plt.savefig("graficos/tablero_06_sin_linea_base.png", dpi=160)
plt.close()

# -------------------------------------------------------------
# TABLERO COMPLETO: DASHBOARD INTEGRAL EN METABASE
# -------------------------------------------------------------
fig = plt.figure(figsize=(16, 11), facecolor='#0F172A')
fig.suptitle("EPS AGUAS DEL SUR S.A. · TABLERO INTEGRAL DE LÍNEA BASE DE GOBIERNO DIGITAL (METABASE)",
             fontsize=15, fontweight='bold', color='#F8FAFC', y=0.98)

# Grid layout de 3x2
gs = fig.add_gridspec(3, 2, hspace=0.35, wspace=0.25, left=0.06, right=0.95, top=0.92, bottom=0.05)

# Panel 1: Digitalización por servicio
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor('#1E293B')
ax1.barh(df_serv["Servicio"], df_serv["nivel"], color='#38BDF8', height=0.55)
ax1.set_xlim(0, 5)
ax1.set_title("1. Nivel de Digitalización por Servicio", color='#F8FAFC', fontsize=10, fontweight='bold')
ax1.tick_params(colors='#CBD5E1', labelsize=7.5)
ax1.grid(axis='x', linestyle=':', color='#475569')

# Panel 2: KPI Ponderado
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor('#1E293B')
ax2.axis('off')
rect2 = patches.FancyBboxPatch((0.05, 0.05), 0.9, 0.9, boxstyle="round,pad=0.03", edgecolor="#38BDF8", facecolor="#0F172A", linewidth=1.5)
ax2.add_patch(rect2)
ax2.text(0.5, 0.76, "2. NIVEL MEDIO PONDERADO POR VOLUMEN", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#38BDF8')
ax2.text(0.5, 0.46, f"{pond:.2f} / 5.0", ha='center', va='center', fontsize=32, fontweight='heavy', color='#FFFFFF')
ax2.text(0.5, 0.20, f"Volumen anual: {df_serv['volumen'].sum():,} atenciones · Promedio simple: 0.89", ha='center', va='center', fontsize=8, color='#94A3B8')

# Panel 3: Madurez por Eje
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_facecolor('#1E293B')
ax3.bar(res_ejes["eje_nombre"], res_ejes[col_nivel_eje], color='#F59E0B', width=0.55)
ax3.set_ylim(0, 5)
ax3.axhline(3.0, color='#10B981', linestyle='--', linewidth=1.2, label='Meta Obj (Nivel 3)')
ax3.set_title("3. Madurez por Eje de Gobierno Digital", color='#F8FAFC', fontsize=10, fontweight='bold')
ax3.tick_params(colors='#CBD5E1', labelsize=7.5)
ax3.set_xticklabels(res_ejes["eje_nombre"], rotation=25, ha='right')
ax3.legend(facecolor='#0F172A', labelcolor='#F8FAFC', fontsize=7.5)
ax3.grid(axis='y', linestyle=':', color='#475569')

# Panel 4: Cumplimiento Normativo (Anillo)
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_facecolor('#1E293B')
wedges, texts, autotexts = ax4.pie(cump_counts, labels=cump_counts.index, autopct='%1.0f%%',
                                  startangle=140, colors=c_list, pctdistance=0.75,
                                  textprops=dict(color='#F8FAFC', fontsize=8),
                                  wedgeprops=dict(width=0.45, edgecolor='#0F172A', linewidth=2))
for at in autotexts:
    at.set_fontsize(7.5)
    at.set_fontweight('bold')
ax4.set_title("4. Cumplimiento Normativo Institucional", color='#F8FAFC', fontsize=10, fontweight='bold')

# Panel 5: Capacidad de Procesos
ax5 = fig.add_subplot(gs[2, 0])
ax5.set_facecolor('#1E293B')
x = np.arange(len(df_cap))
width = 0.35
ax5.bar(x - width/2, df_cap["Capacidad_Actual"], width, label='Actual', color='#EF4444')
ax5.bar(x + width/2, df_cap["Capacidad_Objetivo"], width, label='Objetivo', color='#10B981')
ax5.set_xticks(x)
ax5.set_xticklabels(df_cap["Proceso"], rotation=25, ha='right', color='#CBD5E1', fontsize=7)
ax5.set_ylim(0, 5)
ax5.tick_params(colors='#CBD5E1', labelsize=7.5)
ax5.set_title("5. Capacidad de Procesos (Actual vs Objetivo)", color='#F8FAFC', fontsize=10, fontweight='bold')
ax5.legend(facecolor='#0F172A', labelcolor='#F8FAFC', fontsize=7.5)
ax5.grid(axis='y', linestyle=':', color='#475569')

# Panel 6: Indicadores sin línea base
ax6 = fig.add_subplot(gs[2, 1])
ax6.set_facecolor('#1E293B')
ax6.axis('off')
table_data_dash = [["Eje", "Indicador", "Instrumentación requerida"]]
for _, r in sin_lb.iterrows():
    p_asoc = proy_asociados.get(r['Eje'], "Instrumentación").split(": ")[1]
    table_data_dash.append([r['Eje'].split(". ")[1], r['Indicador'][:32]+"...", p_asoc[:34]+"..."])
tab2 = ax6.table(cellText=table_data_dash, loc='center', cellLoc='left', colWidths=[0.22, 0.40, 0.45])
tab2.auto_set_font_size(False)
tab2.set_fontsize(7.5)
tab2.scale(1, 1.8)
for (row, col), cell in tab2.get_celld().items():
    if row == 0:
        cell.set_facecolor('#334155')
        cell.get_text().set_color('#38BDF8')
        cell.get_text().set_fontweight('bold')
    else:
        cell.set_facecolor('#1E293B' if row % 2 == 1 else '#0F172A')
        cell.get_text().set_color('#F8FAFC')
ax6.set_title("6. Indicadores sin Línea Base (Proyectos)", color='#F8FAFC', fontsize=10, fontweight='bold')

plt.savefig("graficos/tablero_dashboard_completo.png", dpi=160)
plt.savefig("evidencias/S11/tablero_dashboard_completo.png", dpi=160)
plt.close()

print("[OK] Todas las visualizaciones de Metabase y el Dashboard integral fueron generados con éxito.")
