class StringUtils:
    def __init__(self):
        pass

    def capitalize(self, string):
        if not isinstance(string, str):
            raise TypeError("Input must be a string")
        return string.capitalize()

    def upper(self, string):
        if not isinstance(string, str):
            raise TypeError("Input must be a string")
        return string.upper()

    def join(self, strings, delimiter):
        if not all(isinstance(s, str) for s in strings):
            raise TypeError("All elements must be strings")
        return delimiter.join(strings)

    def split(self, string, delimiter=" "):
        if not isinstance(string, str):
            raise TypeError("Input must be a string")
        return string.split(delimiter)
