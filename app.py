import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from src.data.transform import process_raw_todoist_data

def analyze_todoist_labels(df, columns_of_interest, goals):
    sums = [df[col].eq(True).sum() for col in columns_of_interest]
    percentages = [(count / goals[col]) * 100 for col, count in zip(columns_of_interest, sums)]
    sorted_indices = sorted(range(len(percentages)), key=lambda i: percentages[i])
    sorted_cols = [columns_of_interest[i] for i in sorted_indices]
    sorted_perc = [percentages[i] for i in sorted_indices]
    fig = go.Figure([
        go.Bar(
            x=sorted_cols,
            y=sorted_perc,
            marker=dict(color=sorted_perc, colorscale="RdYlGn", cmin=0, cmax=100)
        )
    ])
    fig.update_layout(title="Completion % vs Goals", yaxis=dict(range=[0, 100]))
    return fig

def main():
    st.title("Todoist Label Analytics")
    csv_path = st.text_input("Raw CSV Path", "data/raw_todoist_data.csv")
    df = process_raw_todoist_data(csv_path)

    excluded_columns = [col for col in df.columns if any(c.isupper() for c in col)]
    allowed_columns = [col for col in df.columns if col not in excluded_columns]
    columns_of_interest = st.multiselect(
        "Select columns to analyze",
        allowed_columns,
    )

    goals = {}
    for col in columns_of_interest:
        goals[col] = st.number_input(f"Goal for '{col}'", min_value=0, value=5, step=1)

    if st.button("Analyze"):
        fig = analyze_todoist_labels(df, columns_of_interest, goals)
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()