class Format:
    @staticmethod
    def underline(text):
        return f"\033[4m{text}\033[0m"

    @staticmethod
    def bold(text):
        return f"\033[1m{text}\033[0m"

    @staticmethod
    def italic(text):
        return f"\033[3m{text}\033[0m"