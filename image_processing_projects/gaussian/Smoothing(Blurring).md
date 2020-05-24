# Smoothing(Blurring)

1. 이미지 블러링이란?

   - 이미지를 로우 패스 필터 커널로 컨벌루션 하는 것
   - 이미지에서 고주파인 노이즈가 흐려짐
   - 이때 같은 고주파인 선도 같이 흐려짐

2. 컨볼루션(Convolution)

   - 이미지에서 커널을 컨볼루션하여 블러링, 샤프닝 등의 처리가 가능
   - 컨볼루션 계산은 커널과 이미지 상에 대응하는 값끼리 곱한 후 모두 더하여 구함
   - 이 결과값을 결과 영상의 현재 위치에 기록하면 됨

3.  filter2D

   - openCV에서는 컨볼루션을 쉽게 할 수 있도록 filter2D 함수를 제공

     ```python
     import numpy as np
     import cv2
     
     
     img = cv2.imread('test.png')
     kernel = np.ones((5,5),np.float32)/25
     dst = cv2.filter2D(img, -1, kernel)
     
     
     cv2.imshow('Original', img)
     cv2.imshow('Result', dst)
     
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     ```

4. 평균 블러링 (Averaging Blurring)

   - 커널을 만들어서 컨볼루션하는 번거로움을 줄이기 위해 OpenCV에서는 블러링 하는 함수를 제공

   - 위의 코드는 5X5 범위내 이웃 픽셀의 평균을 결과 이미지 픽셀 값으로 하는 평균 블러링을하는 blur 함수가 있다.

     ```python
     import cv2
     
     
     img = cv2.imread('test.png')
     blur = cv2.blur(img,(5,5))
     
     
     cv2.imshow('Original', img)
     cv2.imshow('Result', blur)
     
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     ```

5. 가우시안 블러링 (Gaussian Blurring)

   - 모든 픽셀에 똑같은 가중치를 부여했던 평균 블러링과 달리 가우시안 블러링은 중심에 있는 픽셀에 높은 가중치를 부여

   - 평균 블러링은 에지 포함해서 전체적으로 블러링된 반면 가우시안 블러링은 에지가 남아 있는 상태에서 블러링이 이루어진다.

   - ``캐니로 에지를 검출하기 전``에 노이즈를 제거하기 위해 사용된다.

     ```python
     import cv2
     
     
     img = cv2.imread('test.png')
     blur = cv2.GaussianBlur(img,(5,5),0)
     
     
     cv2.imshow('Original', img)
     cv2.imshow('Result', blur)
     
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     ```

6. 미디안 블러링(Median Blurring)

   - 관심화소 주변으로 지정한 커널 크기 (5x5)내의 픽셀을 크기순으로 정렬한 후 중간 값을 뽑아서 픽셀값으로 사용

   - 무작위 노이즈를 제거하는데 효과적

   - 하지만 에지가 있는 이미지의 경우에는 결과 이미지에서 에지가 사라질 수 있음

     ```python
     import cv2
     
     
     img = cv2.imread('circle.png')
     median = cv2.medianBlur(img, 5)
     
     cv2.imshow('Original', img)
     cv2.imshow('Result', median)
     
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     ```

7. Bilateral Filtering

   - 에지를 보존하면서 노이즈를 감소시킬 수 있는 방법

   - 결과 이미지에서 질감있는 부분만 블러링 되고 에지 부분은 보존됨

     ![bilateral filtering](\bilateral filtering.PNG)

     ```python
     import cv2
     
     
     img = cv2.imread('texture.png')
     blur = cv2.bilateralFilter(img,9,75,75)
     
     cv2.imshow('Original', img)
     cv2.imshow('Result', blur)
     
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     ```

     