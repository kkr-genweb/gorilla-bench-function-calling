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
## **✅ Notes**
- This example runs the model locally. For a **hosted endpoint**, you can use the Berkeley OpenFunctions API.
- Works well with quantized models (GGUF) too if you prefer llama.cpp.
## **📚 References**
- 🤗 [Gorilla OpenFunctions V2 Model Card](https://huggingface.co/gorilla-llm/gorilla-openfunctions-v2)
- 📝 [Gorilla Paper](https://arxiv.org/abs/2305.15334)