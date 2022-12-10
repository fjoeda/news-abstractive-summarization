import streamlit as st
from summarizer import NewsSummarizer

news_sumarizer = NewsSummarizer()

def summarize_from_text():
    text = st.text_area("News text")

    if st.button("Summarize"):
        st.write("Result : ")
        output_text = news_sumarizer.summarize(text, translate_to_id=True)
        st.write(output_text)
    else:
        st.write("Result : ")

def summarize_from_url():
    url = st.text_input("News url")

    if st.button("Summarize"):
        st.write("Result : ")
        output_text = news_sumarizer.summarize_url(url, translate_to_id=True)
        st.write(output_text)
    else:
        st.write("Result : ")

def intro():
    st.write(" 👈 Select mode from the dropdown")

pages_dict = {
    "-":intro,
    "News Text":summarize_from_text,
    "News Url":summarize_from_url
}

st.markdown("# News Summarizer Demo")
demo_name = st.sidebar.selectbox("Choose a demo", pages_dict.keys())
pages_dict[demo_name]()



