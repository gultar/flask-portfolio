from modules.dependencies import *

def read_file(filename, encoding="latin-1"):
    with open(filename, 'r', encoding=encoding) as f:
        file = f.read()
        return file.strip()
    
def write_file(filename, content, encoding="latin-1"):
    with open(filename, 'w', encoding=encoding) as f:
        cleaned = content.strip()
        f.write(cleaned)

def wrap_title_with_link(text, post_slug):
    match = re.search(r'^(#+)\s*(.*)', text, re.MULTILINE)
    
    if match:
        title_level = match.group(1)
        print(title_level)
        title = match.group(2)
        wrapped_title = f"<h2><a href='/blog/{post_slug}' class='post-title-link'>{title}</a></h2>"
        modified_text = re.sub(r'^(#+)\s*(.*)$', wrapped_title, text, flags=re.MULTILINE)
        return modified_text
    else:
        return text
    
def extract_text_until_subtitle(text):
    match = re.search(r'^(.+?)(?=\n\n## )', text, re.MULTILINE | re.DOTALL)

    if match:
        text = match.group(1)
        return text.strip()
    else:
        return None

def extract_post_title(text):
    match = re.search(r'^# (.+)$', text, re.MULTILINE)

    if match:
        return match.group(1)
    else:
        return None
    
def format_to_slug(title: str)-> str:
    title = title.lower()
    title = remove_special_characters(title)
    title = title.replace(" ","-")
    return title

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9\s\-]'
    return re.sub(pattern, '', text)
