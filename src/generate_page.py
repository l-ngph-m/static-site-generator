from markdown_blocks import markdown_to_html_node
import os

def extract_title(md):
    md = md.split("\n")
    for line in md:
        if line.strip().startswith("# "):
            return line[2:]

    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_page_recursive(content_dir_path, template_path, dest_dir_path):
    content_files = os.listdir(content_dir_path)
    for file in content_files:
        from_path = os.path.join(content_dir_path, file)
        dest_path = os.path.join(dest_dir_path, file)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(
                    # os.path.join(from_path, "index.md"),
                    from_path,
                    template_path,
                    dest_path
                    # os.path.join(dest_path, "index.html")
            )
        else:
            generate_page_recursive(from_path, template_path, dest_path)
