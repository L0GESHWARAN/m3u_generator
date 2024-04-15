import streamlit as st
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

def main():
    st.title("URL to File Downloader")
    
    url = st.text_input("Enter the URL:")
    filename = st.text_input("Enter the filename to save as (with extension):")
    
    if st.button("Download"):
        if url and filename:
            try:
                download_file(url, filename)
                st.success(f"File '{filename}' downloaded successfully!")
            except Exception as e:
                st.error(f"Error occurred: {e}")
        else:
            st.warning("Please enter both URL and filename.")

if __name__ == "__main__":
    main()
