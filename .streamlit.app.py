import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Data definition
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator", "Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"],
    [None, "Innovation Type", "Incremental", "Radical", "Sustaining", "Disruptive"],
    [None, "Aim", "Product Innovation", "Process Innovation", "Business Model Innovation"],
    [None, "Ambidexterity", "Exploration", "Exploitation"],
    ["Technology (How)", "AI Role", "Automaton", "Assistant", "Partner"],
    [None, "AI Concepts", "Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
    [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
    [None, "Analytics Problem", "Description/Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Place (Where)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

# Create a DataFrame
df = pd.DataFrame(data)

# Build AgGrid options
options_builder = GridOptionsBuilder.from_dataframe(df)
options_builder.configure_column("0", pinned="left")  # Pin the first column for better navigation
options_builder.configure_default_column(resizable=True, wrapText=True, autoHeight=True)

grid_options = options_builder.build()

# Display the table using AgGrid
st.write("### Dynamic Table with Streamlit AgGrid")
AgGrid(
    df,
    gridOptions=grid_options,
    height=500,
    fit_columns_on_grid_load=True,
    enable_enterprise_modules=False,
)
