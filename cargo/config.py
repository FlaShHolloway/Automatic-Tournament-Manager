import socket
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import os

SECRET_KEY = 'THISISKYEY'
DATABASE = r"/root/cargowin/"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE + 'database.db&apos'
SERVER_URL = 'cargowin.herokuapp.com'
STEAM_API_KEY = '4D68245A82B5ACC74BD1068378A09AAD'
SQLALCHEMY_TRACK_MODIFICATIONS = True
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LctrIMhAAAAAKPG3dqPPLsiNPobQCJeD_JtpsV-'
RECAPTCHA_PRIVATE_KEY = '6LctrIMhAAAAAFcOhIVOeOwVpTvN-P6FGZCuGmQo'
RECAPTCHA_OPTIONS = {'theme': 'dark'}
SCHEDULER_JOBSTORES = {"default": SQLAlchemyJobStore(url="sqlite:///" + os.path.join(DATABASE, 'jobstore.db&apos'))}
SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 20}}
SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 3}
SCHEDULER_API_ENABLED = False
FTP_PORT = 2121
FTP_DIRECTORY = r"within static folder with folder name 'demos'"
IP = socket.gethostbyname(SERVER_URL.replace("https://", "").replace("https://", "").replace("/", ""))
