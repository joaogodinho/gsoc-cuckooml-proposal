from os import listdir, makedirs
from os.path import join
import json


VIRUSTOTAL_DIR = 'virustotal/'
SAMPLES_DIR = 'samples/'


# Returns a list with the path for all reports
def listReportsPath():
    paths = []
    for f in listdir(SAMPLES_DIR):
        paths.append(join(SAMPLES_DIR, f))
    return paths


# Returns a list of json objects
def loadSamples(reports):
    objs = []
    for r in reports:
        with open(r, 'r') as file:
            objs.append(json.load(file))
    return objs


# Returns a list where the first dimension is the report, second is a list of virustotal matches
def extractVT(reports):
    files = []
    for r in reports:
        try:
            files.append(r['virustotal']['normalized'])
        except:
            # Sample was not scanned
            pass
    return files


def createFiles(filesCalls):
    try:
        makedirs(VIRUSTOTAL_DIR)
    except:
        # Directory already exists
        pass
    # File order may be different from original samples
    for i, f in enumerate(filesCalls, start=1):
        with open(join(VIRUSTOTAL_DIR, str(i)), 'w') as file:
            file.write(" ".join(f))


def main():
    reports = listReportsPath()
    jsonObjs = loadSamples(reports)
    filesVT = extractVT(jsonObjs)
    createFiles(filesVT)


if __name__ == '__main__':
    main()
