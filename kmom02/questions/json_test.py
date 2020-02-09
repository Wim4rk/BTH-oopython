#!/usr/bin/env python3
"""
Test the json file
"""

import pprint
import json

json = json.load(open("questions.json", encoding="utf-8"))

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(json)

print(json["1"]["answer"])

pp.pprint(json["1"]["alternative"][3])
