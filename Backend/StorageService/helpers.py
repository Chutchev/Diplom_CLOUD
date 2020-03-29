import hashlib

def read_hash(filename):
    with open(filename, 'rb') as f:
        hash_md5 = hashlib.md5()
        image = f.read(65536)
        hash_md5.update(image)
        return hash_md5.hexdigest()