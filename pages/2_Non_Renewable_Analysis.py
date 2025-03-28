import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(
    page_title="Non-Renewable Energy Analysis",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #0d1117;
    }
    .header-container {
        padding: 1rem;
        margin-bottom: 2rem;
        border-radius: 10px;
        background-color: #161b22;
        border: 1px solid #30363d;
    }
    .metric-card {
        background-color: #1f2937;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #30363d;
    }
    .plot-container {
        background-color: #161b22;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.title("Non-Renewable Energy Analysis")
st.markdown("Detailed analysis of coal, nuclear, and oil energy consumption patterns")
st.markdown('</div>', unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv("World Energy Consumption.clean.csv")

df = load_data()

# Sidebar filters
st.sidebar.markdown("## Analysis Controls")
year_range = st.sidebar.slider(
    "Select Year Range",
    int(df['year'].min()),
    int(df['year'].max()),
    (2010, 2023)
)

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    coal_avg = df[df['year'].between(*year_range)]['coal_cons_per_capita'].mean()
    st.metric("Average Coal Consumption", f"{coal_avg:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    nuclear_avg = df[df['year'].between(*year_range)]['nuclear_energy_per_capita'].mean()
    st.metric("Average Nuclear Energy", f"{nuclear_avg:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    oil_avg = df[df['year'].between(*year_range)]['oil_energy_per_capita'].mean()
    st.metric("Average Oil Energy", f"{oil_avg:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

# Visualization section
st.markdown('<div class="plot-container">', unsafe_allow_html=True)
st.subheader("Consumption Trends Over Time")

# Create trend plot
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#161b22')
ax.set_facecolor('#1f2937')

df_grouped = df.groupby('year')[['coal_cons_per_capita', 'nuclear_energy_per_capita', 'oil_energy_per_capita']].mean()
sns.lineplot(data=df_grouped, ax=ax)
ax.grid(True, alpha=0.2)
ax.set_title('Non-Renewable Energy Consumption Trends', color='#c9d1d9')
ax.set_xlabel('Year', color='#c9d1d9')
ax.set_ylabel('Per Capita Consumption', color='#c9d1d9')
plt.legend(labels=['Coal', 'Nuclear', 'Oil'], facecolor='#161b22', labelcolor='#c9d1d9')

st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)