import re

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix line endings
    content = content.replace('\r\r\n', '\n').replace('\r\n', '\n')
    
    # Update css cache buster
    content = re.sub(r'css/style\.css\?v=\d+', 'css/style.css?v=103', content)
    
    # Add cache busters to the logos in brands.html and index.html
    # Find all png/jpg/svg inside assets/brands and append or update ?v=xxx
    def replace_img(match):
        path = match.group(1)
        # remove existing query string if any
        path = path.split('?')[0]
        return f'src="{path}?v=103"'
    
    content = re.sub(r'src="(assets/brands/[^"]+)"', replace_img, content)
    
    with open(filename, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f"Fixed {filename}")

fix_file('brands.html')
fix_file('index.html')
