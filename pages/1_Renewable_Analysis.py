import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(
    page_title="Renewable Energy Analysis",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS (same as Home.py)
st.markdown("""
<style>
    /* Add the same CSS as Home.py */
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">Renewable Energy Analysis</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("World Energy Consumption.clean.csv")
    return df

df = load_data()

# Analysis container
st.markdown('<div class="card-container">', unsafe_allow_html=True)

# Add filters in columns
col1, col2, col3 = st.columns(3)

with col1:
    selected_year = st.slider("Select Year", int(df['year'].min()), int(df['year'].max()), int(df['year'].max()))

with col2:
    top_n = st.selectbox("Top N Countries", [5, 10, 15, 20], index=1)

with col3:
    energy_type = st.selectbox("Energy Type", ["Solar", "Wind", "Biofuel", "All Renewable"])

# Create visualizations
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
fig.patch.set_facecolor('#0d1117')
ax1.set_facecolor('#161b22')
ax2.set_facecolor('#161b22')

# Plot 1: Trend over time
sns.lineplot(data=df, x='year', y='solar_energy_per_capita', ax=ax1, color='#2ea043')
ax1.set_title('Solar Energy Consumption Trend', color='#c9d1d9')
ax1.grid(True, alpha=0.2)

# Plot 2: Top countries
top_countries = df[df['year'] == selected_year].nlargest(top_n, 'solar_energy_per_capita')
sns.barplot(data=top_countries, x='country', y='solar_energy_per_capita', ax=ax2, color='#2ea043')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
ax2.set_title(f'Top {top_n} Countries by Solar Energy Usage ({selected_year})', color='#c9d1d9')

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)