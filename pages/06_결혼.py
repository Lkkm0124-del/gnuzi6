import streamlit as st

st.title("💍 결혼")

choice = st.radio(
    "가정생활",
    [
        "가족을 소중히 한다",
        "일만 한다"
    ]
)

if st.button("선택 완료"):
    if choice == "가족을 소중히 한다":
        st.session_state.score += 10
    else:
        st.session_state.score += 0

    st.success("결과 페이지로 이동하세요.")
