# -*- coding: utf-8 -*-
# Created At 2017-09-17 15:04
# Author: LCAR979 <tcoperator@163.com>
# Version: 1.0
# License: GPL 2.0
# Description:

import re
import os
import requests
import wget
from bs4 import BeautifulSoup


def get_links():
    """get all *-handout.tar file links from CSAPP lab page"""
    base_url ='http://csapp.cs.cmu.edu/public/labs.html'
    webpage = requests.get(base_url).content
    soup = BeautifulSoup(webpage, 'lxml')
    a_tag_list = soup.findAll('a', attrs={'href': re.compile(r"handout.tar")})
    link_list = [a_tag['href'] for a_tag in a_tag_list]
    return link_list


def download_files(link_list):
    """download all the files specified in link_list and save"""
    save_path = os.path.expanduser('~/Downloads/CSAPP_labs/')
    if os.path.exists(save_path) is False:
        os.makedirs(save_path)

    downloaded_count = 0
    for link in link_list:
        file_name = link.split('/')[-1]
        wget.download(link, out=save_path + file_name)
        downloaded_count += 1
        print('File {} downloaded. {}/{}'.format(file_name, downloaded_count, len(link_list)))

if __name__ == "__main__":
    download_files(get_links())
