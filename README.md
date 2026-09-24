# Computer Vision Techniques
 
A hands-on collection of OpenCV fundamentals — reading media, drawing shapes, core image-processing operations, and geometric transformations — each demonstrated in its own script with visual output.
 
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
---
 
## Reading Media — `read.py`
 
Basic methods to read images and video streams.
 
### Reading an image
```python
cv.imread(img_path)        # load the image
cv.imshow(window_name, img) # display it in a window
```
 
**Output:**
 
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/7352af8b-572a-4e03-ac03-b0c65aef4e0c" />

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
 
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/9df8bbfa-22e4-4592-9b69-f65b623b0eed" />

---
 
## Basic Operations — `basic.py`
 
**Original image:**
 
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/b3da69eb-6089-43f8-9b94-8bae992431f0" />

### 1. Grayscale conversion
```python
cv.cvtColor(source_image, cv.COLOR_BGR2GRAY)
```

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/264e9220-3938-487d-ab86-294bcc059417" />

### 2. Blurring

Applies a Gaussian filter to reduce noise.
```python
cv.GaussianBlur(img, kernel_size, border_setting)
```
- `kernel_size` — filter dimensions, e.g. `(3, 3)`
- `border_setting` — typically `cv.BORDER_DEFAULT`

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/0aeb954e-24eb-474e-b374-56ee64eb0e1f" />

### 3. Edge detection (Canny)
```python
cv.Canny(img, threshold1, threshold2)
```
Outlines edges in the image. Feeding in a **blurred** image improves detection quality.
 
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/454d38ec-42fc-4d76-9bb5-0ac98986b2a5" />

### 4. Dilation
Thickens detected edges for better visibility.
```python
cv.dilate(canny_img, kernel_size, iterations=1)
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/28fed016-93f7-4b0d-a404-5d9e8d78052b" />

### 5. Erosion
Shrinks the dilated edges back down — sometimes recovering something close to the original edge-detected image.
```python
cv.erode(image, kernel_size, iterations=1)
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/42c40274-3b2c-4e43-b2d0-1ae7200b308d" />

 
## Geometric Transformations — `transformations.py`
 
### Translation
Shifts the image along the x and/or y axis.
 
```python
transMat = np.float32([[1, 0, x], [0, 1, y]])   # x, y = shift amount
cv.warpAffine(img, transMat, dimensions)
```
*Example: shifted `x = 100`, `y = 100`.*
 
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/e25af4ba-7034-4cf4-a4ba-afd81399bae1" />

### Rotation
Rotates the image about a chosen point.
 
```python
rotMatrix = cv.getRotationMatrix2D(rotation_point, angle, scale)
cv.warpAffine(img, rotMatrix, dimensions)
```
*Example: rotated by `90°`.*
 
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/abb24b01-189a-4f7f-ba02-7ff64c795945" />

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
 
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/f25a72f5-4685-464b-8b1b-1ad962ce3144" />

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

## 🌫️ Blurring Techniques
 
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
 
## 🔀 Bitwise Operations
 
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


  

 
## 🗂️ Repo Structure
 
```
.
├── read.py             # Image & video I/O
├── draw.py             # Shape drawing (rectangle, circle, line)
├── basic.py            # Grayscale, blur, Canny edges, dilation, erosion
├── transformations.py  # Translation, rotation, flipping
├── contours.py         # Contour detection
└── color.py            # Color spaces & channel splitting/merging
```
