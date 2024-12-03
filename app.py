# Import necessary libraries

# Import necessary libraries
import streamlit as st
import os
from together import Together

# Title for the placeholder app
st.title("Secrets and Together Client Debugging")

# Debugging Secrets Manager
st.header("Step 1: Check Streamlit Secrets")

try:
    # Check if the secrets are accessible
    secrets = st.secrets
    st.write("Secrets found:", secrets)
    
    # Try accessing the specific TOGETHER_API_KEY
    api_key = secrets["TOGETHER_API_KEY"]
    st.success(f"TOGETHER_API_KEY is set! Partial value: {api_key[:5]}***")
except KeyError as e:
    st.error(f"KeyError: Missing secret key: {e}")
except Exception as e:
    st.error(f"Unexpected error while accessing secrets: {e}")

# Debugging Together Client Initialization
st.header("Step 2: Initialize Together Client")

try:
    # Set the API key as an environment variable
    os.environ["TOGETHER_API_KEY"] = st.secrets["TOGETHER_API_KEY"]
    
    # Initialize the Together client
    client = Together()
    st.success("Together client initialized successfully!")
except KeyError as e:
    st.error(f"KeyError during Together client setup: {e}")
except Exception as e:
    st.error(f"Unexpected error during Together client setup: {e}")

# Final Debug Output
st.header("Step 3: Ready for Final App")
st.write("If the above steps show success, your app is ready for deployment.")

'''import streamlit as st
import os
from together import Together

os.environ['TOGETHER_API_KEY'] = st.secrets["TOGETHER_API_KEY"]

# Initialize Together client
client = Together()

# Function to generate Python code using CodeLlama
def generate_code_with_codellama(description):
    """
    Generate Python code based on a natural language description using CodeLlama.

    Parameters:
    description (str): A plain-text description of the desired Python code.

    Returns:
    str: Generated Python code or an error message.
    """
    try:
        prompt = (
            f"You are a Python programming assistant. Based on the following description, "
            f"generate the Python code. Ensure the code is clear, well-commented, and includes necessary imports.\n\n"
            f"Description: {description}\n\n"
            f"Generated Python Code:"
        )

        # Call Together AI
        response = client.chat.completions.create(
            model="codellama/CodeLlama-34b-Instruct-hf",  # CodeLlama model
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract the generated code
        generated_code = response.choices[0].message.content.strip()
        return generated_code

    except Exception as e:
        return f"Error with CodeLlama: {e}"


# Streamlit app layout
st.title("Python Code Generator with CodeLlama")
st.write("Enter a description of the Python application or code you need. CodeLlama will generate the corresponding Python code.")

# Input box for the user to enter a description
description = st.text_area("Application or Code Description", placeholder="Describe the application or code you want")

# Button to trigger code generation
if st.button("Generate Code"):
    if description.strip():
        st.write("### Generated Python Code")
        # Generate code
        generated_code = generate_code_with_codellama(description)
        st.code(generated_code, language="python")
    else:
        st.error("Please provide a valid description.")
'''


