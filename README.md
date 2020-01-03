# ppkgbeta
A beta version of my package manager for the Bash shell, called Python Package.

## Information
This is currently a very early stage version of my package manager. One can install a bash script to their own use by creating a custom JSON file, with the package name and the URL of the location.

## JSON
For making your own packages for use with the manager, create your own JSON file. The file should be named `package_name.json` (replace `package_name` with the name of your package. The format of the package is this:

 ```
 {
  "package_name": "",
  "url": ""
}
```
The package name should be the name of the bash script you want, and the url should be a reachable (raw) location of the bash script, so it can be downloaded. The script is not included.


## Testing
To test, just clone the repository and run the `.py` using `python3 ppkg.py (path of JSON file)`. As far as I know, this is Bash-exclusive, though I will try to expand to `dash` soon for Ubuntu.
