# ajaxPagesChecker
This CLI-tool helps to work with Single-page applications, it opens a headless browser and analyzes the page after rendering, thereby allowing you to determine the length of the page after rendering and the presence of any specific words. 
 
## Usage
```
usage: checker.py [-h] -u File [-cl] [-ew Error-words]
options:
  -h, --help            show this help message and exit
  -u File, --urls File  Check pages from file
  -cl                   Get page length
  -ew Error-words       Filter by Error-words
```
### Options
`-h` - show help message  
`-u`, `--urls` - path to file with target urls (required)  
`-cl` - choose this option to get length of target page (optional, default: False)  
`-ew` - write the words that are on the page with the error (optional, default: None)

