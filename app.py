import streamlit as st
import json
from PIL import Image

with open("polymer_data.json", "r") as f:
    data = json.load(f)

st.sidebar.title("🔍 Polymer 검색")
options = [f"{d['id']} - {d['name']}" for d in data]
choice = st.sidebar.selectbox("폴리머를 선택하세요", options)
selected = data[options.index(choice)]

st.title(f"🧪 {selected['name']}")

st.subheader("📄 페이지 1")
st.image(Image.open(selected["page_1_image"]))

st.subheader("📄 페이지 2")
st.image(Image.open(selected["page_2_image"]))

st.markdown("---")
st.caption("열분해 GC/MS 데이터북 기반 스트림릿 뷰어")
