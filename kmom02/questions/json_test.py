#!/usr/bin/env python3
"""Test the json file."""

import pprint
import json

jdata = json.load(open("questions.json", encoding="utf-8"))

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(jdata)

print(jdata["0"]["answer"])

pp.pprint(jdata["6"]["alt"])
