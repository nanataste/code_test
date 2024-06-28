import tensorflow as tf
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# print("train_images shape:", train_images.shape)
# print("train_labels shape:", train_labels.shape)
# print("test_images shape:", test_images.shape)
# print("test_labels shape:", test_labels.shape)

plt.imshow(train_images[115], cmap="Greys")
plt.show()