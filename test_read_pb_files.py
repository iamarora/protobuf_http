import person_pb2 as proto
import os

for filename in os.listdir('.'):
    if filename.endswith('.pb'):
        print filename
        with open(filename, 'rb') as f:
            print proto.Person().FromString(f.read())

