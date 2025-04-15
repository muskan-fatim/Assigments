import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "🟡"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "🟢"
    elif 25 <= bmi < 29.9:
        return "Overweight", "🟠"
    else:
        return "Obesity", "🔴"

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")
st.title("⚖️ BMI Calculator")
st.markdown("Enter your height and weight to calculate your BMI.")

height = st.number_input("Height (in meters)", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("Weight (in kilograms)", min_value=10.0, max_value=300.0, step=0.1)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        category, icon = get_bmi_category(bmi)
        st.success(f"Your BMI is **{bmi:.2f}** {icon}")
        st.info(f"Category: **{category}**")
    else:
        st.error("Please enter a valid height.")
