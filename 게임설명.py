import streamlit as st

st.set_page_config(
    page_title="인생 시뮬레이터",
    page_icon="👤",
    layout="centered"
)

st.title("👤 인생 시뮬레이터")

if "score" not in st.session_state:
    st.session_state.score = 0

if "name" not in st.session_state:
    st.session_state.name = ""

st.markdown("""
당신의 선택에 따라 인생이 달라집니다.

각 단계에서 선택을 하고,
마지막에 어떤 삶을 살게 되었는지 확인하세요.
""")

name = st.text_input("이름 입력")

if st.button("게임 시작"):
    st.session_state.name = name
    st.success("왼쪽 사이드바에서 '초등학교' 페이지로 이동하세요!")
