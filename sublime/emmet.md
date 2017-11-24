# to use single quote instead of double quote in emmet html 

* make a folder in home directory name `emmet`
* make a `syntaxProfiles.json` file inside `emmet` folder.
* write following code
~~~json
{
  "html": {
    "tag_case": "lower",
    "attr_quotes": "single",
    "self_closing_tag": true
  },
  "jsx": {
    "tag_case": "lower",
    "attr_quotes": "single",
    "self_closing_tag": true
  }
}

~~~