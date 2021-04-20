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
            copy_binding_file_to_target_dir(d)  # copy binding files
            trans_info = [doc['trans_info']['vendor'], doc['trans_info']['product'], doc['trans_info']['type'], doc['trans_info']['version']]
            trans_path = copy_translation_script_to_target_dir(d, trans_info)
            trans_point_path = doc['trans_point_path']
            script_name = doc['script_name']
            binding_name = doc['binding_name']
            module_name = doc['module_name']
            # print(trans_info, trans_point_path, script_name, binding_name, module_name)
            register_translation_info(trans_point_path, script_name, binding_name, module_name, trans_path, trans_info)


def copy_binding_file_to_target_dir(d):
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
    return trans_path

def register_translation_info(trans_point_path, script_name, binding_name, module_name, trans_path, trans_info):
    register_path = os.path.join(trans_path, 'register.py')
    if os.path.exists(register_path):
        old = open(register_path, 'r')
        old = old.read()
        s1 = "from mediator_server.translation_scripts.%s.%s.%s.%s import %s\n\n" % (trans_info[0], trans_info[1], trans_info[2], trans_info[3].replace('.', '_'), script_name)
        if old.find(s1) == -1:
            old = s1 + old
        s2 = "from mediator_server.yang_bindings import %s\n" % binding_name
        if old.find(s2) == -1:
            old = s2 + old
        s3 = ''''%s': (%s, %s, "%s")''' % (trans_point_path, script_name, binding_name, module_name)
        if old.find(s3) == -1:
            old = old[:-2] + ',' + '\n' + s3 + '\n' + '}'
        with open(register_path, 'w') as f:
            f.write(old)
            f.close()
    else:
        with open(register_path, 'w') as f:
            f.write("from mediator_server.translation_scripts.%s.%s.%s.%s import %s\n" % (trans_info[0], trans_info[1], trans_info[2], trans_info[3].replace('.', '_'), script_name))
            f.write("from mediator_server.yang_bindings import %s\n" % binding_name)
            f.write('''\ntranslate_yang_registry = {
'%s': (%s, %s, "%s")} ''' % (trans_point_path, script_name, binding_name, module_name))
            f.close()

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
