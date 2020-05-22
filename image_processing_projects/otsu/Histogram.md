# Histogram



1. 이미지 histogram 이란 ?
   - 히스토그램은 이미지를 구성하는 픽셀 값 분포에 대한 그래프임.
   - x 축의 픽셀값으로는 범위는 0 ~ 255 사이이다.
   - y 축은 이미지에서 해당 픽셀값을 가진 픽셀 갯수이다.
   - 히스토그램의 왼쪽에는 가장 어두운 검은색 픽셀의 갯수를 보여주며 오른쪽으로 갈 수록 밝은 픽셀의 갯수를 보여준다.
   - 즉 조명이 알맞은 이미지의 경우 히스토그램이 중앙에서 좌우로 고루 퍼져있다.

2. histogram 구하기

   - **픽셀 강도 범위(RANGE)**

     이미지에서 히스토그램을 찾을 픽셀값 범위를 결정합니다. 예를 들어 0 ~ 15으로 결정합니다.

   

   - **막대 개수(DIMS)**

     앞에서 정한 범위내에서 계산하게될 히스토그램 막대(bin)의 개수입니다. 예를 들어 16개로 결정합니다. 

   

   - **막대의 범위(BINS)**

     하나의 막대로 보여줄 픽셀값의 의 범위입니다. 예를 들어 1입니다.

3. OpenCv 에서는 히스토그램을 구하기 위해 cv.calcHist()함수를 제공한다.

   ``hist = cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])``

   **images**

   uint8 또는 float32 타입의 이미지를 사용해야 하며  대괄호 [ ] 안에 입력해야 합니다. 예) [img]

   

   **channels**

   히스토그램을 계산할 채널의 인덱스입니다. 대괄호 [ ] 안에 입력해야 합니다. 

   예를 들어 그레이스케일 이미지라면 [0] 입니다. 

   컬러 이미지라면 [0], [1], [2] 중 하나를 사용할 수 있습니다. 각각 파란색, 녹색, 빨간색 채널을 의미합니다.

   

   **mask**

   마스크 이미지. 전체 이미지에대한 히스토그램을 구할 거라면 None을 사용해야 합니다. 

   이미지 일부분에 대한 히스토그램을 구하려고 한다면 마스크 이미지를 생성하여 제공해야 합니다.

   

   **histSize**

   계산할 히스토그램 막대(BIN)의 개수입니다. 대괄호 [ ]안에 입력해야 합니다.  전체 영역을 계산한다면 [256]입니다. 

   

   **ranges**

   히스토그램을 계산할 범위입니다. 전체 픽셀 강도 범위를 계산 한다면 [0, 256] 입니다.

4. histogram equalization

   1) 우선 NumPy를 사용하여 히스토그램 평활화를 구한다.

   이미지를 1차원 배열로 변환 후 히스토그램을 구합니다. 

   ``hist, bin = np.histogram(img.flatten(), 256, [0, 256])``

   

   2)히스토그램의 누적합을 구합니다. 

   ``cdf = hist.cumsum()``

   

   

   누적합의 최대값, 최소값을 이용하여 히스토그램이 넓게 분포되도록 만들어해주는 룩업 테이블( look-up table)을 만듭니다. 

   

   cdf = np.uint8((cdf - cdf.min())*255/(cdf.max()-cdf.min()))

   

   

   룩업 테이블을 그레이스케일 이미지에 적용하여 히스토그램 평활화가 적용된 이미지를 얻습니다. 

   

   equ = cdf[gray]

   

   

   속도 개선을 위해 추가로 NumPy의 masked array를 적용합니다. 마스크를 씌운 부분만 계산에서 제외시키는 방법입니다

   

   hist, bin = np.histogram(img.flatten(), 256, [0, 256]) cdf = hist.cumsum() cdf_mask = np.ma.masked_equal(cdf,0) # cdf의 값이 0인 경우는 mask처리를 하여 계산에서 제외시킴 cdf_mask = (cdf_mask - cdf_mask.min())*255/(cdf_mask.max()-cdf_mask.min()) # 계산 cdf = np.ma.filled(cdf_mask,0).astype('uint8')  # Mask처리를 했던 부분을 다시 0으로 변환 equ = cdf[gray]