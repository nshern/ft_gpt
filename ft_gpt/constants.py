import os

FILE_DIR = os.path.dirname(__file__)
PERSIST_DIR = f"{FILE_DIR}/../storage"
DATA_DIR = f"{os.path.dirname(FILE_DIR)}/data/"
DATA_DIR_TEXT = f"{os.path.dirname(FILE_DIR)}/data/text/"
DATA_DIR_XML = f"{os.path.dirname(FILE_DIR)}/data/xml/"
DATA_DIR_XML_RAW = f"{os.path.dirname(FILE_DIR)}/data/xml/raw/"
DATA_DIR_XML_PARSED = f"{os.path.dirname(FILE_DIR)}/data/xml/parsed/"
