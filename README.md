# PubMebGPTUPdated
An updadted GPT  engine for the PubMed database. It concerns people that are associated withint the medical sector.



## **Intro**
We create a PubMedBot App  using Streamlit, llama_index, Langchain and OpenAI. The PudMed Bot is a Medical Scientist  who
can answer you  questions that are related to Medical Science. For this reason you need an account on OpenAI and its associated
api key. More specifically, you need to train our Medical Scientist based on the seacrh query,  number of related files and a specific criterion. The criterion is based on three parameters a)Relevance, b)Publication Date and c)Journal Name.

    
You can find the app on [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://amanatid-pubmebgptupdated-streamlit-pubmedapp-updated-kxty2b.streamlit.app/). In case you find it useful you can donate on [Stripe](https://buy.stripe.com/cN2dUu44OahXaJO288). 



### **Quick Start**  
- Input the OpenAI Api key and press Enter.
- Input Query, number of files and choose Relevance, Publication Date and Journal Name and files are loaded .
- The maximum number of files you can enter are 50. 
- When you see the message "PuBMed papers are loaded based on the criteria" you are ready to chat as a User.
- Under the User ask the question and press the Submit button, wait a little and the PubMed Scientist will respond you.

We are using the default chat model from OpenAI ChatGPT-4.

### Issues
In the case of a free OpenAI API key takes time to index the loaded pdf files since a free API key has a restricted [rate limits](https://platform.openai.com/docs/guides/rate-limits/overview). To make the process fast, you can use a paid API key. It is not so fast during the training along with the response from the Chatbot engine.

### Future Prospectives 
We  are looking to improve the layout and be more self-explanatory. Also, we will provide
option to download the requested pdf files along with their abstracts. 

### **References**
1. https://github.com/emptycrown/llama-hub/blob/main/loader_hub/papers/arxiv/
2. https://llamahub.ai/l/papers-pubmed
3. https://github.com/mmz-001/knowledge_gpt/tree/main
4. https://pubmed.ncbi.nlm.nih.gov/
