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
            if k == 'virustotal':
                if 'scans' in r[k].keys():
                    keysList.append(k)
                else:
                    pass
            elif len(r[k]) > 0:
                keysList.append(k)
    return Counter(keysList)


# Returns all possible normalized virustotal values
def getVirusNorm(reports):
    normList = []
    for r in reports:
        try:
            norm = r['virustotal']['normalized']
            normList += norm
        except:
            # Sample was not scanned
            pass
    return Counter(normList)


# Returns all possible signatures
def getSignatures(reports):
    sigList = []
    for r in reports:
        try:
            sig = r['signatures']
            for s in sig:
                sigList.append(s['name'])
        except:
            # No signature key
            pass
    return Counter(sigList)


# Returns all possible api calls
def getApiCalls(reports):
    apiList = []
    for r in reports:
        try:
            apistats = r['behavior']['apistats']
            for proc in apistats.keys():
                for call in apistats[proc]:
                    apiList.append(call)
        except:
            # No behavior or apistat
            pass
    return Counter(apiList)


def main():
    reports = listReportsPath()
    samplesSize = len(reports)
    jsonObjs = loadSamples(reports)
    keysSet = getSeenKeys(jsonObjs)
    keysDist = getKeysDist(jsonObjs)
    virusNorm = getVirusNorm(jsonObjs)
    sigs = getSignatures(jsonObjs)
    apiCalls = getApiCalls(jsonObjs)
    print('Top level keys seen: {}\n'.format(str(keysSet)))

    for k, v in keysDist.items():
        print('{} appears in {} samples ({:.2f}%)'.format(k, v, float(v) / samplesSize * 100))

    print('\nNumber of unique families: {}'.format(len(virusNorm)))
    print('Ten most common families:')
    print(virusNorm.most_common(10))

    print('\nNumber of unique signatures: {}'.format(len(sigs)))
    print('Ten most common signatures:')
    print(sigs.most_common(10))

    print('\nNumber of unique apicalls: {}'.format(len(apiCalls)))
    print('Ten most common calls:')
    print(apiCalls.most_common(10))


if __name__ == '__main__':
    main()
