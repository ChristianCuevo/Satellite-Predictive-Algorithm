import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from models.cnn_model import build_model

# Set paths to data directories
train_dir = "data/processed/train"
val_dir = "data/processed/val"

# Image size and batch size
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# Data generators for loading and augmenting images
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Build the CNN model
model = build_model(input_shape=(224, 224, 3),
                    num_classes=train_generator.num_classes)

# Train the model
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=10
)

# Save the model
os.makedirs("models/saved", exist_ok=True)
model.save("models/saved/satellite_damage_model.h5")

print("Model training complete and saved.")
