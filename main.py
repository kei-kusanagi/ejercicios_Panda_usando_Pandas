import pandas as pd

# path = "Copia de ETIQUETAR inventario 2015.xlsx"
path = "inventario SIMPLIFICADO.xlsx"
df = pd.read_excel(path)


def busqueda(df):
    solicitud = input("Codigo a buscar: ")
    BUSQUEDA = [solicitud.upper()]

    df["check"] = df["CODIGO"].isin(BUSQUEDA)

    DESC = [df.loc[df.check == True,'DESCRIPCION']]
    SER = [df.loc[df.check == True,'SERIE']]

    return DESC, SER


print(busqueda(df))
