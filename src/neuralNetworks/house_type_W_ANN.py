import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_excel('house_price_label.xlsx')
#leyendo el tipo de casa y mapeando
tipo = dict()
datos = df["house_type"].values
clase = 0
for keyType in datos:
    if keyType not in tipo.keys():
        tipo[keyType] = clase
        clase += 1
df["house_type"] = df["house_type"].map(lambda x: tipo[x])
evidencia = df.iloc[:,[0,2,3,4,5,6,7]].values
etiquetas = df.iloc[:,1].values
X_training, X_testing, y_training, y_testing = train_test_split(
    evidencia, etiquetas, test_size=0.3
)
#creamos el modelo
model = tf.keras.models.Sequential()

#adicion de una capa oculta
model.add(tf.keras.layers.Dense(10, input_shape=(7,), activation="sigmoid" ))
#model.add(tf.keras.layers.Dense(11, activation='tanh'))

#Adicion de capa output
model.add(tf.keras.layers.Dense(4))

model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

model.fit(X_training,y_training,epochs=150)

model.evaluate(X_testing,y_testing,verbose=2)