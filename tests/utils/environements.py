from src.context.environement import ROOT_DIR_VAR_NAME
import os

ROOT_PATH = "/tmp/toto"


def set_env_var():
    os.environ[ROOT_DIR_VAR_NAME] = ROOT_PATH


def unset_env_var():
    del os.environ[ROOT_DIR_VAR_NAME]


def set_env(func):
    def wrapper(*args, **kwargs):
        set_env_var()
        r = func(*args, **kwargs)
        unset_env_var()
        return r
    return wrapper