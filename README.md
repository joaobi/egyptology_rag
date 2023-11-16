# Egyptology Documents
This demo repository holds source code to:
1. Build an Index using the RAG pattern (Retrieve, Annotate, Generate) using LlamaIndex to create a knowledge graph of Egyptology documents.
2. Build a chatBot app (using Streamlit) leveraging the Index above.

## Content
* build_rag.py - Python script to build the RAG index (uses LlamaIndex and OpenAI API )
* app.py - Python script to run the Streamlit app that uses the index to expose a chatInterface

Note: You should add the PDFs you want to index to the data folder.

The app can be run locally or the dockerfile can be used to create the Docker image for the above content and run the app.
