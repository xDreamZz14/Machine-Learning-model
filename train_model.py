from models.naive_model import NaiveModel
import pandas as pd

# Abre el dataframe para que nos permita trabajar con el
df = pd.read_csv("data/mnist_784.csv")   # df = data frame
# print(df)

# Guarda los datos obtenidos en el directorio que nosotros hemos elegido
savePath = "weights/means.pkl"

nv = NaiveModel() # Crea una variable con los metodos de la clase
nv.fit(df)
nv.save(savePath)