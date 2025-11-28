import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="GROK.VIDEO.MAKER", page_icon="🎬", layout="wide")
st.title("🎬 Grok AI – Tạo Phim Dài Tự Động")
st.markdown("**Viết kịch bản phim 15–120 phút chỉ trong vài giây!**")

api_key = st.text_input("Nhập xAI API Key của bạn:", type="password", help="Lấy tại https://console.x.ai")
if not api_key:
    st.warning("Dán API Key vào để bắt đầu nhé!")
    st.stop()

client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")

c1, c2 = st.columns(2)
with c1:
    idea = st.text_area("Ý tưởng phim:", height=130, placeholder="Ví dụ: Cô gái Sài Gòn có khả năng dừng thời gian để cứu người yêu...")
with c2:
    length = st.selectbox("Độ dài phim:", ["15 phút", "60 phút", "120 phút"])
    style = st.selectbox("Thể loại:", ["Hành động", "Tình cảm", "Kinh dị", "Viễn tưởng", "Hài hước", "Tâm lý", "Cổ trang"])

if st.button("TẠO KỊCH BẢN NGAY", type="primary", use_container_width=True):
    with st.spinner("Grok đang viết kịch bản siêu đỉnh..."):
        prompt = f"Viết kịch bản phim hoàn chỉnh bằng tiếng Việt, độ dài {length}, thể loại {style}. Ý tưởng: {idea}\nChia rõ từng Scene, có mô tả hình ảnh + đối thoại chi tiết, sẵn quay phim luôn."
        resp = client.chat.completions.create(
            model="grok-4",
            messages=[{"role":"user","content":prompt}],
            max_tokens=8000,
            temperature=0.85
        )
        script = resp.choices[0].message.content
    
    st.success("HOÀN THÀNH! Kịch bản phim của bạn đây")
    st.markdown(script)
    st.download_button("Tải kịch bản (.txt)", script, f"kichban_{style}_{length}.txt")
    st.balloons()
