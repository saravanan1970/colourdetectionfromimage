import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

def get_dominant_colors(image_path, k=3):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, n_init='auto')
    kmeans.fit(img)
    colors = kmeans.cluster_centers_.astype(int)
    return [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in colors]

def process_images_from_folder(folder_path, output_csv='colors.csv'):
    data = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(folder_path, filename)
            colors = get_dominant_colors(filepath)
            data.append([filename] + colors)

    df = pd.DataFrame(data, columns=['Image', 'Color1', 'Color2', 'Color3'])
    df.to_csv(output_csv, index=False)
    print(f"CSV saved as {output_csv}")

# Example usage
process_images_from_folder('images')
