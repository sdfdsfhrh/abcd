# NumPy 완전 학습 가이드

## 목차
1. [NumPy 소개](#1-numpy-소개)
2. [NumPy 설치 및 가져오기](#2-numpy-설치-및-가져오기)
3. [배열 생성](#3-배열-생성)
4. [배열 속성 및 정보](#4-배열-속성-및-정보)
5. [배열 인덱싱 및 슬라이싱](#5-배열-인덱싱-및-슬라이싱)
6. [배열 연산](#6-배열-연산)
7. [통계 및 집계 함수](#7-통계-및-집계-함수)
8. [축(Axis) 개념 이해](#8-축axis-개념-이해)
9. [실습 예제 및 결과](#9-실습-예제-및-결과)
10. [핵심 정리](#10-핵심-정리)

---

## 1. NumPy 소개

**NumPy(Numerical Python)**는 파이썬의 과학 컴퓨팅을 위한 핵심 라이브러리입니다.

### 주요 특징
- **고성능**: C로 구현된 배열 연산으로 빠른 처리
- **메모리 효율성**: 연속된 메모리 공간 사용
- **벡터화 연산**: 반복문 없이 전체 배열 연산
- **브로드캐스팅**: 크기가 다른 배열 간 연산 지원

### 왜 NumPy를 사용하나요?
- 파이썬 리스트보다 **10~100배 빠름**
- **메모리 사용량이 적음**
- **수학적 연산이 간편함**

---

## 2. NumPy 설치 및 가져오기

### 설치
```bash
pip install numpy
```

### 가져오기
```python
# -*- coding: utf-8 -*-
import numpy as np  # 관례적으로 np로 사용
```

---

## 3. 배열 생성

### 3.1 리스트에서 배열 생성

```python
# 1차원 배열
a = [1, 2, 3]
arr1d = np.array(a)

# 2차원 배열 (행렬)
a = [[1, 2, 3], [4, 5, 6]]
b = np.array(a)
print(a)  # [[1, 2, 3], [4, 5, 6]]
print(b)  # [[1 2 3]
          #  [4 5 6]]
```

**출력 결과:**
```
[[1, 2, 3], [4, 5, 6]]
[[1 2 3]
 [4 5 6]]
```

### 3.2 타입 확인

```python
print(type(a))  # <class 'list'>
print(type(b))  # <class 'numpy.ndarray'>
```

### 3.3 특수 배열 생성

#### 영행렬 (zeros)
```python
# 2x2 영행렬
c = np.zeros([2, 2])
print(c)
# [[0. 0.]
#  [0. 0.]]

# 1차원 배열 (길이 5)
d = np.zeros(5)
print(d)  # [0. 0. 0. 0. 0.]
```

#### 1로 채운 행렬 (ones)
```python
e = np.ones([2, 2])
print(e)
# [[1. 1.]
#  [1. 1.]]
```

#### 특정 값으로 채운 행렬 (full)
```python
f = np.full([2, 3], 5)
print(f)
# [[5 5 5]
#  [5 5 5]]
```

---

## 4. 배열 속성 및 정보

### 4.1 기본 속성

```python
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b.ndim)    # 차원 수: 2
print(b.shape)   # 형태: (2, 3) - 2행 3열
print(b.size)    # 전체 원소 개수: 6
print(b.dtype)   # 데이터 타입: int64 (시스템에 따라 다름)
```

### 4.2 배열 원소 접근

```python
print(b[0, 0])  # 첫 번째 행, 첫 번째 열: 1
print(b[0, 1])  # 첫 번째 행, 두 번째 열: 2
print(b[1, 2])  # 두 번째 행, 세 번째 열: 6
```

---

## 5. 배열 인덱싱 및 슬라이싱

### 5.1 기본 슬라이싱

```python
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
print(arr)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
```

### 5.2 부분 배열 추출

```python
# 첫 2행, 첫 2열
a = arr[0:2, 0:2]
print(a)
# [[1 2]
#  [4 5]]

# 2-3행, 2-3열
b = arr[1:3, 1:3]
print(b)
# [[5 6]
#  [8 9]]

# 2행부터 끝까지, 2열부터 끝까지
c = arr[1:, 1:]
print(c)
# [[5 6]
#  [8 9]]
```

### 5.3 슬라이싱 문법 설명

- `start:end`: start부터 end-1까지
- `start:`: start부터 끝까지
- `:end`: 처음부터 end-1까지
- `:`: 전체

---

## 6. 배열 연산

### 6.1 요소별 연산 (Element-wise Operations)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 덧셈
c = a + b  # 또는 np.add(a, b)
print(c)   # [5 7 9]

# 뺄셈
c = a - b  # 또는 np.subtract(a, b)
print(c)   # [-3 -3 -3]

# 곱셈 (요소별)
c = a * b  # 또는 np.multiply(a, b)
print(c)   # [4 10 18]

# 나눗셈
c = a / b  # 또는 np.divide(a, b)
print(c)   # [0.25 0.4 0.5]
```

### 6.2 행렬 곱셈

```python
arr1 = [[1, 2], [3, 4]]  # 2x2 행렬
arr2 = [[5, 6], [7, 8]]  # 2x2 행렬
a = np.array(arr1)
b = np.array(arr2)

# 행렬 곱셈
c = np.dot(a, b)
print(c)
# [[19 22]  # (1*5 + 2*7, 1*6 + 2*8)
#  [43 50]]  # (3*5 + 4*7, 3*6 + 4*8)
```

### 6.3 연산 방법 비교

| 연산 | 기호 | 함수 | 설명 |
|------|------|------|------|
| 덧셈 | `+` | `np.add()` | 요소별 덧셈 |
| 뺄셈 | `-` | `np.subtract()` | 요소별 뺄셈 |
| 곱셈 | `*` | `np.multiply()` | 요소별 곱셈 |
| 나눗셈 | `/` | `np.divide()` | 요소별 나눗셈 |
| 행렬곱 | `@` | `np.dot()` | 행렬 곱셈 |

---

## 7. 통계 및 집계 함수

### 7.1 기본 통계 함수

```python
a = np.array([[-1, 2, 3], [3, 4, 8]])
print(a)
# [[-1  2  3]
#  [ 3  4  8]]
```

### 7.2 전체 배열 통계

```python
# 전체 합계
s = a.sum()  # 또는 np.sum(a)
print('sum =', s)        # sum = 19

# 평균
print('mean =', a.mean())  # mean = 3.1666666666666665

# 표준편차
print('sd =', a.std())     # sd = 2.9832867780570453

# 전체 곱
print('product =', a.prod())  # product = -576
```

### 7.3 축별 통계 (매우 중요!)

```python
# axis=0: 열 방향 연산 (세로로 계산)
print('sum by column =', a.sum(axis=0))  # [2 6 11]
# 첫 번째 열: -1 + 3 = 2
# 두 번째 열: 2 + 4 = 6  
# 세 번째 열: 3 + 8 = 11

# axis=1: 행 방향 연산 (가로로 계산)
print('sum by row =', a.sum(axis=1))     # [4 15]
# 첫 번째 행: -1 + 2 + 3 = 4
# 두 번째 행: 3 + 4 + 8 = 15
```

---

## 8. 축(Axis) 개념 이해

### 8.1 축의 개념

2차원 배열에서:
- **axis=0**: 행 축 (↓ 세로 방향)
- **axis=1**: 열 축 (→ 가로 방향)

```
    axis=1 →
axis=0 [[-1  2  3]
  ↓     [ 3  4  8]]
```

### 8.2 축별 연산 시각화

```python
a = np.array([[-1, 2, 3], [3, 4, 8]])

# axis=0 연산 (열별 합계)
# 열1: -1 + 3 = 2
# 열2: 2 + 4 = 6
# 열3: 3 + 8 = 11
# 결과: [2, 6, 11]

# axis=1 연산 (행별 합계)  
# 행1: -1 + 2 + 3 = 4
# 행2: 3 + 4 + 8 = 15
# 결과: [4, 15]
```

### 8.3 다양한 통계 함수

| 함수 | 설명 | 예시 |
|------|------|------|
| `np.sum()` | 합계 | `a.sum(axis=0)` |
| `np.mean()` | 평균 | `a.mean(axis=1)` |
| `np.std()` | 표준편차 | `a.std()` |
| `np.var()` | 분산 | `a.var()` |
| `np.min()` | 최솟값 | `a.min(axis=0)` |
| `np.max()` | 최댓값 | `a.max(axis=1)` |

---

## 9. 실습 예제 및 결과

### 9.1 numpy_study1.py 실행 결과

```python
# 원본 코드와 예상 출력
a = [[1,2,3], [4,5,6]]
b = np.array(a)

print(a)           # [[1, 2, 3], [4, 5, 6]]
print(type(a))     # <class 'list'>
print(b)           # [[1 2 3]
                   #  [4 5 6]]
print(type(b))     # <class 'numpy.ndarray'>
print(b.ndim)      # 2
print(b.shape)     # (2, 3)
print(b[0,0])      # 1
print(b[0,1])      # 2

c = np.zeros([2,2])
print(c)           # [[0. 0.]
                   #  [0. 0.]]

d = np.zeros(5)
print(d)           # [0. 0. 0. 0. 0.]

e = np.ones([2,2])
print(e)           # [[1. 1.]
                   #  [1. 1.]]

f = np.full([2,3], 5)
print(f)           # [[5 5 5]
                   #  [5 5 5]]
```

### 9.2 numpy_study2.py 실행 결과

```python
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(lst)

a = arr[0:2, 0:2]
print(a)           # [[1 2]
                   #  [4 5]]

b = arr[1:3, 1:3]
print(b)           # [[5 6]
                   #  [8 9]]

a = arr[1:, 1:]
print(a)           # [[5 6]
                   #  [8 9]]
```

### 9.3 numpy_study3.py 실행 결과

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

c = a + b
print(c)           # [5 7 9]

c = np.multiply(a, b)
print(c)           # [4 10 18]

c = np.divide(a,b)
print(c)           # [0.25 0.4 0.5]

arr1 = [[1,2],[3,4]]
arr2 = [[5,6],[7,8]]
a = np.array(arr1)
b = np.array(arr2)

c = np.dot(a, b)
print(c)           # [[19 22]
                   #  [43 50]]
```

### 9.4 numpy_matrix.py 실행 결과

```python
a = np.array([[-1,2,3],[3,4,8]])

print('sum=', a.sum())                    # sum= 19
print('sum by row=', a.sum(axis=0))       # sum by row= [2 6 11]
print('sum by row=', a.sum(axis=1))       # sum by row= [4 15]
print('mean=', a.mean())                  # mean= 3.1666666666666665
print('sd=', a.std())                     # sd= 2.9832867780570453
print('product=', a.prod())               # product= -576
```

---

## 10. 핵심 정리

### 10.1 NumPy의 장점

1. **성능**: 파이썬 리스트보다 훨씬 빠름
2. **메모리 효율성**: 연속된 메모리 사용으로 효율적
3. **벡터화**: 반복문 없이 배열 전체 연산
4. **브로드캐스팅**: 다른 크기 배열 간 연산
5. **풍부한 함수**: 수학, 통계, 선형대수 함수 제공

### 10.2 기억해야 할 핵심 개념

#### 배열 생성
- `np.array()`: 리스트에서 배열 생성
- `np.zeros()`, `np.ones()`, `np.full()`: 특수 배열

#### 배열 정보
- `.ndim`: 차원 수
- `.shape`: 형태 (행, 열)
- `.size`: 전체 원소 수

#### 축(Axis) 이해
- **axis=0**: 행 방향 (↓ 세로)
- **axis=1**: 열 방향 (→ 가로)

#### 연산 종류
- **요소별 연산**: `+`, `-`, `*`, `/`
- **행렬 곱셈**: `np.dot()` 또는 `@`

#### 통계 함수
- `.sum()`, `.mean()`, `.std()`, `.prod()`
- 축 지정 가능: `axis=0` (열별), `axis=1` (행별)

### 10.3 다음 학습 권장 사항

1. **배열 조작**
   - reshape, transpose
   - 배열 결합 (concatenate, stack)
   - 배열 분할 (split)

2. **조건부 선택**
   - 불린 인덱싱
   - where 함수

3. **선형대수**
   - 행렬식, 역행렬
   - 고유값, 고유벡터

4. **랜덤 모듈**
   - 난수 생성
   - 샘플링

### 10.4 실무 활용 팁

1. **항상 np로 import**: `import numpy as np`
2. **적절한 데이터 타입 사용**: dtype 지정으로 메모리 절약
3. **벡터화 활용**: 반복문 대신 NumPy 연산 사용
4. **축 개념 숙지**: axis 매개변수 정확히 이해
5. **브로드캐스팅 이해**: 다른 크기 배열 간 연산 원리 파악

---

## 참고 자료

- [NumPy 공식 문서](https://numpy.org/doc/)
- [NumPy 튜토리얼](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy 브로드캐스팅 가이드](https://numpy.org/doc/stable/user/basics.broadcasting.html)

---
