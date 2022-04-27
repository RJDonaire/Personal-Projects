import re

# variables
ls_i = ['Type', 'Episode', 'Status', 'Aired', 'Premiered', 'Broadcast', 'Producer', 'Licensor', 'Studio', 'Source', 'Genre', 'Theme', 'Duration', 'Rating']

# functions
# extracts info from the leftside portion of '/anime/n'
def extract_leftside(text):
    ls_dict = {feat: '' for feat in ls_i}

    for feat in ls_i:
        pattern = f"{feat}s*:\s(.+)"
        if re.search(pattern, text):
            ls_dict[feat] = re.search(pattern, text).group(1)
            continue
        ls_dict[feat] = ''

    return ls_dict