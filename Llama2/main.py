from transformers import AutoTokenizer
import transformers
import torch
#huggingface-cli login

model = "meta-llama/Llama-2-7b-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="cuda",
)

sequences = pipeline(
    'Only respond with OSM Overpass QL code. Write an Overpass QL query equivalent to this natural language question: "What is the population of Central Greece?"\n',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

sequences = pipeline(
    'Convert the sentence: "Where is Liverpool located?" into an Overpass QL query.\n',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")