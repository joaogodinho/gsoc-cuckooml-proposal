from os import listdir, makedirs
from os.path import join
import json


SIGNATURES_DIR = 'signatures/'
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


# Returns a list where the first dimension is the report, second is a list of signatures
def extractSigs(reports):
    files = []
    for r in reports:
        sigsList = []
        try:
            signatures = r['signatures']
            for sig in signatures:
                sigsList.append(sig['name'])
        except:
            # No signatures
            pass
        files.append(sigsList)
    return files


def createFiles(filesSigs):
    try:
        makedirs(SIGNATURES_DIR)
    except:
        # Directory already exists
        pass
    # File order may be different from original samples
    for i, f in enumerate(filesSigs, start=1):
        with open(join(SIGNATURES_DIR, str(i)), 'w') as file:
            file.write(" ".join(f))


def main():
    reports = listReportsPath()
    jsonObjs = loadSamples(reports)
    filesSigs = extractSigs(jsonObjs)
    createFiles(filesSigs)


if __name__ == '__main__':
    main()
