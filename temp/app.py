import streamlit as st
import pandas as pd 
import time

# # 없으면 상태 초기화 //키가 있는지 체크먼저한다 없으면 처음 실행한다거나 하는 상태
# if 'counter' in st.session_state:
#     st.session_state['counter']=0

# if st.button('Increment'):
#     st.session_state['counter']+=1

# if st.button('초기화'):
#     st.session_state['counter']= 0

# counter= st.session_state['counter']
# st.write(f'카운터:{counter}')
# #딕셔너리처럼 사용

start_time = time.time()
#@st.cache_data #캐시 데이타 미리 저장해
def load_data(parameter:int): #함수 값 달라지면 캐시가 꺠짐
    df=pd.read_csv('2019-Oct-small.csv')
    return df

data=load_data(1)#바꾸면 다시 데이터 로드 파라미터 함수 기준으로 캐싱 적용 
#데이터가 너무 큰 건 대시보드에 넣지 않는 것이 좋음... 
#캐시를 안써도 바른 상태가 좋음 데이터 개수를 조정한다거나 
#데이터 베이스를 통해서 좀 집계된 결과를 가져와야함 
#3초 이상이 뜨면 안묌

v=st.number_input('파라미터 입력-캐시 깨집'0,100) #바꿀 때마다 rerun 다시 계산 안하고 데이터 부르는 과정 스킵하기 때문에 빨라짐
st.slider('볼륭'0,10,step=1)
st.text_input('아이디')

data=framework
st.dataframe(data.head())

elapsed=time.time()-start_time

st.write(f'소요시간: {elapsed}')

st.write('캐시 데이터 적용')
st.write('파라미터를 주면 캐싱이 구분함')