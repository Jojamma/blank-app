import streamlit as st
import subprocess
import sys

# Title of the Streamlit app
st.title("Online Python Compiler")

# Text area to input Python code
code = st.text_area("Enter your Python code here:", height=300)

# Button to run the code
if st.button("Run"):
    with open("temp_code.py", "w") as f:
        f.write(code)  # Save the user input code to a temporary file
    try:
        # Run the temporary Python file and capture the output
        result = subprocess.run([sys.executable, "temp_code.py"], capture_output=True, text=True)
        st.subheader("Output:")
        # Display the output or errors
        st.code(result.stdout if result.stdout else result.stderr)
    except Exception as e:
        st.error(f"Error: {e}")
