from bs4 import BeautifulSoup
import re
import os
import sys

html_dir = '/Users/mkf26/Documents/code/file-trees'

with open('/Users/mkf26/Documents/code/file-trees/generating-trees/htmlTemplate.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    soup.find('title').string = 'MKFA File Trees'
    body = soup.find('body')
    h1 = soup.new_tag('h1')
    h1.string = 'MKFA Born-Digital File Trees'
    body.append(h1)
    html_file_trees = []
    for file in os.listdir(html_dir):
        if os.path.isfile(os.path.join(html_dir, file)) and 'D-' in file:
            html_file_trees.append(file)
    html_file_trees.sort()
    for file_tree in html_file_trees:        
        digital_media_id_search = re.findall('D-[\dA-E]{4,5}', file_tree)
        digital_media_id = '_'.join(digital_media_id_search)
        anchor = soup.new_tag('a', attrs={"href": file_tree, "target": "_blank"})
        anchor.string = digital_media_id
        body.append(anchor)
    html_content = soup.prettify()
    with open('/Users/mkf26/Documents/code/file-trees/index.html', 'w') as html_file:
        html_file.write(html_content)

