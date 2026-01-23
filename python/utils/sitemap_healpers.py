from .global_variables import *
from .link_helpers import *

def sitemap_entry(loc, lastmod):
    formatted_loc = format_link(loc)
    return f"""
    <url>
        <loc>{formatted_loc}</loc>
        <lastmod>{lastmod}</lastmod>
    </url>"""

def get_keyword_lastmod(keyword_map):
    
    return