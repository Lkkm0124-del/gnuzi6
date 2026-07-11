import streamlit as st

st.title("🏫 초등학교")

choice = st.radio(
    "방과 후 무엇을 할까요?",
    [
        "공부한다",
        "게임만 한다"
    ]
)

if st.button("선택 완료"):
    if choice == "공부한다":
        st.session_state.score += 10
    else:
        st.session_state.score -= 5

    st.success("중학교 페이지로 이동하세요.")
