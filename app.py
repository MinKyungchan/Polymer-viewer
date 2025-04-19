# NOTE: This version avoids importing Streamlit unless explicitly run in a compatible environment.
import json
import os
from PIL import Image  # 이미지 처리를 위해 추가

# Helper to render polymer info in a console environment if needed
def render_polymer_console(data):
    print("Available polymers:")
    for item in data:
        print(f"{item['id']}: {item['name']} ({item['abbreviation']})")
    selected_id = input("Enter polymer ID to view details: ")
    polymer = next((p for p in data if p['id'] == selected_id), None)
    if not polymer:
        print("Polymer not found.")
        return
    print(f"\n--- {polymer['name']} ({polymer['abbreviation']}) ---")
    print(f"Structure Image: {polymer['structure_image']}")
    print(f"Pyrogram Image: {polymer['pyrogram_image']}")
    print(f"Peak Table Image: {polymer['peaks_table_image']}")
    print(f"EGA Image: {polymer['ega_image']}")
    print(f"Decomposition Temp: {polymer['decomposition_temp']['start']}°C - {polymer['decomposition_temp']['end']}°C (peak: {polymer['decomposition_temp']['peak']}°C)")
    print(f"Average Spectrum: {polymer['avg_spectrum_image']}")
    print(f"Top 10 MS Spectra: {polymer['ms_spectra_image']}")

# Load polymer data
with open("polymer_data.json", "r") as f:
    data = json.load(f)

# Check if Streamlit is available
try:
    import streamlit as st

    # Sidebar - Polymer selection
    st.sidebar.title("🔍 Polymer 검색")
    polymer_options = [f"{item['id']} - {item['name']}" for item in data]
    selected_polymer = st.sidebar.selectbox("폴리머를 선택하세요:", polymer_options)

    # Get selected polymer info
    polymer = data[polymer_options.index(selected_polymer)]

    # Main View
    st.title(f"🧪 {polymer['name']} ({polymer['abbreviation']})")

    st.subheader("🧬 화학 구조식")
    with open(polymer["structure_image"], "rb") as f:
        st.image(Image.open(f))

    st.subheader("📈 Pyrogram (열분해 크로마토그램)")
    with open(polymer["pyrogram_image"], "rb") as f:
        st.image(Image.open(f))
    st.caption("Pyrogram에서 얻어진 주요 피크 데이터:")
    with open(polymer["peaks_table_image"], "rb") as f:
        st.image(Image.open(f))

    st.subheader("🌡️ EGA Thermogram")
    with open(polymer["ega_image"], "rb") as f:
        st.image(Image.open(f))
    dt = polymer["decomposition_temp"]
    st.info(f"열분해 온도 범위: {dt['start']}°C ~ {dt['end']}°C (peak: {dt['peak']}°C)")

    st.subheader("💥 평균 Mass Spectrum")
    with open(polymer["avg_spectrum_image"], "rb") as f:
        st.image(Image.open(f))

    st.subheader("🔬 Top 10 MS 스펙트럼")
    with open(polymer["ms_spectra_image"], "rb") as f:
        st.image(Image.open(f))

    st.markdown("---")
    st.markdown("ⓘ 이 뷰어는 Pyrolysis-GC/MS 데이터북 기반입니다. 아이패드에서도 사용 가능: 웹으로 접속하세요!")

except ModuleNotFoundError:
    print("[INFO] Streamlit not found. Falling back to console mode.")
    render_polymer_console(data)
