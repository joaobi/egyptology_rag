import os
import openai
import logging
import sys

from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    set_global_service_context,
    SimpleDirectoryReader,
)

from llama_index.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "REPLACE WITH YOUR OPEN AI API KEY"
openai.api_key = os.environ["OPENAI_API_KEY"]

# load documents
documents = SimpleDirectoryReader("./data/").load_data()
print("Loaded: "+str(len(documents))+" documents")

gpt35_llm = OpenAI(model="gpt-3.5-turbo")
gpt4_llm = OpenAI(model="gpt-4")

llm = gpt35_llm

service_context = ServiceContext.from_defaults(chunk_size=1024, llm=llm)

print("Building Index")
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

set_global_service_context(service_context)

print("Persisting Index")
index.storage_context.persist()


