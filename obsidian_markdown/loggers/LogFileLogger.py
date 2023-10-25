from LoggerInnterface import iLogger
from datetime import datetime

class LogFileLogger(iLogger):
    def __init__(self, format = '{datetime};[{level}];{message}', folder = 'logs', file = 'logs{date}.log'):
        """Logger that just prints the info"""
        date = datetime.now().strftime('%Y%m%d')
        self.path = folder + '/'+ file.format(date = date)
        self.format = format


    def info(self, message: str):
        level = 'INFO'
        with open(self.path, 'a') as f:
            f.write(self._formatted_string(level = level, message = message))

    def error(self, message: str):
        level = 'ERROR'
        with open(self.path, 'a') as f:
            f.write(self._formatted_string(level = level, message = message))

    def debug(self, message: str):
        level = 'DEBUG'
        with open(self.path, 'a') as f:
            f.write(self._formatted_string(level = level, message = message))

    def _formatted_string(self, level: str, message: str)-> str:
        return self.format.format(
            message = message,
            level = level,
            datetime = datetime.now()
        ) + '\n'