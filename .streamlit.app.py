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
if "positions" not in st.session_state:
    st.session_state.positions = set()

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

    html_str = "<table style='border-spacing: 0; width: 100%; border-collapse: collapse; table-layout: fixed; border: 3px solid #000000;'>"

    for i, row in enumerate(data):
        html_str += "<tr>"
        for j, val in enumerate(row):
            if val is None:
                continue

            is_attribute = (i > 0 and j >= 2)
            click_attr = f"onclick='handleCellClick(this)' data-attr='{val}' data-i='{i}' data-j='{j}'" if is_attribute else ""
            cell_class = " class='selected'" if val in st.session_state.selected and is_attribute else ""

            bg_color = "#92D050" if val in st.session_state.selected and is_attribute else "#f1fbfe"
            if j == 0:
                bg_color = "#61cbf3"
            elif j == 1:
                bg_color = "#94dcf8"

            if i == 0:
                if j == 0:
                    html_str += f"<td style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"
                elif j == 1:
                    html_str += f"<td style='{style(second_col_width, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"
                elif j == 2:
                    html_str += f"<td colspan='6' style='{style(base_cell_width * 6, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"
            elif j == 0:
                if i == 1:
                    html_str += f"<td rowspan='4' style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #61cbf3;'>{val}</td>"
                elif i == 5:
                    html_str += f"<td rowspan='5' style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #61cbf3;'>{val}</td>"
                elif i == 10:
                    html_str += f"<td rowspan='2' style='{style(first_col_width, bold=True)} background-color: #61cbf3;'>{val}</td>"
            elif (i == 4 and j == 1) or (i == 9 and j == 1):
                html_str += f"<td {click_attr}{cell_class} style='{style(base_cell_width, bold=True, border_bottom=True)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
            elif i == 9 and j in {2, 4, 6}:
                html_str += f"<td {click_attr}{cell_class} style='{style(base_cell_width)} background-color: {bg_color}; border-bottom: 3px solid #000000; cursor: pointer;'>{val}</td>"
            elif i > 0 and j == 1:
                html_str += f"<td style='{style(second_col_width, bold=True)} background-color: #94dcf8;'>{val}</td>"
            elif (i, j) in colspan_3:
                html_str += f"<td {click_attr}{cell_class} colspan='3' style='{style(base_cell_width * 3)} background-color: {bg_color}; border-bottom: 3px solid #000000; cursor: pointer;'>{val}</td>"
            elif (i, j) in colspan_2:
                html_str += f"<td {click_attr}{cell_class} colspan='2' style='{style(base_cell_width * 2)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
            else:
                html_str += f"<td {click_attr}{cell_class} style='{style(base_cell_width)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
        html_str += "</tr>"

    html_str += "</table>"
    return html_str

# ======= JAVASCRIPT FOR INTERACTIVITY =======
interaction_js = """
<script>
function handleCellClick(element) {
    const attr = element.getAttribute('data-attr');
    const i = element.getAttribute('data-i');
    const j = element.getAttribute('data-j');
    const isSelected = element.style.backgroundColor === 'rgb(146, 208, 80)';
    
    element.style.backgroundColor = isSelected ? '#f1fbfe' : '#92D050';

    window.parent.postMessage({
        isStreamlitMessage: true,
        type: 'cellClick',
        data: {
            attribute: attr,
            selected: !isSelected,
            position: `(${i},${j})`
        }
    }, '*');
}
</script>
"""

# ======= HANDLE CELL CLICKS =======
def handle_cell_click():
    if st.session_state.get('cell_click'):
        attr = st.session_state.cell_click['attribute']
        pos = st.session_state.cell_click['position']
        if st.session_state.cell_click['selected']:
            st.session_state.selected.add(attr)
            st.session_state.positions.add(pos)
        else:
            st.session_state.selected.discard(attr)
            st.session_state.positions.discard(pos)
        st.experimental_rerun()

# Show selected positions
if st.session_state.positions:
    st.markdown("### Selected Cells (i, j):")
    st.markdown(", ".join(sorted(st.session_state.positions)))

# Initialize and handle click
st.session_state.cell_click = None
handle_cell_click()

# Display table
table_html = generate_html_table(data, st.session_state.selected)
html(interaction_js + table_html, height=800)

# JS listener
html("""
<script>
window.addEventListener("message", (event) => {
    const msg = event.data;
    if (msg.type === "cellClick") {
        Streamlit.setComponentValue(msg.data);
    }
});
</script>
""", height=0)
