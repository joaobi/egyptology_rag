import os
import streamlit as st
from llama_index import load_index_from_storage, StorageContext

st.set_page_config(page_title="Chat with the Egyptology PFDs", page_icon="💬", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Chat with the Egyptology docs 𓏞")
# st.subheader("Powered by Streamlit and LlamaIndex 💬🦙")
st.info("Document repository used to build this app is available at the  [Egyptology Books and Articles in PDF online](http://egyptologyresources.x10host.com/er/bibliography/bibliography_data.html) website", icon="📃")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question contained in the Egyptology PDF sources available on the website above!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing – hang tight! This should take 1-2 minutes."):
        
        storage_context = StorageContext.from_defaults(persist_dir="storage")
        index  = load_index_from_storage(storage_context)  
        
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)

            if len(response.source_nodes) > 0:
                st.divider()
                st.write("References:")
                refs = set([x.node.extra_info["file_name"]  for x in response.source_nodes])
                for node in refs:
                    st.caption(node)

            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
