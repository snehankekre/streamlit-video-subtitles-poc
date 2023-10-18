import io

import streamlit as st

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    [
        "Single VTT",
        "Single SRT",
        "Multiple",
        "Single BytesIO",
        "All supprted formats",
        "YouTube",
        "File Uploader",
    ]
)

with tab1:
    st.header("One subtitle in VTT format")
    with st.echo():
        st.video("sample.mp4", subtitles="sample_french.vtt")

with tab2:
    st.header("One subtitle in SRT format")
    with st.echo():
        st.video("sample.mp4", subtitles="sample_english.srt")

with tab3:
    st.header("Multiple subtitles in either VTT or SRT format")
    with st.echo():
        st.video(
            "sample.mp4",
            subtitles={
                "English": "sample_english.srt",
                "French": "sample_french.vtt",
                "German": "sample_german.vtt",
            },
        )

with tab4:
    st.header("One subtitle in SRT format (and BytesIO)")
    with st.echo():
        srt = io.BytesIO(
    """
1
00:00:03,500 --> 00:00:05,000
Everyone wants the most from life

2
00:00:06,000 --> 00:00:09,000
Like internet experiences that are rich and entertaining

3
00:00:11,000 --> 00:00:14,000
Phone conversations where people truly connect

4
00:00:14,500 --> 00:00:18,000
Your favourite TV programmes ready to watch at the touch of a button
""".strip().encode(
        "utf-8"
    )
)

        st.video("sample.mp4", subtitles=srt)

        st.write("Subtitle with label")

        st.video("sample.mp4", subtitles={"LLM 1": srt})

with tab5:
    st.header("Multiple subtitles in either VTT or SRT format (and BytesIO)")
    with st.echo():
        srt = io.BytesIO(
    """
1
00:00:03,500 --> 00:00:05,000
Everyone wants the most from life

2
00:00:06,000 --> 00:00:09,000
Like internet experiences that are rich and entertaining

3
00:00:11,000 --> 00:00:14,000
Phone conversations where people truly connect

4
00:00:14,500 --> 00:00:18,000
Your favourite TV programmes ready to watch at the touch of a button
""".strip().encode(
        "utf-8"
    )
)

        st.video(
            "sample.mp4",
            subtitles={
                "io.BytesIO SRT": srt,
                "German": "sample_german.vtt",
                "English VTT": "sample_english.vtt",
                "English SRT": "sample_english.srt",
            },
        )

with tab6:
    st.header("YouTube")
    if st.checkbox("Show YouTube video"):
        with st.echo():
            st.video(
                "https://www.youtube.com/watch?v=xQwDfW7UHMo",
                subtitles="sample_english.vtt",
            )

with tab7:
    st.header("File Uploader")
    uploaded_file = st.file_uploader("Upload a subtitle file", type=["vtt", "srt"])
    st.video("sample.mp4", subtitles=uploaded_file)
