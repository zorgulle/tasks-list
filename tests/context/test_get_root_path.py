import os

from src.context.environement import get_root_path, ROOT_DIR_VAR_NAME, ROOT_DIR_NAME


def test_get_root_path():
    assert get_root_path() == os.path.join(os.environ.get("HOME"), ROOT_DIR_NAME)


def test_get_root_path_with_var():
    path = "/tmp/toto/" + ROOT_DIR_NAME
    os.environ[ROOT_DIR_VAR_NAME] = path
    assert get_root_path() == path
    del os.environ[ROOT_DIR_VAR_NAME]