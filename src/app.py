import os
import enum
import datetime
import uuid


PATH_VAR = 'TASKS_DIR'
ROOT_PATH = os.environ.get(PATH_VAR)
DATE_FORMAT = "%Y-%m-%d"


class Status(enum.Enum):
    TODO = 1
    IN_PROGRESS = 2
    BLOCKED = 3
    DONE = 4


def get_date_path(date):
    formatted_date = date.strftime(DATE_FORMAT)
    return os.path.join(ROOT_PATH, formatted_date)


def get_status_path(date, status):
    return os.path.join(get_date_path(date), status.name)


def create_status_folder(date):
    for status in Status:
        path = get_status_path(date, status)
        os.makedirs(path, exist_ok=True)


def init():
    date = today()
    create_status_folder(date)

def today():
    return datetime.datetime.today()

import json
class Task:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.label = kwargs.get("label")
        self.description = kwargs.get("description")

    def to_json(self):
        d = {"id": self.id, "label": self.label, "description": self.description}
        return json.dumps(d)

    def __str__(self):
        return "%s > %s > %s" % (self.id, self.label, self.description)


def create_task(label, description):
    task = Task(label=label, description=description)
    date = today()
    filename = '%s.json' % task.id
    status_path = get_status_path(date, Status.TODO)
    file_path = os.path.join(status_path, filename)
    with open(file_path, 'w') as f:
        f.write(task.to_json())


def create():
    label = input("Label: ")
    description = input("Description: ")
    create_task(label, description)


def task_from_file(path):
    with open(path, "r") as f:
        json_task = json.load(f)
    return Task(**json_task)


def list_tasks():
    for s in Status:
        status_path = get_status_path(today(), s)
        files = os.listdir(status_path)

        print("%s" % s.name)
        print("===============")

        for file in files:
            file_path = os.path.join(status_path, file)
            task = task_from_file(file_path)
            print(task)


def yesterday():
    return today() - datetime.timedelta(days=1)

def check_env():
    if not ROOT_PATH:
        raise Exception("%s is empty" %  PATH_VAR)



def dummy_method(*args, **kwargs):
    pass


if __name__ == '__main__':
    #TODO: Do the task copying from day to day
    check_env()

    from argparse import ArgumentParser
    parser = ArgumentParser()

    cmd_mapper = {
        "init": init,
        "create": create,
        "list": list_tasks
    }

    parser.add_argument("cmd", type=str, choices=cmd_mapper.keys())
    args = parser.parse_args()

    cmd_mapper.get(args.cmd, dummy_method)()
