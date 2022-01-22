import pandas as pd

# path = "Copia de ETIQUETAR inventario 2015.xlsx"
path = "inventario SIMPLIFICADO.xlsx"
df = pd.read_excel(path)


def busqueda(df):
    solicitud = input("Codigo a buscar: ").upper()
    BUSQUEDA = [solicitud]

    df["check"] = df["CODIGO"].isin(BUSQUEDA)
    for n in df["check"]:
        if df.loc[n,True]:
            DESC = [df.loc[df.check == True,'DESCRIPCION']]
            SER = [df.loc[df.check == True,'SERIE']]
            return DESC, SER
        else:
            print(f"no se encontro el codigo: {BUSQUEDA} en el inventario")




print(busqueda(df))
