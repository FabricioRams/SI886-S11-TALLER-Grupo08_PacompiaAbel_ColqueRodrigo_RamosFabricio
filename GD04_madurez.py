# 06_gobierno_digital/GD04_madurez.py
import pandas as pd, numpy as np, matplotlib.pyplot as plt
e = pd.read_csv("GD03_ejes.csv")
e["eje_nombre"] = e.Eje.str.split(". ").str[1]

nm = e.groupby("eje_nombre")["Nivel del eje (1–5)"].mean().round(2)
print("=== NIVEL POR EJE ===\n", nm.to_string())
print(f"\nNIVEL DE MADUREZ DE GOBIERNO DIGITAL: {nm.mean():.2f} de 5")
NIV = {1:"Inicial — reactivo", 2:"Emergente — en formación", 3:"Definido — estructurado",
       4:"Gestionado — medido", 5:"Optimizado — centrado en el usuario"}
print(f"→ {NIV[round(nm.mean())]}")

sin = e[e["Línea base"].astype(str).str.contains("No se mide", case=False)]
print(f"\n=== INDICADORES SIN LÍNEA BASE: {len(sin)} de {len(e)} ===")
print(sin[["Eje","Indicador"]].to_string(index=False))
print("→ Cada uno genera un proyecto de instrumentación: no se puede fijar meta")
print("  sobre lo que no se mide.")

ang = np.linspace(0, 2*np.pi, len(nm), endpoint=False).tolist(); ang += ang[:1]
v = nm.tolist(); v += v[:1]
fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))
ax.plot(ang, v, "-", linewidth=2.5, color="#16285C"); ax.fill(ang, v, alpha=.15, color="#16285C")
ax.set_xticks(ang[:-1]); ax.set_xticklabels(nm.index, fontsize=9)
ax.set_yticks(range(6)); ax.set_ylim(0,5)
ax.set_title("Madurez del gobierno digital — situación actual", pad=22)
plt.tight_layout(); plt.savefig("../graficos/GD_madurez.png", dpi=140)
