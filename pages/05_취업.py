import streamlit as st

st.title("💼 취업")

choice = st.radio(
    "취업 준비",
    [
        "자격증 공부",
        "준비 안 함"
    ]
)

if st.button("선택 완료"):
    if choice == "자격증 공부":
        st.session_state.score += 25
    else:
        st.session_state.score -= 20

    st.success("결혼 페이지로 이동하세요.")
