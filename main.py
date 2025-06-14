# import streamlit as st
# from scrape import (
#     scrape_website,
#     split_dom_content,
#     clean_body_content,
#     extract_body_content,
#     )
# from parse import parse_with_ollama

# st.title("AI-Powered Web Scraper")
# url = st.text_input("Enter a Website URL: ")

# if st.button("Scrape Site"):
#     st.write("Scrapping the webiste")
#     dom_content = scrape_website(url)
#     body_content = extract_body_content(dom_content)
#     cleaned_content = clean_body_content(body_content)

#         # Store the DOM content in Streamlit session state
#     st.session_state.dom_content = cleaned_content

#         # Display the DOM content in an expandable text box
#     with st.expander("View DOM Content"):
#             st.text_area("DOM Content", cleaned_content, height=300)

# #ask user
# if "dom_content" in st.session_state:
#     parse_description = st.text_area("Describe what you want to parse")

#     if st.button("Parse Content"):
#         if parse_description:
#             st.write("Parsing the content...")

#             # Parse the content with Ollama
#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             parsed_result = parse_with_ollama(dom_chunks, parse_description)
#             st.write(parsed_result)
































import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
)
from parse import parse_with_ollama

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AI-Powered Web Scrapper",
    # page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR LIGHT THEME ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #ffffff;
            color: #000000;
            font-family: 'Segoe UI', sans-serif;
        }

        .title {
            font-size: 2.8rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 0.2em;
            color: #222222;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #555555;
            text-align: center;
            margin-bottom: 2em;
        }

        .section-header {
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            color: #111111;
        }

        .stTextInput > div > div > input,
        .stTextArea textarea {
            background-color: #f8f9fa !important;
            color: #000000 !important;
            border: 1px solid #cccccc;
        }

        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 0.4rem;
            border: none;
            padding: 0.4em 1.2em;
            font-weight: 500;
        }

        .stButton>button:hover {
            background-color: #0056b3;
        }

        .stExpanderHeader {
            background-color: #f1f1f1 !important;
            color: #000 !important;
        }

        .codebox {
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            padding: 1em;
            font-family: monospace;
            border-radius: 0.4rem;
            color: #111;
        }
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown("<div class='title'>AI- Powewd Web Scrapper</div>", unsafe_allow_html=True)
# st.markdown("<div class='subtitle'>AI-Powered Web Scraping and Parsing Interface</div>", unsafe_allow_html=True)

# --- URL INPUT ---
st.markdown("<div class='section-header'>🔗 Enter a Website URL</div>", unsafe_allow_html=True)
url = st.text_input("", placeholder="https://example.com")

if st.button("🚀 Scrape Site") and url:
    with st.spinner("Scraping the website..."):
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)
        st.session_state.dom_content = cleaned_content

    st.success("✅ Scraping complete!")

    with st.expander("📄 View Extracted DOM Content"):
        st.text_area("Cleaned Content", cleaned_content, height=300)

# --- PARSE INPUT ---
if "dom_content" in st.session_state:
    st.markdown("<div class='section-header'>💬 Describe What You Want to Parse</div>", unsafe_allow_html=True)
    parse_description = st.text_area("Your Prompt", placeholder="e.g. Extract all headings from the page...")

    if st.button("🧠 Parse Content"):
        if parse_description:
            with st.spinner("Parsing the content..."):
                dom_chunks = split_dom_content(st.session_state.dom_content)
                parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.success("✅ Parsing complete!")

            st.markdown("<div class='section-header'>📑 Parsed Result</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='codebox'>{parsed_result}</div>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("## ⚙️ Settings (Coming Soon)")
st.sidebar.info("More controls for model type and output formatting will be available here.")


