import base64
import re

def embed_image():
    with open('profile.jpg', 'rb') as f:
        img_data = base64.b64encode(f.read()).decode('utf-8')
    
    base64_str = f'href="data:image/jpeg;base64,{img_data}"'
    
    for filename in ['dark.svg', 'light.svg']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(r'href="profile\.jpg"', base64_str, content)
        content = re.sub(r'href="data:image/png;base64,[^"]+"', base64_str, content)
        content = re.sub(r'href="data:image/jpeg;base64,[^"]+"', base64_str, content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    embed_image()
