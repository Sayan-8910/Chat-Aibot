@@ -49,7 +49,7 @@ def authenticate() -> stauth.Authenticate | str | None:
        return authenticator
    else:
        # Call generate_fernet_key insternally, pass user name and passwrod and keep the key in server cookies
        authenticator.login('Login', 'main', generate_fernet_key)
        authenticator.login('', 'main', generate_fernet_key)
        if st.session_state["authentication_status"] is False:
            st.error('Username/password is incorrect')
        elif st.session_state["authentication_status"] is None: