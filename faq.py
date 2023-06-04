# flake8: noqa
import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## How does PubMedGPT works work?
When you  load do it will be divided into smaller chunks 
and stored in a special type of database called a vector index 
that allows for semantic search and retrieval.

When you ask a question, PubMedvGPT will search through the
pdf chunks and find the most relevant ones using the vector index.
Then, it will use the powerful language model GPT4 to generate a final answer.

## Why does PubMedGPT take time to index my document?
The reason is the following one. In the case of a free OpenAI API key
takes time to index the loaded pdf files since a free API key has a 
restricted [rate limits](https://platform.openai.com/docs/guides/rate-limits/overview).
To make  the process fast, you can use a paid API key.


## How accurate is  PubMedGPT?
To our experience and our tests, it seems impressive accurate but keep in mind the 
following since GPT-4 is language model  is keen to mistakes. It is 
based on semantic search  and extracts the most relevant chuncks from the pdf 
files. 
"""
    )
