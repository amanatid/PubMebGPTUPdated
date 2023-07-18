from llama_index import  VectorStoreIndex,download_loader
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings

from openai.error import OpenAIError
from base import PubmedReader_mod
import os
import sys
import openai
import streamlit as st
from  sidebar  import *



# create the website reader
PubmedReader = download_loader("PubmedReader")
global loader,documents, index,dummy

loader = None
documents = None
index = None


st.set_page_config(page_title="My App")

st.header("⚕️PubMedGPT ")
sidebar()
st.subheader(
    "I am a PumMedGPT(Chatbot) Medical Scientist. Please fill the fields below to start our discussion.."
    "If you find it useful, you can kindly donate here [Stripe](https://buy.stripe.com/6oEbMm0SCfChbNSfYZ)"
)





api_key_input = st.text_input(
    "OpenAI API Key",
    type="password",
    placeholder="Paste your OpenAI API key here.....",
    help="You can get your API key from https://platform.openai.com/account/api-keys.",
)

os.environ['OPENAI_API_KEY'] = api_key_input



query = st.text_input("What is the medical scientific topic do you want to discuss?")

max_query = st.number_input("How many papers should I investigate?", step=0)

dummy = st.radio(
    "Search Criterion",
    ('Relevance', 'Publication Date', 'Journal Name'))


if query and max_query and dummy:
    try:
        dummy1 = dummy
        if dummy1 == 'Relevance':
            search_query_int = 0

        if dummy1 == 'Publication Date':
            search_query_int = 1

        if dummy1 == "Journal Name":
            search_query_int = 2

        # load the reader
        loader = PubmedReader_mod()
        documents = loader.load_data(search_query=query,max_results=max_query,search_criterion= search_query_int)
        
        openai.api_key = api_key_input
        index =  VectorStoreIndex.from_documents(documents)
        st.markdown("PumMed papers are loaded based on the criteria.")
    except Exception as e:
        st.error("Please configure your OpenAI API key!")


with st.form("my_form"):
    user = st.text_input("Ask me any question about " + query + ":")
    submitted = st.form_submit_button("Submit")

    try:
        if user and index is not None:
            query_engine = index.as_query_engine()
            response = str(query_engine.query(user))   
        # response = index.query(user)
    except Exception as err:
        st.error("User input or Index Error", err)

    if submitted:
        try:
            if not api_key_input:
                st.error("Please enter Open Api Key!")
            if not query:
                st.error("Please enter a topic to discuss!")
            if not max_query:
                st.error("Please choose number of files to be loaded!")
            if (query and max_query):
                st.text_area("Medical Bot 👨‍⚕️", response, height=500)
        except OpenAIError as e:
            st.error(e._message)
        except (RuntimeError, TypeError, NameError):
            st.error("Runtime/Type/Name Error")
        except OSError as err:
            st.error("OS error:", err)
        except ValueError:
            st.error("Could not convert data to string.")
        except Exception as err:
            st.error(f"Unexpected {err=}, {type(err)=}")
        except ConnectionError as err:
            st.error("Connection Error:", err)
