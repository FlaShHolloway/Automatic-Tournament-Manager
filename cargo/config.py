import socket
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import os

SECRET_KEY = 'THISISKYEY'
DATABASE = r"admin:613Jio613@cargoreginfo.c9je3iddxfzn.ap-south-1.rds.amazonaws.com/"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + DATABASE + 'jobdone'
SERVER_URL = 'http://cargo.win'
STEAM_API_KEY = '4D68245A82B5ACC74BD1068378A09AAD'
SQLALCHEMY_TRACK_MODIFICATIONS = True
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LcJpoMhAAAAABHQI2BXtXrVC_fcnyV0S0EQmbpw'
RECAPTCHA_PRIVATE_KEY = '6LcJpoMhAAAAAJbCwyNBDmmJ5GcWdr5G6qiDyXCk'
RECAPTCHA_OPTIONS = {'theme': 'dark'}
SCHEDULER_JOBSTORES = {"default": SQLAlchemyJobStore(url="mysql+pymysql://" + os.path.join(DATABASE, 'jobstore'))}
SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 20}}
SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 3}
SCHEDULER_API_ENABLED = False
FTP_PORT = 2121
FTP_DIRECTORY = r"within static folder with folder name 'demos'"
IP = socket.gethostbyname(SERVER_URL.replace("http://", "").replace("http://", "").replace("/", ""))
