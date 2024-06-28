import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(512, activation ='relu', input_shape=(784,)))
model.add(tf.keras.layers.Dense(10, activation='sigmoid'))

model.compile(optimizer ='rmsprop', loss='mse', metrics =['accuracy'])

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()


train_images = train_images.reshape((60000, 784))
train_images = train_images.astype('float32')/255.0

test_images = test_images.reshape((10000,784))
test_images = test_images.astype('float32')/255.0

train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

model.fit(train_images, train_labels, epochs =5, batch_size =128)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test:', test_acc)

history = model.fit(train_images, train_labels, epochs=5, batch_size=128)
loss = history.history['loss']
acc = history.history['accuracy']
epochs = range(1, len(loss)+1)

plt.plot(epochs, loss, 'b', label='Training Loss')
plt.plot(epochs, acc, 'r', label='Accuracy')
plt.xlabel('epochs')
plt.ylabel('loss/acc')
plt.show()



image = cv.imread('test.png', cv.IMREAD_GRAYSCALE)
image = cv.resize(image, (28, 28))
image = image.astype('float32')
image = image.reshape(1, 784)
image = 255-image
image /= 255.0
model.fit(train_images, train_labels, epochs=1000, batch_size=128)
plt.imshow(image.reshape(28, 28),cmap='Greys')


pred = model.predict(image.reshape(1,784), batch_size=1)
print("predict answer:",pred.argmax())
plt.show()
