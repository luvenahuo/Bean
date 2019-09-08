import os
import subprocess
import sys
import commands
import base64
import json
import skimage.io as si

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "service.json"
encoding = base64.b64encode(si.imread("test.png"))

request = '{"payload": {"image": {"imageBytes": "%s" } } }' %(encoding)

status, output = commands.getstatusoutput('curl -s -X POST -H "Content-Type:application/json"   -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"   https://automl.googleapis.com/v1beta1/projects/140663576171/locations/us-central1/models/IOD8016398540626460672:predict -d %s' %(request))
print(output)