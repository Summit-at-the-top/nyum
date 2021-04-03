#! /usr/bin/env python3

import os

with open(os.getenv('FILE_PATH'), 'w') as file:
    file.write(os.getenv('RECIPE'))