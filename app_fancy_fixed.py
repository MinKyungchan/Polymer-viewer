import streamlit as st
import json
from PIL import Image

# Load data
with open("polymer_data.json", "r") as f:
    data = json.load(f)

# Full-width layout + visual enhancements
st.markdown("""
    <style>
    .main .block-container {
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: none !important;
    }
    .st-emotion-cache-z5fcl4 {
        max-width: 100% !important;
    }
    .title-style {
        font-size: 30px;
        font-weight: 700;
        color: #0072C6;
    }
    .subtitle {
        font-weight: bold;
        font-size: 20px;
        margin-top: 1rem;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔍 Polymer 검색")
search_term = st.sidebar.text_input("이름 또는 약어 검색:")
filtered_data = [d for d in data if search_term.lower() in d['name'].lower()] if search_term else data
options = [f"{d['id']} - {d['name']}" for d in filtered_data]
choice = st.sidebar.selectbox("폴리머를 선택하세요", options)
selected = filtered_data[options.index(choice)]

# Title & Info
st.markdown(f"<div class='title-style'>🧪 {selected['name']}</div>", unsafe_allow_html=True)
st.markdown(f"**🆔 ID:** `{selected['id']}`")
st.markdown(f"**🔤 Abbreviation:** `{selected['abbreviation']}`")
st.markdown(f"**📂 Category:** `{selected['category']}`")
st.markdown(f"**🧬 Type:** `{selected['type']}`")

# Thermal Data
st.markdown("<div class='subtitle'>🌡 열분해 온도 정보</div>", unsafe_allow_html=True)
st.success(
    f"- **온도 범위:** {selected['decomposition_temp']['start']}C ~ {selected['decomposition_temp']['end']}C\n"
    f"- **최대 피크 온도:** {selected['decomposition_temp']['peak']}C"
)

# Images
st.markdown("<div class='subtitle'>🖼 Pyrolysis-GC/MS 이미지</div>", unsafe_allow_html=True)
cols = st.columns(2)
with cols[0]:
    st.markdown("**📄 Page 1**")
    st.image(Image.open(selected["page_1_image"]))
with cols[1]:
    st.markdown("**📄 Page 2**")
    st.image(Image.open(selected["page_2_image"]))

st.markdown("---")
st.caption("📚 Pyrolysis-GC/MS 데이터북 기반 스트림릿 앱 · © 2024 PolymerViewer")
