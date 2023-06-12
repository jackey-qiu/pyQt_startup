from pathlib import Path
import yaml
import logging
import logging.config

def load_config():
    with open(str(Path(__file__).parent.parent.parent/ "res" / "config" / "log.yaml"), 'r') as f:
        config = yaml.safe_load(f.read())
        #print(logging.config)
        logging.config.dictConfig(config)

class InfoFilter(logging.Filter):
    """
    Simple Filter class
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def filter(self, record):
        """
        Return Log Record Object based on condition - Return only info logs
        :param record: Log Record Object
        :return: Log Record Object
        """
        return True
        #raise NotImplementedError