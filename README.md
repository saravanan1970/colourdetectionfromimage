# Color Detection from Images

This project extracts the top 3 dominant colors from images using KMeans clustering and saves the results in a CSV file.

## Features

- Automatically detects dominant colors from images.
- Saves results in `colors.csv` with image names and hex color codes.
- Simple folder-based image processing.
- Easy to integrate into other image analysis projects.

## Folder Structure

```
color-detection-from-images/
├── images/                # Folder to place input images (.jpg/.png/.jpeg)
├── color_detection.py     # Python script for color detection
├── colors.csv             # Output CSV file
└── README.md              # Project description
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/color-detection-from-images.git
cd color-detection-from-images
```

### 2. Install Dependencies

Make sure you have Python 3 installed. Then run:

```bash
pip install opencv-python scikit-learn pandas
```

### 3. Add Images

Place the images you want to analyze in the `images/` folder.

### 4. Run the Script

```bash
python color_detection.py
```

This generates `colors.csv` with the top 3 dominant colors (in HEX) for each image.

## Sample Output (colors.csv)

```
Image,Color1,Color2,Color3
photo1.jpg,#d4c5b9,#7a5c3b,#1e1c1a
photo2.jpg,#a1b2c3,#334455,#ddeeff
```

## License

This project is licensed under the MIT License.

## Author

[Your Name] – GitHub: [@your-username](https://github.com/your-username)
