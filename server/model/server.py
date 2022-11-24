#!/usr/bin/env python
from pywhisper import main as whisper
from gpt import translate as gpt
import sys

model = "small"
args = sys.argv[1:]
func = args[0]
url = args[1]

print('Func:', str(func), " Lang: ", str(url))

if func == "transcribe":
    link = url
    result = whisper(link, model)
    print(result)
