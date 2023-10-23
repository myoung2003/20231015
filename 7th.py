'''
import numpy as np

#리스트를 배열로 변환
list1=[1,2,3,4]
a = np.array(list1)

print(a)
print(a.shape)
print(a[0])
print(a[1])
'''

'''
#2차원 배열 생성
b = np.array( [[1,2,3],[4,5,6],[7,8,9]] )

print(b)
print(b.shape)
print(b[:2,:2])
'''

'''
# CSV 파일 읽어서 데이터 프레임으로 변환
import pandas as pd

df = pd.read_csv('/content/고객데이터셋.csv', encoding='utf-8')
df
'''

'''
# 행과 열
df.shape
'''

'''
# 열
df.columns
'''

'''
# 데이터 속성
df.info()
'''

'''
# 기술통계요약
df.describe()
'''

'''
# 처음의 5행만 출력
df.head()
'''

'''
#마지막 5행 출력
df.tail()
'''

'''
# 데이터 프레일의 고객병출,성별,나이만  10개의 데이터 출력
df[['고객명','성별','나이']].head(100)
'''

'''
# 고객명 순으로 정렬 + 고객명,성별, 나이만 10의 데이터 출력

sort_df = df.sort_values(by=["고객명"])
sort_df[['고객명','성별','나이']].head(10)
'''
