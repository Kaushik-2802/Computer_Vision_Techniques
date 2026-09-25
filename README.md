# Computer Vision Techniques
 
A hands-on collection of OpenCV fundamentals — reading media, drawing shapes, core image-processing operations, geometric transformations, contour detection, color-space manipulation, blurring, bitwise operations, masking, histograms, thresholding, and gradient-based edge detection — each demonstrated in its own script with visual output.
 
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Contrib-green?logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/status-learning%20log-orange)
 
---
 
## Setup
 
```bash
pip install opencv-contrib-python
```
 
**Useful key:**
 
| Function | Purpose |
|---|---|
| `cv.waitKey()` | Keeps the display window open until a key is pressed |
 
---
 
## Table of Contents
 
1. [Reading Media — `read.py`](#-reading-media--readpy)
2. [Drawing Shapes — `draw.py`](#-drawing-shapes--drawpy)
3. [Basic Operations — `basic.py`](#-basic-operations--basicpy)
4. [Geometric Transformations — `transformations.py`](#-geometric-transformations--transformationspy)
5. [Contour Detection](#-contour-detection)
6. [Color Spaces](#-color-spaces)
7. [Color Channels](#-color-channels)
8. [Blurring Techniques](#-blurring-techniques)
9. [Bitwise Operations](#-bitwise-operations)
10. [Masking](#-masking)
11. [Histogram Computation](#-histogram-computation)
12. [Thresholding](#-thresholding)
13. [Gradients / Edge Detection](#-gradients--edge-detection)
---
 
## Reading Media — `read.py`
 
Basic methods to read images and video streams.
 
### Reading an image
```python
cv.imread(img_path)        # load the image
cv.imshow(window_name, img) # display it in a window
```
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/7352af8b-572a-4e03-ac03-b0c65aef4e0c" />
</p>

### Reading a video
```python
cv.VideoCapture(0)   # 0 = default webcam
```
A `while` loop confirms the camera is accessible and reads the feed frame by frame.
 
---
 
## Drawing Shapes — `draw.py`
 
Simple shape-drawing primitives:
 
| Function | Description | Syntax |
|---|---|---|
| `cv.rectangle()` | Draws a rectangle | `cv.rectangle(img, start_pt, end_pt, color, thickness)` |
| `cv.circle()` | Draws a circle | `cv.circle(img, center, radius, color, thickness)` |
| `cv.line()` | Draws a line | `cv.line(img, start_pt, end_pt, color, thickness)` |
 
> Pass `cv.FILLED` (or `-1`) as thickness to fill the shape.
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/9df8bbfa-22e4-4592-9b69-f65b623b0eed" />
</p>

---
 
## Basic Operations — `basic.py`
 
**Original image:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/b3da69eb-6089-43f8-9b94-8bae992431f0" />
</p>

### 1. Grayscale conversion
```python
cv.cvtColor(source_image, cv.COLOR_BGR2GRAY)
```
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/264e9220-3938-487d-ab86-294bcc059417" />
</p>

### 2. Blurring
Applies a Gaussian filter to reduce noise.
```python
cv.GaussianBlur(img, kernel_size, border_setting)
```
- `kernel_size` — filter dimensions, e.g. `(3, 3)`
- `border_setting` — typically `cv.BORDER_DEFAULT`
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/0aeb954e-24eb-474e-b374-56ee64eb0e1f" />
</p>

### 3. Edge detection (Canny)
```python
cv.Canny(img, threshold1, threshold2)
```
Outlines edges in the image. Feeding in a **blurred** image improves detection quality.
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/454d38ec-42fc-4d76-9bb5-0ac98986b2a5" />
</p>

### 4. Dilation
Thickens detected edges for better visibility.
```python
cv.dilate(canny_img, kernel_size, iterations=1)
```
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/28fed016-93f7-4b0d-a404-5d9e8d78052b" />
</p>

### 5. Erosion
Shrinks the dilated edges back down — sometimes recovering something close to the original edge-detected image.
```python
cv.erode(image, kernel_size, iterations=1)
```
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/42c40274-3b2c-4e43-b2d0-1ae7200b308d" />
</p>

---
 
## Geometric Transformations — `transformations.py`
 
### Translation
Shifts the image along the x and/or y axis.
 
```python
transMat = np.float32([[1, 0, x], [0, 1, y]])   # x, y = shift amount
cv.warpAffine(img, transMat, dimensions)
```
*Example: shifted `x = 100`, `y = 100`.*
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/e25af4ba-7034-4cf4-a4ba-afd81399bae1" />
</p>

### Rotation
Rotates the image about a chosen point.
 
```python
rotMatrix = cv.getRotationMatrix2D(rotation_point, angle, scale)
cv.warpAffine(img, rotMatrix, dimensions)
```
*Example: rotated by `90°`.*
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/abb24b01-189a-4f7f-ba02-7ff64c795945" />
</p>

### Flipping
Mirrors the image horizontally, vertically, or both.
 
```python
cv.flip(image, code)
```
 
| Code | Effect |
|---|---|
| `0` | Vertical flip |
| `1` | Horizontal flip |
| `-1` | Both (horizontal + vertical) |
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/f25a72f5-4685-464b-8b1b-1ad962ce3144" />
</p>

---
 
## Contour Detection
 
Contours are the **boundaries of an object** in an image.
 
```python
contours, hierarchies = cv.findContours(canny_img, contour_detection, contour_approximation_method)
```
 
**Parameters:**
 
| Parameter | Options | Description |
|---|---|---|
| `contour_detection` | `cv.RETR_TREE` | Returns hierarchical contours in the image |
| | `cv.RETR_EXTERNAL` | Returns only the external boundaries of image objects |
| | `cv.RETR_LIST` | Lists all contours present in the image |
| `contour_approximation_method` | `cv.CHAIN_APPROX_NONE` | Default approximation method (no compression) |
| | `cv.CHAIN_APPROX_SIMPLE` | Simplified/compressed approximation method |
 
> Instead of a Canny edge image, a **thresholded** image can also be used as the contour-detection input:
> ```python
> cv.threshold(image, threshold1, maxVal, type)
> ```
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Contour detection output" src="https://github.com/user-attachments/assets/ed4cb8c1-430b-47aa-9c08-87071d18a577" />
</p>

---
 
## Color Spaces
 
Images can be converted from one color scale to another using `cv.cvtColor()`.
 
```python
cv.cvtColor(src_img, code)
```
 
**Common conversion codes:**
 
| Code | Converts to |
|---|---|
| `cv.COLOR_BGR2GRAY` | Grayscale |
| `cv.COLOR_BGR2HSV` | HSV (Hue, Saturation, Value) |
| `cv.COLOR_BGR2LAB` | LAB color space |
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Color spaces output" src="https://github.com/user-attachments/assets/994ec1d6-a082-4ad3-ae47-b00f360cdf9e" />
</p>

---
 
## Color Channels
 
Just like color spaces, individual color channels can be **split** or **merged**.
 
### Splitting channels
```python
b, g, r = cv.split(img)
```
Splits the image into its Blue, Green, and Red channels, each highlighting the intensity of that color across the image.
 
**Output:**
 
*A blue-channel image — lighter regions represent less blue, darker regions represent more blue.*
 
<p align="center">
  <img width="500" height="500" alt="Blue channel split output" src="https://github.com/user-attachments/assets/9560993a-5254-4ff3-a390-51ba5903b050" />
</p>

### Merging channels
```python
cv.merge([value1, value2, value3])
```
Produces a clearer, color-accurate channel view by recombining specific intensity values.
 
**Output:**
 
*The blue channel, reconstructed using `cv.merge()` to clearly isolate blue intensity.*
 
<p align="center">
  <img width="500" height="500" alt="Blue channel merge output" src="https://github.com/user-attachments/assets/17538227-9e0d-410e-983f-067ed34fa86e" />
</p>

---
 
## Blurring Techniques
 
Beyond the basic Gaussian blur, OpenCV offers several blurring methods, each trading off smoothness, edge preservation, and speed differently.
 
### 1. Average Blur
Replaces each pixel with the **average** of its surrounding pixels.
 
```python
cv.blur(img, kernel_size)
```
> A larger `kernel_size` produces a stronger blur.
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Average blur output" src="https://github.com/user-attachments/assets/b1283020-67ad-4897-a4df-7f942e744e25" />
</p>

### 2. Gaussian Blur
Assigns **weights** to surrounding pixels and blurs based on their weighted average — smoother and generally better than the average blur.
 
```python
cv.GaussianBlur(img, kernel_size, sigmaX)
```
- `sigmaX` — standard deviation of a pixel from its surrounding pixels
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Gaussian blur output" src="https://github.com/user-attachments/assets/74720d27-d2f4-4f72-bd86-c59c11d3149f" />
</p>

### 3. Median Blur
Uses the **median** of surrounding pixels instead of the average or a weighted average — better at removing noise while preserving detail than the two methods above.
 
```python
cv.medianBlur(img, kernel_size)
```
> Note: `kernel_size` here is a plain **integer**, not a tuple.
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Median blur output" src="https://github.com/user-attachments/assets/97622625-f1d7-4f30-b2ff-cb35d0d11833" />
</p>

### 4. Bilateral Filter
Blurs the image while **preserving edges** — the most visually refined of the four methods.
 
```python
cv.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
```
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Bilateral filter output" src="https://github.com/user-attachments/assets/42e45416-2ece-4975-89e5-5b55a1b0feb6" />
</p>

---
 
## Bitwise Operations
 
OpenCV also supports pixel-wise **bitwise operations** between images.
 
```python
cv.bitwise_and(img1, img2)
```
 
| Function | Operation |
|---|---|
| `cv.bitwise_and()` | AND |
| `cv.bitwise_or()` | OR |
| `cv.bitwise_not()` | NOT |
| `cv.bitwise_xor()` | XOR |
 
**Output — Bitwise AND:**
 
*A rectangle and a circle image combined using a bitwise AND operation.*
 
<p align="center">
  <img width="500" height="500" alt="Bitwise AND output" src="https://github.com/user-attachments/assets/6aa0e27a-bb53-4764-a8f2-53dc43f3b8e6" />
</p>

---
 
## Masking
 
Masking isolates specific regions of an image by discarding everything outside a defined shape.
 
**Steps:**
1. Define a shape — `cv.rectangle()`, `cv.circle()`, or a combination of shapes — on a blank canvas the same size as the image.
2. Apply that shape onto the target image using **bitwise operations**, keeping only the pixels that fall inside it.
**The mask shape used:**
 
<p align="center">
  <img width="500" height="500" alt="Mask shape" src="https://github.com/user-attachments/assets/0f6b9ac9-7094-4135-9bc3-b93a0e61527a" />
</p>

**The source image:**
 
<p align="center">
  <img width="500" height="500" alt="Source image for masking" src="https://github.com/user-attachments/assets/7aac2d37-b018-4c79-b4a8-f1fbfd402376" />
</p>

**Output — after masking:**
 
<p align="center">
  <img width="500" height="500" alt="Masking output" src="https://github.com/user-attachments/assets/78868b3e-9241-4b39-858f-a3accdee9ea4" />
</p>

---
 
## Histogram Computation
 
A histogram shows how pixel intensities are **distributed** across an image, computed with `cv.calcHist()`.
 
```python
cv.calcHist(list_images, channels, mask, histSize, range)
```
 
| Parameter | Description |
|---|---|
| `histSize` | Size of the histogram (number of bins) |
| `range` | Range of pixel values covered by the histogram |
 
### Grayscale histogram
 
**Source image:**
 
<p align="center">
  <img width="500" height="441" alt="Grayscale source image" src="https://github.com/user-attachments/assets/473a3ec7-2ea7-4ded-b007-134043ca19ac" />
</p>

**Output — pixel distribution across bins:**
 
<p align="center">
  <img width="500" height="500" alt="Grayscale histogram output" src="https://github.com/user-attachments/assets/f25654e1-d46f-4052-b4d6-5db8dd8bec0b" />
</p>

### Color histogram
 
**Source image:**
 
<p align="center">
  <img width="500" height="441" alt="Color source image" src="https://github.com/user-attachments/assets/20176ab3-42a3-4d72-97d5-1175279e660e" />
</p>

**Output — distribution of red, green, and blue pixels:**
 
<p align="center">
  <img width="500" height="500" alt="Color histogram output" src="https://github.com/user-attachments/assets/41a67677-657b-4489-a704-eb2826ce8acc" />
</p>

---
 
## Thresholding
 
Converts pixel values within a certain range into another value — most commonly used for binary image transformations. There are two main approaches:
 
### 1. Simple Thresholding
 
```python
threshold, thresh = cv.threshold(src_img, thresh, maxVal, thresh_type)
```
 
| Parameter | Description |
|---|---|
| `maxVal` | The value assigned to pixels that cross the threshold |
| `thresh_type` | The thresholding mode — `cv.THRESH_BINARY` for standard binary, `cv.THRESH_BINARY_INV` for inverse binary |
 
**Output — binary threshold:**
 
<p align="center">
  <img width="500" height="500" alt="Binary threshold output" src="https://github.com/user-attachments/assets/3e276ea3-343e-4182-958f-3adc4c99d950" />
</p>

**Output — inverse binary threshold:**
 
<p align="center">
  <img width="500" height="500" alt="Inverse binary threshold output" src="https://github.com/user-attachments/assets/1df803dd-d7a3-4619-ab8a-34d2f2b95a92" />
</p>

### 2. Adaptive Thresholding
 
Automatically computes the threshold value for an image instead of requiring a manual value.
 
```python
cv.adaptiveThreshold(src_img, maxVal, adaptiveMethod, thresh_type, k_size, C)
```
 
| Parameter | Description |
|---|---|
| `adaptiveMethod` | `cv.ADAPTIVE_THRESH_MEAN_C` or `cv.ADAPTIVE_THRESH_GAUSSIAN_C` |
| `k_size` | Kernel size used to calculate the local mean/Gaussian mean |
| `C` | A fine-tuning constant subtracted from the computed mean |
 
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Adaptive threshold output" src="https://github.com/user-attachments/assets/cad77136-ab93-459b-91a8-a1f3a9f77155" />
</p>

---
 
## Gradients / Edge Detection
 
Several methods exist for computing image gradients to detect edges.
 
### 1. Laplacian
 
A second-order derivative filter that highlights rapid intensity shifts. For an image function `f(x, y)`, the Laplacian **∇²f** sums the second-order partial derivatives in the horizontal (x) and vertical (y) directions:
 
<p align="center">
  <img width="335" height="110" alt="Laplacian formula" src="https://github.com/user-attachments/assets/c50db032-cdf6-44ee-9e8c-531d2c3ee172" />
</p>

```python
cv.Laplacian(src_img, ddepth)
```
- `ddepth` — the desired bit-depth of the output image
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Laplacian output" src="https://github.com/user-attachments/assets/2f7673e7-b137-4502-a2a9-0412b8b4a8d3" />
</p>

> Since pixel values can't be negative, the code applies `np.uint8(np.absolute(lap))` to take the absolute value before casting to `uint8` (the standard image pixel datatype).
 
<p align="center">
  <img width="500" height="132" alt="uint8 absolute value note" src="https://github.com/user-attachments/assets/db483199-2e4c-478a-85d3-42e6fbebe920" />
</p>

### 2. Sobel
 
Calculates the first-order derivative of image intensity using two `3×3` convolution kernels — one detects vertical edges (**Gx**), the other detects horizontal edges (**Gy**).
 
**Horizontal gradient kernel (Gx):**
 
<p align="center">
  <img width="411" height="166" alt="Sobel Gx kernel" src="https://github.com/user-attachments/assets/a6b46aab-9691-4547-9ee0-74951f58b262" />
</p>

**Vertical gradient kernel (Gy):**
 
<p align="center">
  <img width="388" height="151" alt="Sobel Gy kernel" src="https://github.com/user-attachments/assets/83495c98-df87-4a3a-ba3f-77517c10b938" />
</p>

For an input image `I`, the gradient components at each pixel `(x, y)` come from convolving the image with each kernel:
 
<p align="center">
  <img width="215" height="126" alt="Sobel convolution formula" src="https://github.com/user-attachments/assets/38b6b9d9-3e5a-4b22-88c7-5dbb095c9ef1" />
</p>

Combining both directions gives the overall edge strength and orientation:
 
**Gradient magnitude (G)** — the edge intensity at a pixel:
 
<p align="center">
  <img width="302" height="92" alt="Gradient magnitude formula" src="https://github.com/user-attachments/assets/cc6ff3fb-4842-483c-8343-7537fe73ca11" />
</p>

**Gradient direction (θ)** — the angle of the edge orientation:
 
<p align="center">
  <img width="332" height="109" alt="Gradient direction formula" src="https://github.com/user-attachments/assets/40c4aa1c-5195-4902-94e5-79561fe7c813" />
</p>

```python
cv.Sobel(src_img, ddepth, dx, dy)
```
- `dx`, `dy` — direction flags; Sobel can compute the x- and y-direction gradients independently
**Output — Sobel in the x-direction** (`dx=1, dy=0`):
 
<p align="center">
  <img width="500" height="500" alt="Sobel x-direction output" src="https://github.com/user-attachments/assets/19f892f9-d652-4e37-8bbb-e0159b218e2b" />
</p>

**Output — Sobel in the y-direction** (`dx=0, dy=1`):
 
<p align="center">
  <img width="500" height="500" alt="Sobel y-direction output" src="https://github.com/user-attachments/assets/d801162b-5e02-4b36-b2b4-5630f8e667ae" />
</p>

**Output — combined:**
 
<p align="center">
  <img width="500" height="500" alt="Sobel combined output" src="https://github.com/user-attachments/assets/c9c2eaf0-2a45-4291-a49e-f30bf4ffae43" />
</p>

### 3. Canny Edge Detection
 
A multi-step algorithm that identifies object boundaries by detecting sharp intensity changes while minimizing noise.
 
**The 5 stages of Canny edge detection:**
 
| Stage | Description |
|---|---|
| 1. Gaussian filtering | Blurs the image to remove noise and prevent false edges |
| 2. Gradient calculation | Computes intensity gradients (magnitude & direction) using operators like Sobel |
| 3. Non-maximum suppression | Thins wide gradient ridges into sharp, one-pixel-wide boundaries |
| 4. Double thresholding | Classifies pixels as strong, weak, or non-edges using two thresholds |
| 5. Hysteresis tracking | Keeps weak edges only if they connect to strong edges, for continuous lines |
 
```python
cv.Canny(src_img, threshold1, threshold2)
```
- `threshold1`, `threshold2` — the lower and upper thresholds respectively
**Output:**
 
<p align="center">
  <img width="500" height="500" alt="Canny edge detection output" src="https://github.com/user-attachments/assets/37d0de3f-8e13-4fa1-9b33-784e921c1dbd" />
</p>

---
 
## Repo Structure
 
```
.
├── read.py             # Image & video I/O
├── draw.py             # Shape drawing (rectangle, circle, line)
├── basic.py            # Grayscale, blur, Canny edges, dilation, erosion
├── transformations.py  # Translation, rotation, flipping
├── contours.py         # Contour detection
├── color.py            # Color spaces & channel splitting/merging
├── blurring.py         # Average, Gaussian, median & bilateral blurring
├── bitwise.py          # Bitwise AND / OR / NOT / XOR operations
├── masking.py          # Region-of-interest masking
├── histogram.py        # Grayscale & color histogram computation
├── thresholding.py     # Simple & adaptive thresholding
└── gradients.py        # Laplacian, Sobel & Canny edge detection
```
 
