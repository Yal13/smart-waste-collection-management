import streamlit as st
from database import get_connection

def login_page():

    st.markdown(
        """
        <h1 style='text-align:center;color:green;'>
        🗑 Smart Waste Collection Management System
        </h1>
        <h4 style='text-align:center;color:gray;'>
        Secure Login Portal
        </h4>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    role = st.selectbox(
        "Login As",
        ["Admin", "Worker", "User"]
    )

    email = st.text_input("📧 Email")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    login = st.button("🔐 Login", use_container_width=True)

    if login:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT user_id,
                   name,
                   role
            FROM users
            WHERE email=%s
            AND password=%s
            AND role=%s
        """, (
            email,
            password,
            role
        ))

        user = cursor.fetchone()

        conn.close()

        if user:

            st.session_state.logged_in = True
            st.session_state.user_id = user[0]
            st.session_state.name = user[1]
            st.session_state.role = user[2]

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Email or Password")
