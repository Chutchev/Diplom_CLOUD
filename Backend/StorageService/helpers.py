import os


def delete_file(filepath, filename):
    os.remove(os.path.normpath(os.path.join(filepath, filename)))