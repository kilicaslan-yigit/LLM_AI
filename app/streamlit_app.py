import streamlit as st
from llm_script import generate_output
import requests

def search_elastiscsearch(index, query):
    url = f"http://elasticsearch:9200/{index}/_search?q={query}"
    response = requests.get(url)
    return response.json()

def shorten_string(input_string):
    max_length = 255
    if len(input_string) <= max_length:
        return input_string
    else:
        return input_string[:max_length]

def main():
    st.title("Llama Streamlit Demo")

    # Get user input
    prompt = st.text_input("Enter your question:")

    if st.button("Generate Answer"):
        if prompt:
            # Search Elasticsearch for the given question
            es_result = search_elastiscsearch(index="attention_is_all_you_need", query=prompt)

            if es_result['hits']['total']['value'] > 0:
                # Extract the document content from the first hit
                document_content = es_result['hits']['hits'][0]['_source']['content']

                # Generate output using Llama model
                output = generate_output("Q: " + prompt + " A:"+ shorten_string(document_content))
                st.markdown(f"**Answer:** {output['choices'][0]['text']}")
            else:
                st.warning("No matching documents found in Elasticsearch.")
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
