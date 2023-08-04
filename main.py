from typing import Union

from fastapi import FastAPI

app = FastAPI()

from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "GanymedeNil/text2vec-large-chinese"
embeddings = HuggingFaceEmbeddings(model_name=model_name,model_kwargs={'device': "cpu"})

@app.get("/embedding/{input_str}")
def read_item(input_str: str):
    return embeddings.embed_query(input_str)