
import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Ultimate Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS for a modern UI
st.markdown("""
    <style>
        .stApp {
            background: radial-gradient(circle, #141e30, #243b55);
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 15px;
            color: #00d4ff;
        }
        .subtext {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
            color: #a8dadc;
        }
        .stButton button {
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            color: white;
            font-size: 18px;
            padding: 12px 24px;
            border-radius: 12px;
            transition: all 0.3s ease-in-out;
            box-shadow: 0px 4px 15px rgba(255, 75, 43, 0.4);
        }
        .stButton button:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 20px rgba(255, 75, 43, 0.6);
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 50px;
            color: #bbb;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'> Ultimate Unit Converter</h1>", unsafe_allow_html=True)


# Unit categories
units = {
    'Length': {'meters': 1, 'kilometers': 1000, 'centimeters': 0.01, 'millimeters': 0.001, 'miles': 1609.344, 'yards': 0.9144, 'feet': 0.3048, 'inches': 0.0254},
    'Mass': {'kilograms': 1, 'grams': 0.001, 'milligrams': 1e-6, 'pounds': 0.453592, 'ounces': 0.0283495},
    'Time': {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400},
    'Speed': {'meters/second': 1, 'kilometers/hour': 0.277778, 'miles/hour': 0.44704},
    'Temperature': {}
}

categories = list(units.keys())
category = st.selectbox("📂 Select Category", categories)

if category == 'Temperature':
    units_list = ['Celsius', 'Fahrenheit', 'Kelvin']
else:
    units_list = list(units[category].keys())

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("🔄 From", units_list)
with col2:
    to_unit = st.selectbox("➡️ To", units_list)

input_value = st.number_input("✏️ Enter Value", min_value=0.0, value=0.0, step=0.1)

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        return (value * 9/5 + 32) if to_unit == 'Fahrenheit' else (value + 273.15)
    if from_unit == 'Fahrenheit':
        return ((value - 32) * 5/9) if to_unit == 'Celsius' else ((value - 32) * 5/9 + 273.15)
    if from_unit == 'Kelvin':
        return (value - 273.15) if to_unit == 'Celsius' else ((value - 273.15) * 9/5 + 32)

if st.button("🚀 Convert"):
    with st.spinner("⏳ Converting..."):
        time.sleep(1)
        try:
            if category == 'Temperature':
                result = convert_temperature(input_value, from_unit, to_unit)
            else:
                from_factor = units[category][from_unit]
                to_factor = units[category][to_unit]
                base_value = input_value * from_factor
                result = base_value / to_factor
            
            formatted_result = f"{result:.6g}"
            st.success(f"✅ **Result:** {input_value} {from_unit} = {formatted_result} {to_unit}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("<p class='footer'> Developed with using Streamlit | Modern UI | Created by: Muhammad Hassann Khann </p>", unsafe_allow_html=True)

