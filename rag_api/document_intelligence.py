# import os
# from azure.ai.formrecognizer import DocumentAnalysisClient
# from azure.core.credentials import AzureKeyCredential
# from langchain import hub
# from langchain_openai import AzureChatOpenAI
# from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader
# from langchain_openai import AzureOpenAIEmbeddings
# from langchain.schema import StrOutputParser
# from langchain.schema.runnable import RunnablePassthrough
# from langchain.text_splitter import MarkdownHeaderTextSplitter
# from langchain.vectorstores.azuresearch import AzureSearch
# import openai

# openai.api_key = os.getenv("OPENAI_KEY")
# openai.azure_endpoint = os.getenv("OPENAI_ENDPOINT")
# document_intelligence_key = os.getenv("DOCUMENT_INTELLIGENCE_KEY")
# document_intelligence_endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")
# vector_store_address: str = os.getenv("AI_SEARCH_ENDPOINT")
# vector_store_password: str = os.getenv("AI_SEARCH_ADMIN_KEY")

# document_analysis_client = DocumentAnalysisClient(
#     credential=AzureKeyCredential(document_intelligence_key),
#     endpoint=document_intelligence_endpoint,
# )


# def document_intelligence(file_url):

#     headers_to_split_on = [
#         ("#", "Header 1"),
#         ("##", "Header 2"),
#         ("###", "Header 3"),
#     ]

#     loader = AzureAIDocumentIntelligenceLoader(
#         file_path=file_url,
#         api_key=document_intelligence_key,
#         api_endpoint=document_intelligence_endpoint,
#         api_model="prebuilt-layout",
#     )

#     aoai_embeddings = AzureOpenAIEmbeddings(
#         azure_deployment="text-embedding-ada-002",
#         openai_api_version="2023-05-15",
#         api_key=openai.api_key,
#         azure_endpoint=openai.azure_endpoint,
#     )

#     index_name: str = "idx-rag-dev"
#     vector_store: AzureSearch = AzureSearch(
#         azure_search_endpoint=vector_store_address,
#         azure_search_key=vector_store_password,
#         index_name=index_name,
#         embedding_function=aoai_embeddings.embed_query,
#     )

    
#     docs = loader.load()
#     text_splitter = MarkdownHeaderTextSplitter(
#         headers_to_split_on=headers_to_split_on
#     )
#     docs_string = "\n\n".join(doc.page_content for doc in docs)
#     splits = text_splitter.split_text(docs_string)
#     print("Length of splits: " + str(len(splits)))

#     for split in splits:
#         print(f"\n\n{split}\n\n")

#     # vector_store.add_documents(documents=splits)

#     retriever = vector_store.as_retriever(search_type="similarity")
#     retrieved_docs = retriever.get_relevant_documents("仮条件の決定について教えて。")

#     prompt = hub.pull("rlm/rag-prompt")

#     llm = AzureChatOpenAI(
#         openai_api_version="2023-05-15",
#         azure_deployment="gpt-35-turbo",
#         temperature=0,
#         api_key=openai.api_key,
#         azure_endpoint=openai.azure_endpoint,
#     )


#     rag_chain = (
#         {"context": retriever | retrieved_docs, "question": RunnablePassthrough()}
#         | prompt
#         | llm
#         | StrOutputParser()
#     )
#     rag_chain.invoke("テキストを抽出してください。")
