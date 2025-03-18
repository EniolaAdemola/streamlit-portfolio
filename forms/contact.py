import streamlit as st
import re
import requests


# Create a webhook url
WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"




def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


email = "test@email.com"

is_valid = is_valid_email(email)
print("Is valid: ",is_valid)

def contact_form():
    with st.form("COntact Form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not name:
                st.error("Please enter your name", icon="🧑")
                st.stop()

            if not email:
                st.error("Please enter your email", icon="📧")
                st.stop()

            if not message:
                st.error("Please enter your message", icon="📝")
                st.stop()

            if not is_valid_email(email):
                st.error("Please enter a valid email", icon="📧")
                st.stop()

            data = {
                "name": name,
                "email": email,
                "message": message
            }
            print(data)
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Message sent successfully", icon="🚀")
            else:
                st.error("An error occurred while sending your message", icon="🚫")