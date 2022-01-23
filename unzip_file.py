import zipfile
import os


def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir.encode('cp437').decode('gbk')):
        os.mkdir(unziptodir.encode('cp437').decode('gbk'), 0o777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\', '/')
        if name.endswith('/'):
            _dir = os.path.join(unziptodir, name).encode('cp437').decode('gbk')
            if not os.path.exists(_dir):
                os.mkdir(_dir)
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir):
                os.mkdir(ext_dir.encode('cp437').decode('gbk'), 0o777)
            outfile = open(ext_filename.encode('cp437').decode('gbk'), 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


if __name__ == '__main__':
    unzip_file("rfe.zip", "./")
