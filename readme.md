# LLM_AI Project

## Overview

This project is a language model-based application that leverages Elasticsearch for document indexing and a Streamlit web application for user interaction for creating a conversational AI system capable of discussing and extracting information from a specific research paper, in this case the paper is "Attention Is All You Need" 

## Setup Instructions

### Virtual Environment

1. Navigate to the `elasticserach` directory:

    ```bash
    cd elasticserach
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```
4. Run the Elasticsearch indexing script:

    ```bash
    python index_pdf_to_elasticserach.py
    ```


### Application Setup

1. Navigate to the root directory:

    ```bash
    cd LLM_AI
    ```

2. Build the Docker containers:

    ```bash
    docker-compose build
    ```

3. Start the Docker containers:

    ```bash
    docker-compose up
    ```

4. Access the Streamlit app at [http://localhost:8501](http://localhost:8501).
