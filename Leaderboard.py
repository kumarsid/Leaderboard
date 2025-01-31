import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="SWL Training Leaderboard",
    page_icon="🏆",
    layout="centered"
)

# Show balloons on load
st.balloons()

# Custom CSS with more modern styling
st.markdown("""
    <style>
        /* Main container styling */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        
        /* Header styling */
        .title {
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            text-align: center;
            color: #1f1f1f;
            margin-bottom: 1rem;
            padding: 1rem;
            background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Table styling */
        .stDataFrame {
            font-family: 'Inter', sans-serif;
            margin: 0 auto;
            width: 100% ;
            text-align: center ;
        }
        
        .stDataFrame td {
            font-size: 1.5rem ;
            padding: 20px ;
            text-align: center ;
        }
        
        .stDataFrame th {
            font-size: 1.5rem ;
            padding: 20px ;
            background-color: #f8f9fa ;
            font-weight: 600 ;
            text-align: center ;
        }

        /* Center the refresh button */
        .stButton {
            text-align: center;
        }

        /* Center the footer text */
        .footer {
            text-align: center;
            color: #666;
            padding: 20px;
            margin: 0 auto;
        }

        /* Make sure container is centered */
        [data-testid="stAppViewContainer"] > .main {
            max-width: 1000px;
            margin: 0 auto;
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">🏆 SWL Python Training Leaderboard 🏆</h1>', unsafe_allow_html=True)

# Leaderboard data
data = {
    'Rank': [2, 1, 3, 3],
    'Team': ['SWL Critical Creators', 'ByteMe', 'Ummmm', 'SNL'],
    'Points': [8, 1,000,008, 2, 2],
    'Last Updated': [datetime.now().strftime("%Y-%m-%d")] * 4
}

# Create DataFrame
df = pd.DataFrame(data)

# Add trophies based on rank
def get_trophy(rank):
    if rank == 1:
        return "🏆"
    elif rank == 2:
        return "🥈"
    elif rank == 3:
        return "🥉"
    return ""

df['Trophy'] = df['Rank'].apply(get_trophy)

# Create columns to center the dataframe
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # Main leaderboard display
    st.dataframe(
        df,
        column_config={
            "Rank": st.column_config.NumberColumn(
                "Rank",
                help="Current position on the leaderboard",
                format="%d"
            ),
            "Points": st.column_config.NumberColumn(
                "Points",
                help="Total points earned",
                format="%d ⭐"
            ),
            "Trophy": st.column_config.Column(
                "Trophy",
                help="Achievement trophy"
            ),
        },
        hide_index=True,
    )

# Footer
st.markdown("""
    <div class="footer">
        Last updated: {}
    </div>
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)
