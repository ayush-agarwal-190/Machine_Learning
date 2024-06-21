# Batch Normalization Using Keras

model =Sequential()

model.add(Dense(3,activation='relu',input_dim=2))
model.add(BatchNormalization())
model.add(Dense(2activation='relu'))
model.add(BatchNormalization())
model.add(Dense(1,activation='sigmoid'))
