import re

def fix_syntax():
    file_path = 'data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the double ], ], added by mistake
    content = content.replace('    ],\n    ],', '    ],')
    
    # Check for any other double commas or braces
    content = content.replace('    ],\n    "roast"', '    ],\n    "roast"') # Should be fine

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_syntax()
