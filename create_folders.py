import os


dataset_path = "dataset"

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

for letter in range(ord('A'), ord('B') + 1):
    folder_path = os.path.join(dataset_path, chr(letter))
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

print("✅ A-Z folders created successfully inside TRANSLA/dataset/")
