#!/bin/python3

import math
import os
import random
import re
import sys



if name == 'main':
    n = int(input().strip())
    if n % 2:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
