import streamlit as st
import pandas as pd
from streamlit_javascript import st_javascript

# Set page layout
st.set_page_config(layout="wide")

# ======= TABLE DATA =======
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

# Extract all attributes
attributes = []
for row in data[1:]:
    attributes.extend([x for x in row[2:] if x])

# ======= SESSION STATE =======
if "selected" not in st.session_state:
    st.session_state.selected = set()

# ======= HTML TABLE WITH CLICK HANDLER =======
def generate_html(data, selected):
    html = "<table style='border-collapse:collapse; width:100%;'>"
    for i, row in enumerate(data):
        html += "<tr>"
        for j, val in enumerate(row):
            if val is None:
                continue
            bg = "#92D050" if val in selected else "#f1fbfe"
            if j == 0:
                bg = "#61cbf3"
            elif j == 1:
                bg = "#94dcf8"
            attr_id = f"cell_{i}_{j}"
            click_attr = f"data-attr='{val}'" if val in attributes else ""
            html += f"<td id='{attr_id}' {click_attr} style='border:1px solid black; padding:10px; background-color:{bg}; cursor:pointer;'>{val}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# ======= RENDER HTML TABLE =======
st.markdown(generate_html(data, st.session_state.selected), unsafe_allow_html=True)

# ======= JAVASCRIPT TO CAPTURE CLICK =======
js_code = """
Array.from(document.querySelectorAll('td[data-attr]')).forEach(cell => {
    cell.addEventListener('click', event => {
        const clickedValue = cell.getAttribute('data-attr');
        window.parent.postMessage({
            isStreamlitMessage: true,
            type: 'streamlit_javascript',
            data: clickedValue
        }, '*')
    })
})
"""

# Capture the clicked value using Streamlit's custom javascript handler
clicked = st_javascript(js_code=js_code)

# Update session state based on the clicked value
if clicked:
    if clicked in st.session_state.selected:
        st.session_state.selected.remove(clicked)
    else:
        st.session_state.selected.add(clicked)
    st.experimental_rerun()

# ======= DUMMY ANALYSIS DATAFRAME =======
analysis_df = pd.DataFrame({
   





   
    "Use Case": [
        "AI-infused experiments in R&D",
        "AI-powered manufacturing planning in smart factories",
        "AI-driven Human-Machine Collaboration in ideation",
        "AI-enabled idea generation in the Metaverse",
        "AI-optimized patent analysis",
        "AI-powered forecasting of the technology life cycle of EVs (S-Curve)",
        "AI-enabled bionic digital twin production planning",
        "AI-infused Human-Robot Collaboration planning",
        "AI-powered material flow planning",
        "AI-assisted ideation",
        "AI-driven interactive collaborative innovation",
        "AI-based digital twin for lithium-ion battery development",
        "AI- and Genetic Algorithms-based vehicle design",
        "AI-augmented visual inspections",
        "AI-optimized scenario engineering",
        "AI-driven design process",
        "AI- and Bio-inspired Design",
        "AI-assisted quality control of the bumper warpage",
        "AI-enabled predictive maintenance",
        "AI-optimized braking system test",
        "AI-based identification of consumer adoption stage",
        "AI-powered marketing campaign",
        "AI-driven relationship marketing",
        "AI-assisted customer service in after-sales",
        "AI-enabled battery monitoring",
        "AI-assisted staff training",
        "AI-driven predictive quality models for customer defects",
        "AI-powered customer satisfaction analysis",
        "AI-driven competition analysis",
        "AI-driven vehicles sales prediction"
    ],
    "Quality/Scope/Knowledge": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "Time Efficiency": [2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 2, 0, 0],
    "Cost": [2, 2, 0, 0, 0, 0, 2, 1, 2, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0],
    "Customer Segments": [0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2],
    "Value Proposition": [2, 0, 0, 2, 0, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2],
    "Value Chain": [2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0],
    "Revenue Model": [0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    "Product Innovation": [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 1, 0, 0, 2, 0, 0, 2],
    "Process Innovation": [1, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2],
    "Business Model Innovation": [0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 0, 2],
    "Exploration": [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2],
    "Exploitation": [0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 0, 0, 0, 2, 2],
    "Automaton": [2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "Helper": [1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 2, 0],
    "Partner": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "Machine Learning": [2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
    "Deep Learning": [2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Artificial Neural Networks": [0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 2],
    "Natural Language Processing": [2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    "Computer Vision": [0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Robotics": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Descriptive": [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0],
    "Diagnostic": [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
    "Predictive": [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0],
    "Prescriptive": [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
    "Description/ Summary": [1, 0, 0, 0, 2, 2, 0, 0, 1, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0],
    "Clustering": [0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2],
    "Classification": [2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2],
    "Dependency Analysis": [0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 1, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2],
    "Regression": [1, 1, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "Customer Data": [2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1],
    "Machine Data": [0, 1, 2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 1],
    "Business Data (Internal Data)": [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 2, 2, 0, 0, 2, 2, 2],
    "Market Data": [2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    "Public & Regulatory Data": [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0],
    "Synthetic Data": [2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2],
    "Front End": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 2, 2],
    "Development": [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 0, 0, 1, 1, 1, 2, 2, 1, 0, 1],
    "Market Introduction": [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 1],
    "R&D": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    "Manufacturing": [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 0, 1, 0, 1, 0, 2, 2, 0, 1],
    "Marketing & Sales": [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1],
    "Customer Service": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2]











})

# Display the dataframe below the table
st.write(analysis_df)









