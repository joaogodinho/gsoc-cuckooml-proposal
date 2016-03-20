from os import listdir
from os.path import join
import json


SAMPLES_DIR = 'samples/'


# Returns a list with the path for all reports
def listReportsPath():
    paths = []
    for f in listdir(SAMPLES_DIR):
        paths.append(join(SAMPLES_DIR, f))
    return paths


# Returns a set with all top level keys seen
def getSeenKeys(reports):
    keys = set()
    for r in reports:
        with open(r, 'r') as file:
            jsonObj = json.load(file)
            keys.update(jsonObj.keys())
    return keys


def main():
    reports = listReportsPath()
    keysSet = getSeenKeys(reports)
    print('Top level keys seen: {}'.format(str(keysSet)))

if __name__ == '__main__':
    main()
