import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
import json
import plotly.graph_objects as go
import streamlit.components.v1 as components

# ... [everything above remains unchanged, including Streamlit layout, funnel, and use_case_descriptions, etc.] ...

#-------------------------------------------------------------------------------------------- Table for category, dimension and attributes -------------------------------------------------------------
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

# ... [unchanged: analysis_table_data, use_case_to_cluster, cluster_details, etc.] ...

analysis_table = pd.DataFrame(analysis_table_data)
analysis_table.set_index("Use Case", inplace=True)

# ------------------------------------------------------------------------------------------------------- Session state --------------------------------------------------------------------------------

# --- Only table cell selection: no dropdown ---
if "selected" not in st.session_state:
    st.session_state.selected = set()

if "js_message" not in st.session_state:
    st.session_state.js_message = None

# Handle incoming JavaScript messages (attribute selection from HTML table)
def handle_js_messages():
    if st.session_state.js_message:
        message = st.session_state.js_message
        if message['type'] == 'updateSelections':
            new_selections = set(message['data'])
            if new_selections != st.session_state.selected:
                st.session_state.selected = new_selections

handle_js_messages()

selected_attributes = list(st.session_state.selected)

#--------------------------------------------------------------------------------------------------------- Table layout --------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------------- Python, Javascript, Streamlit Communication -----------------------------------------------------------

#------------------ Javascript for interactivity ----------------------------------
interaction_js = f"""
<script>
// Track selected items globally
let selectedItems = new Set({json.dumps(list(st.session_state.selected))});

function updateStreamlit() {{
    // Send selected items to Streamlit
    const selections = Array.from(selectedItems);
    const out = {{
        isStreamlitMessage: true,
        type: 'updateSelections',
        data: selections
    }};
    window.parent.postMessage(out, '*');
}}

// Click handler for attribute cells
function handleCellClick(element) {{
    const attr = element.getAttribute('data-attr');
    const isSelected = element.style.backgroundColor === 'rgb(146, 208, 80)';

    // Toggle visual selection
    element.style.backgroundColor = isSelected ? element.dataset.originalColor : '#92D050';

    if (!isSelected) {{
        selectedItems.add(attr);
    }} else {{
        selectedItems.delete(attr);
    }}

    // Update Streamlit after every selection
    updateStreamlit();
}}

document.addEventListener("DOMContentLoaded", function() {{
    // Store original background color of each cell
    const cells = document.querySelectorAll('td');
    cells.forEach(cell => {{
        const original = getComputedStyle(cell).backgroundColor;
        cell.dataset.originalColor = original;

        // Initialize selected cells
        const attr = cell.getAttribute('data-attr');
        if (attr && selectedItems.has(attr)) {{
            cell.style.backgroundColor = '#92D050';
        }}
    }});
}});
</script>
"""

#--------------------------- JavaScript to handle Streamlit communication--------
streamlit_js = """
<script>
// Function to handle messages from Streamlit
function handleStreamlitMessage(event) {
    if (event.data.isStreamlitMessage) {
        if (event.data.type === 'updateSelections') {
            window.parent.postMessage({
                isStreamlitMessage: true,
                type: 'js_message',
                data: event.data
            }, '*');
        }
    }
}
window.addEventListener('message', handleStreamlitMessage);
</script>
"""

# Generate the full HTML
html_code = f"""
<div style="overflow-x: auto; width: 100%; padding: 10px; box-sizing: border-box;">
  <div class="zoomed-table">
      {generate_html_table(data, st.session_state.selected)}
  </div>
</div>
{interaction_js}
{streamlit_js}
<style>
.zoomed-table {{
  transform: scale(0.75);
  transform-origin: top center;
  width: 100%;
}}
</style>
"""

# Display the HTML table (with embedded JS for interaction)
html(html_code, height=700)

#------------------------------------------------------------------------------------------ Top use case selection and display -------------------------------------------------------------------------

# ---------------------------- Calculate and show top use case -----------------------
if selected_attributes:
    summed = analysis_table[selected_attributes].sum(axis=1)
    top_use_case = summed.idxmax()

    # Combine the title and the paragraph with spacing
    use_case_info = f"<b>{top_use_case}</b><br>{use_case_descriptions.get(top_use_case, '')}"

    # Display top use case inside a styled box
    st.markdown(
        f"""
        <div style="margin-top: 1em;">
        <label style="font-weight: 700; color: #000;"> Most relevant AI Use Case </label><br>
        <div style="
            background-color: #A8E060;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #000;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
            color: #000;
            white-space: pre-wrap;
           "> {use_case_info}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    top_use_case = None  # Default value if no attributes are selected
    st.info("Please select attributes by clicking fields in the table above to display relevant information.")

#------------------------------------------------------------------------------------------------- Top use case graph display --------------------------------------------------------------------------

st.markdown(
   "<h3 style='font-size:18px; font-weight:700; margin-bottom:0; margin-top:2em; text-align:center;'>Significance levels of attributes for the most relevant AI use case in automotive, based on the use cases selected above</h3>",
   unsafe_allow_html=True
)

if top_use_case:
    # Get all attribute columns for the selected top use case
    attribute_columns = list(analysis_table.columns)
    all_values = analysis_table.loc[top_use_case, attribute_columns]

    fig = go.Figure(data=[
        go.Bar(
            x=attribute_columns,
            y=all_values,
            marker_color=[
                '#92D050' if v == 2 else '#FFD966' if v == 1 else '#D9D9D9'
                for v in all_values
            ],
        )
    ])

    fig.update_yaxes(
        tickvals=[0, 1, 2],
        ticktext=["Low", "Moderate", "High"],
        title_text="Significance Level",
        range=[0, 2],
        title_font=dict(family='Arial Bold', color='black'),
        tickfont=dict(color='black'),

    )
    fig.update_xaxes(
    title_text="Attributes",
    automargin=True,
    title_standoff=30,  # Lower value brings title closer to axis
    tickangle=50,
    title_font=dict(family='Arial Bold', color='black'),
    tickfont=dict(color='black'),
    )
    fig.update_layout(
    margin=dict(t=0, b=40)  # Adjust bottom margin (try 20-60)
    )
    st.plotly_chart(fig, use_container_width=True)

#-------------------------------------------------------------------------------------------------------- Cluster Analysis -----------------------------------------------------------------------------

# ... [unchanged: cluster analysis and cluster bar graph code] ...

if top_use_case:
    cluster_name = use_case_to_cluster.get(top_use_case, "Unknown Cluster")
    cluster_info = cluster_details.get(cluster_name, "Detailed information about this cluster is not available.")

    st.markdown(
        f"""
        <div style="margin-top: 1em;">
            <label style="font-weight: 700; color: #000;">Cluster details for the most relevant AI use case</label><br>
            <div style="
                width: 100%;
                background-color: #F5F5F5;
                color: #000;
                padding: 10px;
                border: 1px solid #000;
                border-radius: 8px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 14px;
            ">
                <span style="font-weight:bold;">{cluster_name}</span><br>
                <span>{cluster_info}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Please select attributes by clicking fields in the table above to display relevant information.")

if top_use_case:
    # Step 1: Find the cluster for the selected top use case
    cluster_name = use_case_to_cluster.get(top_use_case)

    if cluster_name:
        # Step 2: Get all use cases in that cluster
        cluster_use_cases = [
            use_case for use_case, cluster in use_case_to_cluster.items()
            if cluster == cluster_name
        ]

        # Step 3: Filter the analysis table to include only those use cases
        cluster_df = analysis_table.loc[
            analysis_table.index.intersection(cluster_use_cases)
        ]

        if not cluster_df.empty:
            # Step 4: Calculate average values for each attribute
            avg_values = cluster_df.mean()

            # Step 5: Create the bar chart
            fig = go.Figure(data=[
                go.Bar(
                    x=avg_values.index,
                    y=avg_values.values,
                    marker_color=[
                        '#92D050' if v >= 1.5 else '#FFD966' if v >= 0.5 else '#D9D9D9'
                        for v in avg_values.values
                    ],
                )
            ])

            # Step 6: Format the chart
            fig.update_yaxes(
                tickvals=[0, 1, 2],
                ticktext=["Low", "Moderate", "High"],
                title_text="Average Significance Level",
                range=[0, 2],
                title_font=dict(family='Arial Bold', color='black'),
                tickfont=dict(color='black'),
            )
            fig.update_xaxes(
                title_text="Attributes",
                tickangle=50,
                title_font=dict(family='Arial Bold', color='black'),
                tickfont=dict(color='black'),
                automargin=True,
                title_standoff=30
            )
            fig.update_layout(
                title=f"Average Attribute Significance for {cluster_name}",
                title_font=dict(family='Arial Bold', size=18, color='black'),
                margin=dict(t=150, b=80),
                title_x=0.2,
                height=500
            )

            # Step 7: Show chart
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data found for the cluster's use cases.")
    else:
        st.warning("Selected use case does not belong to a known cluster.")

# -------------------------------------------------------------------------------------------------- Calculate and show other relevant use case --------------------------------------------------------
if selected_attributes:
    summed = analysis_table[selected_attributes].sum(axis=1)
    top_6_use_cases = summed.nlargest(6).index[1:]  # Get indices of top 6 use cases

    # single string for all use cases, separated by <br><br>
    use_cases_info = ""
    for use_case in top_6_use_cases:
        description = use_case_descriptions.get(use_case, "")
        use_cases_info += f"<b>{use_case}</b><br>{description}<br><br>"

    # Strip the trailing <br><br> for a clean finish
    use_cases_info = use_cases_info.rstrip("<br><br>")

    st.markdown("---")
    st.markdown(
        f"""
        <div style="margin-top: 1em;">
            <label style="font-weight: 700; color: #000;"> Other relevant AI Use Cases</label><br>
            <div style="
                background-color: #f7cbb5;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #000;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 14px;
                color: #000;
                white-space: pre-wrap;
            ">{use_cases_info}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Please select attributes by clicking fields in the table above to display relevant information.")

# [End of code]
