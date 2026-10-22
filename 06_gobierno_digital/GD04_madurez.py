# -*- coding: utf-8 -*-
# 06_gobierno_digital/GD04_madurez.py
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

try:
    e = pd.read_csv("GD03_ejes.csv", encoding="utf-8")
except Exception:
    e = pd.read_csv("GD03_ejes.csv")

# Extraer el número y nombre del eje sin que el punto sea interpretado como regex
e["eje_num"] = e["Eje"].str.split(".", regex=False).str[0].astype(int)
e["eje_nombre"] = e["Eje"].str.split(". ", regex=False).str[1]

# Encontrar columna de nivel del eje
col_nivel = [c for c in e.columns if "Nivel del eje" in c][0]
col_lb = [c for c in e.columns if "nea base" in c or "Línea base" in c][0]

e[col_nivel] = pd.to_numeric(e[col_nivel])

# Resumen por eje ordenado según los 8 ejes oficiales
nm = e.groupby(["eje_num", "eje_nombre"])[col_nivel].mean().round(2).reset_index()
nm = nm.sort_values("eje_num")

print("================================================================")
print("  EPS AGUAS DEL SUR S.A. - NIVEL DE MADUREZ POR EJE DE GOBIERNO DIGITAL")
print("================================================================")
for _, row in nm.iterrows():
    print(f"Eje {row['eje_num']}. {row['eje_nombre']:<24} : {row[col_nivel]:.2f} de 5")

madurez_prom = nm[col_nivel].mean()
print(f"\nNIVEL DE MADUREZ DE GOBIERNO DIGITAL : {madurez_prom:.2f} de 5")

NIV = {
    1: "Inicial — reactivo",
    2: "Emergente — en formación",
    3: "Definido — estructurado",
    4: "Gestionado — medido",
    5: "Optimizado — centrado en el usuario"
}
nivel_redondeado = int(round(madurez_prom))
print(f"-> Estado institucional : Nivel {nivel_redondeado} ({NIV[nivel_redondeado]})")

sin = e[e[col_lb].astype(str).str.contains("No se mide", case=False)]
print(f"\n=== INDICADORES SIN LÍNEA BASE: {len(sin)} de {len(e)} ===")
for _, r in sin.iterrows():
    print(f"- [{r['Eje']}] {r['Indicador']}")
print("-> Cada uno genera un proyecto de instrumentación: no se puede fijar meta")
print("  sobre lo que no se mide.")

# Gráfico de radar (Spider Chart)
os.makedirs("../graficos", exist_ok=True)
categorias = nm["eje_nombre"].tolist()
valores = nm[col_nivel].tolist()

# Cerrar el círculo para el polígono del radar
ang = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
ang += ang[:1]
valores_cerrados = valores + valores[:1]

fig, ax = plt.subplots(figsize=(8.5, 8.5), subplot_kw=dict(polar=True))

# Graficar contorno y relleno
ax.plot(ang, valores_cerrados, "o-", linewidth=2.5, color="#16285C", label="Madurez actual")
ax.fill(ang, valores_cerrados, alpha=0.20, color="#0EA5E9")

# Meta objetivo de referencia (Nivel 3 - Definido)
meta_objetivo = [3.0] * len(categorias)
meta_cerrada = meta_objetivo + meta_objetivo[:1]
ax.plot(ang, meta_cerrada, "--", linewidth=1.5, color="#10B981", label="Meta estratégica (Nivel 3)")

# Configurar ángulos y etiquetas
ax.set_xticks(ang[:-1])
ax.set_xticklabels(categorias, fontsize=9.5, fontweight="bold", color="#1E293B")
ax.set_yticks(range(1, 6))
ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8, color="#64748B")
ax.set_ylim(0, 5.2)

ax.set_title("Madurez de Gobierno Digital — EPS Aguas del Sur S.A.\n(Diagnóstico de Línea Base en 8 Ejes)",
             pad=25, fontsize=12, fontweight="bold", color="#0F172A")
ax.legend(loc="upper right", bbox_to_anchor=(1.15, 1.12), frameon=True)
plt.tight_layout()

ruta_grafico = "../graficos/GD_madurez.png"
plt.savefig(ruta_grafico, dpi=160)
print(f"\n[OK] Gráfico de radar guardado exitosamente en: {ruta_grafico}")
