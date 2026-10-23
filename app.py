"""Streamlit front end for the document summarizer. See README.md to run it."""

import json
import os

import streamlit as st

from summarize import AnalysisError, MESSAGES, analyze, decode_upload, make_client

st.set_page_config(page_title="Document Analyzer", page_icon="📄")
st.title("📄 Document Analyzer")
st.caption("Paste text or upload a file to get a summary, key points, and action items.")


def get_api_key():
    """Look for the key in the environment first, then in Streamlit secrets (for deployment)."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except Exception:
        return None


# ---- Input ----
uploaded = st.file_uploader("Upload a text file", type=["txt", "md"])
pasted = st.text_area("...or paste text here", height=200)

# ---- Run ----
if st.button("Analyze", type="primary"):
    try:
        text = decode_upload(uploaded.getvalue()) if uploaded is not None else pasted
        client = make_client(get_api_key())
        with st.spinner("Analyzing..."):
            result, warnings = analyze(client, text)
    except AnalysisError as e:
        st.error(str(e))  # every expected problem has its own message in summarize.MESSAGES
    except Exception:
        st.error(MESSAGES["unexpected"])
    else:
        for w in warnings:
            st.warning(w)

        # ---- Output ----
        st.header(result["title"])
        st.write(result["summary"])

        st.subheader("Key points")
        for point in result["key_points"]:
            st.markdown(f"- {point}")

        st.subheader("Action items")
        if result["action_items"]:
            st.table(result["action_items"])
        else:
            st.write("None found.")

        with st.expander("Entities"):
            st.json(result["entities"])

        with st.expander("Raw JSON"):
            st.json(result)
        st.download_button(
            "Download JSON",
            data=json.dumps(result, indent=2),
            file_name="analysis.json",
            mime="application/json",
        )
