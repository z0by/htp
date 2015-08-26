# -*- coding: utf-8 -*-

import ast
import os
import sys
import jinja2
import time
import codecs


def get_docstring(module):
    """
    Function take ast object and return  docstring from it
    """
    docstring = ast.get_docstring(module)
    if docstring:
        return docstring
    return None


def object_list(module, node_type):
    """
    Function generate  nodes comprehensions from module abstract syntax tree(ast) for given nody_type
    """
    return [node for node in module.body if isinstance(node, node_type)]


def timer(f):
    """
    Decorator for counting render time
    """
    def wrapper(*args, **kwargs):
        t_start = time.time()
        f(*args, **kwargs)
        t_end = time.time()
        t_result = t_end - t_start
        res = f(t_result = t_result, *args, **kwargs)
        return res
    return wrapper


@timer
def render_template(*args, **kwargs):
    """
    Function render jinja template and return html object
    """
    templateLoader = jinja2.FileSystemLoader(searchpath=".")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template_file = "index.jinja"
    template = templateEnv.get_template(template_file)
    outputhtml = template.render(*args, **kwargs).encode("utf-8")
    return outputhtml


def write_html(html):
    """
    Function write html file
    """
    with codecs.open("index.html", "wb",  "utf-8") as f:
        f.write(html)


def run(path):
    """
    Main fucntion. 
    Traverse directory in specified path argument and return list of dictionaries.
    Each dictionaries has the following form:
    {'Module filepath':[ Module docstring, { Class name:[Class docstring,[{Class method name:Class method docstrong}]],[{Function name:Function docstring}]}]}     
    """
    _module_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                _func_dict = {}
                _method_dict = {}
                _class_dict = {}
                _module_dict = {}
                filepath = os.path.join(root, file)
                filename = file.replace('.py', '')
                with open(filepath) as fd:
                    file_contents = fd.read()
                try:
                    module = ast.parse(file_contents)
                except:
                    pass
                module_docstring = get_docstring(module)
                class_definitions = object_list(module, ast.ClassDef)
                for class_def in class_definitions:
                    method_definitions = object_list(class_def,
                                                     ast.FunctionDef)
                    class_docstring = get_docstring(class_def)
                    for method_def in method_definitions:
                        method_docstring = get_docstring(method_def)
                        if method_docstring:
                            _method_dict[method_def.name] = method_docstring
                    _class_dict[class_def.name] = [class_docstring,
                                                   [_method_dict]]
                function_definitions = object_list(module, ast.FunctionDef)
                for func_def in function_definitions:
                    function_docstring = get_docstring(func_def)
                    if function_docstring:
                        _func_dict[func_def.name] = function_docstring

                _module_dict[filepath] = [module_docstring,
                                         [_class_dict], _func_dict]
                _module_list.append(_module_dict)
    return _module_list


if __name__ == '__main__':
    path = sys.argv[1:]
    if len(path) < 1:
        raise Exception('Specify the directory')
    if os.path.exists(path[0]):
        module_dict_list = run(path[0])
        result_list = []
        for module_dict in module_dict_list:
            for key, value in module_dict.iteritems():
                module_docstring = value[0]
                class_dict = value[1][0]
                func_dict = value[2]
                if module_docstring or class_dict or func_dict:
                    result_list.append(module_dict)
        render = render_template(result_list = result_list, path = path[0])
        write_html(render)
