# import os
# import tempfile
# from azure.ai.formrecognizer import DocumentAnalysisClient
# from azure.core.credentials import AzureKeyCredential
# from io import BytesIO
# from langchain import hub
# from langchain_openai import AzureChatOpenAI
# from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader
# from langchain_openai import AzureOpenAIEmbeddings
# from langchain.schema import StrOutputParser
# from langchain.schema.runnable import RunnablePassthrough
# from langchain.text_splitter import MarkdownHeaderTextSplitter
# from langchain.vectorstores.azuresearch import AzureSearch
# import ipdb

# openai_key = os.getenv("OPENAI_KEY")
# openai_endpoint = os.getenv("OPENAI_ENDPOINT")
# document_intelligence_key = os.getenv("DOCUMENT_INTELLIGENCE_KEY")
# document_intelligence_endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")

# document_analysis_client = DocumentAnalysisClient(
#     credential=AzureKeyCredential(document_intelligence_key),
#     endpoint=document_intelligence_endpoint,
# )


# def pdf_processor(blob_data):
#     blob_data = BytesIO(blob_data)

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
#         temp_file.write(blob_data.read())
#         temp_file_path = temp_file.name

#     headers_to_split_on = [
#             ("#", "Header 1"),
#             ("##", "Header 2"),
#             ("###", "Header 3"),
#         ]

#     try:
#         loader = AzureAIDocumentIntelligenceLoader(
#             file_path=temp_file_path,
#             api_key=document_intelligence_key,
#             api_endpoint=document_intelligence_endpoint,
#             api_model="prebuilt-layout",
#             mode="markdown"
#         )
        
#         docs = loader.load()
#         text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

#         docs_string = docs[0].page_content
#         splits = text_splitter.split_text(docs_string)
#         # ipdb.set_trace()
        
#         extracted_text = ""
#         for doc in docs:
#             docs_string = doc.page_content
#             splits = text_splitter.split_text(docs_string)
            
#             for split in splits:
#                 if 'Header 1' in split.metadata:
#                     extracted_text += split.metadata['Header 1'] + "\n"
#                 if 'Header 2' in split.metadata:
#                     extracted_text += split.metadata['Header 2'] + "\n"
#                 if 'Header 3' in split.metadata:
#                     extracted_text += split.metadata['Header 3'] + "\n"
                
#                 extracted_text += split.page_content + "\n\n"

#         return extracted_text.strip()
#     finally:
#         os.remove(temp_file_path)
