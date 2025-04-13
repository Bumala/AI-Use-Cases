import streamlit as st
import pandas as pd

data = [
    ["Teaching Method", "Knowledge", "Factual", "Conceptual", "Procedural", "Metacognitive"],
    [None, "Cognitive processes", "Remembering", "Understanding", "Applying", "Analyzing", "Evaluating", "Creating"],
    [None, "Content presentation", "Expository", "", "", "Explorative"],
    [None, "Knowledge acquisition", "Cumulative", "", "", "Cyclic"],
    [None, "Level", "Undergraduate", "Master", "MBA", "", ""],
  
]

df = pd.DataFrame(data)

def render_morphological_box_with_refined_grid(df):
    num_rows = len(df)
    num_cols = df.shape[1]

    col_widths = [1, 1.5, 1, 1, 1, 1, 1, 1, 1]
    row_heights = [1] * num_rows

    with st.container():
        st.markdown(
            f"""
            <style>
                .square-container {{
                    width: 800px;
                    aspect-ratio: 1 / 1;
                    border: 1px solid #ccc;
                    display: grid;
                    grid-template-columns: {' '.join([f'{w}fr' for w in col_widths[:df.shape[1]]])};
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
                    min-height: 30px;
                }}
                .r-span-tm {{ grid-row: span 5; }}
                .r-span-cs {{ grid-row: span 4; }}
                .r-span-cc {{ grid-row: span 3; }}
                .r-span-ia {{ grid-row: span 7; }}

                .c-span-k {{ grid-column: 2 / span 5; }} /* Start at the second column */
                .c-span-cp {{ grid-column: 2 / span 7; }}
                .c-span-cpres {{ grid-column: 2 / span 3; }}
                .c-span-caq {{ grid-column: 2 / span 3; }}
                .c-span-cf {{ grid-column: 2 / span 7; }}
                .c-span-pa {{ grid-column: 2 / span 5; }}
                .c-span-tc {{ grid-column: 2 / span 5; }}
                .c-span-tpi {{ grid-column: 2 / span 5; }}
                .c-span-dvc {{ grid-column: 2 / span 6; }}
                .c-span-ap {{ grid-column: 2 / span 3; }}
                .c-span-at {{ grid-column: 2 / span 5; }}
                .c-span-im {{ grid-column: 2 / span 5; }}
                .c-span-ct {{ grid-column: 2 / span 3; }}
                .c-span-iapp {{ grid-column: 2 / span 2; }}
                .c-span-il {{ grid-column: 2 / span 3; }}
                .c-span-do {{ grid-column: 2 / span 4; }}
                .c-span-to {{ grid-column: 2 / span 2; }}
                .c-span-doe {{ grid-column: 2 / span 3; }}
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
                    grid_row_start = f"style='grid-row-start: {i + 1};'"
                    grid_col_start = f"style='grid-column-start: {j + 1};'"

                    # Row Spans for the first column
                    if i == 0 and j == 0: row_span_class = "r-span-tm"
                    elif i == 5 and j == 0: row_span_class = "r-span-cs"
                    elif i == 9 and j == 0: row_span_class = "r-span-cc"
                    elif i == 12 and j == 0: row_span_class = "r-span-ia"

                    # Column Spans for the second column (Dimension) and onwards
                    if j == 1:
                        if i == 0: col_span_class = "c-span-k"
                        elif i == 1: col_span_class = "c-span-cp"
                        elif i == 2: col_span_class = "c-span-cpres"
                        elif i == 3: col_span_class = "c-span-caq"
                        elif i == 5: col_span_class = "c-span-cf"
                        elif i == 6: col_span_class = "c-span-pa"
                        elif i == 7: col_span_class = "c-span-tc"
                        elif i == 8: col_span_class = "c-span-tpi"
                        elif i == 9: col_span_class = "c-span-dvc"
                        elif i == 10: col_span_class = "c-span-ap"
                        elif i == 11: col_span_class = "c-span-at"
                        elif i == 12: col_span_class = "c-span-im"
                        elif i == 13: col_span_class = "c-span-ct"
                        elif i == 14: col_span_class = "c-span-iapp"
                        elif i == 15: col_span_class = "c-span-il"
                        elif i == 16: col_span_class = "c-span-do"
                        elif i == 17: col_span_class = "c-span-to"
                        elif i == 18: col_span_class = "c-span-doe"
                    elif j > 1 and df.iloc[i, 1] is None:
                        continue # Skip rendering if the corresponding Dimension cell is None

                    html_grid += f"<div class='cell {row_span_class} {col_span_class}'>{value}</div>"
        html_grid += "</div>"
        st.markdown(html_grid, unsafe_allow_html=True)

render_morphological_box_with_refined_grid(df)
