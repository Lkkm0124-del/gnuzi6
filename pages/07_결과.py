import streamlit as st

st.title("🏆 최종 결과")

score = st.session_state.get("score", 0)
name = st.session_state.get("name", "플레이어")

st.subheader(f"{name}님의 인생 결과")
st.write(f"최종 점수: {score}")

if score >= 80:
    st.success("""
🏆 대기업 CEO

명문대 졸업 후 대기업 CEO가 되었습니다.

연봉: 5억원
자산: 100억원
행복도: ★★★★★
""")

elif score >= 50:
    st.info("""
💼 대기업 직원

안정적인 직장에 취업했습니다.

연봉: 8천만원
자산: 15억원
행복도: ★★★★☆
""")

elif score >= 20:
    st.warning("""
🏠 평범한 직장인

무난한 삶을 살았습니다.

연봉: 4천만원
자산: 5억원
행복도: ★★★☆☆
""")

else:
    st.error("""
🎮 프로 게이머 지망생

공부보다는 게임을 선택했습니다.

연봉: 변동적
자산: 5백만원
행복도: ★★☆☆☆
""")

if st.button("다시 시작"):
    st.session_state.score = 0
