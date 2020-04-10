import string
import hashlib
import random


def generate_url(lenght=15):
    return ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(lenght)])


def md5_hash(filepath):
        with open(filepath, 'rb') as f:
            hash_md5 = hashlib.md5()
            image = f.read(65536)
            hash_md5.update(image)
            return hash_md5.hexdigest()