import streamlit as st

with st.echo():
    st.video(
        "sample.mp4",
        subtitles=[
            {"lang": "en", "url": "sample_english.vtt"},
            {"lang": "fr", "url": "sample_french.vtt"},
            {"lang": "zh", "url": "sample_chinese.vtt"},
            {"lang": "de", "url": "sample_german.vtt"},
        ],
    )
