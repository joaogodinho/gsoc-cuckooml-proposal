from os import listdir, makedirs
from os.path import join
import json


APISTATS_DIR = 'apistats/'
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


# Returns a list where the first dimension is the report, second is a list of calls
def extractAPI(reports):
    files = []
    for r in reports:
        apiList = []
        try:
            apistats = r['behavior']['apistats']
            for proc in apistats.keys():
                for call in apistats[proc]:
                    apiList.append(call)
        except:
            # No behavior or apistat
            pass
        files.append(apiList)
    return files


def createFiles(filesCalls):
    try:
        makedirs(APISTATS_DIR)
    except:
        # Directory already exists
        pass
    # File order may be different from original samples
    for i, f in enumerate(filesCalls, start=1):
        with open(join(APISTATS_DIR, str(i)), 'w') as file:
            file.write(" ".join(f))


def main():
    reports = listReportsPath()
    jsonObjs = loadSamples(reports)
    filesCalls = extractAPI(jsonObjs)
    createFiles(filesCalls)


if __name__ == '__main__':
    main()
