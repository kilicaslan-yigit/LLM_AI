import PyPDF2
from elasticsearch import Elasticsearch

def index_pdf_content(es, index_name, pdf_path):
    # Create an Elasticsearch index if it doesn't exist
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)

    # Read PDF content
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        total_pages = pdf_reader.numPages
        pdf_content = ""

        # Extract text from each page
        for page_number in range(total_pages):
            page = pdf_reader.getPage(page_number)
            pdf_content += page.extractText()

    # Index the PDF content into Elasticsearch
    doc = {
        'content': pdf_content,
        'file_path': pdf_path
    }
    es.index(index=index_name, body=doc)

if __name__ == "__main__":
    # Specify Elasticsearch settings
    es_host = 'localhost'
    es_port = 9200
    index_name = 'attention_is_all_you_need'

    # Specify the path to your PDF file
    pdf_path = 'attention_is_all_you_need.pdf'

    # Connect to Elasticsearch
    es = Elasticsearch([{'host': es_host, 'port': es_port}])

    # Index the PDF content
    index_pdf_content(es, index_name, pdf_path)

    print(f"PDF content indexed successfully into '{index_name}' index.")
