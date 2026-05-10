from tensorflow.keras.layers import *
from tensorflow.keras.models import Model

MAX_URL_LEN = 200
MAX_HTML_LEN = 1000
VOCAB_SIZE = 128


def build_model():

    # URL CNN
    u_in = Input((MAX_URL_LEN,))

    u = Embedding(VOCAB_SIZE,32)(u_in)
    u = Conv1D(64,5,activation='relu')(u)
    u = MaxPooling1D(2)(u)
    u = Flatten()(u)

    # HTML CNN
    h_in = Input((MAX_HTML_LEN,))

    h = Embedding(VOCAB_SIZE,32)(h_in)
    h = Conv1D(32,3,activation='relu')(h)
    h = MaxPooling1D(2)(h)
    h = Flatten()(h)

    # IMAGE CNN
    i_in = Input((64,64,3))

    i = Conv2D(32,(3,3),activation='relu')(i_in)
    i = MaxPooling2D()(i)

    i = Conv2D(64,(3,3),activation='relu')(i)
    i = MaxPooling2D()(i)

    i = Flatten()(i)

    # FEATURE FUSION
    x = Concatenate()([u,h,i])

    x = Dense(128,activation='relu')(x)

    out = Dense(1,activation='sigmoid')(x)

    model = Model([u_in,h_in,i_in], out)

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model
