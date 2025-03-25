import markdown, frontmatter, os, sys, jinja2

def get_md_files():
    path = os.getcwd() + "/pages"
    files = os.listdir(path)
    return [path + "/" + file for file in files if file.endswith(".md")]

