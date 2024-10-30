# Master OpenCV with Python

### Lecture01 - 이미지, 비디오, 웹캠(Webcam), RTSP 및 RTMP 스트림 처리 
* [이미지 읽기 및 저장](ch01-01.py)  
* [비디오 파일 읽기 및 저장](ch01-02.py)  
* [웹캠 사용 및 저장](ch01-03.py)  
* [RTSP/RTMP 스트리밍 사용](ch01-04.py)  

### Lecture02 - 다양한 그리기 함수 및 출력
* [선 그리기](ch02-01.py)  
* [직선 자르기](ch02-02.py)  
* [사각형 그리기](ch02-03.py)  
* [원 그리기](ch02-04.py)  
* [타원 그리기](ch02-05.py)  
* [다각형 그리기](ch02-06.py)  
* [타원 폴리곤 좌표 생성](ch02-07.py)  
* [볼록 다각형 채우기](ch02-08.py)  
* [다각형 채우기](ch02-09.py)  
* [문자열 출력하기](ch02-10.py)

### Lecture03 - 마우스 및 키보드 이벤트 처리와 트랙바 활용하기
* [키보드 이벤트 처리](ch03-01.py)  
* [모든 마우스 이벤트 처리](ch03-02.py)  
* [키보드 이벤트 처리](ch03-03.py)  
* [단순 슬라이더 트랙바](ch03-04.py)  
* [비디오 파일을 트랙바로 제어](ch03-05.py)  

### Lecture04 - 한글 폰트 출력하기
* [기본적인 텍스트 출력](ch04-01.py)  
* [한글 텍스트 출력](ch04-02.py)

### Lecture05 - 이미지 밝기와 명암 조절
* [cv2.imread로 직접 그레이스케일 변환](ch05-01.py)  
* [cv2.cvtColor로 그레이스케일 변환](ch05-02.py)  
* [이미지 밝기(brightness) 조절](ch05-03.py)  
* [이미지 명암(contrast) 조절](ch05-04.py)  
* [cv2.addWeighted함수를 사용한 밝기 및 명암 조절](ch05-05.py)  
* [트랙바를 사용한 기본적인 밝기와 명암 조절](ch05-06.py)  
* [트랙바를 사용한 cv2.addWeighted 밝기와 명암 조절](ch05-07.py)  

### Lecture06 - 히스토그램(histogram) 분석
* [그레이스케일 이미지에서 히스토그램 계산](ch06-01.py)  
* [컬러 이미지에서 히스토그램 계산 (R,G,B 각각 계산)](ch06-02.py)  
* [특정 영역에서 히스토그램 계산 (마스크 사용)](ch06-03.py)  
* [그레이스케일 이미지에서 히스토그램 PDF와 CDF 계산](ch06-04.py)  
* [cv2.equalizeHist를 사용한 히스토그램 평활화](ch06-05.py)  
* [히스토그램 평활화의 CDF 계산 및 적용](ch06-06.py)  
* [CLAHE(Contrast Limited Adaptive Histogram Equalization)](ch06-07.py)  
* [히스토그램 스트레칭(stretching)](ch06-08.py)  
* [히스토그램 매칭(matching)](ch06-09.py)  

### Lecture07 - 산술 연산과 논리 연산
* [이미지와 상수 간 덧셈과 곱셈 연산](ch07-01.py)  
* [이미지 간 덧셈 연산](ch07-02.py)  
* [이미지 간 뺄셈 연산](ch07-03.py)  
* [cv2.addWeighted함수를 사용한 산술 연산(blending)](ch07-04.py)  
* [이미지 논리 연산(masking)](ch07-05.py)  

### Lecture08 - 이미지 크기 조정 및 자르기
* [이미지 자르기](ch08-01.py)  
* [이미지 크기조정 (확대)](ch08-02.py)  
* [이미지 크기조정 (축소)](ch08-03.py)  

### Lecture09 - 색상 검출 및 색 공간 변환
* [칼라 이미지 채널 분리(splitting)와 병합(merging)](ch09-01.py)  
* [트랙바를 이용한 색상 검출(color segmentation)](ch09-02.py)  

### Lecture10 - 필터와 컨볼루션
* [2D-이미지 필터링](ch10-01.py)
* [2D-이미지 블러링](ch10-02.py)
* [2D-이미지 엠보싱](ch10-03.py)
* [2D-이미지 샤프닝](ch10-04.py)

### Lecture11 - 엣지 검출
* [OpenCV 엣지 검출](ch11-01.py)
* [cv2.HoughLines](ch11-02.py)
* [cv2.HoughLinesP](ch11-03.py)
* [cv2.HoughCircles](ch11-04.py)

### Lecture12 - 이진화 (임계처리)
* [cv2.Threshold](ch12-01.py)
* [cv2.adaptiveThreshold](ch12-02.py)
* [Otsu's threshold](ch12-03.py)

### Lecture13 - 모폴로지
* [OpenCV 모폴로지 함수](ch13-01.py)
* [watershed 알고리즘을 이용한 동전 분류](ch13-02.py)

### Lecture14 - 외곽선 검출과 레이블링
* [cv2.findContours](ch14-01.py)
* [cv2.approxPolyDP](ch14-02.py)
* [cv2.convexHull](ch14-03.py)
* [cv2.moments](ch14-04.py)
* [실시간 외곽선 검출](ch14-05.py)
* [cv2.connectedComponents를 사용한 레이블링](ch14-06.py)
* [cv2.findContours를 사용한 레이블링](ch14-07.py)

### Practice01 - 각도 측정기
* [세점을 사용하는 각도 측정 방법](pt01-01.py)  

### Practice02 - 웹캠을 활용한 생상 인식 및 그리기
* [웹캠을 활용한 색상 인식 및 그리기 실습](pt02-01.py)