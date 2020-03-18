import os
import shutil
import pydicom as dicom
import csv

PATHS = {
    "intraparenchymal": os.path.join(os.getcwd(), "intraparenchymal"),
    "intraventricular": os.path.join(os.getcwd(), "intraventricular"),
    "subarachnoid": os.path.join(os.getcwd(), "subarachnoid"),
    "subdural": os.path.join(os.getcwd(), "subdural"),
    "epidural": os.path.join(os.getcwd(), "epidural"),
    "none": os.path.join(os.getcwd(), "none"),
}

NUMBER_OF_FILES = {
    "intraparenchymal": 0,
    "intraventricular": 0,
    "subarachnoid": 0,
    "subdural": 0,
    "epidural": 0,
    "none": 0
}

attributesOfData = []

def fileInspect(csvInfo):
    print("Begin")
    pathToPhotos = os.path.join(os.getcwd(), "stage_1_train_images")
    for info in csvInfo:
        file = os.path.join(os.getcwd(), "stage_1_train_images", info[0])
        if (not os.path.isfile(file)):
            continue
        if (info[2] == "1" and info[1] != "any"):
            if(NUMBER_OF_FILES[info[1]] == 2000):
                continue
            else:
                NUMBER_OF_FILES[info[1]] += 1
                print("{0} {1}".format(info[1], NUMBER_OF_FILES[info[1]]))
                shutil.move(os.path.join(os.getcwd(), "stage_1_train_images", info[0]),
                        os.path.join(os.getcwd(), info[1]))
        if(info[2] == "0" and info[1] == "any"):
            if(NUMBER_OF_FILES["none"] == 2000):
                continue
            else:
                NUMBER_OF_FILES["none"] += 1
                print("{0} {1}".format("none", NUMBER_OF_FILES["none"]))
                shutil.move(os.path.join(os.getcwd(), "stage_1_train_images", info[0]),
                        os.path.join(os.getcwd(), "none"))


def csvExtraction():
    with open("stage_1_train.csv", "r") as csvfs:
        csvReader = csv.reader(csvfs)
        csvReader = list(csvReader)[1:]

        for row in csvReader:
            data = row[0].split("_")
            data = ["_".join(data[:2])+".png", data[2]]
            data.append(row[1])
            attributesOfData.append(data)

    return attributesOfData


def setup():
    if (not os.path.isdir(PATHS["epidural"])):
        os.mkdir(PATHS["epidural"])
    if (not os.path.isdir(PATHS["intraparenchymal"])):
        os.mkdir(PATHS["intraparenchymal"])
    if (not os.path.isdir(PATHS["intraventricular"])):
        os.mkdir(PATHS["intraventricular"])
    if (not os.path.isdir(PATHS["subarachnoid"])):
        os.mkdir(PATHS["subarachnoid"])
    if (not os.path.isdir(PATHS["subdural"])):
        os.mkdir(PATHS["subdural"])
    if (not os.path.isdir(PATHS["none"])):
        os.mkdir(PATHS["none"])


if __name__ == "__main__":
    setup()
    csvInfo = csvExtraction()
    fileInspect(csvInfo)
