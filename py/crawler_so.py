# -*- coding: utf-8 -*-
# Created At 2017-08-19 15:44
# Author: LCAR979 <tcoperator@163.com>
# Version: 1.0
# License: GPL 2.0
# Description:

import requests
from bs4 import BeautifulSoup
import pathlib
import pdfkit


def get_root_page_content(page_num):
    """get content from root page with specified page number"""
    root_url = 'https://stackoverflow.com/documentation/python/topics?page=' + str(page_num) + '&tab=popular"'
    return requests.get(root_url).text


def parse_content(content):
    """get topic links for pages to save"""
    soup = BeautifulSoup(content, "lxml")
    topic_tag_list = soup.findAll('a', attrs={'class':'doc-topic-link'})
    topic_link_list = []
    for topic in topic_tag_list:
        topic_link_list.append('https://stackoverflow.com' + topic['href'])
    return topic_link_list


def convert_web_page_to_pdf(topic_link_list):
    """visit each topic links and save them as pdfs"""
    for topic_link in topic_link_list:
        topic_name = topic_link.split('/')[-1]
        options = {
            'page-size': 'Letter',
            'margin-top': '0.25in',
            'margin-right': '0.75in',
            'margin-bottom': '0.25in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        save_path_name = 'StackoverflowDocs/' + topic_name + '.pdf'
        p = pathlib.Path(save_path_name)
        if p.is_file():
            continue
        try:
            pdfkit.from_url(topic_link, save_path_name)
        except OSError:
            pass
        print("Printed {}.pdf".format(topic_name))

if __name__ == '__main__':
    MAX_PAGE_NUM = 12
    for page_num in range(1, MAX_PAGE_NUM):
        content = get_root_page_content(page_num)
        topic_link_list = parse_content(content)
        # print(topic_link_list)
        convert_web_page_to_pdf(topic_link_list)