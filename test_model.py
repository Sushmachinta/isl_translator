
import tensorflow as tf
import numpy as np
import cv2
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("sign_language_model.h5")

labels = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

img_path = img_path = r"C:\Users\CHINTA.SUSHMA\Desktop\transla\dataset\A\A (1).jpg"
  

img = image.load_img(img_path, target_size=(64, 64))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0  

prediction = model.predict(img_array)
predicted_label = labels[np.argmax(prediction)]

print(f"✅ Predicted Sign: {predicted_label}")
