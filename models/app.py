import os
from flask import Flask, jsonify, request
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import InMemoryVectorStore
from langchain import LLMChain, PromptTemplate
from langchain.docstore.document import Document
from pypdf import PdfReader
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader

OPENAI_API_KEY='AIzaSyDSFSqcDt43ezHzFW1npREHhQ_E6Lvox2M'
loader=PyPDFLoader("C:/SDG EXPOLRER/models/SDG.pdf")
pages=loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
texts=text_splitter.split_documents(pages)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=OPENAI_API_KEY)
docsearch = InMemoryVectorStore.from_documents(texts,embeddings)

docsearch.embeddings

template = """You are a teaching assistant:
{context}
Now, based on this information and some of your knowledge about SDG, answer the following question:
{question}
Provide a concise and accurate response based of all the given information not just below:
"""

prompt = PromptTemplate(
    input_variables=["context", "question"], template=template
)

retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={"k":2})
llm=ChatGoogleGenerativeAI(google_api_key=OPENAI_API_KEY,model="gemini-1.5-flash",temperature=0)

qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}

)

def get_text_response(message):
  query = message
  result = qa_chain.invoke(query)
  response= result['result']
  return response


app = Flask(__name__)

# Store the key-value pairs in a dictionary
data = {}

@app.route('/dashboard/api', methods=['POST'])
def update_data():
    global data
    key = request.json['key']
    value = request.json['value']
    data[key] = value
    return jsonify({'message': 'Data updated successfully'})

@app.route('/dashboard/api', methods=['GET'])
def get_data():
    global data
    value=get_text_response(data["Quest"])
    data['Prompt']=value
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
