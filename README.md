# RecipeCMS

The CMS behind [JustMy.Cooking](https://justmy.cooking). The aim of this CMS was to create a static HTML website that could be uploaded anywhere and did not rely on JS frameworks that required updating or maintaining. This could be hosted anywhere, on anything and it is as secure as the host. For example, Cloudflare Pages!

If you want to try and use it for yourself, read on.

# Prerequisites

### Environment Variables JSON

Exluded using the `.gitignore`, there is a file called `environment_variables.json` housed within the python folder which is vital for the script to run. An example of the structure of that file can be found in the `variables_template.json` file at the root of this project. You can copy it into the python folder and rename it. Inside are 3 variables which are described below:
- `search_path` is the path your script will search for recipe JSON files. In the context of this project, that would be the `recipes` folder at the root of the project.
- `url` is the URL you are using for your website. At the time of writing, this is not used everywhere, so if you were to use the project yourself to create a recipe website you would need to manually update some stuff. You could `ctrl` + `f` to find instances of `justmy.cooking` to find where the url is still hard coded.
- `header` is a variable which can be used to inject custom HTML into the header. I use it to inject my analytics HTML.

### Python

I used python 3.11.9 to creat this project. It has not been tested with any other version.

### Folder Structure

The folder structure of the project is as follows:

```

root
├───data
├───python
│   ├───main.py
│   |───utils
|   |   ├───utils.py
│   |   └───otherUtils.py
|───recipes
|   |───recipeName
|   |   |───recipeName.json
|   |   └───recipeName_0.jpg
|   |───otherRecipeName
|   |   |───otherRecipeName.json
|   |   └───otherRecipeName_0.jpg
|

```
