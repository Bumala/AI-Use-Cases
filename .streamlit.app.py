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
    ["Course Content", "Data value chain", "Data generation", "Data acquisition", "Data processing", "Data aggregation", "Analytics", "Visualization"],
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

def render_morphological_box_flexible(df):
    num_rows = len(df)
    num_cols = df.shape[1]

    with st.container():
        st.markdown(
            f"""
            <style>
                .morph-box {{
                    display: grid;
                    grid-template-columns: repeat({num_cols}, auto); /* Columns auto-sized */
                    grid-template-rows: repeat({num_rows}, auto);
                    gap: 5px;
                    border: 1px solid #000;
                    width: 900px; /* Adjust as needed */
                }}
                .cell {{
                    border: 1px solid black;
                    padding: 8px;
                    text-align: center;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    word-break: break-word;
                    min-width: 80px; /* Minimum width for most cells */
                }}

                /* Category Spans */
                .tm {{ grid-row: 1 / span 5; grid-column: 1; }}
                .cs {{ grid-row: 6 / span 4; grid-column: 1; }}
                .cc {{ grid-row: 10 / span 3; grid-column: 1; }}
                .ia {{ grid-row: 13 / span 7; grid-column: 1; }}

                /* Dimension Positioning and Widths */
                .dim-k {{ grid-column: 2; grid-row: 1; grid-column-span: 5; min-width: 120px; }}
                .dim-cp {{ grid-column: 2; grid-row: 2; grid-column-span: 7; min-width: 120px; }}
                .dim-cpres {{ grid-column: 2; grid-row: 3; grid-column-span: 3; min-width: 100px; }}
                .dim-ka {{ grid-column: 2; grid-row: 4; grid-column-span: 3; min-width: 100px; }}
                .dim-l {{ grid-column: 2; grid-row: 5; grid-column-span: 3; min-width: 100px; }}
                .dim-cf {{ grid-column: 2; grid-row: 6; grid-column-span: 7; min-width: 120px; }}
                .dim-pa {{ grid-column: 2; grid-row: 7; grid-column-span: 5; min-width: 120px; }}
                .dim-tc {{ grid-column: 2; grid-row: 8; grid-column-span: 5; min-width: 120px; }}
                .dim-tpi {{ grid-column: 2; grid-row: 9; grid-column-span: 5; min-width: 120px; }}
                .dim-dvc {{ grid-column: 2; grid-row: 10; grid-column-span: 6; min-width: 120px; }}
                .dim-ap {{ grid-column: 2; grid-row: 11; grid-column-span: 3; min-width: 100px; }}
                .dim-at {{ grid-column: 2; grid-row: 12; grid-column-span: 5; min-width: 120px; }}
                .dim-im {{ grid-column: 2; grid-row: 13; grid-column-span: 5; min-width: 120px; }}
                .dim-ct {{ grid-column: 2; grid-row: 14; grid-column-span: 3; min-width: 100px; }}
                .dim-iapp {{ grid-column: 2; grid-row: 15; grid-column-span: 2; min-width: 90px; }}
                .dim-il {{ grid-column: 2; grid-row: 16; grid-column-span: 3; min-width: 100px; }}
                .dim-do {{ grid-column: 2; grid-row: 17; grid-column-span: 4; min-width: 110px; }}
                .dim-to {{ grid-column: 2; grid-row: 18; grid-column-span: 2; min-width: 90px; }}
                .dim-doe {{ grid-column: 2; grid-row: 19; grid-column-span: 3; min-width: 100px; }}

            </style>
            """,
            unsafe_allow_html=True,
        )

        html_grid = "<div class='morph-box'>"
        for i in range(num_rows):
            for j in range(num_cols):
                value = df.iloc[i, j]
                if pd.notna(value) and value != "":
                    cell_class = "cell"
                    position_class = ""

                    # Category Cells
                    if i == 0 and j == 0: position_class = "tm"
                    elif i == 5 and j == 0: position_class = "cs"
                    elif i == 9 and j == 0: position_class = "cc"
                    elif i == 12 and j == 0: position_class = "ia"

                    # Dimension Cells
                    elif i == 0 and j == 1: position_class = "dim-k"
                    elif i == 1 and j == 1: position_class = "dim-cp"
                    elif i == 2 and j == 1: position_class = "dim-cpres"
                    elif i == 3 and j == 1: position_class = "dim-ka"
                    elif i == 4 and j == 1: position_class = "dim-l"
                    elif i == 5 and j == 1: position_class = "dim-cf"
                    elif i == 6 and j == 1: position_class = "dim-pa"
                    elif i == 7 and j == 1: position_class = "dim-tc"
                    elif i == 8 and j == 1: position_class = "dim-tpi"
                    elif i == 9 and j == 1: position_class = "dim-dvc"
                    elif i == 10 and j == 1: position_class = "dim-ap"
                    elif i == 11 and j == 1: position_class = "dim-at"
                    elif i == 12 and j == 1: position_class = "dim-im"
                    elif i == 13 and j == 1: position_class = "dim-ct"
                    elif i == 14 and j == 1: position_class = "dim-iapp"
                    elif i == 15 and j == 1: position_class = "dim-il"
                    elif i == 16 and j == 1: position_class = "dim-do"
                    elif i == 17 and j == 1: position_class = "dim-to"
                    elif i == 18 and j == 1: position_class = "dim-doe"

                    html_grid += f"<div class='{cell_class} {position_class}'>{value}</div>"
        html_grid += "</div>"
        st.markdown(html_grid, unsafe_allow_html=True)

render_morphological_box_flexible(df)
