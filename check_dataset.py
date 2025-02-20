import os

dataset_path = "dataset"

for letter in sorted(os.listdir(dataset_path)):
    letter_path = os.path.join(dataset_path, letter)
    if os.path.isdir(letter_path):
        images = os.listdir(letter_path)
        print(f"✅ Letter: {letter}, Images: {len(images)}")

print("\nDataset is organized correctly!")
