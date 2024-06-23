from typing import Any, Optional

import openai

from uaf.enums.file_paths import FilePaths
from uaf.utilities.parser.yaml_parser_utils import YamlParser

config = YamlParser(FilePaths.COMMON)
openai.api_key = config.get_value("chatgpt", "api_key")
completion = openai.ChatCompletion()


class bot:
    def get_chat_response(
        self,
        question: str,
        chat_log: list[dict[str, Any]] | None = None,
        require_chat_log_output: bool = False,
    ):
        """Provisions users to asks question on trivial or complicated scenarios using chat gpt

        Args:
            message (str): query to be answered
        """
        if chat_log is None:
            chat_log = [
                {
                    "role": "system",
                    "content": "You are a helpful, upbeat and funny assistant.",
                }
            ]
        chat_log.append({"role": "user", "content": question})
        response = completion.create(
            model=config.get_value("chatgpt", "engine"),
            messages=chat_log,
            max_tokens=config.get_value("chatgpt", "max_tokens"),
            temperature=config.get_value("chatgpt", "temperature"),
            n=1,
            stop=None,
        )
        answer = response.choices[0]["message"]["content"]
        chat_log.append({"role": "assistant", "content": answer})
        if require_chat_log_output:
            return answer, chat_log
        return bot.__print_response(answer)

    @staticmethod
    def __print_response(response):
        """Prints response in a formatted way just like web page

        Args:
            response (str): unformatted text
        """
        # Add indentation to each line of the response
        formatted_response = "\n".join(["    " + line for line in response.split("\n")])
        print(formatted_response)
