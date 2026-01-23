from .global_variables import *
from .link_helpers import *
from datetime import datetime

def get_footer():
    return f"""
        </div>
        <footer>
            <div id=\"foot\">
                <div class=\"keywords border\">
                    <a href=\"{format_link(f'{directory_path}/all_recipes.html')}\">
                        <p>All Recipes</p>
                    </a>
                </div>
                <div class=\"keywords border\">
                    <a href=\"{format_link(f'{directory_path}/all_keywords.html')}\">
                        <p>All Keywords</p>
                    </a>
                </div>
                <div class=\"keywords border\">
                    <a href=\"{format_link(f'{directory_path}/listacles.html')}\">
                        <p>Listacles</p>
                    </a>
                </div>
                <div class=\"keywords border\">
                    <a href=\"#head\">
                        <p>Top</p>
                    </a>
                </div> 
                <div class=\"keywords border\">
                    <p>&copy; {datetime.now().year} Just My Cooking</p>
                </div>
            </div>
        </footer>
    </body>
</html>"""

