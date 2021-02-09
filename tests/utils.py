import os


def fixture_path(file_path):
    return os.path.abspath(os.path.join(__file__, '..', 'resources', file_path))