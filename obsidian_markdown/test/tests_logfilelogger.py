import sys
from pathlib import Path

sys.path.append('./obsidian_markdown')
sys.path.append('./obsidian_markdown/loggers')

#Setup Logger
from loggers.PrintLogger import PrintLogger
Logger = PrintLogger()

from loggers.LogFileLogger import LogFileLogger


def main():
    test_info()
    test_date_logger()

def test_info():
    FileLogger = LogFileLogger(folder = './obsidian_markdown/test/results')
    FileLogger.info('Test')

def test_date_logger():
    FileLogger = LogFileLogger(folder = './obsidian_markdown/test/results', file = '{date}.log')
    FileLogger.info('Test date logger')

if __name__ == '__main__':
    main()