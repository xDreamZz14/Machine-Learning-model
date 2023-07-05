from models.naive_model import NaiveModel
import pandas as pd

# Abre el dataframe y las medias previamente obtenidas para poder trabajar con ellas
df = pd.read_csv("data/mnist_784.csv")
loadPath = "weights/means.pkl"

# Directorio donde queremos guardar el archivo y el nombre elegido en formato .csv
savePath = "data/fichero.csv"

nv = NaiveModel() # Crea una variable con los metodos de la clase

nv.load(loadPath)
newDf = nv.predict(df)
newDf.to_csv(savePath, index = False) # Convierte el dataframe en .csv e indica que no se muestren los indicen de cada fila