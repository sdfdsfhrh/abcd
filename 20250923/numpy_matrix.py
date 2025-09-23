import numpy as np

a = np.array([[-1,2,3],[3,4,8]])

s = np.sum(a)

print('sum=',a.sum()) 

print('sum by row =',a.sum(axis=0)) # 행 방향을 연산(위아래 계산)
print('sum by row =',a.sum(axis=1)) # 가로 방향 (열방향)

print('mean=',a.mean())
print('sd=',a.std())
print('product=',a.prod()) 