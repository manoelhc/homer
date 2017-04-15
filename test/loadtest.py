#!/usr/bin/python3
import sys
import os
import homer
import yaml

conf = homer.Config(app="test", secret_key='1')
conf.reset()
path = os.path.dirname(__file__)
stream = open('{}/performance'.format(path), 'r')
data = yaml.load(stream)    # Write a YAML representation of data to 'document.yaml'.
keys    = data.keys()
ksorted = sorted(keys)

for i in ksorted:
    conf[i] = data[i]

for key in keys:
    k1 = conf[key]
    k2 = data[key]
    if k1 != k2:
        print(k1,' != ',k2)
        print("ERROR:Wrong Saved Data")
        sys.exit(1)

if len(conf) != len(conf.search('keynum')):
    print("ERROR:Wrong Search Query")
    sys.exit(1)

for i in keys:
    conf.unset(i)

if conf.count() > 0:
    print("Error:Different data")
    sys.exit(1)
