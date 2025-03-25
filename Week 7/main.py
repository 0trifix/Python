import markdown, frontmatter, os, sys, jinja2

def get_md_files():
    path = os.getcwd() + "/pages"
    files = os.listdir(path)
    return [path + "/" + file for file in files if file.endswith(".md")]

def get_yaml(file):
    with open(file, 'r') as f:
        post = frontmatter.load(f)
        return post.metadata    

def get_file_content(file):
    with open(file, 'r') as f:
        return f.read()

def remove_yaml_from_content(content):
    return content.split("---")[2]
