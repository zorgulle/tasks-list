from src.context.environement import get_root_path, create_today_dir, DATE_FORMAT
from tests.utils.environements import set_env
from datetime import datetime

import os

@set_env
def test_create_today_date_dir():
    create_today_dir()


    current_date = datetime.today().strftime(DATE_FORMAT)
    path = os.path.join(get_root_path(), current_date)

    assert os.path.isdir(path)
