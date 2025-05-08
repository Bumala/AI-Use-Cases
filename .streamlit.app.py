import streamlit as st
import pandas as pd

# Set page layout
st.set_page_config(layout="wide")
st.title("AI Innovation Framework Explorer")

# ---------------------------
# Data: Category-Dimension-Attributes table
# ---------------------------
data = [
    ["Category", "Dimension", "Attributes"],
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator", "Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"],
    [None, "Aim", "Product Innovation", "Process Innovation", "Business Model Innovation"],
    [None, "Ambidexterity", "Exploration", "Exploitation"],
    ["Technology (How)", "AI Role", "Automaton", "Helper", "Partner"],
    [None, "AI Concepts", "Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
    [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
    [None, "Analytics Problem", "Description/ Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Context (Where/When)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "Department", "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

df_categories = pd.DataFrame(data, columns=["Category", "Dimension", "Attributes"])

# ---------------------------
# Function: Generate styled HTML table
# ---------------------------
def generate_html_table(df):
    html = df.to_html(index=False, escape=False)
    return html

# ---------------------------
# Analysis table (use case data)
# ---------------------------
analysis_data = {
    # Keep only a few columns here to fit the example; replace with full data in your app
    "Use Case": ["AI-infused experiments in R&D", "AI-powered manufacturing planning"],
    "Quality/Scope/Knowledge": [2, 2],
    "Time Efficiency": [2, 2],
    "Cost": [2, 2],
    "Customer Segments": [0, 0],
    "Value Proposition": [2, 0],
    "Product Innovation": [2, 0],
    "Process Innovation": [1, 2],
    "Exploration": [2, 0],
    "Exploitation": [0, 2],
    "Automaton": [2, 0],
    "Helper": [1, 0],
    "Partner": [2, 2],
}

df_analysis = pd.DataFrame(analysis_data)

# ---------------------------
# Sidebar filters
# ---------------------------
st.sidebar.header("Filters")

use_cases = st.sidebar.multiselect("Select Use Cases", df_analysis["Use Case"].unique(), default=df_analysis["Use Case"].unique())
attributes = st.sidebar.multiselect("Select Attributes", df_analysis.columns[1:], default=df_analysis.columns[1:])

# Filter the DataFrame
filtered_df = df_analysis[df_analysis["Use Case"].isin(use_cases)][["Use Case"] + attributes]

# ---------------------------
# Main App Display
# ---------------------------
with st.expander("📊 Category-Dimension-Attribute Table", expanded=True):
    st.markdown(generate_html_table(df_categories), unsafe_allow_html=True)

with st.expander("🔍 Use Case Analysis Table", expanded=True):
    st.dataframe(filtered_df, use_container_width=True)

# ---------------------------
# Summary Metrics
# ---------------------------
with st.expander("📈 Summary Statistics"):
    summary = filtered_df.describe()
    st.dataframe(summary)

# ---------------------------
# Download section
# ---------------------------
st.sidebar.header("Download")
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.sidebar.download_button("Download Filtered Data as CSV", csv, "filtered_data.csv", "text/csv")

