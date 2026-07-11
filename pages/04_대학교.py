import streamlit as st

st.title("🏛️ 대학교")

choice = st.radio(
    "대학교 생활",
    [
        "학점 관리",
        "매일 놀기"
    ]
)

if st.button("선택 완료"):
    if choice == "학점 관리":
        st.session_state.score += 20
    else:
        st.session_state.score -= 15

    st.success("취업 페이지로 이동하세요.")
