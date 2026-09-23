import os
import argparse

def generate(prompt: str) -> str:
    # Example API integration. Install the official OpenAI SDK and set
    # OPENAI_API_KEY before running. Replace MODEL with a model available
    # to your account.
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    model = os.environ.get("OPENAI_MODEL", "gpt-5")
    response = client.responses.create(
        model=model,
        input=prompt,
    )
    return response.output_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    args = parser.parse_args()
    print(generate(args.prompt))
