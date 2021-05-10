import uuid


def randomFileName(ending: str):
    """
    :ending: Расширение файла
    :return: Случайное название файла
    """

    filename = str(uuid.uuid4())
    filename += ending
    return filename
