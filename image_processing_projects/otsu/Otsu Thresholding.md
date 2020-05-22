# Otsu Thresholding

1. Thresholding 이란 ?
   - threshold 는 임계값 이라는 의미
   - threshold 값을 기준으로 특정 픽셀값을 할당 ( 크면 검정색 / 작으면 흰색)
   - OpenCv에서 Thresholding 을 적용하려면 gray scale 이미지로 변환하여 적용한다.
   -  Threshold 는 Global Threshold와 Adaptive threshold 로 나뉜다.

2. Global Thresholding 이란 ?

   - 이미지 전체에 하나의 threshold 값으로 thresholding 적용

   ```
   cv2.threshold(img, threshold_value, value, flag)
   
   img: Grayscale 이미지
   threshold_value: 픽셀 threshold 값
   value: 픽셀 threshold 보다 클 때 적용되는 최대값
   (적용되는 플래그에 따라 픽셀 threshold 값보다 작을 때 적용되는 최대값)
   flag: threshold 값 적용 방법 또는 스타일
   
   cv2.THRESH_BINARY: 픽셀 값이 threshold_value 보다 크면 value, 작으면 0으로 할당
   cv2.THRESH_BINARY_INV: 픽셀 값이 threshold_value 보다 크면 0, 작으면 value로 할당
   cv2.THRESH_TRUNC: 픽셀 값이 threshold_value 보다 크면 threshold_value, 작으면 픽셀 값 그대로할당
   cv2.THRESH_TOERO: 픽셀 값이 threshold_value 보다 크면 픽셀 값 그대로, 작으면 0으로 할당
   cv2.THRESH_TOZERO_INV: 픽셀 값이 threshold_value 보다 크면 0, 작으면 픽셀 값 그대로 할당
   
   ```

   

3. Adaptive Threshold란 ?

   - global threshold는 이미지 전체에 threshold를 적용
   - 따라서 음영이 다르면 일부 영역이 모두 흰색 또는 검정색으로 보여지게 되어 버려지는 영역이 많아짐
   - 이 문제를 해결하기 위해 이미지의 작은 영역별로 나누어 Thresholding을 하는 것이 Adaptive Threshold 이다.
   - 이미지의 영역을 분할하고 임계값을 자동으로 조정해 흑백 이미지를 얻을 수 있다.
   - OpenCv에 있는 기능이다.

   ```
   cv2.adaptiveThreshold(img, value, adaptiveMethod, thresholdType, blocksize, C)
   
   img: Grayscale 이미지를 넣어줘야한다! 
   value: adaptiveMethod에 의해 계산된 threshold값과 thresholdType에 의해 픽셀에 적용될 최대값
   adaptiveMethod: 사용할 Adaptive Thresholding 알고리즘
   cv2.ADAPTIVE_THRESH_MEAN_C: 적용할 픽셀 (x,y)를 중심으로 하는 blocksize x blocksize 안에 있는 픽셀값의 평균에서 C를 뺀 값을 threshold값으로 함
   cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 적용할 픽셀 (x,y)를 중심으로 하는 blocksize x blocksize안에 있는 Gaussian 윈도우 기반 가중치들의 합에서 C를 뺀 값을 threshold값으로 함
   blocksize: 픽셀에 적용할 threshold값을 계산하기 위한 블럭 크기. 적용될 픽셀이 블럭의 중심이 됨. 따라서 blocksize는 홀수여야 함
   C: 보정 상수로, 이 값이 양수이면 계산된 adaptive threshold값에서 빼고, 음수면 더해줌. 0이면 그대로..
   
   ```

