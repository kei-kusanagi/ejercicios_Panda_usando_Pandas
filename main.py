import pandas as pd
from pprint import pprint

# path = "Copia de ETIQUETAR inventario 2015.xlsx"
path = "inventario SIMPLIFICADO.xlsx"
sample_dataframe = pd.read_excel(path)

def search_by_code(dataframe):
    """
    Busca un código
    :param dataframe: The code that will be searched.
    :return:
    """

    search_input = input("Inserte el código a buscar: ").upper()

    if not search_input:
        print(f"no ha introducido un código, por favor introduzca un código.")
        return

    search_list = [search_input]

    result = dataframe["CODIGO"].isin(search_list)
    could_find_code = result.any()

    if not could_find_code:
        print(f"no se encontro el codigo: {search_input} en el inventario")
        return

    print("\n- Printing result:")
    print(result)

    print("\n- Printing result.any():")
    print(result.any())

    result[""]

    # description = [dataframe.loc[dataframe.check == True, 'DESCRIPCION']]
    # series = [dataframe.loc[dataframe.check == True, 'SERIE']]
    # return description, series


result = search_by_code(sample_dataframe)
# print(result)
