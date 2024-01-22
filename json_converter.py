from entity.history import History
from entity.container import Container
from entity.file import File
from entity.folder import Folder

import json


def container_to_json(filepath: str,
                      container: Container):
    j_obj = {"file": {"history": {}}, "folder": {}}
    j_obj["folder"]["folder_id"] = container.folder.id
    j_obj["folder"]["folder_name"] = container.folder.name
    if container.file:
        j_obj["file"]["folder_id"] = container.folder.id
        j_obj["file"]["file_id"] = container.file.id
        j_obj["file"]["file_name"] = container.file.name
        j_obj["file"]["file_tag"] = container.file.tag
        j_obj["file"]["file_date"] = container.file.date
    if container.history:
        j_obj["file"]["history"]["name"] = container.history.name
        j_obj["file"]["history"]["surname"] = container.history.surname
        j_obj["file"]["history"]["patronymic"] = container.history.patronymic
        j_obj["file"]["history"]["age"] = container.history.age
        j_obj["file"]["history"]["height"] = container.history.height
        j_obj["file"]["history"]["weight"] = container.history.weight
        j_obj["file"]["history"]["date"] = container.history.date
        j_obj["file"]["history"]["live_address"] = container.history.live_address
        j_obj["file"]["history"]["job"] = container.history.job
        j_obj["file"]["history"]["doctor_name"] = container.history.doctor_name
        j_obj["file"]["history"]["doctor_surname"] = container.history.doctor_surname
        j_obj["file"]["history"]["doctor_patronymic"] = container.history.doctor_patronymic
        j_obj["file"]["history"]["address"] = container.history.address
        j_obj["file"]["history"]["diagnosis"] = container.history.diagnosis
        j_obj["file"]["history"]["info"] = container.history.info
        j_obj["file"]["history"]["text"] = container.history.text

    j_obj = json.dumps(j_obj, indent=4, ensure_ascii=False)
    with open(filepath, mode="w", encoding="UTF-8") as file:
        file.write(j_obj)


def json_to_container(path: str) -> Container:
    with open(path, mode="r", encoding="UTF-8") as file:
        data = json.load(file)
        history_data = data["file"]["history"]
        file_data = data["file"]
        folder_data = data["folder"]
        hist = None
        fil = None
        fol = None

        if len(list(history_data.keys())) > 0:
            hist = History(name=history_data["name"],
                           surname=history_data["surname"],
                           patronymic=history_data["patronymic"],
                           age=history_data["age"],
                           height=history_data["height"],
                           weight=history_data["weight"],
                           date=history_data["date"],
                           live_address=history_data["live_address"],
                           job=history_data["job"],
                           doctor_name=history_data["doctor_name"],
                           doctor_surname=history_data["doctor_surname"],
                           doctor_patronymic=history_data["doctor_patronymic"],
                           address=history_data["address"],
                           diagnosis=history_data["diagnosis"],
                           info=history_data["info"],
                           text=history_data["text"])

        if len(list(file_data.keys())) > 1:
            fil = File(id=file_data["file_id"],
                       name=file_data["file_name"],
                       tag=file_data["file_tag"],
                       date=file_data["file_date"])

        if len(list(folder_data.keys())) > 0:
            fol = Folder(id=folder_data["folder_id"],
                         name=folder_data["folder_name"])

        cont = Container(file=fil,
                         folder=fol,
                         hist=hist)

        return cont


if __name__ == '__main__':
    cont = json_to_container("memory/file_0.json")
    container_to_json("memory/test_0.json", cont)