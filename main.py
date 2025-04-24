import streamlit as st
import string

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter Your Password", type="password")

def is_password_valid(password):
    has_number = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in string.punctuation for char in password)
    is_long_enough = len(password) >= 8

    return has_number, has_upper, has_lower, has_special, is_long_enough

def calculate_strength_score(conditions):
    return sum(conditions)

if st.button("✅ Validate Password"):
    has_number, has_upper, has_lower, has_special, is_long_enough = is_password_valid(password)
    score = calculate_strength_score([has_number, has_upper, has_lower, has_special, is_long_enough])

    st.markdown("### 🔎 Password Analysis:")
    
    st.write(f"- 🔢 Contains number: {'✅' if has_number else '❌'}")
    st.write(f"- 🔠 Contains uppercase letter: {'✅' if has_upper else '❌'}")
    st.write(f"- 🔡 Contains lowercase letter: {'✅' if has_lower else '❌'}")
    st.write(f"- 🔣 Contains special character: {'✅' if has_special else '❌'}")
    st.write(f"- 📏 Minimum 8 characters: {'✅' if is_long_enough else '❌'}")

    st.markdown("### 🧠 Password Strength Result:")
    
    if score == 5:
        st.success("✅ Excellent! Your password is very strong. 🔐")
    elif score == 4:
        st.info("🙂 Good password, but you can make it stronger.")
    elif score == 3:
        st.warning("⚠️ Your password is average. Add more variety.")
    else:
        st.error("❌ Weak password! Please improve it with numbers, symbols, or uppercase letters.")
