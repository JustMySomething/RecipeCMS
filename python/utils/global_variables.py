search_path = ""
directory_path = ""
custom_header_html = ""


remove_html_extension = True


keyword_map = {}
cuisine_map = {}
category_map = {}
ingredient_map = {}
equipment_map = {}
listacle_map = {}
recipes = []
ingredient_prefix = {}

small_keyword_map = []
small_cuisine_map = []
small_category_map = []
small_ingredient_map = []
small_equipment_map = []
small_recipes = []

smallest_recipes = []
index_pages = []

shared_notes = {}
shared_note_map = {}

def get_sorted_keywords(map):
    sorted_items = sorted(map.items(), key=lambda item: len(item[1]), reverse=True)
    sorted_map = {k: v for k, v in sorted_items}
    return sorted_map

def get_sorted_recipes():
    sorted_items = sorted(recipes, key=lambda x: x['datePublished'], reverse=True)
    return sorted_items

def get_keyword_lastmod(keyword, map):
    values = map[keyword]
    published = "19900101"
    returnValue = ""
    for value in values:
        date = value['datePublished'].replace("-", "")
        if int(date) > int(published):
            published = date
            returnValue = value['datePublished']
    return returnValue

def get_recipe(folder):
    for recipe in recipes:
        if recipe["folder"] == folder:
            return recipe
        
