import streamlit as st

st.set_page_config(page_title="무드 플레이리스트 🎶", page_icon="🎧")

st.title("🎧 나만의 무드 플레이리스트")
st.write("당신의 기분에 딱 맞는 음악을 추천해드려요!")

# 기분 선택
mood = st.selectbox(
    "오늘의 기분을 선택해 주세요",
    ["😊 행복", "😢 우울", "😎 신남", "😴 피곤", "❤️ 사랑", "😤 화남"]
)

# 기분별 음악 추천 데이터
playlist = {
    "😊 행복": [
        ("Pharrell Williams - Happy", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Katrina & The Waves - Walking on Sunshine", "https://www.youtube.com/watch?v=iPUmE-tne5U"),
    ],
    "😢 우울": [
        ("Adele - Someone Like You", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Coldplay - Fix You", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
    ],
    "😎 신남": [
        ("Daft Punk - Get Lucky", "https://www.youtube.com/watch?v=5NV6Rdv1a3I"),
        ("Bruno Mar
