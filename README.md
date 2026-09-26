# 3×3 Mean Filter for Image Smoothing

##  Project Description

This project demonstrates how to apply a **3×3 Mean (Average) Filter** to a grayscale image using Python.

A mean filter is a simple **image smoothing technique**. It reduces small variations and noise in an image by replacing each pixel with the average value of the pixels in its 3×3 neighborhood.

##  Technologies Used

* Python
* OpenCV (`cv2`)
* NumPy
* Matplotlib

##  Project Structure

```text
Mean-Filter/
│
├── main.py
├── img1.jpg
└── README.md
```

## 📦 Required Libraries

Install the required libraries using:

```bash
pip install opencv-python numpy matplotlib
```

## ▶️ How the Program Works

### 1. Import Libraries

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

* `cv2` → Used for reading the image.
* `numpy` → Used for creating the filter kernel and mathematical operations.
* `matplotlib` → Used for displaying the filtered image.

### 2. Read the Image

```python
img1 = cv2.imread("img1.jpg", 0)
```

The `0` means that the image is loaded in **grayscale**.

### 3. Create the 3×3 Mean Filter

```python
kernel = np.ones((3,3)) * 1/9
```

The kernel contains nine values, each equal to:

```text
1/9
```

So the kernel is:

```text
1/9  1/9  1/9
1/9  1/9  1/9
1/9  1/9  1/9
```

The sum of all kernel values is `1`.

### 4. Set Kernel Size

```python
k_s = 3
```

This specifies that a **3×3 neighborhood** is used for filtering.

### 5. Get Image Dimensions

```python
m = img1.shape[0]
x = img1.shape[1]
```

* `m` → Number of rows (image height)
* `x` → Number of columns (image width)

### 6. Create the Output Image

```python
filtered_image = np.zeros((m,x))
```

This creates an empty image where the filtered values will be stored.

### 7. Apply the Mean Filter

```python
for i in range(0, m-k_s+1):
    for j in range(0, x-k_s+1):
        filtered_image[i][j] = np.sum(
            kernel * img1[i:i+k_s, j:j+k_s]
        )
```

The program moves the 3×3 kernel across the image.

For every 3×3 region:

1. The image pixels are selected.
2. Each pixel is multiplied by `1/9`.
3. All nine values are added.
4. The result becomes the new pixel value.

Therefore:

**Filtered Pixel = Sum of 3×3 Neighborhood Pixels / 9**

## 🖼️ Display the Result

```python
plt.imshow(filtered_image, cmap='gray')
plt.show()
```

The filtered image is displayed in grayscale.

## 🎯 Purpose

The main purpose of this project is to understand how a **Mean Filter works internally**, without directly using OpenCV's built-in filtering function.

It demonstrates:

* Image reading
* Grayscale image processing
* Kernel creation
* Convolution/filtering
* Image smoothing
* Pixel-level operations

## 📊 Expected Result

The output image will appear **smoother** than the original image.

Small variations and noise are reduced because each output pixel is calculated from the average of its neighboring pixels.

## 🧮 Example

Suppose a 3×3 region is:

```text
10  20  30
20  30  40
30  40  50
```

The filtered value is:

```text
(10 + 20 + 30 + 20 + 30 + 40 + 30 + 40 in v + 50) / 9
```

```text
= 270 / 9
= 30
```

So the center pixel becomes approximately:

```text
30
```

## ⚠️ Important Note

Make sure `img1.jpg` is present in the **same folder** as the Python program.

If the image is stored somewhere else, provide the correct image path in:

```python
cv2.imread("img1.jpg", 0)
```

## 👨‍💻 Author

**Sai**

## 📄 License

This project is created for educational and academic purposes.
