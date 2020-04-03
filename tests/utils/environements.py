from src.context.environement import ROOT_DIR_VAR_NAME
import os
import shutil
import logging
logger = logging.getLogger(__file__)


ROOT_PATH = "/tmp/toto"


def set_env_var():
    os.environ[ROOT_DIR_VAR_NAME] = ROOT_PATH


def unset_env_var():
    del os.environ[ROOT_DIR_VAR_NAME]


def set_env(func):
    def wrapper(*args, **kwargs):
        setup_env()
        r = func(*args, **kwargs)
        clean_env()
        return r
    return wrapper

def clean_dir():
    try:
        shutil.rmtree(ROOT_PATH)
    except:
        logger.warning("Fail to remove %s", ROOT_PATH)

def clean_env():
    unset_env_var()
    clean_dir()

def setup_env():
    set_env_var()
    clean_dir()
