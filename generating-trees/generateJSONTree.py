import subprocess
import sys
import os
import re

def getFileTreeJSON(dir_path):
    print(f"Getting file tree for {dir_path}")
    tree = subprocess.run(["tree", "-JDh", dir_path], capture_output=True, text=True)
    return tree.stdout

def main():
    dir_path = sys.argv[1]
    # Check if a second argument was provided and is not an empty string
    file_name_addition = f"_{sys.argv[2]}" if len(sys.argv) > 2 and sys.argv[2] else ''
    file_tree_json = getFileTreeJSON(dir_path)
    digital_media_id_search = re.findall('D-[\dA-E]{4,5}', dir_path)
    digital_media_id = '_'.join(digital_media_id_search)
    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Step up one directory level
    parent_dir = os.path.dirname(script_dir)
    with open(os.path.join(parent_dir, f"json/{digital_media_id}_file_tree{file_name_addition}.json"), "w") as json_file:
        json_file.write(file_tree_json)
    print(f"JSON file tree created for {digital_media_id}")

if __name__ == "__main__":
    main()
