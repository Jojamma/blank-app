import streamlit as st
import subprocess
import sys
import importlib

# Function to install missing packages
def install_package(package_name):
    try:
        # Special case for scikit-learn
        if package_name == "sklearn":
            package_name = "scikit-learn"
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        st.success(f"Successfully installed {package_name}")
    except Exception as e:
        st.error(f"Failed to install {package_name}: {e}")

# Title of the Streamlit app
st.title("Online Python Compiler with Library Support")

# Text area to input Python code
code = st.text_area("Enter your Python code here:", height=300)

# Button to run the code
if st.button("Run"):
    with open("temp_code.py", "w") as f:
        f.write(code)  # Save the user input code to a temporary file
    
    # Extract package imports from the code
    imported_packages = []
    for line in code.splitlines():
        if line.startswith("import ") or line.startswith("from "):
            parts = line.split()
            if "import" in parts:
                imported_packages.append(parts[1].split('.')[0])
    
    # Check for and install missing packages
    for package in set(imported_packages):
        try:
            importlib.import_module(package)
        except ModuleNotFoundError:
            st.warning(f"Package '{package}' not found. Attempting to install...")
            install_package(package)
    
    # Run the Python file and capture output
    try:
        result = subprocess.run([sys.executable, "temp_code.py"], capture_output=True, text=True)
        st.subheader("Output:")
        st.code(result.stdout if result.stdout else result.stderr)
    except Exception as e:
        st.error(f"Error while executing the code: {e}")

# Footer with a helpful link
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
