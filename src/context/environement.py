import os

ROOT_DIR_VAR_NAME = "TASKHOME"
ROOT_DIR_NAME = '.tasks'


def get_root_path():
    path = os.environ.get(ROOT_DIR_VAR_NAME)
    if not path:
        path = os.path.join(os.environ.get("HOME"), ROOT_DIR_NAME)
    return path


def create_root_dir():
    """
    Create the dir that will contains all the data
    for the app to run and be persistent
    :return:
    """
    root_path = get_root_path()
    os.makedirs(root_path, exist_ok=True)
