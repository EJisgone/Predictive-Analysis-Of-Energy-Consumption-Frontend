import streamlit as st
from datetime import datetime
import pytz
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Energy Analysis Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for sophisticated UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #0d1117;
        padding: 2rem;
    }
    
    /* Header styling */
    .header-container {
        padding: 1rem;
        margin-bottom: 2rem;
        border-radius: 10px;
        background-color: #161b22;
        border: 1px solid #30363d;
    }
    
    /* Title styling */
    .main-title {
        color: #c9d1d9;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    /* Subtitle styling */
    .subtitle {
        color: #8b949e;
        font-size: 1.2rem;
        margin-bottom: 1.5rem;
    }
    
    /* Card container styling */
    .card-container {
        background-color: #161b22;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid #30363d;
    }
    
    /* Info text styling */
    .info-text {
        color: #8b949e;
        font-size: 0.9rem;
    }
    
    /* Metrics styling */
    .metric-container {
        background-color: #1f2937;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        border: none;
    }
    
    /* Dataframe styling */
    .dataframe {
        background-color: #161b22;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=100)
    st.title("Energy Analysis Assistant")
    
    # User info and time
    st.markdown(f"""
    ### User Information
    - **Login:** {st.session_state.get('user_login', 'EJisgone')}
    - **UTC Time:** {datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')}
    """)
    
    st.divider()
    
    # Navigation options
    st.subheader("Navigation")
    pages = {
        "Overview": "📊",
        "Renewable Analysis": "🌱",
        "Non-Renewable Analysis": "⚡",
        "Statistical Insights": "📈"
    }
    for page, icon in pages.items():
        st.button(f"{icon} {page}")

# Main content
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">World Energy Consumption Analysis</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Interactive Analysis and Insights Platform</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("World Energy Consumption.clean.csv")

df = load_data()

# Quick stats in cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.metric("Total Countries", len(df['country'].unique()))
    st.markdown('<p class="info-text">Comprehensive global coverage</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.metric("Years of Data", f"{int(df['year'].max() - df['year'].min())} years")
    st.markdown('<p class="info-text">Long-term trend analysis</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.metric("Data Points", f"{len(df):,}")
    st.markdown('<p class="info-text">Rich analytical foundation</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Main content sections
st.markdown('<div class="card-container">', unsafe_allow_html=True)
st.subheader("Dataset Overview")
st.markdown("""
This comprehensive energy consumption dataset includes:

- **Renewable Energy Metrics:**
  - Biofuel consumption rates
  - Solar energy utilization
  - Wind energy generation
  - Other renewable sources

- **Non-Renewable Energy Metrics:**
  - Coal consumption patterns
  - Nuclear energy usage
  - Oil energy consumption

- **Economic Indicators:**
  - GDP trends
  - Population data
  - Per capita consumption
""")
st.markdown('</div>', unsafe_allow_html=True)

# Quick Actions
st.markdown('<div class="card-container">', unsafe_allow_html=True)
st.subheader("Quick Actions")
col1, col2, col3 = st.columns(3)

with col1:
    st.button("🔍 Explore Data")
with col2:
    st.button("📊 View Analytics")
with col3:
    st.button("📥 Download Report")
st.markdown('</div>', unsafe_allow_html=True)