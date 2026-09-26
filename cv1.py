import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load image in grayscale
img1 = cv2.imread("nature.jpg", 0)

if img1 is None:
    print("Error: nature.jpg not found")
else:
    # Create 3x3 mean filter kernel
    kernel = np.ones((3, 3)) * (1 / 9)

    k_s = 3

    m = img1.shape[0]
    x = img1.shape[1]

    # Create output folder
    os.makedirs("output", exist_ok=True)

    # Create filtered image
    filtered_image = np.zeros((m, x))

    for i in range(0, m - k_s + 1):
        for j in range(0, x - k_s + 1):
            filtered_image[i][j] = np.sum(
                kernel * img1[i:i+k_s, j:j+k_s]
            )

    # Display filtered image
    plt.imshow(filtered_image, cmap='gray')
    plt.axis('off')
    plt.title("Mean Filter Output")

    # Save output image
    plt.savefig(
        "output/mean_filter_output.png",
        bbox_inches='tight',
        pad_inches=0
    )

    plt.show()

    print("Output saved as output/mean_filter_output.png")