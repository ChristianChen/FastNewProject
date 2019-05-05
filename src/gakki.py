import os
from enum import IntEnum


class GakkiType(IntEnum):
    java = 1


class Gakki:

    def __init__(self, project_name, project_type: GakkiType = GakkiType.java):
        if project_name is None:
            raise RuntimeError('Project_name is mandatory!')
        self.project_name = project_name
        self.project_type = project_type

    def create_project(self):
        os.makedirs(self.project_name)


def gakki(gakki_args: Gakki = None):
    if gakki_args is None:
        return dict(code=-1, msg='''Usage:
gakki project_name <java|python|node> [optional libraries]''')

    gakki_args.create_project()
    return dict(code=0, msg='Created %s project[%s] successfully.' % (gakki_args.project_type, gakki_args.project_name))
