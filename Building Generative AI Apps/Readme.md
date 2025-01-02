# Langchain Demo with Google Gemini

This project demonstrates how to build a simple web application using **Streamlit** that integrates **Langchain** and **Google's Gemini 1.5 Pro model** for question answering. The application allows users to enter a question, which is then processed by the Gemini model to generate a response.

## Features
- **Streamlit Interface**: A user-friendly web interface where users can type their questions and get responses.
- **Langchain Integration**: The application uses Langchain to handle prompt creation, model interaction, and output parsing, making it easy to manage the flow of data.
- **Google Gemini Model**: The core of the system is the **Gemini-1.5-Pro model** from Google, which processes the user's input and generates human-like responses.
- **Customizable**: Easily change parameters like temperature, retries, and more to tune the model's behavior.

## How it Works
1. **User Input**: The user enters a question in the input field provided by Streamlit.
2. **Langchain Pipeline**: The input is passed through Langchain, where it is formatted using a predefined prompt template.
3. **Model Response**: The question is sent to the **Gemini-1.5-Pro** model, which generates a response.
4. **Output Parsing**: The response is processed by Langchain’s output parser and displayed on the webpage.

## Requirements
- Python 3.x
- Streamlit
- Langchain
- dotenv
- Google API credentials
![Screenshot 2025-01-03 011933](https://github.com/user-attachments/assets/ba78752d-3687-4ffd-96b9-b9199b017f30)

![Screenshot 2025-01-03 011950](https://github.com/user-attachments/assets/7b6d5e60-dec8-46da-80dc-ddc41ea07590)
