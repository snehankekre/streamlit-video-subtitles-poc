import io

import streamlit as st

st.title("📽️ st.video with subtitle/CC support")

st.markdown("For more information, see the [Subtitle/CC support in st.video](https://www.notion.so/snowflake-corp/Subtitle-CC-support-in-st-video-39bd511be61c49dab094672dcd38c09a) Notion page. Get the wheel file [here](https://github.com/snehankekre/streamlit-video-subtitles-poc/raw/main/streamlit-1.28.0-py2.py3-none-any.whl).")
st.write("This feature adds an argument to `st.video` to accept subtitle files")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
    [
        "Single VTT",
        "Single VTT (with label)",
        "Single SRT",
        "Single SRT (with label)",
        "Multiple",
        "Single raw string",
        "Single BytesIO",
        "All supported formats",
        "YouTube",
        "File Uploader",
    ]
)

with tab1:
    st.header("One subtitle in VTT format")
    with st.echo():
        st.video("sample.mp4", subtitles="sample_french.vtt")

with tab2:
    st.header("One labeled subtitle in VTT format")
    with st.echo():
        st.video("sample.mp4", subtitles={"French": "sample_french.vtt"})

with tab3:
    st.header("One subtitle in SRT format")
    with st.echo():
        st.video("sample.mp4", subtitles="sample_english.srt")

with tab4:
    st.header("One labeled subtitle in SRT format")
    with st.echo():
        st.video("sample.mp4", subtitles={"English": "sample_english.srt"})

with tab5:
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

with tab6:
    st.header("Raw string")
    with st.echo():
        vtt = """
        WEBVTT FILE

        1
        00:00:03.500 --> 00:00:05.000 D:vertical A:start
        Jeder möchte das Meiste aus dem Leben herausholen

        2
        00:00:06.000 --> 00:00:09.000 A:start
        Wie Internet-Erlebnisse, die reichhaltig <b>und</b> unterhaltsam sind

        3
        00:00:11.000 --> 00:00:14.000 A:end
        Telefongespräche, bei denen Menschen wirklich <c.highlight>verbinden</c>
        """
        st.video("sample.mp4", subtitles=vtt)

with tab7:
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

with tab8:
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

with tab9:
    st.header("YouTube")
    st.write(
        "Checking the checkbox below will raise a `StreamlitAPIException` since YouTube videos do not support subtitles."
    )
    if st.checkbox("Show YouTube video"):
        with st.echo():
            st.video(
                "https://www.youtube.com/watch?v=xQwDfW7UHMo",
                subtitles="sample_english.vtt",
            )

with tab10:
    st.header("File Uploader")
    uploaded_file = st.file_uploader("Upload a subtitle file", type=["vtt", "srt"])
    st.video("sample.mp4", subtitles=uploaded_file)
