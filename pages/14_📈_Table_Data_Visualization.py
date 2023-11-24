import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Function for the CSV Visualization App
def app():
    st.title('CSV Data Visualization')

    # File uploader allows user to add their own CSV
    uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

    # Pandas DataFrame is created from the CSV file
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)  # Display the dataframe on the app

        # Create a selectbox for user to choose the column to visualize
        columns = df.columns.tolist()
        selected_column = st.selectbox('Select a column to visualize', columns)

        # Using seaborn to create a count plot
        fig, ax = plt.subplots()
        sns.countplot(data=df, x=selected_column, ax=ax)
        plt.xticks(rotation=45)  # Rotate X-axis labels to 45 degrees
        # Show the plot
        st.pyplot(fig)

app()