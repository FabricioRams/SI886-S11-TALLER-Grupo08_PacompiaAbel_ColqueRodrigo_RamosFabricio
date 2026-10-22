# 06_gobierno_digital/GD02_analisis_servicios.py
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Cargar catálogo
try:
    s = pd.read_csv("GD01_catalogo_servicios.csv", encoding="utf-8")
except Exception:
    s = pd.read_csv("GD01_catalogo_servicios.csv")

# Localizar la columna de nivel actual sea con guion simple o en-dash
nivel_col = [c for c in s.columns if "Nivel actual" in c][0]
s["nivel"] = s[nivel_col]

print(f"Servicios catalogados        : {len(s)}")
print(f"Volumen anual total          : {s['Volumen anual'].sum():,} atenciones")
print(f"Nivel medio de digitalización: {s.nivel.mean():.2f} de 5")
print(f"Servicios en nivel >= 4      : {(s.nivel>=4).sum()} ({(s.nivel>=4).mean():.0%})")
print(f"Servicios en nivel 0 o 1     : {(s.nivel<=1).sum()}")

# Ponderado por volumen: qué proporción de las atenciones es realmente digital
pond = (s.nivel * s['Volumen anual']).sum() / s['Volumen anual'].sum()
print(f"\nNivel medio PONDERADO por volumen: {pond:.2f}")
print("-> El promedio simple sobrevalora la digitalización si los servicios de mayor")
print("  volumen son los menos digitalizados. Este es el indicador que importa.")

print("\n=== PRINCIPIO DE UNA SOLA VEZ ===")
col_red = [c for c in s.columns if "poder de la" in c][0]
red = s[col_red].sum()
tot = s['Documentos solicitados'].sum()
print(f"Documentos solicitados: {tot} | de ellos ya en poder de la organización: {red} "
      f"({red/max(tot,1):.0%})")
print("-> Cada documento redundante es una solicitud que el rediseño debe eliminar.")

print("\n=== BRECHA POR SERVICIO, PONDERADA POR VOLUMEN ===")
s["brecha"] = s["Nivel objetivo"] - s.nivel
s["impacto"] = s.brecha * s['Volumen anual']
print(s.nlargest(5, "impacto")[["id","Servicio","nivel","Nivel objetivo","Volumen anual","impacto"]]
      .to_string(index=False))
print("-> Estos servicios encabezan el portafolio: mayor brecha x mayor volumen.")

os.makedirs("../graficos", exist_ok=True)
fig, ax = plt.subplots(figsize=(11, 5.5))
ax.barh(s.Servicio, s.nivel, color="#16285C", label="Nivel actual (0–5)")
ax.barh(s.Servicio, s["Nivel objetivo"] - s.nivel, left=s.nivel,
        color="#0EA5E9", alpha=.65, label="Brecha al objetivo")

for i, (act, obj) in enumerate(zip(s.nivel, s["Nivel objetivo"])):
    ax.text(obj + 0.06, i, f"Act: {act} -> Obj: {obj}", va='center', fontsize=9, fontweight='bold', color="#1E293B")

ax.set_xlabel("Nivel de digitalización (0–5)", fontsize=10, fontweight="bold")
ax.set_xlim(0, 5.5)
ax.set_title("Catálogo de servicios: nivel actual y objetivo — EPS Aguas del Sur S.A.", fontsize=12, fontweight="bold")
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig("../graficos/GD_servicios.png", dpi=160)
print("\n[OK] Grafico guardado en ../graficos/GD_servicios.png")
