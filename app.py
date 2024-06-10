import streamlit as st
from streamlit_option_menu import option_menu
# Import all your page scripts

from pages import Math, Science,MoralEdu,Social

st.set_page_config(layout="wide", page_title="Student Progress Analysis")


# CSS to hide the "Pages" link in the sidebar
no_pages_link_style = """
    <style>
        /* Hide the "Pages" link in the sidebar */
        div[data-testid="stSidebarNav"] ul {
            display: none;
        }
    </style>
"""

# Display the CSS to hide the "Pages" link
st.markdown(no_pages_link_style, unsafe_allow_html=True)



# Function to check password
def check_password(page):
    """Returns `True` if the user had a correct password."""


    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state[f"password_{page}"] == st.secrets[page]["password"]:
            st.session_state[f"password_correct_{page}"] = True
            del st.session_state[f"password_{page}"]  # don't store password
        else:
            st.session_state[f"password_correct_{page}"] = False

    if f"password_correct_{page}" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            f"Password for {page}", type="password", on_change=password_entered, key=f"password_{page}"
        )
        return False
    elif not st.session_state[f"password_correct_{page}"]:
        # Password not correct, show input + error.
        st.text_input(
            f"Password for {page}", type="password", on_change=password_entered, key=f"password_{page}"
        )
        st.error(f"😕 Password incorrect for {page}")
        return False
    else:
        # Password correct.
        return True

# Dictionary to map page names to their respective modules
PAGES = {
    "Mathematic": Math,
    "Science": Science,
    "MoralEdu": MoralEdu,
    "Social": Social,
}


# Create a sidebar menu for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(PAGES.keys()))

# Render the selected page
if check_password(page):
    PAGES[page].show()