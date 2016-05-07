#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

source = ['I:' + os.sep + 'Work\Proj1\pythonCodingPrac\pyCharmProjs', 'I:\Work\Proj1\pythonCodingPrac\pyCharmProjs\.idea']

target_dir = "I:\Work\Proj1\pythonCodingPrac\zipExperiment\\"

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" % (target, ' '.join(source))
print zip_command

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'