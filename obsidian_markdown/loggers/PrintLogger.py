from LoggerInnterface import iLogger

class PrintLogger(iLogger):
    def __init__(self):
        """Logger that just prints the info"""

    def info(self, message: str):
        print(f'[INFO] {message}')

    def error(self, message: str):
        print(f'[ERROR] {message}')

    def debug(self, message: str):
        print("------- DEBUG -------")
        print(message)
        print("------- DEBUG -------")
    