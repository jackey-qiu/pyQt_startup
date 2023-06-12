import yaml
import os
import shutil

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())

root = config['root']
pkg = config['pkg_name']
project_folder_info = config['folder_structure'][config['project_structure']]
root_dir = config['root_dir']
rse_dir = []

for each in project_folder_info:
    folder_encoded = project_folder_info[each]
    folder_encoded = folder_encoded.replace(' ','')
    items = folder_encoded.rstrip().rsplit('/')
    subfolders = []
    for i in range(len(items)):
        item = items[i]
        if item.startswith('[') and item.endswith(']'):
            items[i] = item[1:-1].rstrip().rsplit(',')
            subfolders.append(i)
    assert len(subfolders)<=1, 'wrong structure for {}, since more than one subfolder structure'.format(items)
    if items[-1] == '__init__.py':
        if len(subfolders)==1:
            folder_front = '/'.join(items[0:subfolders[0]])
            folder_end = '/'.join(items[subfolders[0]+1:-1])
            folder_middle_items = items[subfolders[0]]
            for middle_item in folder_middle_items:
                full_path = '/'.join([root, pkg, folder_front, middle_item, folder_end])
                full_path_items = full_path.rsplit('/')
                for i in range(2,len(full_path_items)+1*0):
                    full_path_temp = '/'.join(full_path_items[0:i])
                    os.makedirs(full_path_temp, exist_ok=True)
                    try:
                        with open(full_path_temp+'/__init__.py', 'w+') as f:
                            f.write('')
                        print('Success to create path: {}'.format(full_path_temp+'/__init__.py'))
                    except Exception as e:
                        print('Failed to create folder: {} due to {}'.format(full_path_temp+'/__init__.py', e))
        elif len(subfolders)==0:
            full_path = '/'.join([root, pkg]+items[0:-1])
            full_path_items = full_path.rsplit('/')
            for i in range(2,len(full_path_items)+1):
                full_path_temp = '/'.join(full_path_items[0:i])
                os.makedirs(full_path_temp, exist_ok=True)
                try:
                    with open(full_path_temp+'/__init__.py', 'w+') as f:
                        f.write('')
                    print('Success to create path: {}'.format(full_path_temp+'/__init__.py'))
                except Exception as e:
                    print('Failed to create folder due to {}'.format(e))
    else:
        if len(subfolders)==1:
            folder_front = '/'.join(items[0:subfolders[0]])
            folder_end = '/'.join(items[subfolders[0]+1:])
            folder_middle_items = items[subfolders[0]]
            for middle_item in folder_middle_items:
                full_path = '/'.join([root, pkg, folder_front, middle_item, folder_end])
                full_path_items = full_path.rsplit('/')
                for i in range(2,len(full_path_items)):
                    full_path_temp = '/'.join(full_path_items[0:i])
                    os.makedirs(full_path_temp, exist_ok=True)
                    try:
                        if i!=len(full_path_items)-1:
                            with open(full_path_temp+'/__init__.py', 'x') as f:
                                f.write('')
                            print('Success to create path: {}'.format(full_path_temp+'/__init__.py'))
                        else:
                            rse_dir.append('.'.join(full_path_items[1:i]))
                    except Exception as e:
                        print('Failed to create folder due to {}'.format(e))
        elif len(subfolders)==0:
            full_path = '/'.join([root, pkg]+items)
            full_path_items = full_path.rsplit('/')
            for i in range(2,len(full_path_items)):
                full_path_temp = '/'.join(full_path_items[0:i])
                os.makedirs(full_path_temp, exist_ok=True)
                try:
                    if i!=len(full_path_items)-1:
                        with open(full_path_temp+'/__init__.py', 'x') as f:
                            f.write('')
                        print('Success to create path: {}'.format(full_path_temp+'/__init__.py'))                    
                    else:
                        rse_dir.append('.'.join(full_path_items[1:i]))
                except Exception as e:
                    print('Failed to create folder due to {}'.format(e))        

rse_info = {}
for each in rse_dir:
    items = each.rsplit('.')
    pkg_ = '.'.join(items[0:-1])
    rse = items[-1]+'/*'
    if pkg_ not in rse_info:
        rse_info[pkg_] = [rse]
    else:
        rse_info[pkg_].append(rse)

classifiers = [f'{each}::{value}' for each, value in config['setup']['classifiers'].items()]

def make_setup():
    with open(os.path.join(root, 'setup.py'), 'w') as f:
        f.write('from setuptools import setup, find_packages\n')
        f.write('setup(\n')
        f.write(f"    name = '{pkg}',\n")
        f.write(f"    version = '{config['setup']['version']}',\n")
        f.write(f"    description = '{config['setup']['description']}',\n")
        f.write(f"    author = '{config['setup']['author']}',\n")
        f.write(f"    author_email = '{config['setup']['author_email']}',\n")
        f.write(f"    url = '{config['setup']['url']}',\n")
        f.write(f"    classifiers = {classifiers},\n")
        f.write(f"    license = '{config['setup']['license']}',\n")
        f.write(f"    install_requires = {config['setup']['install_requires'].rsplit(',')},\n")
        f.write(f"    packages = find_packages(),\n")
        f.write(f"    package_data = {rse_info},\n")
        f.write(f"    scripts = [],\n")
        f.write("     entry_points = {\n")
        f.write("         'console_scripts' : [\n")
        for each, value in config['setup']['entry_points']['console_scripts'].items():
            f.write(f"             '{each} = {'.'.join(value.rsplit('.')[0:-1])}:{value.rsplit('.')[-1]}',\n")
        f.write("         ],\n")
        f.write("     }\n")
        f.write(")\n")

make_setup()
shutil.copyfile(f"./licenses/{config['setup']['license']}",f"./{root}/LICENSE")
shutil.copyfile(f"./main_gui_temp.py",f"./{root}/{pkg}/bin/main_gui.py")
shutil.copyfile(f"./main_gui_funcs_temp.py",f"./{root}/{pkg}/core/gui_funcs/main_gui_funcs.py")
shutil.copyfile(f"./log_util_funcs_temp.py",f"./{root}/{pkg}/util/log_util/log_util_funcs.py")
shutil.copyfile(f"./log.yaml",f"./{root}/{pkg}/res/config/log.yaml")
shutil.copyfile(f"./licenses/{config['setup']['license']}",f"./{root}/LICENSE")
shutil.move(f'./{root}', root_dir)
