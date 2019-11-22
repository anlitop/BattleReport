from json import dumps,load,dump
import json
import numpy

class NpEncoder(json.JSONEncoder):
    def default(self, obj):# pylint: disable=E0202
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def get_config(name):
    with open(name,'r',encoding = 'utf-8') as f:
        return load(f)
def save_config(kdict):
    content=dumps(kdict,ensure_ascii=False,cls=NpEncoder)
    with open("Config.json",'w',encoding = 'utf-8') as f:
        f.write(content)
def save_dict(kdict):
    content=dumps(kdict,ensure_ascii=False,cls=NpEncoder)
    with open("Config.json",'w',encoding = 'utf-8') as f:
        f.write(content)
def get_dict(name):
    with open(name,'r',encoding = 'utf-8') as f:
        return load(f)