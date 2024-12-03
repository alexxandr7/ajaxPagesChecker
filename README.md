# ajaxPagesChecker
This CLI-tool helps to work with Single-page applications, it opens a headless browser and analyzes the page after rendering, thereby allowing you to determine the length of the page after rendering and the presence of any specific words. 
 
## Usage
```
usage: checker.py [-h] -u File [-cl] [-ew Error-words] [-sp]
options:
  -h, --help            show this help message and exit
  -u File, --urls File  Check pages from file
  -cl                   Get page length
  -ew Error-words       Filter by Error-words
  -sp                   Take a screenshot of pages
```
### Options
`-h` - show help message  
`-u`, `--urls` - path to file with target urls (required)  
`-cl` - choose this option to get length of target page (optional, default: False)  
`-ew` - write the words that are on the page with the error. (optional, default: None)  
`-sp` - take a screenshot for each page. A "checker_screenshots" folder will be created where the screenshots will be saved (optional, default: False)

### Examples
Get the length of each page after rendering:
```shell
python3 checker.py -u urls.txt -cl
```

Highlight pages that contain error-words after rendering:
```shell
python3 checker.py -u urls.txt -ew "Page Not Found"
```

Take a screenshot for each page after rendering:
```shell
python3 checker.py -u urls.txt -sp
```
The results will be saved to the "checker_screenshots" folder.


All at once:
```shell
python3 checker.py -u urls.txt -cl -ew "Page Not Found" -sp
```
