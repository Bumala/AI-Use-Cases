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

# Extract all attributes
attributes = []
for row in data[1:]:
    attributes.extend([x for x in row[2:] if x])

# ======= SESSION STATE =======
if "selected" not in st.session_state:
    st.session_state.selected = set()

# ======= IMPROVED HTML TABLE GENERATION =======
def generate_html_table(data, selected):
    html = """
    <style>
        .ai-table {
            border-collapse: collapse;
            width: 100%;
            font-family: Arial, sans-serif;
            table-layout: fixed;
        }
        .ai-table td {
            border: 1px solid #000;
            padding: 8px;
            text-align: center;
            vertical-align: middle;
        }
        .category-header {
            background-color: #61cbf3;
            font-weight: bold;
            width: 160px;
        }
        .dimension-header {
            background-color: #94dcf8;
            font-weight: bold;
            width: 200px;
        }
        .attribute-cell {
            background-color: #f1fbfe;
            cursor: pointer;
            width: 150px;
        }
        .selected {
            background-color: #92D050 !important;
        }
        .header-row {
            background-color: #E8E8E8;
            font-weight: bold;
        }
    </style>
    <table class="ai-table">
    """
    
    # Header row
    html += """
    <tr class="header-row">
        <td>Category</td>
        <td>Dimension</td>
        <td colspan="6">Attributes</td>
    </tr>
    """
    
    # Impact (What) section
    html += """
    <tr>
        <td rowspan="4" class="category-header">Impact (What)</td>
        <td class="dimension-header">Benefits</td>
        <td class="attribute-cell" data-attr="Quality/Scope/Knowledge">Quality/Scope/Knowledge</td>
        <td class="attribute-cell" data-attr="Time Efficiency">Time Efficiency</td>
        <td class="attribute-cell" data-attr="Cost">Cost</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td class="dimension-header">Focus within Business Model Navigator</td>
        <td class="attribute-cell" data-attr="Customer Segments">Customer Segments</td>
        <td class="attribute-cell" data-attr="Value Proposition">Value Proposition</td>
        <td class="attribute-cell" data-attr="Value Chain">Value Chain</td>
        <td class="attribute-cell" data-attr="Revenue Model">Revenue Model</td>
        <td colspan="2"></td>
    </tr>
    <tr>
        <td class="dimension-header">Aim</td>
        <td class="attribute-cell" data-attr="Product Innovation">Product Innovation</td>
        <td class="attribute-cell" data-attr="Process Innovation">Process Innovation</td>
        <td class="attribute-cell" data-attr="Business Model Innovation">Business Model Innovation</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td class="dimension-header">Ambidexterity</td>
        <td class="attribute-cell" data-attr="Exploration">Exploration</td>
        <td class="attribute-cell" data-attr="Exploitation">Exploitation</td>
        <td colspan="4"></td>
    </tr>
    """
    
    # Technology (How) section
    html += """
    <tr>
        <td rowspan="5" class="category-header">Technology (How)</td>
        <td class="dimension-header">AI Role</td>
        <td class="attribute-cell" data-attr="Automaton">Automaton</td>
        <td class="attribute-cell" data-attr="Helper">Helper</td>
        <td class="attribute-cell" data-attr="Partner">Partner</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td class="dimension-header">AI Concepts</td>
        <td class="attribute-cell" data-attr="Machine Learning">Machine Learning</td>
        <td class="attribute-cell" data-attr="Deep Learning">Deep Learning</td>
        <td class="attribute-cell" data-attr="Artificial Neural Networks">Artificial Neural Networks</td>
        <td class="attribute-cell" data-attr="Natural Language Processing">Natural Language Processing</td>
        <td class="attribute-cell" data-attr="Computer Vision">Computer Vision</td>
        <td class="attribute-cell" data-attr="Robotics">Robotics</td>
    </tr>
    <tr>
        <td class="dimension-header">Analytics Focus</td>
        <td class="attribute-cell" data-attr="Descriptive">Descriptive</td>
        <td class="attribute-cell" data-attr="Diagnostic">Diagnostic</td>
        <td class="attribute-cell" data-attr="Predictive">Predictive</td>
        <td class="attribute-cell" data-attr="Prescriptive">Prescriptive</td>
        <td colspan="2"></td>
    </tr>
    <tr>
        <td class="dimension-header">Analytics Problem</td>
        <td class="attribute-cell" data-attr="Description/ Summary">Description/ Summary</td>
        <td class="attribute-cell" data-attr="Clustering">Clustering</td>
        <td class="attribute-cell" data-attr="Classification">Classification</td>
        <td class="attribute-cell" data-attr="Dependency Analysis">Dependency Analysis</td>
        <td class="attribute-cell" data-attr="Regression">Regression</td>
        <td></td>
    </tr>
    <tr>
        <td class="dimension-header">Data Type</td>
        <td class="attribute-cell" data-attr="Customer Data">Customer Data</td>
        <td class="attribute-cell" data-attr="Machine Data">Machine Data</td>
        <td class="attribute-cell" data-attr="Business Data (Internal Data)">Business Data (Internal Data)</td>
        <td class="attribute-cell" data-attr="Market Data">Market Data</td>
        <td class="attribute-cell" data-attr="Public & Regulatory Data">Public & Regulatory Data</td>
        <td class="attribute-cell" data-attr="Synthetic Data">Synthetic Data</td>
    </tr>
    """
    
    # Context (Where/When) section
    html += """
    <tr>
        <td rowspan="2" class="category-header">Context (Where/When)</td>
        <td class="dimension-header">Innovation Phase</td>
        <td class="attribute-cell" data-attr="Front End">Front End</td>
        <td class="attribute-cell" data-attr="Development">Development</td>
        <td class="attribute-cell" data-attr="Market Introduction">Market Introduction</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td class="dimension-header">Department</td>
        <td class="attribute-cell" data-attr="R&D">R&D</td>
        <td class="attribute-cell" data-attr="Manufacturing">Manufacturing</td>
        <td class="attribute-cell" data-attr="Marketing & Sales">Marketing & Sales</td>
        <td class="attribute-cell" data-attr="Customer Service">Customer Service</td>
        <td colspan="2"></td>
    </tr>
    </table>
    """
    
    # Add selected class to selected cells
    for attr in selected:
        html = html.replace(f'data-attr="{attr}"', f'data-attr="{attr}" class="selected"')
    
    return html

# ======= JAVASCRIPT FOR INTERACTIVITY =======
interaction_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const table = document.querySelector('.ai-table');
    
    table.addEventListener('click', function(e) {
        const cell = e.target.closest('[data-attr]');
        if (!cell) return;
        
        const attr = cell.getAttribute('data-attr');
        const isSelected = cell.classList.contains('selected');
        
        // Toggle selection
        if (isSelected) {
            cell.classList.remove('selected');
        } else {
            cell.classList.add('selected');
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
    });
});
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

# ======= DISPLAY THE TABLE =======
html(generate_html_table(data, st.session_state.selected) + interaction_js, height=800)

# ======= USE CASE ANALYSIS =======
# (Include your analysis_df here - same as before)
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

# Display selected attributes
if st.session_state.selected:
    st.subheader("Selected Attributes")
    cols = st.columns(4)
    for i, attr in enumerate(st.session_state.selected):
        cols[i % 4].write(f"✓ {attr}")

    # Find matching use cases
    matching_use_cases = []
    for _, row in analysis_df.iterrows():
        match = all(row.get(attr, 0) > 0 for attr in st.session_state.selected)
        if match:
            matching_use_cases.append(row["Use Case"])

    if matching_use_cases:
        st.subheader("Recommended Use Cases")
        for use_case in matching_use_cases:
            st.success(f"▪ {use_case}")
    else:
        st.warning("No use cases match all selected attributes. Try selecting fewer or different attributes.")
else:
    st.info("Click on attributes in the table to see recommended use cases")
