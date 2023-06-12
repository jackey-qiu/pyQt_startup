# pyQt_startup
creating boilerplate code structure for a pyqt5 project

# purpose
Start up quickly a boiler-plate code structure for making a PyQt5 app project. Besides empty package folders, some template module files will be created in place as well. One can eidt the template file accordingly. In addition, a setup.py file will be created in the root directory according to the config file.

# How to use it?
1. Edit the config.yaml. Explanation of some keys in the config.yaml are listed below.
- root_dir: root directory for your project folder, default to '..' which is the parent of this boiler-plate creater folder
- root: the folder name of the project to be built, all files will be in this folder
- pkg_name: the package name, also the folder name of the python package (note different from root folder name)
- project_structure: the tag to specifiy the code structure. The tag has to be one of the keys in the folder_structure (read below)
- folder_structure: here you specify the foler strucutre for your package. You can add as many chains as you want (names are arbitrary but have to be unique each). The value of each chain define one root to bottom folder structure either being ended with __init__.py or folder name. The ones ending with __init__.py means the last folder in this chain is supposed to be an importable module. Otherwise, the last folder in the chain is not supposed to be a module, but a common folder storing some resource files, that should be included later in the setup.py file. Each chain is '/' seperated, for parallel folders (sitting on the same chain level) they are specified in a square bracket (eg. [folder1, folder2] ). There are two folder structure types being provied now. But you can eidt the existing one or create a new one with a different key. Whichever type you would like to use, you will need to specifiy that in the project_structure by giving the key name.
- Under the setup tag, most are self-explanary, except for
  - name: the name of your package reconized by pypi (different from the package name)
  - console_scripts: entry points for console scripts, keys are arbitrary, values should be the associated callable. eg in this specification app_launcher: bin.app_gui.main, you are guarantee that you can import main like list from the python interpreter interface `from pkg_name.bin.app_gui import main`, note the pkg_name was not needed int he config for simplicity, it will be added in the created setup.py file.
2. Run `python make_app.py`. 
3. You should see the created code folder as well as setup.py file in the specified location. Done!
