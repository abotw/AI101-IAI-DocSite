下面给出**一个清晰、可直接运行的 OpenCV 模板匹配示例代码（Python）**，并包含英文注释。代码示例同时展示如何可视化匹配结果，并支持多种匹配方法。

---

# ✅ **OpenCV Template Matching Example (Python)**

```python
import cv2  
  
# Load images  
# source_img: the large image where we search  
# template_img: the small image (template)  
source_img = cv2.imread('cola-bottle.png')  
template_img = cv2.imread('cola-logo.png')  
  
if source_img is None or template_img is None:  
    raise FileNotFoundError("Failed to load images. Check file paths.")  
  
# Convert to grayscale for template matching  
source_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)  
template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)  
  
# Template size  
h, w = template_gray.shape[:2]  
  
# Apply template matching  
# Method options:  
#   cv2.TM_CCOEFF_NORMED  (most commonly used)  
#   cv2.TM_SQDIFF         (lower value = better match)  
#   cv2.TM_CCORR_NORMED   etc.  
method = cv2.TM_CCOEFF_NORMED  
  
result = cv2.matchTemplate(source_gray, template_gray, method)  
  
# Locate the best match  
# For TM_SQDIFF family, minimum is the best match.  
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  
  
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:  
    top_left = min_loc  
else:  
    top_left = max_loc  
  
bottom_right = (top_left[0] + w, top_left[1] + h)  
  
# Draw rectangle on result  
output = source_img.copy()  
cv2.rectangle(output, top_left, bottom_right, (0, 255, 0), 2)  
  
# Show results  
cv2.imshow('Source Image', source_img)  
cv2.imshow('Template', template_img)  
cv2.imshow('Matched Result', output)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
```

---

# 📌 **How It Works**

1. 加载原图和模板图。
    
2. 统一转换为灰度图（模板匹配通常在灰度空间进行）。
    
3. 使用 `cv2.matchTemplate()` 进行匹配。
    
4. 使用 `cv2.minMaxLoc()` 找到最佳匹配位置。
    
5. 在原图上绘制矩形框。
    

---

# ⭐ 常用匹配方法对比

|Method|Meaning|Good Match|
|---|---|---|
|`TM_CCOEFF_NORMED`|相关系数|数值越大越好|
|`TM_CCORR_NORMED`|互相关|数值越大越好|
|`TM_SQDIFF`|差值|数值越小越好|
|`TM_SQDIFF_NORMED`|差值归一化|数值越小越好|

---

如有需要，我也可以给你：  
✅ 在视频中进行模板匹配的版本  
✅ 多目标匹配（找到所有匹配位置）  
✅ 带阈值的匹配过滤  
✅ 高分辨率下的性能优化建议

随时告诉我你想进一步扩展哪部分！