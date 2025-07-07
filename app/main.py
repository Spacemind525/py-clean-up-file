import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> str:
        return self

    def __exit__(self,a,b,c) -> None:
        try:
            if self.filename:
                os.remove(self.filename)
        except FileNotFoundError:
            pass
