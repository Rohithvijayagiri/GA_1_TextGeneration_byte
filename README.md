# GA_1_TextGeneration_byte

## AVIP 2026 — Generative AI Task 1: Text Generation

This project demonstrates text generation using a hosted GPT-5+ class model. It contains 20 diverse prompts, the resulting generated samples, model/source documentation, an inference example, and a concise qualitative evaluation.

### Model
- Generation context: OpenAI GPT-5.6 Luna (hosted ChatGPT model), September 2026.
- OpenAI: https://openai.com/
- For API-based reproduction, use the current official OpenAI API documentation and an API model available to your account.
- Never place an API key directly in source code.

### Repository structure

```text
GA_1_TextGeneration_byte/
├── README.md
├── prompts.txt
├── generated_samples/
│   ├── sample_01.txt
│   └── ...
├── inference.py
├── evaluation_summary.md
└── corpus/
    └── generation_context.txt
```

### Reproduction with an API

Set the environment variable `OPENAI_API_KEY`, then run:

```bash
python inference.py --prompt "Explain the Internet of Things in simple terms."
```

The script is an example and uses the current API SDK. Check the official documentation for the exact model name and SDK syntax available to your account.

### Safety
Prompts were designed to avoid copyrighted text requests, personal data, and sensitive instructions. The evaluation focuses on coherence, relevance, instruction following, and common failure modes.

### License / source
OpenAI: https://openai.com/
