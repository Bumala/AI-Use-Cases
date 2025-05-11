import streamlit as st

# Grid labels
rows = ["Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"]
columns = ["Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"]

st.write("## Select Relevant Attributes")

# Create selection matrix
selected = {}
for i, row in enumerate(rows):
    cols = st.columns(len(columns))
    for j, col in enumerate(cols):
        key = f"{i}-{j}"
        selected[key] = col.checkbox(f"", key=key)

# Show results
st.write("### Selected Cells:")
for key, value in selected.items():
    if value:
        i, j = map(int, key.split('-'))
        st.write(f"Row: {rows[i]}, Column: {columns[j]}")
