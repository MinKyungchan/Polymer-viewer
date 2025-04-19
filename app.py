
import json
import streamlit as st
from PIL import Image

# 데이터 로드
with open("polymer_data.json", "r") as f:
    data = json.load(f)

# 사이드바
st.sidebar.title("🔍 Polymer 검색")
options = [f"{item['id']} - {item['name']}" for item in data]
selection = st.sidebar.selectbox("폴리머를 선택하세요:", options)

# 선택된 폴리머 정보
polymer = data[options.index(selection)]
st.title(f"🧪 {polymer['name']} ({polymer['abbreviation']})")

# 이미지 표시
st.subheader("📄 Page 1 (구조식, Pyrogram, Peak Table)")
st.image(Image.open(polymer["page_1_image"]))

st.subheader("📄 Page 2 (Mass Spectra, EGA, Top 10 MS)")
st.image(Image.open(polymer["page_2_image"]))

# 열분해 온도 정보
dt = polymer["decomposition_temp"]
st.info(f"열분해 온도 범위: {dt['start']}°C ~ {dt['end']}°C (peak: {dt['peak']}°C)")
