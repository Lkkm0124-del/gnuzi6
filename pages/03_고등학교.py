import streamlit as st

st.title("🎓 고등학교")

choice = st.radio(
    "진로를 선택하세요",
    [
        "대학 진학 준비",
        "놀면서 지낸다"
    ]
)

if st.button("선택 완료"):
    if choice == "대학 진학 준비":
        st.session_state.score += 20
    else:
        st.session_state.score -= 15

    st.success("대학교 페이지로 이동하세요.")
