import streamlit as st

# Calculate BMR using Mifflin-St Jeor Equation
def calculate_bmr(gender, weight, height_ft, height_in, age):
    height_cm = (height_ft * 30.48) + (height_in * 2.54)
    weight_kg = weight * 0.453592

    if gender == "Male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

# Get activity multiplier
def get_activity_multiplier(activity):
    return {
        "🛌 Sedentary (little or no exercise)": 1.2,
        "🚶 Light (exercise 1–3 days/week)": 1.375,
        "🏃 Moderate (exercise 4–5 days/week)": 1.55,
        "🏋️ Active (daily or intense 3–4 days/week)": 1.725,
        "🔥 Very Active (intense 6–7 days/week)": 1.9
    }[activity]

# Streamlit UI
def main():
    st.set_page_config(page_title="Calorie Calculator", page_icon="🔥", layout="centered")
    st.title("🔥 Daily Calorie Needs Calculator")
    st.markdown("Estimate how many calories you need daily based on your **age**, **gender**, **height**, **weight**, and **activity level**.")

    with st.form("calorie_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("🎂 Age", min_value=15, max_value=80, value=25)
            gender = st.radio("⚧️ Gender", ["Male", "Female"], horizontal=True)
        with col2:
            weight = st.number_input("⚖️ Weight (lbs)", min_value=50, max_value=500, value=165)

        st.markdown("### 📏 Height")
        height_col1, height_col2 = st.columns(2)
        with height_col1:
            height_ft = st.number_input("Feet", min_value=0, value=5)
        with height_col2:
            height_in = st.number_input("Inches", min_value=0, value=10)

        st.markdown("### 🏃 Activity Level")
        activity = st.selectbox("How active are you?", [
            "🛌 Sedentary (little or no exercise)",
            "🚶 Light (exercise 1–3 days/week)",
            "🏃 Moderate (exercise 4–5 days/week)",
            "🏋️ Active (daily or intense 3–4 days/week)",
            "🔥 Very Active (intense 6–7 days/week)"
        ])

        submitted = st.form_submit_button("Calculate Calories 🔍")

        if submitted:
            bmr = calculate_bmr(gender, weight, height_ft, height_in, age)
            multiplier = get_activity_multiplier(activity)
            calories = round(bmr * multiplier)

            st.success(f"✅ **Estimated Daily Calories Needed:** {calories} kcal")
            st.info("This is an estimate based on your current inputs. For specific dietary needs, consult a health professional.")

if __name__ == "__main__":
    main()  
