from os import path

def getRealPathRelativeToFile(file: str, joinPath: str):
    """
    根据文件路径获取相对于文件的绝对路径
    """
    fileDir = path.dirname(file)
    filePath = path.realpath(fileDir)
    return path.join(filePath, joinPath)