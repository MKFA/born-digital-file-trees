import subprocess
from bs4 import BeautifulSoup
import re
import sys
import os

# Use file tree util to get a json file tree from a given directory
def getFileTreeJSON(dir_path):
    print(f"Getting file tree for {dir_path}")
    tree = subprocess.run(["tree", "-JDh", dir_path], capture_output=True, text=True)
    return tree.stdout

def generateHTML(dir_path, soup):
    tree_data = getFileTreeJSON(dir_path)
    tree_data = eval(tree_data)  # Convert JSON string to Python dict
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

def fileTreetoHTML(dir_path, html_file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, 'htmlTemplate.html'), 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    generateHTML(dir_path, soup)

    html_content = soup.prettify()
    with open(html_file_path, 'w') as html_file:
        html_file.write(html_content)

def main():
    files_path = sys.argv[1]
    # Check if a second argument was provided and is not an empty string
    file_name_addition = f"-{sys.argv[2]}" if len(sys.argv) > 2 and sys.argv[2] else ''
    digital_media_id_search = re.findall('D-[\dA-E]{4,5}', files_path)
    digital_media_id = '_'.join(digital_media_id_search)
    fileTreetoHTML(files_path, f'/Users/mkf26/Documents/code/file-trees/{digital_media_id}-tree{file_name_addition}.html')
    print(f"HTML tree created for {digital_media_id}")

if __name__ == "__main__":
    main()
