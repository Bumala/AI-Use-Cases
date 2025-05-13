import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
import json

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

df = pd.DataFrame(data)

# ---------- Load analysis table ----------

analysis_table_data = {
   "Use Case": [
       "AI-infused experiments in R&D",
       "AI-powered manufacturing planning in smart factories",
       # ... (rest of your use cases) ...
       "AI-driven vehicles sales prediction"
   ],
   "Quality/Scope/Knowledge": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
   # ... (rest of your attribute columns) ...
   "Customer Service": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2]
}

analysis_table = pd.DataFrame(analysis_table_data)
analysis_table.set_index("Use Case", inplace=True)

# ======= SESSION STATE =======
if "selected_attrs" not in st.session_state:
    st.session_state.selected_attrs = []
if "current_selection" not in st.session_state:
    st.session_state.current_selection = "None"

# ======= TABLE GENERATION =======
def generate_html_table(data):
    # ... (same table generation code as before, but simplified) ...
    return html_table

# ======= TOP USE CASE CALCULATION =======
def calculate_top_use_case(selected_attrs):
    if not selected_attrs or selected_attrs == ["None"]:
        return None
    
    valid_attrs = [attr for attr in selected_attrs if attr in analysis_table.columns]
    
    if not valid_attrs:
        return None
    
    try:
        summed = analysis_table[valid_attrs].sum(axis=1)
        return summed.idxmax()
    except Exception as e:
        st.error(f"Error calculating top use case: {str(e)}")
        return None

# ======= MAIN APP =======
# Display the top use case
top_use_case = calculate_top_use_case(st.session_state.selected_attrs)
if top_use_case:
    st.success(f"🚀 **Top Use Case:** {top_use_case}")
else:
    st.info("👆 Click on attributes in the table to see the top use case")

# JavaScript to extract selected items from the bar
js_code = f"""
<script>
// Track selected items
let selectedItems = {json.dumps(st.session_state.selected_attrs)};

function updateSelectedBar() {{
    const bar = document.getElementById("selectedItems");
    if (selectedItems.length === 0 || (selectedItems.length === 1 && selectedItems[0] === "None")) {{
        bar.innerText = "None";
    }} else {{
        bar.innerText = selectedItems.join(", ");
    }}
    
    // Send current selection to Python
    window.parent.postMessage({{
        isStreamlitMessage: true,
        type: 'selectionUpdate',
        data: {{ 
            selected: selectedItems,
            selectionText: bar.innerText
        }}
    }}, '*');
}}

function handleCellClick(element) {{
    const attr = element.getAttribute('data-attr');
    const isSelected = element.style.backgroundColor === 'rgb(146, 208, 80)';

    // Toggle visual selection
    element.style.backgroundColor = isSelected ? element.dataset.originalColor : '#92D050';

    // Update selected items
    if (!isSelected) {{
        if (!selectedItems.includes(attr)) {{
            if (selectedItems[0] === "None") {{
                selectedItems = [attr];
            }} else {{
                selectedItems.push(attr);
            }}
        }}
    }} else {{
        selectedItems = selectedItems.filter(item => item !== attr);
        if (selectedItems.length === 0) {{
            selectedItems = ["None"];
        }}
    }}

    updateSelectedBar();
}}

function resetSelection() {{
    // Clear selections
    selectedItems = ["None"];
    
    // Reset all cell colors
    document.querySelectorAll('td[data-attr]').forEach(cell => {{
        cell.style.backgroundColor = cell.dataset.originalColor;
    }});
    
    updateSelectedBar();
}}

document.addEventListener("DOMContentLoaded", function() {{
    // Store original background color of each cell
    document.querySelectorAll('td').forEach(cell => {{
        const original = getComputedStyle(cell).backgroundColor;
        cell.dataset.originalColor = original;
    }});

    // Initialize selected items
    updateSelectedBar();
    
    // Highlight initially selected cells
    document.querySelectorAll('td[data-attr]').forEach(cell => {{
        const attr = cell.getAttribute('data-attr');
        if (selectedItems.includes(attr)) {{
            cell.style.backgroundColor = '#92D050';
        }}
    }});

    // Set up reset button
    document.getElementById('resetButton').addEventListener('click', resetSelection);
}});

// Listen for messages from Streamlit
window.addEventListener('message', function(event) {{
    const data = event.data;
    if (data.isStreamlitMessage && data.type === 'initialSelection') {{
        selectedItems = data.data.selected || ["None"];
        updateSelectedBar();
    }}
}});
</script>
"""

# HTML layout
html_layout = f"""
<div id="resetButtonContainer" style="padding: 10px; background-color: #f1fbfe; text-align: center;">
    <button id="resetButton" style="padding: 10px 20px; background-color: #61cbf3; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">
        Reset Selection
    </button>
</div>
<div id="selectedBar" style="margin-bottom: 10px; padding: 10px; background-color: #dceefc; border: 2px solid #61cbf3; border-radius: 8px; font-weight: bold;">
    Selected Attributes: <span id="selectedItems">{', '.join(st.session_state.selected_attrs) if st.session_state.selected_attrs else 'None'}</span>
</div>
<div style="overflow-x: auto; width: 100%; padding: 10px; box-sizing: border-box;">
    <div class="zoomed-table">
        {generate_html_table(data)}
    </div>
</div>
{js_code}
<style>
.zoomed-table {{
    transform: scale(0.75);
    transform-origin: top center;
    width: 100%;
}}
</style>
"""

# Handle messages from JavaScript
if st.session_state.get('selection_update'):
    new_selection = st.session_state.selection_update.get('selected', [])
    st.session_state.selected_attrs = new_selection if new_selection != ["None"] else []
    st.session_state.current_selection = st.session_state.selection_update.get('selectionText', 'None')
    st.experimental_rerun()

# Display the component
html(html_layout, height=1200)

# Initialize component with current selection
html(f"""
<script>
window.parent.postMessage({{
    isStreamlitMessage: true,
    type: 'initialSelection',
    data: {{ 
        selected: {json.dumps(st.session_state.selected_attrs)},
        selectionText: "{', '.join(st.session_state.selected_attrs) if st.session_state.selected_attrs else 'None'}"
    }}
}}, '*');
</script>
""")
