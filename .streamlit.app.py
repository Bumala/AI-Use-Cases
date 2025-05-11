import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

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

# ======= SESSION STATE =======
if "selected" not in st.session_state:
    st.session_state.selected = set()

# ======= JAVASCRIPT FOR INTERACTIVITY =======
interaction_js = """
<script>
function handleCellClick(element) {
    const attr = element.getAttribute('data-attr');
    const isSelected = element.style.backgroundColor === 'rgb(146, 208, 80)';
    
    // Toggle visual selection immediately
    element.style.backgroundColor = isSelected ? '#f1fbfe' : '#92D050';
    
    // Send message to Streamlit
    window.parent.postMessage({
        isStreamlitMessage: true,
        type: 'cellClick',
        data: {
            attribute: attr,
            selected: !isSelected
        }
    }, '*');
}
</script>
"""

# ======= HANDLE CELL CLICKS =======
def handle_cell_click():
    if st.session_state.get('cell_click'):
        attr = st.session_state.cell_click['attribute']
        if st.session_state.cell_click['selected']:
            st.session_state.selected.add(attr)
        else:
            st.session_state.selected.discard(attr)
        st.experimental_rerun()

# Initialize and handle clicks
st.session_state.cell_click = None
handle_cell_click()

# ======= PERFECT TABLE LAYOUT GENERATION =======
def generate_html_table(data, selected):
    first_col_width = 160
    second_col_width = 200
    base_cell_width = 150
    cell_height = 50

    def style(width, bold=False, border_bottom=False):
        bold_style = "font-weight: bold;" if bold else ""
        border_bottom_style = "border-bottom: 3px solid #000000;" if border_bottom else ""
        return f"text-align: center; vertical-align: middle; padding: 10px; border: 1px solid #000000; width: {width}px; height: {cell_height}px; {bold_style} {border_bottom_style}"

    html = "<table style='border-spacing: 0; width: 100%; border-collapse: collapse; table-layout: fixed; border: 3px solid #000000;'>"

    for i, row in enumerate(data):
        html += "<tr>"
        for j, val in enumerate(row):
            if val is None:
                continue

            # Determine if this is an attribute cell that can be selected
            is_attribute = (i > 0 and j >= 2) 
            click_attr = f"onclick='handleCellClick(this)' data-attr='{val}'" if is_attribute else ""
            cell_class = " class='selected'" if val in selected and is_attribute else ""
            
            # Base cell style
            bg_color = "#92D050" if val in selected and is_attribute else "#f1fbfe"
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
            else:
                html += f"<td {click_attr}{cell_class} style='{style(base_cell_width)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
        html += "</tr>"

    html += "</table>"
    return html

# ======= DISPLAY THE TABLE =======
zoomed_html = f"""
<div style="display: flex; justify-content: center; align-items: center; height: 100%; transform: scale(0.8); transform-origin: top;">
    {generate_html_table(data, st.session_state.selected)}
</div>
{interaction_js}
"""

html(zoomed_html, height=800)

# ======= USE CASE ANALYSIS =======
analysis_table_data = {
    "Use Case": [
        "AI-infused experiments in R&D",
        "AI-powered manufacturing planning in smart factories",
        "AI-driven Human-Machine Collaboration in ideation",
        # Add more rows as needed
    ],
    "Attribute 1": [2, 3, 5],
    "Attribute 2": [1, 4, 2],
    # Add more columns as needed
}
analysis_table = pd.DataFrame(analysis_table_data)
analysis_table.set_index("Use Case", inplace=True)

attribute_columns = list(analysis_table.columns)
selected_attributes = st.multiselect(
    "Select attributes (these match the table cells you want to 'click'):",
    attribute_columns,
    default=list(st.session_state.selected)  # Sync with selected cells
)

if selected_attributes:
    summed = analysis_table[selected_attributes].sum(axis=1)
    top_use_case = summed.idxmax()
    st.success(f"🚀 **Top Use Case:** {top_use_case}")
else:
    st.info("👆 Select attributes above to see the top use case.")
