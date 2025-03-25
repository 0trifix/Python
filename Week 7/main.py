import markdown, frontmatter, os, jinja2

def get_md_files(location):
    files = os.listdir(f"{location}/")
    return [location + "/" + file for file in files if file.endswith(".md")]

def get_yaml(file):
    with open(file, 'r') as f:
        file = frontmatter.load(f)
        return file.metadata    

def get_content(file):
    with open(file, 'r') as f:
        post = frontmatter.load(f)
        return post.content

def list_pages(folder):
    pages = []
    for page in get_md_files(folder):
        metadata = get_yaml(page)
        pages.append({
            'title': metadata["title"],
            'url': metadata["url"],
            'order': metadata["order"]
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
    try:
        os.mkdir("pages")
    except FileExistsError:
        pass
    pages = list_pages(folder)
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
