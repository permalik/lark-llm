"""
main
"""

from events import consumer
from utilities import lg


def main():
    lg.logger.info("Starting lark-llm..")
    consumer.inference_request()


if __name__ == "__main__":
    main()
