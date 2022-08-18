import socket
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'some_secret_key'
DATABASE = basedir + "/"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(DATABASE, 'database.db')
SERVER_URL = 'https://cargo.win'
STEAM_API_KEY = '4D68245A82B5ACC74BD1068378A09AAD'
SQLALCHEMY_TRACK_MODIFICATIONS = True
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LctrIMhAAAAAKPG3dqPPLsiNPobQCJeD_JtpsV-'
RECAPTCHA_PRIVATE_KEY = '6LctrIMhAAAAAFcOhIVOeOwVpTvN-P6FGZCuGmQo'
RECAPTCHA_OPTIONS = {'theme': 'dark'}
SCHEDULER_JOBSTORES = {"default": SQLAlchemyJobStore(url="sqlite:///" + os.path.join(DATABASE, 'jobstore.db'))}
SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 20}}
SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 3}
SCHEDULER_API_ENABLED = False
FTP_PORT = 2121
FTP_DIRECTORY = r"within static folder with folder name 'demos'"
IP = socket.gethostbyname(SERVER_URL.replace("https://", "").replace("http://", "").replace("/", ""))
