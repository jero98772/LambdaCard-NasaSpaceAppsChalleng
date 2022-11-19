#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#Sky-eye - by lambdaCard

from core.main import webpage
from core.main import app
try:
    if __name__ == '__main__':
        app.run(debug=True,host="0.0.0.0",port=9600)
except :
    if __name__ == '__main__':
        app.run(debug=True,host="0.0.0.0",port=9600)