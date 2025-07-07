"""
main
"""

from ollama import chat

stream = chat(
    model="gemma2:2b",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?",
        }
    ],
    stream=True,
)


def main():
    print("Starting llm..")
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)


if __name__ == "__main__":
    main()
