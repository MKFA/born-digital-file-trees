import sys
import json
from bs4 import BeautifulSoup
import re
import os

def generateHTML(dir_path, tree_data, soup):
    print(f"Generating HTML for {dir_path} tree")
    body = soup.find('body')
    digital_media_id_search = re.findall('D-[\dA-E]{4,5}', dir_path)
    digital_media_id = '_'.join(digital_media_id_search)
    soup.find('title').string = f"{digital_media_id} File Tree"
    header = soup.new_tag('h1')
    header.string = digital_media_id + " File Tree"
    body.append(header)
    collapse_button = soup.new_tag('button', attrs={"class": "button", "id": "collapseButton", "onclick":"toggleCollapse()"})
    collapse_button.string = "Collapse All Directories"
    body.append(collapse_button)
    def process_entry(entry, parent, margin):
        if entry["type"] == "directory":
            # If the directory is not the top-level one, create HTML elements
            if entry.get("contents"):
                margin = margin + 5
                dir_div = soup.new_tag("div", attrs={"class": "directory", "id":entry['name'], "style":f"margin-left:{margin}px"})
                parent.append(dir_div)
                dir_anchor = soup.new_tag('a', attrs={"href":f"#{entry['name']}", "onclick":'toggleDropdown(this)'})
                dir_anchor.string = "📁 "+ " " + entry["name"]
                dir_div.append(dir_anchor)
                dropdown_div = soup.new_tag('div', attrs={'class':'dropdown-content'})
                dir_div.append(dropdown_div)
                if entry.get("contents"):
                    for child_entry in entry["contents"]:
                        process_entry(child_entry, dropdown_div, margin)
        elif entry["type"] == "file":
            file_span = soup.new_tag('p', attrs={"class": "file", "style":f"margin-left:{margin}px"})
            file_span.string = "📃 " + f'"{entry["name"]}"' + f" - {entry['size']}b - [{entry['time']}]"
            parent.append(file_span)
    if tree_data[0].get('contents'):
        for entry in tree_data[0]['contents']:
            process_entry(entry, body, 5)

def main():
    json_file_path = sys.argv[1]
    # Check if a second argument was provided and is not an empty string
    file_name_addition = f"_{sys.argv[2]}" if len(sys.argv) > 2 and sys.argv[2] else ''
     # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Step up one directory level
    parent_dir = os.path.dirname(script_dir)

    digital_media_id_search = re.findall('D-[\dA-E]{4,5}', json_file_path)
    digital_media_id = '_'.join(digital_media_id_search)

    with open(json_file_path, 'r') as json_file:
        tree_data = json.load(json_file)
    with open(os.path.join(script_dir, 'htmlTemplate.html'), 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    generateHTML(json_file_path, tree_data, soup)
    
    html_content = soup.prettify()
    html_output_path = os.path.join(parent_dir, f"html/{digital_media_id}_file_tree{file_name_addition}.html")
    with open(html_output_path, 'w') as html_file:
        html_file.write(html_content)
    print(f"HTML tree created for {json_file_path}")

if __name__ == "__main__":
    main()
