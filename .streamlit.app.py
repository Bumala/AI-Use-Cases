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

# ---------- Analysis Table Data ----------

analysis_table_data = {
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
 

}

analysis_table = pd.DataFrame(analysis_table_data)
analysis_table.set_index("Use Case", inplace=True)

# ======= SESSION STATE =======
if "selected_attrs" not in st.session_state:
    st.session_state.selected_attrs = set()

# ======= TOP USE CASE CALCULATION =======
def calculate_top_use_case(selected_attrs):
    if selected_attrs:
        valid_attrs = [attr for attr in selected_attrs if attr in analysis_table.columns]
        if valid_attrs:
            summed = analysis_table[valid_attrs].sum(axis=1)
            return summed.idxmax()
    return None

# ======= TABLE GENERATION =======
def generate_html_table(data, selected_attrs):
    # ... (keep your existing table generation code exactly as is)
    pass

# ======= JAVASCRIPT FOR INTERACTIVITY =======
interaction_js = f"""
<script>
// Track selected attributes
let selectedAttributes = new Set({list(st.session_state.selected_attrs)});

function handleCellClick(element) {{
    const attr = element.getAttribute('data-attr');
    
    // Toggle selection
    if (selectedAttributes.has(attr)) {{
        element.style.backgroundColor = '#f1fbfe';
        selectedAttributes.delete(attr);
    }} else {{
        element.style.backgroundColor = '#92D050';
        selectedAttributes.add(attr);
    }}
    
    // Update the display
    updateSelectedDisplay();
    
    // Immediately trigger top use case calculation
    calculateTopUseCase();
}}

function updateSelectedDisplay() {{
    const displayElement = document.getElementById('selectedItemsDisplay');
    displayElement.textContent = selectedAttributes.size > 0 ? 
        Array.from(selectedAttributes).join(', ') : 'None';
}}

function calculateTopUseCase() {{
    // Send current selections to Streamlit for calculation
    window.parent.postMessage({{
        isStreamlitMessage: true,
        type: 'calculateTopUseCase',
        data: Array.from(selectedAttributes)
    }}, '*');
}}

document.addEventListener("DOMContentLoaded", function() {{
    // Initialize selections from Python
    const initialSelections = {list(st.session_state.selected_attrs)};
    initialSelections.forEach(attr => {{
        const elements = document.querySelectorAll(`td[data-attr="${{attr}}"]`);
        elements.forEach(el => {{
            el.style.backgroundColor = '#92D050';
            selectedAttributes.add(attr);
        }});
    }});
    updateSelectedDisplay();
    
    // Reset button
    document.getElementById('resetButton').addEventListener('click', function() {{
        document.querySelectorAll('td[data-attr]').forEach(el => {{
            el.style.backgroundColor = '#f1fbfe';
        }});
        selectedAttributes.clear();
        updateSelectedDisplay();
        calculateTopUseCase();
    }});
}});
</script>
"""

# ======= HANDLE FRONTEND MESSAGES =======
def handle_frontend_message():
    if st.session_state.get('frontend_message'):
        msg = st.session_state.frontend_message
        if msg['type'] == 'calculateTopUseCase':
            st.session_state.selected_attrs = set(msg['data'])
            st.experimental_rerun()

# Initialize message handler
st.session_state.frontend_message = None
handle_frontend_message()

# Display current top use case
current_top_use_case = calculate_top_use_case(st.session_state.selected_attrs)
if current_top_use_case:
    st.success(f"🚀 **Top Use Case:** {current_top_use_case}")
else:
    st.info("👆 Select attributes in the table below to see the top use case.")

# Generate and display the table
selected_bar_html = f"""
<div id="resetButtonContainer" style="padding: 10px; background-color: #f1fbfe; text-align: center;">
  <button id="resetButton" style="padding: 10px 20px; background-color: #61cbf3; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">
      Reset Selection
  </button>
</div>
<div id="selectedBar" style="margin-bottom: 10px; padding: 10px; background-color: #dceefc; border: 2px solid #61cbf3; border-radius: 8px; font-weight: bold;">
  Selected Attributes: <span id="selectedItemsDisplay">{', '.join(st.session_state.selected_attrs) if st.session_state.selected_attrs else 'None'}</span>
</div>
"""

html_code = selected_bar_html + f"""
<div style="overflow-x: auto; width: 100%; padding: 10px; box-sizing: border-box;">
  <div class="zoomed-table">
      {generate_html_table(data, st.session_state.selected_attrs)}
  </div>
</div>
""" + interaction_js

html_code += """
<style>
.zoomed-table {
  transform: scale(0.75);
  transform-origin: top center;
  width: 100%;
}
</style>
"""

# Add message listener component
components.html("""
<script>
const sendMessage = (type, data) => {
    window.parent.postMessage({
        isStreamlitMessage: true,
        type: type,
        data: data
    }, '*');
};

window.addEventListener("message", (event) => {
    if (event.data.isStreamlitMessage) {
        Streamlit.setComponentValue(event.data);
    }
});
</script>
""", height=0)

html(html_code, height=1200)
