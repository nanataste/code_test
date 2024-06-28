import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 이미지 파일 경로를 확인하세요.
image_path = 'test.png'

# 이미지 읽기
image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# 이미지 파일이 제대로 읽혔는지 확인
if image is None:
    raise ValueError(f"이미지를 찾을 수 없습니다: {image_path}")

# 이미지 리사이즈
image = cv.resize(image, (28, 28))

# 데이터 타입 변환
image = image.astype('float32')

# 이미지 reshape
image = image.reshape(1, 784)

# 이미지 반전
image = 255 - image

# 정규화
image /= 255.0

# 이미지 시각화
plt.imshow(image.reshape(28, 28), cmap='Greys')
plt.show()
