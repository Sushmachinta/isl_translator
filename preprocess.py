import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

dataset_path = "dataset"

datagen = ImageDataGenerator(
    rescale=1./255,  
    rotation_range=10,  
    width_shift_range=0.1,  
    height_shift_range=0.1, 
    shear_range=0.1,  
    zoom_range=0.1,  
    validation_split=0.2  
)

train_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

val_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

print("✅ Dataset Preprocessing Done!")
