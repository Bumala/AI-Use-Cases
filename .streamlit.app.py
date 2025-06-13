import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
from streamlit_javascript import st_javascript

# --- Install streamlit-javascript via pip:
# pip install streamlit-javascript

# Page setup
st.set_page_config(layout="wide")
if "selected" not in st.session_state:
    st.session_state.selected = set()

# Listen for JS messages via URL params (populated via st_javascript)
js_code = """
window.addEventListener("message", (event) => {
    const m = event.data;
    if (m?.isStreamlitMessage && m.type === "cellClick") {
        const p = JSON.stringify(m.data);
        const url = new URL(window.location.href);
        url.searchParams.set("cellClickData", p);
        window.location.href = url;
    }
});
"""
st_javascript(js_code=js_code)

# Process any click event
params = st.experimental_get_query_params()
if "cellClickData" in params:
    import json
    data = json.loads(params["cellClickData"][0])
    attr, sel = data["attribute"], data["selected"]
    if sel:
        st.session_state.selected.add(attr)
    else:
        st.session_state.selected.discard(attr)
    st.experimental_set_query_params()
    st.experimental_rerun()

# Core table HTML/JS (same as your version)
def generate_html_table(data, selected):
    first_col_width = 160
    second_col_width = 200
    base_cell_width = 150
    cell_height = 50

    def style(width, bold=False, border_bottom=False):
        bold_style = "font-weight: bold;" if bold else ""
        border_bottom_style = "border-bottom: 3px solid #000000;" if border_bottom else ""
        return f"text-align: center; vertical-align: middle; padding: 10px; border: 1px solid #000000; width: {width}px; height: {cell_height}px; {bold_style} {border_bottom_style}"

    # Define colspan rules
    colspan_2 = {
        (1, 2), (1, 3), (1, 4),
        (2, 2), (2, 5),
        (3, 2), (3, 3), (3, 4), 
        (5, 2), (5, 3), (5, 4),
        (7, 2), (7, 5),
        (8, 4),
        (10, 2), (10, 3), (10, 4),
        (11, 2), (11, 5), 
    }

    colspan_3 = {
        (4, 2), (4, 3)
    }

    html = "<table style='border-spacing: 0; width: 100%; border-collapse: collapse; table-layout: fixed; border: 3px solid #000000;'>"

    for i, row in enumerate(data):
        html += "<tr>"
        for j, val in enumerate(row):
            if val is None:
                continue

            # Determine if this is an attribute cell that can be selected
            is_attribute = (i > 0 and j >= 2) 
            click_attr = f"onclick='handleCellClick(this)' data-attr='{val}'" if is_attribute else ""
            cell_class = " class='selected'" if val in st.session_state.selected and is_attribute else ""
            
            # Base cell style
            bg_color = "#92D050" if val in st.session_state.selected and is_attribute else "#f1fbfe"
            if j == 0:
                bg_color = "#61cbf3"
            elif j == 1:
                bg_color = "#94dcf8"

            # Header row
            if i == 0:
                if j == 0:
                    html += f"<td style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"
                elif j == 1:
                    html += f"<td style='{style(second_col_width, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"
                elif j == 2:
                    html += f"<td colspan='6' style='{style(base_cell_width * 6, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"
            
            # First column cells with rowspan
            elif j == 0:
                if i == 1:
                    html += f"<td rowspan='4' style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #61cbf3;'>{val}</td>"
                elif i == 5:
                    html += f"<td rowspan='5' style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #61cbf3;'>{val}</td>"
                elif i == 10:
                    html += f"<td rowspan='2' style='{style(first_col_width, bold=True)} background-color: #61cbf3;'>{val}</td>"
            
            # Special formatting for certain cells
            elif (i == 4 and j == 1) or (i == 9 and j == 1):
                html += f"<td {click_attr}{cell_class} style='{style(base_cell_width, bold=True, border_bottom=True)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
            elif i == 9 and j in {2, 4, 6}:
                html += f"<td {click_attr}{cell_class} style='{style(base_cell_width)} background-color: {bg_color}; border-bottom: 3px solid #000000; cursor: pointer;'>{val}</td>"
            elif i > 0 and j == 1:
                html += f"<td style='{style(second_col_width, bold=True)} background-color: #94dcf8;'>{val}</td>"
            
            # Cells with colspan
            elif (i, j) in colspan_3:
                html += f"<td {click_attr}{cell_class} colspan='3' style='{style(base_cell_width * 3)} background-color: {bg_color}; border-bottom: 3px solid #000000; cursor: pointer;'>{val}</td>"
            elif (i, j) in colspan_2:
                html += f"<td {click_attr}{cell_class} colspan='2' style='{style(base_cell_width * 2)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
            else:
                html += f"<td {click_attr}{cell_class} style='{style(base_cell_width)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
        html += "</tr>"

    html += "</table>"
  

    return html_table

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

  # same data structure as you provided ... ]
table_html = generate_html_table(data, st.session_state.selected)

# Wrap with interactive JS
full_html = f"""
<script>
{js_code}
function handleCellClick(el) {{
    const attr = el.getAttribute('data-attr');
    const sel = el.classList.toggle('selected');
    el.style.backgroundColor = sel ? '#92D050' : el.dataset.originalColor;
    window.parent.postMessage({{
        isStreamlitMessage: true,
        type: 'cellClick',
        data: {{attribute: attr, selected: sel}}
    }}, '*');
}}
</script>

<div style="padding:10px; background:#f1fbfe; text-align:center;">
  <button id="reset">Reset Selection</button>
</div>
<div style="margin-bottom:10px; padding:10px; background:#dceefc; border:2px solid #61cbf3;">
  Selected: <span id="sel">None</span>
</div>

<div style="overflow-x:auto; width:100%; padding:10px;">
  {table_html}
</div>

<script>
const cells = document.querySelectorAll('td[data-attr]');
cells.forEach(c => c.dataset.originalColor = getComputedStyle(c).backgroundColor);
cells.forEach(c => c.onclick = () => handleCellClick(c));
document.getElementById('reset').onclick = () => {{
  window.location.search = '';  // clears all selections
}};
</script>
"""

html(full_html, height=1200)

# --- Data & use-case logic
analysis_df = pd.DataFrame({ ... your analysis_df data ... })
use_case_descriptions = {   
        "AI-infused experiments in R&D": "This use case focuses on integrating AI into experimental R&D processes to accelerate discovery and optimize results.",
        "AI-powered manufacturing planning in smart factories": "This use case enables intelligent scheduling, resource allocation, and process optimization using AI in smart factories.",
        "AI-driven Human-Machine Collaboration in ideation": "This use case explores collaboration between AI tools and human designers during early-stage ideation.",
        "Predictive Maintenance using AI sensors": "Leverages AI and sensor data to predict and prevent equipment failures before they happen.",
        "AI for Customer Behavior Analysis": "Analyzes large sets of customer interaction data to find actionable insights.",
        "AI-assisted Prototyping": "Automates parts of the prototyping process using generative AI models.",
        "Natural Language Processing in Customer Feedback": "Uses NLP to analyze unstructured feedback and identify key themes.",
        "AI for Market Trend Forecasting": "Predicts future market directions using large-scale data and AI models.",
        "Generative Design for Engineering": "Uses AI to generate thousands of design options based on constraints.",
        "AI-enhanced Risk Management": "Automates risk detection and mitigation strategies using predictive analytics.",
        "AI for Supply Chain Optimization": "Improves logistics and supply chain operations through intelligent forecasting.",
        "AI in Quality Control": "Detects defects in real-time through computer vision systems.",
        "Conversational AI for Support": "Implements AI chatbots to assist customers and employees efficiently.",
        "AI-powered Personalization Engines": "Delivers hyper-personalized product recommendations using AI.",
        "AI in Product Lifecycle Management": "Optimizes every stage of a product’s life using AI analytics.",
        "AI for Competitive Intelligence": "Monitors competitor behavior and market shifts automatically.",
        "AI-based Design Validation": "Simulates and tests design concepts using machine learning.",
        "AI in Inventory Management": "Reduces overstock and stockouts with smarter predictions.",
        "Smart Energy Management with AI": "Optimizes factory energy use based on AI models.",
        "AI-driven Regulatory Compliance": "Helps ensure products meet legal and safety standards via automation.",
        "AI in User Behavior Modeling": "Understands how users interact with products using behavioral models.",
        "Voice-Activated Interfaces": "Enables control of systems using natural language commands.",
        "AI-assisted UX Design": "Provides data-driven recommendations to improve user experience.",
        "AI in Product Customization": "Automatically configures products to customer preferences.",
        "AI-driven Feature Prioritization": "Ranks feature development priorities based on predicted impact.",
        "Digital Twin with AI": "Creates a real-time digital replica of a product or system.",
        "AI-powered Testing Automation": "Speeds up QA by automatically generating and executing test cases.",
        "Autonomous Product Testing": "AI runs independent tests without human involvement.",
        "AI in Materials Discovery": "Uses AI to find and evaluate new materials faster.",
        "AI-enhanced Collaboration Platforms": "Improves team creativity and efficiency through smart assistance." }

sel = list(st.session_state.selected)
if sel:
    summed = analysis_df.set_index("Use Case")[sel].sum(axis=1)
    top = summed.idxmax()
    desc = use_case_descriptions.get(top, "")
    st.markdown(f"""
      <div style="margin-top:1em;">
        <label style="font-weight:700;">Most relevant AI Use Case</label><br>
        <div style="background:#A8E060; padding:10px; border-radius:8px;">
          <b>{top}</b><br>{desc}
        </div>
      </div>
    """, unsafe_allow_html=True)
else:
    st.info("Please select the attributes above…")
