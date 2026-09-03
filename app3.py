import streamlit as st
from database.manager import 
#데이터 베이스 관련 모듈은 가져다가 사용하기만 함 

#앱구동하기 위한 추가 모듈 파일들 뺴두고 
#따로 빼두고 메인으로 구동- 코드 진입전 파일은 길어지지 않음 
#나누는 것 괜찮은 설계 서로가 독립적인데 혼자로 완전할 수 있게 관리 but ... 응집이 생기는 경우 파라미터 같은 걸로 넣어주기 
#코드를 모아서 가져다가 사용하는 식 
import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd

# 코드 실행 진입점 = app.py

# 추가 모듈, 파일들
from database.manager import connect, select_order
from pages import home
from components import sidebar, item
from state.initlize import initlize

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', '3306')),
    'user': os.getenv('DB_USER', 'analysis'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', ''),
}

initlize()

conn = connect(DB_CONFIG)

orders = select_order(conn)
df = pd.DataFrame(orders)

conn.close()
st.dataframe(df)

page = sidebar.render()

print(st.session_state['page'])

if st.session_state['page'] == 0:
    home.page()
if st.session_state['page'] == 1:
    st.write('다른 페이지')

    for i in range(10):
        item.Item()