import streamlit as st
from datetime import datetime
import pytz

# Page config
st.set_page_config(
    page_title="My Global Website",
    page_icon="🌎",
    layout="wide"
)

# Main content
st.title("My Global Website")

# Display current UTC time
utc_now = datetime.now(pytz.UTC)
st.write(f"Current UTC time: {utc_now.strftime('%Y-%m-%d %H:%M:%S')}")

# Your other website content here