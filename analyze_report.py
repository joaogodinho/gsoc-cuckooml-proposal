from os import listdir
from os.path import join
from collections import Counter
import json


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


# Returns a set with all top level keys seen
def getSeenKeys(reports):
    keys = set()
    for r in reports:
        keys.update(r.keys())
    return keys


# Counts the number of top level keys that contain information
# some keys might contain no information and they're still defined
# so need to manually filter them
def getKeysDist(reports):
    keysList = []
    for r in reports:
        for k in r.keys():
            if k == u'virustotal':
                if 'scans' in r[k].keys():
                    keysList.append(k)
                else:
                    pass
            elif len(r[k]) > 0:
                keysList.append(k)
    return Counter(keysList)


def main():
    reports = listReportsPath()
    samplesSize = len(reports)
    jsonObjs = loadSamples(reports)
    keysSet = getSeenKeys(jsonObjs)
    keysDist = getKeysDist(jsonObjs)
    print('Top level keys seen: {}'.format(str(keysSet)))
    for k, v in keysDist.items():
        print('{} appears in {} samples ({:.2f}%)'.format(k, v, float(v) / samplesSize * 100))

if __name__ == '__main__':
    main()
