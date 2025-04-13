import streamlit as st
import pandas as pd

data = [
    ["Teaching Method", "Knowledge", "Factual", "Conceptual", "Procedural", "Metacognitive"],
    [None, "Cognitive processes", "Remembering", "Understanding", "Applying", "Analyzing", "Evaluating", "Creating"],
    [None, "Content presentation", "Expository", "", "", "Explorative"],
    [None, "Knowledge acquisition", "Cumulative", "", "", "Cyclic"],
    [None, "Level", "Undergraduate", "Master", "MBA", "", ""],
    ["Course setting", "Course format", "Lecture", "Tutorial", "Workshop", "Project", "Hackathon", "Innovation lab", "Innovation contest"],
    [None, "Participation as", "Individual", "", "", "Team"],
    [None, "Team composition", "Monodisciplinary", "", "", "Interdisciplinary"],
    [None, "Third party involvement", "Involved", "", "", "No involved"],
    ["Course Content", "Data value chain", "Data generation", "Data acquisition", "Data processing", "Data aggregation", "Data Analytics", "Visualization"],
    [None, "Analytics perspective", "Descriptive", "Predictive", "Prescriptive", "", ""],
    [None, "Analytics technologies", "(Big) Data analytics", "Text analytics", "Network analytics", "Streaming analytics", "Web analytics"],
    ["Innovation Approach", "Innovation method", "Grounded in innovation mgt.", "", "", "Grounded in analytics"],
    [None, "Creativity technique", "Intuitive", "Discursive", "Mixed", "", ""],
    [None, "Ideation approach", "Data first", "Business first", "", "", ""],
    [None, "Innovation level", "Conceptual", "Metadata", "Data", "", ""],
    [None, "Data origin", "Open data", "Company", "Teacher", "Self-generation", ""],
    [None, "Tools", "Given", "Self-selected", "", "", ""],
    [None, "Degree of elaboration", "Concept", "Prototype", "Full-fledged service", "", ""],
]

df = pd.DataFrame(data)

def render_morphological_box_with_columns(df):
    num_rows = len(df)
    num_cols = df.shape[1]

    # Determine relative widths based on the longest row
    max_cols = df.apply(lambda row: row.astype(bool).sum(), axis=1).max()
    col_widths = [1] * num_cols  # Default equal widths

    # Adjust widths based on the structure (very rough approximation)
    col_widths[0] = 2  # Make the category column wider
    col_widths[1] = 2  # Make the dimension column wider

    row_heights = [1] * num_rows

    # Create a container for the square aspect ratio (visual guide - might not be perfect)
    with st.container():
        st.markdown(
            f"""
            <style>
                .square-container {{
                    width: 600px; /* Adjust as needed */
                    aspect-ratio: 1 / 1;
                    border: 1px solid #ccc;
                    display: grid;
                    grid-template-columns: {' '.join([f'{w}fr' for w in col_widths])};
                    grid-template-rows: {' '.join([f'{h}fr' for h in row_heights])};
                }}
                .cell {{
                    border: 1px solid black;
                    padding: 8px;
                    text-align: center;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    word-break: break-word;
                    min-height: 40px; /* Adjust as needed */
                }}
                .row-span-5 {{ grid-row: span 5; }}
                .row-span-4 {{ grid-row: span 4; }}
                .row-span-3 {{ grid-row: span 3; }}
                .row-span-7 {{ grid-row: span 7; }}
                .col-span-5 {{ grid-column: span 5; }}
                .col-span-7 {{ grid-column: span 7; }}
                .col-span-3 {{ grid-column: span 3; }}
                .col-span-6 {{ grid-column: span 6; }}
                .col-span-2 {{ grid-column: span 2; }}
                .col-span-4 {{ grid-column: span 4; }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        html_grid = "<div class='square-container'>"
        for i in range(num_rows):
            for j in range(num_cols):
                value = df.iloc[i, j]
                if pd.notna(value) and value != "":
                    row_span_class = ""
                    col_span_class = ""

                    if i == 0 and j == 0: row_span_class = "row-span-5"
                    elif i == 5 and j == 0: row_span_class = "row-span-4"
                    elif i == 9 and j == 0: row_span_class = "row-span-3"
                    elif i == 12 and j == 0: row_span_class = "row-span-7"

                    if i == 0 and j == 1: col_span_class = "col-span-5"
                    elif i == 1 and j == 1: col_span_class = "col-span-7"
                    elif i == 2 and j == 1: col_span_class = "col-span-3"
                    elif i == 3 and j == 1: col_span_class = "col-span-3"
                    elif i == 5 and j == 1: col_span_class = "col-span-7"
                    elif i == 6 and j == 1: col_span_class = "col-span-5"
                    elif i == 7 and j == 1: col_span_class = "col-span-5"
                    elif i == 8 and j == 1: col_span_class = "col-span-5"
                    elif i == 9 and j == 1: col_span_class = "col-span-6"
                    elif i == 10 and j == 1: col_span_class = "col-span-3"
                    elif i == 11 and j == 1: col_span_class = "col-span-5"
                    elif i == 12 and j == 1: col_span_class = "col-span-5"
                    elif i == 13 and j == 1: col_span_class = "col-span-3"
                    elif i == 14 and j == 1: col_span_class = "col-span-2"
                    elif i == 15 and j == 1: col_span_class = "col-span-3"
                    elif i == 16 and j == 1: col_span_class = "col-span-4"
                    elif i == 17 and j == 1: col_span_class = "col-span-2"
                    elif i == 18 and j == 1: col_span_class = "col-span-3"

                    html_grid += f"<div class='cell {row_span_class} {col_span_class}'>{value}</div>"
        html_grid += "</div>"
        st.markdown(html_grid, unsafe_allow_html=True)

render_morphological_box_with_columns(df)
