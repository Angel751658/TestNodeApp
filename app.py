import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 35, 29],
    'Ciudad': ['Lima', 'Bogotá', 'México']
}

df = pd.DataFrame(data)
print("Datos de ejemplo:")
print(df)
