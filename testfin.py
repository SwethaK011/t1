import os
from dotenv import load_dotenv
import json
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from streamlit_lottie import st_lottie_spinner
from langchain.memory import ConversationBufferMemory
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL
import uuid

from streamlit_cookies_controller import CookieController

def render_animation():
    path = "typing_animation.json"
    with open(path,"r") as file: 
        animation_json = json.load(file)
        return animation_json



def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
    return conversation_string

st.set_page_config(
    page_title="Softsquare AI",
    page_icon="🤖",
)
 
controller = CookieController()
 
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
# Function to handle login
def login(email):
        st.session_state.logged_in = True
# Register the cookie manager
aq=controller.set('email_id','')
# Check if the user has a unique ID cookie
cookies=controller.getAll()
if not st.session_state.logged_in:
    if (aq is None):
    # Generate a unique user ID
        user_id = controller.get("ajs_anonymous_id")
    # Set the user ID cookie
        s1=st.text_input("Enter email")
        controller.set("email_id",s1)
        st.write(cookies)
        login(s1)
       
    else:
    # Retrieve the user ID from the cookie
        user_id = controller.get("ajs_anonymous_id")
        st.title("Confirmation")
        Email=controller.get("email_id")
        st.write("Is this ur email{Email}")
        Email="hello"
        st.write(cookies)
        login(Email)
       
if st.session_state.logged_in:
   st.write(controller.get('email_id'))
