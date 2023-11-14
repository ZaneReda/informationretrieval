from dotenv import load_dotenv
import pymongo
import os
import json
import time
import logging
import pandas as pd
import data_manager as dm

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='driver_logger.log', filemode='w')
driver_logger = logging.getLogger("driver_logger")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
driver_logger.addHandler(console_handler)

data_importer = dm.DataImporter()
data_exporter = dm.DataExporter()



