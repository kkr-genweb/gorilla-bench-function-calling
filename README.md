# **🦍 Gorilla OpenFunctions V2 — Local Function Calling Example**

This repository shows how to run the [**gorilla-llm/gorilla-openfunctions-v2**](https://huggingface.co/gorilla-llm/gorilla-openfunctions-v2) model locally using 🤗 Transformers. It demonstrates how to supply structured function definitions and get the model to return function calls as output.

---
## **📦 Requirements**
- [transformers](https://pypi.org/project/transformers/)
- [torch](https://pytorch.org/)
Install dependencies:
```
uv sync
```
## **⚡ How it works**
- The model receives a **system instruction** telling it to use function calls only.
- You pass in your function definitions as JSON.
- You ask a natural language question.
- The model returns a **structured function call** (in text) you can parse and execute.

```
 % uv run main.py
Loading checkpoint shards:   ...
Setting `pad_token_id` to `eos_token_id`:100015 for open-end generation.

You are Gorilla OpenFunctions, answer using function calls only.
<<function>>[{"name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": {"type": "object", "properties": {"location": {"type": "string", "description": "City, state"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}}, "required": ["location"]}}]

<<question>>What's the weather like in Boston and San Francisco?

<<function>>get_current_weather(location='Boston')<<function>>get_current_weather(location='San Francisco')
```

## **✅ Notes**
- This example runs the model locally. For a **hosted endpoint**, you can use the Berkeley OpenFunctions API [instructions from their website](https://gorilla.cs.berkeley.edu/blogs/7_open_functions_v2.html).
- Works well with quantized models (GGUF) too if you prefer llama.cpp.
## **📚 References**
- 🤗 [Gorilla OpenFunctions V2 Model Card](https://huggingface.co/gorilla-llm/gorilla-openfunctions-v2)
- 📝 [Gorilla Paper](https://arxiv.org/abs/2305.15334)

### Requirements (From talk given by Shishir Patil last year, see below)
1. API choice: should we use Stripe, or Wells Fargo, or something else
2. Syntax translation: how to call the API to avoid a stack trace error
3. Argument extraction: provide the right parameters for the API

### Direction taken by Gorilla (Finetuning)
- [Fine tune a model for api and function calling](https://youtube.com/clip/UgkxqNG_-w-fO-YHzDl-0589Jx4eR0yPp_Yh?si=2dAaPFUNH--6peVi)

### Direction taken by Others (Prompt-loading, RAG)
- Prompt loading (include api spec in prompt, doesn't scale)
- RAG across functions (can scale, and potentially more timely, but may not be as accurate as fine tuning approach)

### Tips
- APIs are changing frequently, so don't forget that latest version is key and not stale
- Consider retrieval aware fine tuning as a way to do this -- if you are doing RAG, do RAFT (optimize for particular type of open book exam; double digit percent improvements possible)
