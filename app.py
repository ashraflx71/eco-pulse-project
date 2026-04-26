import streamlit as st
import pandas as pd
import numpy as np
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="Eco-Pulse Simulator", page_icon="⚡", layout="wide")

# 2. تنسيق الواجهة (Black & Blue Theme) بمقاس 22px
st.markdown("""
    <style>
        /* الخلفية السوداء والنص الأبيض */
        .stApp, [data-testid="stAppViewContainer"] { 
            background-color: #000000; 
            color: #ffffff; 
        }
        
        /* ضبط حجم الخط 22px لسهولة القراءة من الهاتف */
        .main .block-container, p, li, span, label, .stMarkdown { 
            font-size: 22px !important; 
            color: #ffffff !important;
        }

        /* العناوين باللون الأزرق المضيء */
        h1, h2, h3 { 
            color: #00d4ff !important; 
            text-align: center; 
            font-weight: bold; 
        }

        /* تنسيق كروت البيانات */
        [data-testid="stMetricValue"] {
            background-color: #111111 !important; 
            border: 1px solid #0056b3 !important; 
            border-radius: 10px; 
            padding: 10px;
            color: #00d4ff !important;
        }
    </style>
    """, unsafe_allow_html=True)

def fetch_philosophy():
    try:
        response = requests.get("https://api.github.com/zen", timeout=5)
        return response.text if response.status_code == 200 else "Keep it simple."
    except:
        return "Stay focused."

def main():
    st.title("⚡ Eco-Pulse: MIT Armband Simulator")
    st.info(f"💡 فلسفة التصميم: {fetch_philosophy()}")

    st.sidebar.header("التحكم بالمحاكاة")
    sample_size = st.sidebar.slider("حجم العينة", 10, 500, 100)

    # توليد بيانات عشوائية للمحاكاة
    np.random.seed(42)
    raw_data = np.random.randn(sample_size, 3)
    df = pd.DataFrame(raw_data, columns=["نبض القلب", "الحركة", "الإشارة الكهربائية"])

    st.subheader("البيانات المعالجة (أول 5 صفوف)")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("التحليل البصري للبيانات")
    st.line_chart(df)
    st.success("تم توليد المحاكاة بنجاح!")

if __name__ == "__main__":
    main()
