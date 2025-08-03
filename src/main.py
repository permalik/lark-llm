"""
main
"""

from events import consumer


def main():
    print("Starting lark-llm..")
    consumer.inference_request()


if __name__ == "__main__":
    main()
