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
 
## 🗂️ Repo Structure
 
```
.
├── read.py             # Image & video I/O
├── draw.py             # Shape drawing (rectangle, circle, line)
├── basic.py            # Grayscale, blur, Canny edges, dilation, erosion
└── transformations.py  # Translation, rotation, flipping
```
