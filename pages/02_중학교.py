import streamlit as st

st.title("📚 중학교")

choice = st.radio(
    "시험 기간입니다.",
    [
        "열심히 공부",
        "놀러 다닌다"
    ]
)

if st.button("선택 완료"):
    if choice == "열심히 공부":
        st.session_state.score += 15
    else:
        st.session_state.score -= 10

    st.success("고등학교 페이지로 이동하세요.")
