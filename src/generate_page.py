def extract_title(md):
    md = md.split("\n")
    for line in md:
        if line.strip().startswith("# "):
            return line[2:]

    raise Exception("No title found")
