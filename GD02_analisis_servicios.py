# 06_gobierno_digital/GD02_analisis_servicios.py
import pandas as pd, matplotlib.pyplot as plt

s = pd.read_csv("GD01_catalogo_servicios.csv")
s["nivel"] = s["Nivel actual (0–5)"]

print(f"Servicios catalogados        : {len(s)}")
print(f"Volumen anual total          : {s['Volumen anual'].sum():,} atenciones")
print(f"Nivel medio de digitalización: {s.nivel.mean():.2f} de 5")
print(f"Servicios en nivel ≥ 4       : {(s.nivel>=4).sum()} ({(s.nivel>=4).mean():.0%})")
print(f"Servicios en nivel 0 o 1     : {(s.nivel<=1).sum()}")

# Ponderado por volumen: qué proporción de las atenciones es realmente digital
pond = (s.nivel * s['Volumen anual']).sum() / s['Volumen anual'].sum()
print(f"\nNivel medio PONDERADO por volumen: {pond:.2f}")
print("→ El promedio simple sobrevalora la digitalización si los servicios de mayor")
print("  volumen son los menos digitalizados. Este es el indicador que importa.")

print("\n=== PRINCIPIO DE UNA SOLA VEZ ===")
red = s['De ellos, ya en poder de la organización'].sum()
tot = s['Documentos solicitados'].sum()
print(f"Documentos solicitados: {tot} | de ellos ya en poder de la organización: {red} "
      f"({red/max(tot,1):.0%})")
print("→ Cada documento redundante es una solicitud que el rediseño debe eliminar.")

print("\n=== BRECHA POR SERVICIO, PONDERADA POR VOLUMEN ===")
s["brecha"] = s["Nivel objetivo"] - s.nivel
s["impacto"] = s.brecha * s['Volumen anual']
print(s.nlargest(5, "impacto")[["id","Servicio","nivel","Nivel objetivo","Volumen anual","impacto"]]
      .to_string(index=False))
print("→ Estos servicios encabezan el portafolio: mayor brecha × mayor volumen.")

fig, ax = plt.subplots(figsize=(10,5))
ax.barh(s.Servicio, s.nivel, color="#16285C", label="Nivel actual")
ax.barh(s.Servicio, s["Nivel objetivo"] - s.nivel, left=s.nivel,
        color="#0EA5E9", alpha=.55, label="Brecha al objetivo")
ax.set_xlabel("Nivel de digitalización (0–5)"); ax.set_xlim(0,5)
ax.set_title("Catálogo de servicios: nivel actual y objetivo")
ax.legend(); plt.tight_layout(); plt.savefig("../graficos/GD_servicios.png", dpi=140)
