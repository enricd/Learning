# pip install streamlit langchain_core langchain_community langchain_openai langchain chromadb beautifulsoup4 python-dotenv

import os
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import dotenv

dotenv.load_dotenv()

llm = AzureChatOpenAI(
    openai_api_key=os.getenv("AZ_OPENAI_API_KEY"),
    openai_api_base=os.getenv("AZ_OPENAI_API_BASE"),
    api_version="2024-02-15-preview",
    model_name="gpt-4-1106-preview",
    openai_api_type="azure",
    temperature=0.2,
)


def get_vectorstore_from_url(url):
    # Get the text in document form
    loader = WebBaseLoader(url)
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # Create a vectorstore from the chunks
    vector_store = Chroma.from_documents(
        document_chunks, 
        AzureOpenAIEmbeddings(
            openai_api_key=os.getenv("AZ_OPENAI_API_KEY"),
            openai_api_base=os.getenv("AZ_OPENAI_API_BASE"),
            api_version="2024-02-15-preview",
        )
    ) 

    return vector_store


def get_context_retriever_chain(vector_store, llm):

    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        ("user", "Given the above conversation, generate a search query to look up in order to get inforamtion relevant to the conversation, focusing on the most recent messages."),
    ])

    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

    return retriever_chain


def get_conversational_rag_chain(retriever_chain, llm):
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer the user's questions based on the below context\n\n{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ])

    stuff_documents_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(retriever_chain, stuff_documents_chain)


def get_response(user_input):
    # Create converation chain
    # st.info(f"Chatting with {website_url}")
    retriever_chain = get_context_retriever_chain(st.session_state.vector_store, llm)
    converation_rag_chain = get_conversational_rag_chain(retriever_chain, llm)

    response = converation_rag_chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_query,
    })

    return response["answer"]
    

# App config
st.set_page_config(
    page_title="Chat with websites",
    page_icon="🤖"
)

st.title("Chat with websites")


# Sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

if website_url is None or website_url == "":
    st.error("Please provide a website URL")
    st.stop()

else:
    # Session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage("Hello! How can I help you today?"),
        ]

    if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vectorstore_from_url(website_url)

    # User input
    user_query = st.chat_input("Type a message...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)

        st.session_state.chat_history.append(HumanMessage(user_query))
        st.session_state.chat_history.append(AIMessage(response))

        # retrieved_documents = retriever_chain.invoke({
        #     "chat_history": st.session_state.chat_history,
        #     "input": user_query
        # })
        # st.write(retrieved_documents)

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        else:
            with st.chat_message("Human"):
                st.write(message.content)