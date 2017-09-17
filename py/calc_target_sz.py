# -*- coding: utf-8 -*-
# Created At 2017-09-16 21:51
# Author: LCAR979 <tcoperator@163.com>
# Version: 1.0
# License: GPL 2.0
# Description:

import os
import csv
import re

database_base_dir = os.path.expanduser('~/Database/VTB100')
stat_record = []

with open('target_sz_grdtruth.csv', 'w') as csvf:
    writer = csv.writer(csvf, quoting=csv.QUOTE_ALL)
    writer.writerow(['Sequence', 'x', 'y', 'width', 'height', 'Area'])
    for sequence_name in os.listdir(database_base_dir):
        txt_path = database_base_dir + '/' + sequence_name + '/groundtruth_rect.txt'
        with open(txt_path, 'r') as f:
            line = f.readline().strip()
            if line == "" or line == " " or line == '\n':
                continue
            stat = re.split('[\s,]', line)
            writer.writerow([sequence_name, stat[0], stat[1], stat[2], stat[3], str(int(stat[2]) * int(stat[3]))])


