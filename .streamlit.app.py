import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode

# Define your data (you can paste your full analysis_table_data here)
analysis_table_data = {
    "Use Case": ["AI-infused experiments in R&D", "AI-powered manufacturing planning in smart factories", "AI-driven Human-Machine Collaboration in ideation"],
    "Quality/Scope/Knowledge": [2, 2, 2],
    "Time Efficiency": [2, 2, 2],
    "Cost": [2, 2, 0]
}

df = pd.DataFrame(analysis_table_data)

# Initialize session state to store toggled cells
if 'selected_cells' not in st.session_state:
    st.session_state.selected_cells = set()

# Define custom JS for cell color toggle
cell_renderer_js = JsCode('''
    class ClickableCellRenderer {
        init(params) {
            this.params = params;
            this.eGui = document.createElement('div');
            this.eGui.innerHTML = params.value;
            this.eGui.style.backgroundColor = params.valueSelected ? '#90ee90' : '';
            this.eGui.addEventListener('click', () => {
                const event = new CustomEvent('cellClicked', { detail: { row: params.rowIndex, col: params.colDef.field } });
                window.dispatchEvent(event);
            });
        }
        getGui() {
            return this.eGui;
        }
        refresh(params) {
            this.eGui.innerHTML = params.value;
            this.eGui.style.backgroundColor = params.valueSelected ? '#90ee90' : '';
            return true;
        }
    }
''')

# Create grid options
gb = GridOptionsBuilder.from_dataframe(df)
for col in df.columns[1:]:
    gb.configure_column(col, cellRenderer=cell_renderer_js)

grid_options = gb.build()

# Display AgGrid table
grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    update_mode=GridUpdateMode.NO_UPDATE,
    allow_unsafe_jscode=True,
    height=300
)

# Handle frontend → backend events (Streamlit limitation workaround)
st.markdown("""
<script>
const streamlitEvents = () => {
    window.addEventListener('cellClicked', (e) => {
        const row = e.detail.row;
        const col = e.detail.col;
        const pyMsg = JSON.stringify({row, col});
        window.parent.postMessage({ isStreamlitMessage: true, type: 'streamlit:setComponentValue', value: pyMsg }, '*');
    });
};
if (!window.hasRunStreamlitEvents) {
    window.hasRunStreamlitEvents = true;
    streamlitEvents();
}
</script>
""", unsafe_allow_html=True)

# Read the clicked cell from frontend
clicked_cell = st.experimental_get_query_params().get('cell')
if clicked_cell:
    row, col = eval(clicked_cell[0])['row'], eval(clicked_cell[0])['col']
    cell_key = (row, col)
    if cell_key in st.session_state.selected_cells:
        st.session_state.selected_cells.remove(cell_key)
    else:
        st.session_state.selected_cells.add(cell_key)

# Calculate updated sums and display top use case
df_copy = df.copy()
for row, col in st.session_state.selected_cells:
    if col != 'Use Case':
        df_copy.at[row, col] = df_copy.at[row, col] + 1  # artificially boost selected cell

df_copy['Sum'] = df_copy[df.columns[1:]].sum(axis=1)
top_use_case = df_copy.loc[df_copy['Sum'].idxmax(), 'Use Case']

st.write(f"### 🚀 Top Use Case: {top_use_case}")

