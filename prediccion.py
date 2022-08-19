import numpy as np
from PIL import Image
from keras.models import load_model
import tensorflow as tf
from keras.layers import Input
from keras import Model
from keras.applications.densenet import preprocess_input

classes = ['Carton', 'Vidrio', 'Metal', 'Organico', 'Papel', 'Plastico', 'Desechable']
modelo = load_model('Modelo\Modelo.h5')

i = Input([None, None, 3], dtype = tf.uint8)
x = tf.cast(i, tf.float32)
x = preprocess_input(x)
x = modelo(x)
model_new = Model(inputs=[i], outputs=[x])

model_new.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.00001, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])

def predict(image):
    data_s = Image.open(image)
    image_res = data_s.resize((224,224), Image.BILINEAR)
    image_dim = np.array(image_res)
    image_dim = np.expand_dims(image_dim, axis=0)
    resultado = model_new.predict(image_dim)
    clases = classes[np.argmax(resultado)]
    porcentaje = str(round(resultado[0,np.argmax(resultado)]*100, 2))

    return clases,porcentaje
