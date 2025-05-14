import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

# Set Streamlit page layout
st.set_page_config(layout="wide")

# ---------- Data for the HTML table ----------

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

# analysis_table_data as before...
# [TRUNCATED FOR BREVITY: include the full analysis_table_data and DataFrame creation here]

# ---------- Prepare session state ----------
if 'selected' not in st.session_state:
    st.session_state.selected = set()

# ---------- Handle messages from the HTML component ----------

def handle_component_message(msg):
    t = msg.get('type')
    data = msg.get('data', {})
    if t == 'cellClick':
        attr = data.get('attribute')
        if data.get('selected'):
            st.session_state.selected.add(attr)
        else:
            st.session_state.selected.discard(attr)
    elif t == 'resetSelection':
        st.session_state.selected.clear()

# ---------- Calculate and show top use case ----------
if st.session_state.selected:
    summed = analysis_table[list(st.session_state.selected)].sum(axis=1)
    top_use_case = summed.idxmax()
    st.success(f"🚀 **Top Use Case:** {top_use_case}")
else:
    st.info("👆 Click table cells above to select attributes and see the top use case.")

# HTML generator (same as before)...
# generate_html_table(data, st.session_state.selected)
# selected_bar_html, interaction_js, update script, styles...

# ---------- Render component and capture messages ----------
component_value = html(html_code, height=1200)
if component_value:
    handle_component_message(component_value)
    st.experimental_rerun()
