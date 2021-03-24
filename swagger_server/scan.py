import os
import shutil

import yaml


def load_yaml_file(d):
    yaml_file = os.path.join(d, 'register.yml')
    if not os.path.exists(yaml_file):
        print('%s is not exist!' % yaml_file)
    else:
        with open(yaml_file) as f:
            doc = yaml.safe_load(f)
            cp_binding_file_to_target_dir(d)  # copy binding files
            trans_info = [doc['trans_info']['vendor'], doc['trans_info']['product'], doc['trans_info']['type'], doc['trans_info']['version']]
            copy_translation_script_to_target_dir(d, trans_info)
            # trans_point_path = doc['trans_point_path']
            # script_name = doc['script_name']
            # binding_name = doc['binding_name']
            # module_name = doc['module_name']
            # print(trans_info, trans_point_path, script_name, binding_name, module_name)

def cp_binding_file_to_target_dir(d):
    for root, dirs, files in os.walk(d):
        for file in files:
            cur_path = os.getcwd()
            if 'binding' in file and 'pyc' not in file:
                # print("binding file is: ", file)
                bind_path = os.path.join(cur_path, 'yang_bindings')
                src_file = os.path.join(root, file)
                target_file = os.path.join(bind_path, file)
                try:
                    shutil.copyfile(src_file, target_file)
                    print('copy %s to %s successfully!' % (src_file, target_file))
                except Exception as e:
                    print(e.args)


def copy_translation_script_to_target_dir(d, trans_info):
    cur_path = os.getcwd()
    trans_path = os.path.join(cur_path, 'translation_scripts')  # the dir of translation scripts
    for item in trans_info:
        trans_path = os.path.join(trans_path, item)
        if not os.path.exists(trans_path):
            os.mkdir(trans_path)
            fp = open(os.path.join(trans_path, '__init__.py'), 'w')  # create __init__.py
            fp.close()
    """if the translation dir is not exist, create it"""
    print('translation script dir is :', trans_path)
    for root, dirs, files in os.walk(d):
        for file in files:
            if 'translate' in file and 'pyc' not in file:
                src_file = os.path.join(root, file)
                target_file = os.path.join(trans_path, file)
                try:
                    shutil.copyfile(src_file, target_file)
                    print('copy %s to %s successfully!' % (src_file, target_file))
                except Exception as e:
                    print(e.args)

def main():
    search_path = os.path.join(os.getcwd(), 'developer')
    for root, dirs, files in os.walk(search_path):
        for d in dirs:
            absolute_path = os.path.join(root, d)
            if 'translation' in d:
                load_yaml_file(absolute_path)
                # cp_file_to_target_dir()


if __name__ == '__main__':
    main()
