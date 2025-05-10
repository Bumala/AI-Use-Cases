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

# Extract all attributes (all cells from 3rd column and 2nd row onwards)
attributes = []
for row in data[1:]:
    attributes.extend([x for x in row[2:] if x and x not in ["Attributes"]])

# ======= SESSION STATE =======
if "selected" not in st.session_state:
    st.session_state.selected = set()

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

    html = "<table style='border-spacing: 0; border-collapse: collapse; table-layout: fixed; border: 3px solid #000000;'>"

    for i, row in enumerate(data):
        html += "<tr>"
        for j, val in enumerate(row):
            if val is None:
                continue

            # Determine if this is an attribute cell that can be selected
            is_attribute = (i > 0 and j >= 2) and val in attributes
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
    return html

# ======= JAVASCRIPT FOR INTERACTIVITY =======
interaction_js = """
<script>
function handleCellClick(element) {
    const attr = element.getAttribute('data-attr');
    const isSelected = element.classList.contains('selected');
    
    // Toggle visual selection immediately
    if (isSelected) {
        element.classList.remove('selected');
    } else {
        element.classList.add('selected');
    }
    
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


### Continuation of the Code:

```python
# ======= HANDLE CELL CLICKS =======
def handle_cell_click():
    if "cell_click" in st.session_state and st.session_state.cell_click:
        attr = st.session_state.cell_click.get("attribute")
        selected = st.session_state.cell_click.get("selected")
        if attr:
            if selected:
                st.session_state.selected.add(attr)
            else:
                st.session_state.selected.discard(attr)
        st.session_state.cell_click = None

# Initialize and handle clicks
handle_cell_click()

# ======= USE CASE ANALYSIS DATAFRAME =======
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
    "Cost": [2, 2, 0, 0, 0, 0, 2, 1, 2, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0]
    # ... Add remaining columns here
})

# ======= DISPLAY THE TABLE =======
st.markdown("""
    <style>
        .center-table {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            margin: 0 auto;
            transform: scale(0.9);
            transform-origin: top center;
        }
        table {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="center-table">' + generate_html_table(data, st.session_state.selected) + '</div>', unsafe_allow_html=True)

# Add JavaScript for interactivity
html(interaction_js)

# ======= USE CASE RECOMMENDATION LOGIC =======
if st.session_state.selected:
    st.subheader("Selected Attributes")
    cols = st.columns(4)
    for i, attr in enumerate(st.session_state.selected):
        cols[i % 4].write(f"✓ {attr}")

    # Calculate scores for each use case (sum of selected attribute values)
    analysis_df['Score'] = 0
    for attr in st.session_state.selected:
        if attr in analysis_df.columns:
            analysis_df['Score'] += analysis_df[attr]
    
    # Filter out use cases with score 0
    filtered_df = analysis_df[analysis_df['Score'] > 0]
    
    if not filtered_df.empty:
        # Get the highest score
        highest_score = filtered_df['Score'].max()
        top_use_cases = filtered_df[filtered_df['Score'] == highest_score]

        # Randomly select one use case in case of ties
        recommended_use_case = top_use_cases.sample(1).iloc[0]

        st.subheader("Recommended Use Case")
        st.success(f"▪ {recommended_use_case['Use Case']} (Score: {recommended_use_case['Score']})")
    else:
        st.warning("No use cases match the selected attributes")
else:
    st.info("Click on attributes in the table to see recommended use cases")
