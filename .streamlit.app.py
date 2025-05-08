import streamlit as st
import pandas as pd

# Set page layout
st.set_page_config(layout="wide")
st.title("AI Innovation Framework Explorer")

# ---------------------------
# Data: Category-Dimension-Attributes table
# ---------------------------
data = [
    ["Impact (What)", "Benefits", ["Quality/Scope/Knowledge", "Time Efficiency", "Cost"]],
    ["Impact (What)", "Focus within Business Model Navigator", ["Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"]],
    ["Impact (What)", "Aim", ["Product Innovation", "Process Innovation", "Business Model Innovation"]],
    ["Impact (What)", "Ambidexterity", ["Exploration", "Exploitation"]],
    ["Technology (How)", "AI Role", ["Automaton", "Helper", "Partner"]],
    ["Technology (How)", "AI Concepts", ["Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"]],
    ["Technology (How)", "Analytics Focus", ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"]],
    ["Technology (How)", "Analytics Problem", ["Description/ Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"]],
    ["Technology (How)", "Data Type", ["Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"]],
    ["Context (Where/When)", "Innovation Phase", ["Front End", "Development", "Market Introduction"]],
    ["Context (Where/When)", "Department", ["R&D", "Manufacturing", "Marketing & Sales", "Customer Service"]],
]

# ---------------------------
# Function: Generate HTML table with colspan
# ---------------------------
def generate_html_table(data):
    html = "<table border='1' style='border-collapse: collapse; width: 100%; text-align: center;'>"
    html += "<thead><tr><th>Category</th><th>Dimension</th><th>Attribute</th></tr></thead><tbody>"

    current_category = ""
    current_dimension = ""

    for row in data:
        category, dimension, attributes = row
        for i, attribute in enumerate(attributes):
            html += "<tr>"
            # Category cell with rowspan
            if category != current_category:
                cat_rowspan = sum(1 for r in data if r[0] == category for _ in r[2])
                html += f"<td rowspan='{cat_rowspan}' style='background-color: #f0f0f0; font-weight: bold;'>{category}</td>"
                current_category = category
            # Dimension cell with rowspan
            if dimension != current_dimension:
                dim_rowspan = len(attributes)
                html += f"<td rowspan='{dim_rowspan}' style='background-color: #f9f9f9;'>{dimension}</td>"
                current_dimension = dimension
            # Attribute cell
            html += f"<td>{attribute}</td>"
            html += "</tr>"

    html += "</tbody></table>"
    return html

# ---------------------------
# Analysis table (use case data)
# ---------------------------
analysis_data = {
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
    st.markdown(generate_html_table(data), unsafe_allow_html=True)

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
