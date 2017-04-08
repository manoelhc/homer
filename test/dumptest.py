#!/usr/bin/python3
import sys
import os
import homer
import yaml

conf = homer.Config(app="test")
conf.reset()
path = os.path.dirname(__file__)
stream = open('{}/performance'.format(path), 'r')
data = yaml.load(stream)    # Write a YAML representation of data to 'document.yaml'.
for i in data.keys():
    conf.set(i, data[i])
c=0
for i in conf:
    c+=1
if c != len(conf):
    print("ERROR: DATA MISMATCHING")
    sys.exit(1)
