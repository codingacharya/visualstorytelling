import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt

# Set page config
st.set_page_config(page_title="Visual Storytelling", layout="wide")

# Custom theme
st.markdown("""
    <style>
    body {background-color: #f4f4f8;}
    .stApp {background-color: #f4f4f8;}
    </style>
    """, unsafe_allow_html=True)

# Generate sample data
df = pd.DataFrame({
    'Year': np.arange(2015, 2025),
    'Revenue': np.random.randint(50, 200, 10),
    'Profit': np.random.randint(10, 100, 10),
    'Market Share': np.random.randint(5, 30, 10)
})

# Sidebar filters
st.sidebar.header("Customize Story")
chart_type = st.sidebar.selectbox("Select a chart type", ["Line Chart", "Bar Chart", "Pie Chart", "Animated Chart"])

# Title
st.title("📊 Interactive Visual Storytelling with Streamlit")

# Line Chart
if chart_type == "Line Chart":
    fig = px.line(df, x='Year', y=['Revenue', 'Profit'], markers=True, title="Revenue & Profit Over Years")
    fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True)

# Bar Chart
elif chart_type == "Bar Chart":
    fig = px.bar(df, x='Year', y=['Revenue', 'Profit'], barmode='group', title="Revenue vs Profit")
    st.plotly_chart(fig, use_container_width=True)

# Pie Chart
elif chart_type == "Pie Chart":
    fig = px.pie(df, values='Market Share', names='Year', title="Market Share Distribution")
    st.plotly_chart(fig, use_container_width=True)

# Animated Chart (Altair)
elif chart_type == "Animated Chart":
    chart = alt.Chart(df).mark_bar().encode(
        x='Year:O',
        y='Revenue:Q',
        color=alt.Color('Year:O', scale=alt.Scale(scheme='tableau10'))
    ).properties(
        width=700,
        height=400
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

# Conclusion
st.success("🎉 Thank you for exploring interactive visual storytelling!")
