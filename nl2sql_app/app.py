import streamlit as st
from llm import generate_sql
from db import run_query

st.set_page_config(page_title="NL2SQL A/B Testing", layout="wide")

st.title("📊 NL2SQL - A/B Testing Analytics")

query = st.text_input("Ask a question:")

if st.button("Run Query"):
    if query:
        # Step 1: Generate SQL
        with st.spinner("Generating SQL..."):
            sql_query = generate_sql(query)

        st.subheader("Generated SQL")
        st.code(sql_query, language="sql")

        # Step 2: Safety check
        if not sql_query.lower().strip().startswith("select"):
            st.error("Only SELECT queries are allowed")
            st.stop()

        # Step 3: Run query
        try:
            df = run_query(sql_query)

            st.subheader("Results")
            st.dataframe(df)

            # Optional visualization
            if len(df.columns) >= 2:
                st.subheader("Visualization")
                st.line_chart(df.set_index(df.columns[0]))

        except Exception as e:
            st.error(f"Error: {e}")