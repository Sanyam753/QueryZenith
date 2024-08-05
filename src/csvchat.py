from langchain_groq import ChatGroq
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Function to chat with CSV data
def chat_with_csv(df, query):
    try:
        # Initialize ChatGroq with the API key
        chat_groq = ChatGroq(api_key=groq_api_key)
        
        # Initialize SmartDataframe with DataFrame and LLM configuration
        pandas_ai = SmartDataframe(df, config={"llm": chat_groq})
        
        # Chat with the DataFrame using the provided query
        result = pandas_ai.chat(query)
        
        # Check if the result contains code
        if not result:
            raise ValueError("Empty response received from the model.")
        
        return result
    except ValueError as ve:
        # Handle the case where no code is found
        return f"ValueError: {ve}"
    except Exception as e:
        # Handle other exceptions
        return f"An error occurred: {e}"

# Set layout configuration for the Streamlit page
st.set_page_config(layout='wide')
# Set title for the Streamlit application
st.title("Multiple-CSV ChatApp powered by LLM")

# Upload multiple CSV files
input_csvs = st.sidebar.file_uploader("Upload your CSV files", type=['csv'], accept_multiple_files=True)

# Check if CSV files are uploaded
if input_csvs:
    # Select a CSV file from the uploaded files using a dropdown menu
    selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    # Load and display the selected CSV file
    st.info("CSV uploaded successfully")
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data.head(3), use_container_width=True)

    # Enter the query for analysis
    st.info("Chat Below")
    input_text = st.text_area("Enter the query")

    # Perform analysis
    if input_text:
        if st.button("Chat with csv"):
            st.info("Your Query: " + input_text)
            result = chat_with_csv(data, input_text)
            st.success(result)
