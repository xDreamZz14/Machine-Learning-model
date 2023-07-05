import pickle


class NaiveModel:
    """
    Clase que trabaja con dataframes.

    Tiene como metodos:

    fit(): Necesita un dataFrame como argumento
    predict(): Necesita un dataFrame como argumento y tambien trabaja con el diccionario instanciado
    en la clase, self.meansByColumn
    save(): Permite almacenar todos los datos obtenidos previamente en un archivo .pkl (Pickle)
    load(): Permite abrir y trabajar con el archivo guardado con save()
    """
    def __init__(self):
        """
        Args:
            self.meansByColumn (dict): Instancia un diccionario vacio en el cual se pueden
            almacenar los nuevos datos obtenidos sin modificar el archivo original.
        """
        self.meansByColumn = {}

    def fit(self,dataFrame):
        """
        Toma como argumento un dataFrame de el cual recorre cada columna y obtiene la media
        de cada una

        Actualiza el diccionario previamente instanciado en la clase
        NaiveModel con los datos recibidos

        :param dataFrame:
        :return:
        """
        for columnName, columnData in dataFrame.items():
            """
            print('Column Name : ', columnName)
            print('Column Contents : ', columnData.values)
            """
            totalValue = 0
            for value in columnData.values:
                totalValue += value
            meanValue = totalValue / len(columnData.values)
            self.meansByColumn[columnName] = meanValue
        # print(self.meansByColumn)

    def predict(self,dataFrame):
        """
        Toma como argumento un dataFrame y lo actualiza en una nueva variable dentro del metodo
        para no modificar los datos originales.

        Recorre cada fila de todas las columnas de este nuevo dataFrame
        y divide cada uno de los valores por la media previamente guardada en self.meansByColumn

        Retorna los datos obtenidos al nuevo dataFrame

        :param dataFrame:
        :return:
        """
        newDataFrame = dataFrame
        for columnName, columnData in newDataFrame.items():
            mean = self.meansByColumn[columnName]
            rowNumber = 0
            for value in columnData.values:
                """
                if str(value / mean) == "NaN":
                    newDataFrame.at[rowNumber, columnName] = 0
                else:
                """
                newDataFrame.at[rowNumber,columnName] = value / mean
                rowNumber += 1
        return newDataFrame

    def save(self,savePath):
        """
        Toma como argumento la ruta del directorio (savePath) donde queremos guardar los
        datos e indicar el nombre del archivo con el que queremos guardarlo y en este caso en
        formato .pkl (pickle)

        :param savePath:
        :return:
        """
        means = self.meansByColumn
        with open(savePath, "wb") as mFile:  # mFile = meansFile
            pickle.dump(means,mFile)

    def load(self,savePath):
        """
        Toma como argumento la ruta del directorio (savePath) y el archivo que deseamos cargar/abrir
        y nos deja trabajar con el

        :param savePath:
        :return:
        """
        with open(savePath, "rb") as mFile:
            self.meansByColumn = pickle.load(mFile)
            # print(means)