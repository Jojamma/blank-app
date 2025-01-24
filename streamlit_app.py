# Create the Streamlit app
%%writefile app.py
import streamlit as st
import subprocess
import sys
st.title("Online Python Compiler")
code = st.text_area("Enter your Python code here:", height=300)
if st.button("Run"):
    with open("temp_code.py", "w") as f:
        f.write(code)
    try:
        result = subprocess.run([sys.executable, "temp_code.py"], capture_output=True, text=True)
        st.subheader("Output:")
        st.code(result.stdout if result.stdout else result.stderr)
    except Exception as e:
        st.error(f"Error: {e}")
# Run the Streamlit app in the background
!streamlit run app.py &>/content/logs.txt &
# Expose the app using ngrok
from pyngrok import ngrok
# Start ngrok tunnel on port 8501 (default Streamlit port)
public_url = ngrok.connect(port=8501)
print(f"Access your app at: {blank-app-30doficgjie.streamlit.app}")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
