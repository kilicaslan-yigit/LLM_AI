from llama_cpp import Llama

# Load Llama model
llm = Llama(model_path="./mistral-7b-openorca.Q4_K_M.gguf")

def generate_output(prompt):
    output = llm(
        prompt,
        max_tokens=32,
        stop=["Q:", "\n"],
        echo=False
    )
    return output