import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="🎰 로또 번호 생성기", page_icon="🎯", layout="centered")

# 2. 제목 및 설명
st.title("🎰 로또 번호 생성기 (보너스 포함)")
st.markdown("버튼을 누르면 **1~45** 중에서 **메인 6개 + 보너스 1개** 번호를 뽑아요! 🍀")

# 3. 사용자 입력 (슬라이더)
count = st.slider("몇 세트를 뽑을까요?", 1, 10, 1)

# 4. 로또 번호 추출 함수
def draw_one_set():
    main_numbers = sorted(random.sample(range(1, 46), 6))
    remaining = [n for n in range(1, 46) if n not in main_numbers]
    bonus = random.choice(remaining)
    return main_numbers, bonus

# 5. 실행 버튼 및 결과 출력
if st.button("🎲 로또 번호 뽑기"):
    for i in range(1, count + 1):
        main, bonus = draw_one_set()
        st.success(f"세트 {i} ➜ 🎯 메인: {', '.join(map(str, main))}")
        st.info(f"세트 {i} ➜ 💎 보너스: {bonus}")
    st.balloons()  # 축하 풍선 효과
else:
    st.caption("⬆️ 세트 개수를 정하고 버튼을 눌러보세요!")

# 6. 하단 푸터
st.markdown("---")
st.caption("Made with Streamlit · 행운 가득! 🍀")
