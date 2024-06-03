@@ -3,7 +3,7 @@
from ui.login import authenticate, show_logout, get_user_name, get_enc_key
from ui.home import show_home
from logic.crypto import *
from ui.ui_helpers import hide_streamlit_menu, hide_streamlit_toolbar
from ui.ui_helpers import add_theme_customizations, hide_streamlit_menu, hide_streamlit_toolbar

st.set_page_config(
    page_title="Py Chat",
@@ -12,6 +12,7 @@

hide_streamlit_menu()
hide_streamlit_toolbar()
#add_theme_customizations()

if auth:=authenticate():
    user = get_user_name()
