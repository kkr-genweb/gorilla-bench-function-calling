from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "gorilla-llm/gorilla-openfunctions-v2",
    torch_dtype=torch.float16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("gorilla-llm/gorilla-openfunctions-v2")

def chat_with_functions(prompt: str, functions: list):
    # Merge prompt with function JSON in system instruction
    import json
    system = "You are Gorilla OpenFunctions, answer using function calls only."
    func_json = json.dumps(functions)
    full_prompt = f"{system}\n<<function>>{func_json}\n<<question>>{prompt}\n"
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    out = model.generate(**inputs, max_new_tokens=256)
    response = tokenizer.decode(out[0], skip_special_tokens=True)
    return response

# Use chat_with_functions same way
# Example usage:
functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City, state"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
]

resp = chat_with_functions(
    "What's the weather like in Boston and San Francisco?",
    functions=functions,
)

print(resp)