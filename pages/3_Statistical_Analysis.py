import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page config
st.set_page_config(
    page_title="Statistical Analysis",
    page_icon="📈",
    layout="wide"
)

# Custom CSS (same as before)
st.markdown("""
<style>
    /* Add the same CSS styles as other pages */
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.title("Statistical Insights")
st.markdown("Advanced statistical analysis of energy consumption patterns")
st.markdown('</div>', unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv("World Energy Consumption.clean.csv")

df = load_data()

# Analysis Controls
st.sidebar.markdown("## Analysis Parameters")
analysis_type = st.sidebar.selectbox(
    "Select Analysis Type",
    ["Correlation Analysis", "Distribution Analysis", "Time Series Analysis"]
)

# Main content based on selection
if analysis_type == "Correlation Analysis":
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("Energy Sources Correlation Matrix")
    
    # Calculate correlation matrix
    energy_columns = [
        'biofuel_cons_per_capita', 'solar_energy_per_capita',
        'wind_energy_per_capita', 'coal_cons_per_capita',
        'nuclear_energy_per_capita', 'oil_energy_per_capita'
    ]
    
    corr_matrix = df[energy_columns].corr()
    
    # Plot correlation heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor('#161b22')
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='RdYlGn',
        center=0,
        ax=ax
    )
    plt.title('Energy Sources Correlation Matrix', color='#c9d1d9')
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

elif analysis_type == "Distribution Analysis":
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("Energy Consumption Distribution")
    
    energy_source = st.selectbox(
        "Select Energy Source",
        ['solar_energy_per_capita', 'wind_energy_per_capita', 'coal_cons_per_capita']
    )
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.patch.set_facecolor('#161b22')
    
    # Box plot
    sns.boxplot(data=df, y=energy_source, ax=ax1)
    ax1.set_facecolor('#1f2937')
    ax1.set_title('Box Plot', color='#c9d1d9')
    
    # Distribution plot
    sns.histplot(data=df, x=energy_source, ax=ax2)
    ax2.set_facecolor('#1f2937')
    ax2.set_title('Distribution', color='#c9d1d9')
    
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

else:  # Time Series Analysis
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("Time Series Decomposition")
    
    # Calculate moving averages
    energy_type = st.selectbox(
        "Select Energy Type",
        ['solar_energy_per_capita', 'wind_energy_per_capita', 'coal_cons_per_capita']
    )
    
    df_grouped = df.groupby('year')[energy_type].mean().reset_index()
    df_grouped['MA12'] = df_grouped[energy_type].rolling(window=12, center=True).mean()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#161b22')
    ax.set_facecolor('#1f2937')
    
    # Plot original and MA
    sns.lineplot(data=df_grouped, x='year', y=energy_type, label='Original', ax=ax)
    sns.lineplot(data=df_grouped, x='year', y='MA12', label='12-Year MA', ax=ax)
    
    plt.title('Time Series Analysis with Moving Average', color='#c9d1d9')
    plt.legend(facecolor='#161b22', labelcolor='#c9d1d9')
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)