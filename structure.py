##########
# python script that will create a basic folder structure for an HTML, CSS, and JS project
# and it will create the basic files and write content to them
# it is also a way for me to practice python
##########

########## 
# save script in a file named 'structure.py'
# open a terminal or command prompt
# navigate to the folder where the script is saved
# run the script with the desired folder name as an argument 
# e.g. python3 structure.py my_project_folder
##########



import os
import sys

def generate_html_structure(folder_path):
    # create main folder
    os.makedirs(folder_path, exist_ok=True)

    # create subfolders
    css_folder = os.path.join(folder_path, 'styles')
    js_folder = os.path.join(folder_path, 'scripts')
    img_folder = os.path.join(folder_path, 'images')
    os.makedirs(css_folder, exist_ok=True)
    os.makedirs(js_folder, exist_ok=True)
    os.makedirs(img_folder, exist_ok=True)

    # create html, css and js files
    html_file = os.path.join(folder_path, 'index.html')
    css_file = os.path.join(css_folder, 'style.css')
    js_file = os.path.join(js_folder, 'script.js')

    # write content to files
    with open(html_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="en">\n')
        f.write('   <meta charset="UTF-8">\n')
        f.write('   <title>Page Title</title>\n')
        f.write('   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write('   <link rel="stylesheet" href="styles/style.css">\n')
        f.write('   <script src="scripts/script.js"></script>\n')
        f.write('   <body>\n')
        f.write('       <img src="images/image.jpg" alt="image" style="width:100%">\n')
        f.write('       <div class="">\n')
        f.write('           <h1>This is a heading</h1>\n')
        f.write('           <p>This is a paragraph.</p>\n')
        f.write('           <p>This is another paragraph.</p>\n')
        f.write('       </div>\n')
        f.write('   </body>\n')
        f.write('</html>\n')
        
    with open(css_file, 'w') as f:
        f.write('/* CSS Styles */\n')
        f.write('h1 {\n')
        f.write('   color: blue;\n')
        f.write('}\n')

    with open(js_file, 'w') as f:
        f.write('// JavaScript Scripts\n')
        f.write('console.log("Hello World");\n')

    print(f'Successfully created folder structure in {folder_path}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Provide a folder name as an argument')
        sys.exit(1)

    folder_name = sys.argv[1]
    generate_html_structure(folder_name)