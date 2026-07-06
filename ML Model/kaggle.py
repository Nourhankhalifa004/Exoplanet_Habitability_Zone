import kagglehub

# Download latest version
path = kagglehub.dataset_download("walididbennacer/exohabx-habitable-exoplanets-dataset-nasa-hwc")

print("Path to dataset files:", path)