from ollama import ChatResponse, chat


def generate_response(role, content):
    response: ChatResponse = chat(
        model="gemma2:2b",
        messages=[
            {
                "role": role,
                "content": content,
            }
        ],
    )

    return response
