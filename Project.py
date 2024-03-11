import streamlit as st

# สร้างฟังก์ชันสำหรับประมวลผล
def calculate_style(height, weight, body_type):
    # ตัวอย่าง: ประมวลผลตามข้อมูลที่รับเข้ามา
    # ในที่นี้คือตัวอย่างเท่านั้น
    # คุณควรทำการวิเคราะห์และประมวลผลจริงๆ
    return f"ควรสวมใส่ลุค {body_type} เพราะมีสัดส่วนที่สมสามารถ"

# หน้าเว็บ
def main():
    st.title("เว็บไซต์สไตล์ หุ่นเเบบนี้เเต่งตัวเเบบไหนดี")

    # ส่วนของกรอกข้อมูล
    height = st.slider("ส่วนสูง (เซนติเมตร)", 140, 200, 170)
    weight = st.slider("น้ำหนัก (กิโลกรัม)", 40, 120, 60)
    body_type_options = ["กล้ามเนื้อ", "ผอม", "น้ำหนักเกิน", "ปกติ"]
    body_type = st.selectbox("รูปร่างของร่างกาย", body_type_options)
    
    import streamlit as st

# สร้างเริ่มต้นสำหรับเลือกหุ่น
st.sidebar.header('เลือกหุ่น')
selected_body_type = st.sidebar.radio('', ['โอเอวใหญ่', 'ตัวเอ', 'เอ้ก', 'เอส', 'h', 'ที'])

# รายละเอียดของแต่ละประเภทหุ่น
body_types_details = {
    'โอเอวใหญ่': 'หุ่นรูปตัวโอเอวใหญ่กว่าสะโพกคล้ายรูปแอปเปิ้ล',
    'ตัวเอ': 'หุ่นรูปตัวเอ',
    'เอ้ก': 'หุ่นรูปตัวเอ้ก',
    'เอส': 'หุ่นรูปตัวเอส',
    'h': 'หุ่นรูปตัว h',
    'ที': 'หุ่นรูปตัวที'
}

# แสดงรายละเอียดของหุ่นที่เลือก
st.write(f"## รูปแบบหุ่น: {selected_body_type}")
st.write(body_types_details[selected_body_type])

    # ปุ่มสำหรับประมวลผล
if st.button("ประมวลผล"):
        result = calculate_style(height, weight, body_type)
        st.success(result)

if __name__ == "__main__":
    main()


