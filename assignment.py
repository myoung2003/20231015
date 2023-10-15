'''
import pandas as pd

# Series로 데이터 프레임 생성
a=pd.Series(["Sonny","Park","Lee"])
# print(a)
b=pd.Series(["Sonny","Park","Lee"], index=["a","b","c"])
print(b)
'''

'''
# 1,2차원 리스트로 생성
list2=[["Son","M",32],["Park","M",30],["Lee","M",10]]
pd.DataFrame(list2, columns=["Name","Gender","Age"])
'''

'''
# 딕셔너리 데이터 프레임으로 생성
dict = {"Team":["Cubs","Bulls","Fires"],
        "Event":["Baseball","Basketball","Soccer"],
        "Rank":[3,2,5]}
df1=pd.DataFrame(dict)
df1["Player"]=["Swanwon","Lavine","Shaqiri"]
df1
'''

'''
df1.shape
'''

'''
df1.columns
'''

'''
df1.index
'''

'''
# 데이터 프레임 빈도수 기술통계량 확인
df1.describe()
'''

'''
#처음 데이터 5개만 출력
df1.head()
'''

'''
#끝에서 데이터 5개 출력
df1.tail()
'''

'''
# 데이터 프레임 CSV 파일로 저장

colname = ["Team","Event","Rank","Player"]
list3=[["Cubs","Baseball",3,"Swanson"],["Bulls","Basketball",2,"Lavine"],["Fires","Soccer",5,"Shaqiri"],["Sox","Baseball",4,"Robert"]]

df=pd.DataFrame(list3,columns=colname)
df
'''

'''
# 저장
df.to_csv( "./df_file1.csv",encoding="utf-8",index = False )

# /content/df_file1.csv
'''

'''
# 읽어오기 => 데이터 프레임 생성
df2=pd.read_csv( "/content/df_file1.csv",sep="," )
df2
'''

'''
# 데이터 정렬 (오름차순 asc)

df2.sort_values( by = ["Rank"], ascending=False)
'''

'''
# 특정 column만 보고 싶을 때

df2[["Team","Player"]]
'''

'''
# 특정 조건에 해당하는

df2[ df2["Rank"]<4]
'''

'''
df2[ (df2["Rank"]<4) & (df2["Event"] == "Basketball") ]
'''

'''
df2[ (df2["Rank"]<4) | (df2["Event"] == "Basketball") ]
# and 기호 &
# or 기호 | (\위에)
'''

'''
# 데이터 조회 시 특정 문자열을 포함하는 데이터 조회
df2[df2["Team"].str.contains("s")]
'''

'''
# 인덱스 변경
df2=df2.set_index("Team")
df2
'''

'''
# 복구
df2=df2.reset_index()
df2
'''

'''
# 데이터 값 일괄 변경
df2["Event"]=df2["Event"].replace({"Baseball":"BS","Basketball":"BK","Soccer":"SC"})
df2
'''

'''
# 특정 데이터 기준으로 그룹핑

# 종목별 평균 순위
mean_df=df2.groupby(by=["Event"], as_index=False)["Rank"].mean()
mean_df

# 종목별 최고 순위
max_rankdf=df2.groupby(by=["Event"], as_index=False)["Rank"].max()
max_rankdf
'''

'''
'''

'''
'''

'''
'''

'''
'''




