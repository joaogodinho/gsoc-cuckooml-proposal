from os import listdir, makedirs
from os.path import join
import json


APISTATS_DIR = 'apistats2/'
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
# Remove W and A from the call, since it's the same but on different encodings
def extractAPI(reports):
    files = []
    for r in reports:
        apiList = set()
        try:
            apistats = r['behavior']['apistats']
            for proc in apistats.keys():
                for call in apistats[proc]:
                    if call.endswith('W') or call.endswith('A'):
                        apiList.add(call[:-1])
                    else:
                        apiList.add(call)
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
