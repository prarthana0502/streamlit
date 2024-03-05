# Importing necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title('CSV File Explorer')

# File uploader widget
file = st.file_uploader('Upload CSV', type=['csv'])

# Check if a file is uploaded
if file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Display the DataFrame
    st.write('### Data Preview')
    st.write(df)

    # Data visualization
    st.write('### Data Visualization')

    # Select columns for X and Y axes
    x_column = st.selectbox('Select X axis:', options=df.columns)
    y_column = st.selectbox('Select Y axis:', options=df.columns)

    # Scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df[x_column], df[y_column])
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title('Scatter Plot')
    st.pyplot(fig)
