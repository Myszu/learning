import logging, os

class Logger:
    def __init__(self, name: str, file: str):
        path = "./logs/"
        if not os.path.exists(path):
            os.mkdir(path)
            
        self.name = name
        self.file = f'{path}{file}.log'
        
        
    def create(self) -> logging.Logger:
        self.logger = logging.getLogger(self.name)
        handler = logging.FileHandler(self.file)
        formatter = logging.Formatter(fmt=f'%(asctime)s | %(levelname)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.propagate = False
        return self.logger