from bs4 import BeautifulSoup
import re
import os
import sys

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Step up one directory level
parent_dir = os.path.dirname(script_dir)

with open(f'{script_dir}/htmlTemplate.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    soup.find('title').string = 'MKFA File Trees'
    body = soup.find('body')
    h1 = soup.new_tag('h1')
    h1.string = 'MKFA Born-Digital File Trees'
    body.append(h1)
    script = soup.find('script', src='../script.js')
    script['src'] = 'script.js'
    html_file_trees = []
    for file in os.listdir(f"{parent_dir}/html"):
        if os.path.isfile(os.path.join(f"{parent_dir}/html", file)) and 'D-' in file:
            html_file_trees.append(file)
    html_file_trees.sort()
    for file_tree in html_file_trees:        
        digital_media_id_search = re.findall('D-[\dA-E]{4,5}', file_tree)
        digital_media_id = '_'.join(digital_media_id_search)
        anchor = soup.new_tag('a', attrs={"href": f"html/{file_tree}", "target": "_blank"})
        anchor.string = digital_media_id
        body.append(anchor)
    html_content = soup.prettify()
    with open(f'{parent_dir}/index.html', 'w') as html_file:
        html_file.write(html_content)

