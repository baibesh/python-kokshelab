from abc import ABC, abstractmethod


class TextFormatter(ABC):

    @abstractmethod
    def format(text: str):
        raise NotImplementedError


class UppercaseFormatter(TextFormatter):

    @staticmethod
    def format(text: str) -> str:
        return text.upper()


class LowercaseFormatter(TextFormatter):

    @staticmethod
    def format(text: str) -> str:
        return text.lower()


uppercase_formatter = UppercaseFormatter()
print(uppercase_formatter.format("asjdnakjsnddakjs"))

lowercase_formatter = LowercaseFormatter()
print(lowercase_formatter.format("AKSNNDAJSKNDKAJSNKA"))
