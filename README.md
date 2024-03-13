# Generating file trees for born-digital files
HTML file trees for appraisal and description at MKFA.

Video documentation [available here](https://drive.google.com/drive/folders/1ep2jIHv5nC-zeJhnaPgAvBZX_JJblzla).

## Dependencies to install

### Python 3

### Beautiful Soup 4
This library handles html modifcation and is used to generrate the HTML files from file trees
```
pip install beautifulsoup4
```

## Clone this repository to local machine
https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository 

Once you have the repository cloned, pull from main branch in origin prior to creating new branches.

## In order to create new file trees

### Create JSON files for trees

To create a new JSON file for one directory (the basic command):
```
python3 full/path/to/generating-trees/generateJSONtree.py full/path/to/directory [optional string to append to new file]
```
To create JSON files for all directories (AIPs or DIPs):
```
for d in path/to/directories/*;
do python3 full/path/to/generating-trees/generateJSONtree.py ${d}/original_files [optional string to append to new files];
done;
```

### Create HTML files from JSON
To create a new HTML file from one JSON (the basic command):
```
python3 full/path/to/generating-trees/generateHTMLfromJSON.py full/path/to/file.json [optional string to append to new file]
```
To create JSON files for all directories (AIPs or DIPs):
```
for f in path/to/repo/json/*;
do python3 full/path/to/generating-trees/generateHTMLfromJSON.py $f [optional string to append to new files];
done;
```
### Create new index


## Commit and push the JSON, HTML and new index to GitHub
Commit is a local change. Push to origin (GitHub) will synch the selected local commits to the cloud.
You can batch run json and html files for multiple AIPs and then select them all to apply in a single commit/push process.

### Review and merge pull requests in GitHub
Delete the branch in GitHub and locally once completed.
