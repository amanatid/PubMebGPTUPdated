import streamlit as st

from faq import faq


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Choose the Medic Topic to dicuss🚩\n"
            "3. Load the number of  papers you want to investigate. \n"
            "4. Choose a criterion.\n"
            "5. Wait for the message 'PubMed papers are loaded based on the criteria' to be appeared.\n"
        )



        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "⚕️PubMedGPT allows you to  commit a scientific dialogue based on"
            " a specific  question/criterion and the amount of data that are loaded from"
            "[PubMed](https://pubmed.ncbi.nlm.nih.gov/). "
        )
        st.markdown(
            "This is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/amanatid/ArxivChatBot_StreamlitApp) " 
            "with your feedback and suggestions💡.Due to reqular updates from the llama/streamlit team, the app might "
            "crash. I try to maintain it up. In any case, please report any problem in the email below."
        )
        st.markdown("Made by [amanatid](amanatid@gmail.com)")
        st.markdown("---")

        faq()
