
import streamlit as st

# 1. 페이지 설정 (웹 브라우저 탭에 표시될 내용)
st.set_page_config(
    page_title="나의 자기소개 페이지",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 구성 (프로필 요약 및 연락처)
with st.sidebar:
    st.header("📌 Contact")
    st.write("📧 이메일: email@example.com")
    st.write("🐙 GitHub: [github.com/username](https://github.com)")
    st.write("🏠 블로그: [myblog.com](https://blog.com)")
    
    st.markdown("---")
    st.caption("© 2026 홍길동. All rights reserved.")

# 3. 메인 화면 구성
# 타이틀 및 환영 인사
st.title("👋 안녕하세요! 저는 홍길동입니다")
st.subheader("💡 '성장을 즐기는 개발자'를 꿈꾸는 홍길동의 포트폴리오입니다.")

# 프로필 이미지 (가상의 이미지 URL이나 로컬 이미지 경로 사용 가능)
# 로컬 이미지를 쓰려면 'profile.jpg' 등으로 대체하세요.
st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=500&q=80", 
         caption="꾸준함이 무기인 홍길동입니다.", width=250)

st.markdown("---")

# 4. 자기소개 섹션
st.header("🧑‍💻 소개 (About Me)")
st.write("""
- **이름:** 홍길동 (Hong Gil Dong)
- **역할:** 백엔드 개발자 / 데이터 엔지니어
- **한 줄 다짐:** "어제보다 0.1%라도 더 성장하는 개발자가 되자!"
""")
st.write("안녕하세요! 새로운 기술을 배우고 문제를 해결하는 과정에서 큰 보람을 느낍니다. 주로 파이썬과 스트림릿을 활용한 빠른 프로토타이핑과 데이터 시각화에 관심이 많습니다.")

st.markdown("---")

# 5. 기술 스택 섹션
st.header("🛠 기술 스택 (Tech Stacks)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Languages & Frameworks")
    st.markdown("- **Python** (Advanced)")
    st.markdown("- **Streamlit** (Intermediate)")
    st.markdown("- **Django / FastAPI**")

with col2:
    st.subheader("Tools & Databases")
    st.markdown("- **Git / GitHub**")
    st.markdown("- **MySQL / PostgreSQL**")
    st.markdown("- **Docker**")

st.markdown("---")

# 6. 인터랙티브 요소 (방명록 기능 예시)
st.header("💌 응원 메시지 남기기")
st.write("방문해주셔서 감사합니다! 한 줄 방명록을 남겨주세요.")

# 사용자 입력 받기
visitor_name = st.text_input("이름 또는 닉네임", placeholder="홍길동")
message = st.text_area("응원의 한 마디", placeholder="만나서 반가워요!")

if st.button("메시지 보내기"):
    if visitor_name and message:
        st.success(f"🎉 {visitor_name}님의 메시지가 성공적으로 전달되었습니다!")
        st.balloons()  # 축하 효과 효과음/풍선 애니메이션
        st.info(f"**[{visitor_name}]**: {message}")
    else:
        st.warning("이름과 메시지를 모두 입력해주세요!")