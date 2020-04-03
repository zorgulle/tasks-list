from src.context.environement import create_root_dir, get_root_path
from tests.utils.environements import set_env, ROOT_PATH
import os


@set_env
def test_create_root_dir():

    if os.path.isdir(get_root_path()):
        os.removedirs(ROOT_PATH)

    create_root_dir()

    if os.path.isdir(ROOT_PATH):
        assert True
        os.removedirs(ROOT_PATH)
    else:
        assert False