import markdown, frontmatter, os, jinja2

def get_md_files(location):
    path = os.getcwd() + f"/{location}"
    files = os.listdir(path)
    return [path + "/" + file for file in files if file.endswith(".md")]

def get_yaml(file):
    with open(file, 'r') as f:
        file = frontmatter.load(f)
        return file.metadata    

def get_content(file):
    with open(file, 'r') as f:
        post = frontmatter.load(f)
        return post.content

def get_metadata(folder):
    pages = []
    for page in get_md_files(folder):
        pages.append({
            'title': get_yaml(page)["title"],
            'url': get_yaml(page)["url"],
            'order': get_yaml(page)["order"]
        })
    pages = sorted(pages, key=lambda x: x['order'])
    return pages

def get_template():
    with open("templates/base.html", 'r') as f:
        return f.read()

def render_template(template, pages, content):
    template = jinja2.Template(template)
    return template.render(pages=pages, content=content)    

def main():
    folder = "pages"
    pages = get_metadata(folder)
    template = get_template()
    for page in get_md_files(folder):
        content = get_content(page)
        html = markdown.markdown(content)
        try:
            os.mkdir("_site")
        except FileExistsError:
            pass
        with open(f"_site/{get_yaml(page)['url']}", 'w') as f:
            f.write(render_template(template, pages, html))

if __name__ == "__main__":
    main()
