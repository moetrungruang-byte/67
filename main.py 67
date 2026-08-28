import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="J.A.R.V.I.S. System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Cyberpunk Theme Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #020617;
        color: #22d3ee;
        font-family: monospace;
    }
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid rgba(8, 145, 178, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"sender": "jarvis",
         "text": "ระบบเชื่อมต่อและดึงข้อมูลทั้งหมดในเครื่องของคุณสำเร็จแล้วครับเจ้านาย พร้อมปฏิบัติการ"}
    ]

if "memories" not in st.session_state:
    st.session_state.memories = [
        {"id": "dev-1", "text": "อุปกรณ์: Python Streamlit Core (th-TH)", "image": None},
        {"id": "dev-2", "text": "สถานะเชื่อมต่อเครื่อง: สำเร็จ", "image": None}
    ]

if "sys_status" not in st.session_state:
    st.session_state.sys_status = "LOCAL PYTHON CORE ACTIVE"

# Sidebar: System & Memories
with st.sidebar:
    st.markdown("### ⚡ J.A.R.V.I.S.")
    st.caption(f"Status: {st.session_state.sys_status}")
    st.markdown("---")

    st.markdown("#### 💾 บันทึกข้อมูลระบบ")
    with st.form("memory_form", clear_on_submit=True):
        memory_input = st.text_input("เพิ่มข้อมูลหรือบันทึก...", placeholder="พิมพ์ข้อมูลที่ต้องการจำ...")
        uploaded_file = st.file_uploader("แนบภาพ", type=["png", "jpg", "jpeg"])
        submit_memory = st.form_submit_button("บันทึก")

        if submit_memory:
            image_data = uploaded_file if uploaded_file else None
            if memory_input.strip() or image_data:
                new_mem = {
                    "id": f"mem-{time.time()}",
                    "text": memory_input,
                    "image": image_data
                }
                st.session_state.memories.insert(0, new_mem)
                st.rerun()

    st.markdown("---")
    st.markdown(f"#### ความทรงจำที่ซิงค์แล้ว ({len(st.session_state.memories)})")

    for idx, mem in enumerate(st.session_state.memories):
        with st.container():
            st.markdown(f"**[{idx + 1}]** {mem['text']}")
            if mem['image']:
                st.image(mem['image'], width=150)
            if st.button("ลบ", key=f"del_{mem['id']}"):
                st.session_state.memories = [m for m in st.session_state.memories if m['id'] != mem['id']]
                st.rerun()
            st.markdown("---")

# Main Chat Area
st.markdown("## 🤖 J.A.R.V.I.S. Interface")
st.caption("Secure System Online | Python Core v4.2")

# Display Chat Messages
for msg in st.session_state.messages:
    if msg["sender"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.markdown(msg["text"])
            if "image" in msg and msg["image"]:
                st.image(msg["image"], width=200)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg["text"])

# Chat Input
user_input = st.chat_input("ป้อนคำสั่งสำหรับ J.A.R.V.I.S...")

if user_input:
    # Append user message
    st.session_state.messages.append({"sender": "user", "text": user_input})
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # Generate JARVIS response
    with st.chat_message("assistant", avatar="🤖"):
        with st.status("กำลังประมวลผลคำสั่ง...", expanded=False) as status:
            time.sleep(1)
            status.update(label="ประมวลผลสำเร็จ", state="complete", expanded=False)

        # Simple intelligent mock response logic
        reply_text = "รับทราบครับเจ้านาย กำลังดำเนินการตามคำสั่งครับ"
        if "สวัสดี" in user_input or "hello" in user_input.lower():
            reply_text = "สวัสดีครับเจ้านาย J.A.R.V.I.S พร้อมให้บริการแล้วครับ"
        elif "สถานะ" in user_input or "status" in user_input.lower():
            reply_text = f"สถานะระบบ: {st.session_state.sys_status}, ความทรงจำทั้งหมดในฐานข้อมูล: {len(st.session_state.memories)} รายการ"

        st.markdown(reply_text)
        st.session_state.messages.append({"sender": "jarvis", "text": reply_text})
