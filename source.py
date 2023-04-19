import os, shutil

DL_PATH = f'/home/{os.getlogin()}/Downloads'
HOME = f'/home/{os.getlogin()}/'
PATHS = [
    {
        "ext": ['png', 'jpg', 'svg', 'jpeg', 'gif', 'webmp'],
        "path": HOME + 'Pictures/Downloads'
    },
    {
        "ext": ['pdf', 'odt', 'ods', 'odp', 'odg', 'docm', 'docx', 'ppt', 'pptx', 'xlsx', 'doc'],
        "path": HOME + 'Documents/Downloads'
    },
    {
        "ext": ['mp3', 'm4a', 'ogg', 'wav'],
        "path": HOME + 'Music/Downloads'
    },
    {
        "ext": ['webm', '3g2', '3gp', 'mkv', 'mp4', 'mov', 'avi', 'wmv'],
        "path": HOME + 'Videos/Downloads'
    },
    {
        "ext": ['webm', '3g2', '3gp', 'mkv', 'mp4', 'mov', 'avi', 'wmv'],
        "path": HOME + 'Videos/Downloads'
    },
    {
        "ext": ['deb', 'rpm', 'bin'],
        "path": HOME + 'Apps'
    },
    {
        "ext": ['iso', 'tar', 'gz', '7z', 'tar.gz'],
        "path": HOME + 'Compressed'
    }

]

def app():
    files = os.listdir(DL_PATH)
    if len(files) > 0:
        for file in files:
            if os.path.isfile(DL_PATH + '/' + file):
                print(file)
                ext = get_file_extension(file)
                target = False
                for path in PATHS:
                    if ext in path["ext"]:
                        target =  path["path"]
                fabspath = DL_PATH + "/"+file
                # print(fabspath)
                if target:
                    if os.path.isdir(target):
                        shutil.move(fabspath, target + "/" + file)
                    else:
                        os.mkdir(target)
                        shutil.move(fabspath, target + "/" + file)
                else:
                    if os.path.isdir(HOME + "MISCs"):
                        shutil.move(fabspath, HOME + "MISCs")
                    else:
                        os.mkdir(HOME + "MISCs")
                        shutil.move(fabspath, HOME + "MISCs")


def get_file_extension(filename):
    ext = os.path.splitext(filename)
    return ext[1][1:]


def __main__():
    app()

if __name__ == "__main__":
    __main__()