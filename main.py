import google.generativeai as genai
from PIL import Image
import streamlit as st

# ตั้งค่าหน้าจอ Streamlit
st.set_page_config(
    page_title="J.A.R.V.I.S. Interface", page_icon="🤖", layout="wide"
)

# ตรวจสอบและตั้งค่า Gemini API Key จาก Streamlit Secrets
if "GEMINI_API_KEY" in st.secrets:
  genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
  model = genai.GenerativeModel("gemini-1.5-flash")
else:
  st.error("กรุณาตั้งค่า GEMINI_API_KEY ใน Streamlit Secrets ก่อนใช้งาน")

st.markdown("# 🤖 J.A.R.V.I.S. Interface")
st.caption("Secure System Online | Python Core v4.2")

# เก็บประวัติการแชท
if "messages" not in st.session_state:
  st.session_state.messages = []

# แสดงประวัติแชทเก่า
for msg in st.session_state.messages:
  with st.chat_message(
      msg["sender"], avatar="👤" if msg["sender"] == "user" else "🤖"
  ):
    st.markdown(msg["text"])

# ช่องรับข้อความจากผู้ใช้
user_input = st.chat_input("ป้อนคำสั่งสำหรับ J.A.R.V.I.S...")

if user_input:
  # บันทึกและแสดงข้อความผู้ใช้
  st.session_state.messages.append({"sender": "user", "text": user_input})
  with st.chat_message("user", avatar="👤"):
    st.markdown(user_input)

  # ประมวลผลและตอบกลับจาก Gemini AI
  with st.chat_message("assistant", avatar="🤖"):
    with st.spinner("กำลังประมวลผล..."):
      try:
        response = model.generate_content(user_input)
        bot_reply = response.text
      except Exception as e:
        bot_reply = f"เกิดข้อผิดพลาดในการเชื่อมต่อ AI: {e}"
      st.markdown(bot_reply)
      st.session_state.messages.append(
          {"sender": "assistant", "text": bot_reply}
      )
