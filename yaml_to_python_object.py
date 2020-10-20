import json
from yaml import load, Loader

exp_info = [
    {"name": "exp-0", "exp_params_type": "text", "cycle": 0, "cycle_aa": [], "cycle_days": [],
     "params": "{\"list-dnn-disliketf\":\" model_name: biaodan-cvr-sdnn-v6\\n guarantee: biaodan-cvr-sdnn-rf\"}"
     },
    {"name": "exp-1", "exp_params_type": "text", "cycle": 0, "cycle_aa": [], "cycle_days": [],
     "params": "{\"list-ctr-sdnn-merge\":\" model_name: biaodan-cvr-sdnn-rf\\n guarantee: adkddcvr-v4-tf\"}"
     }
]

exp_param_value_sets = set(value for e in exp_info for key, value in json.loads(e['params']).items())
print('exp_param_value_sets')
print(exp_param_value_sets)

model_name_set = set()

# yaml转Python object
for value in exp_param_value_sets:
    print(load(value, Loader=Loader)['model_name'])
    model_name_set.add(load(value, Loader=Loader)['model_name'])
    print("===")

print(model_name_set)



