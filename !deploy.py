import argparse
import os
import re
import subprocess
import sys
import time


if __name__ == "__main__":

    # from client_config import ClientConfig
    # APP_VERSION = ClientConfig.APP_VERSION
    #
    # major, minor, patch, channel, release = APP_VERSION.split('.')

    major = input("major: ")
    minor = input("minor: ")
    patch = input("patch: ")
    channel = input("channel: ")
    release = input("release: ")

    client_write = f'''class ClientConfig(object):
    PUBLIC_KEY = 'gp4xou4FKWdJGoiMHaXH5EMSG7qafZtPqCnLJ0DRxZU'
    APP_NAME = 'ThunderTac'
    APP_VERSION = '{major}.{minor}.{patch}.{channel}.{release}'
    COMPANY_NAME = 'WarThunderApps'
    HTTP_TIMEOUT = 30
    MAX_DOWNLOAD_RETRIES = 3
    UPDATE_URLS = ['https://update.tacserv.tk/files/']'''

    with open('client_config.py', 'w') as f:
        f.write(client_write)


    if channel == "0":
        channel = "a"
    elif channel == "1":
        channel = "b"
    elif channel == "2":
        channel = ""
    else:
        sys.exit(1)

    APP_VERSION = f"{major}.{minor}.{patch}{channel}"

    return_build = os.system(f'pyupdater build --app-version={APP_VERSION} --pyinstaller-log-info win.spec')
    return_pypkg = os.system('pyupdater pkg --process')
    return_pyign = os.system('pyupdater pkg --sign')
    return_pyupl = os.system('pyupdater upload --service scp')

if return_build == return_pypkg == return_pyign == return_pyupl == 0:
    print('all good')

