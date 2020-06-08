import os

from yaml import load, Loader

# ENV_MOD="PROD_MODE"
# ENV_MOD="PRE_MODE"
ENV_MOD="DEV_MODE"

if ENV_MOD == 'PROD_MODE':
    with open(os.path.join(os.path.dirname(__file__), 'settings_prod.yml'), 'r') as file:
        setting = load(file, Loader=Loader)
elif ENV_MOD == 'PRE_MODE':
    with open(os.path.join(os.path.dirname(__file__), 'settings_pre.yml'), 'r') as file:
        setting = load(file, Loader=Loader)
elif ENV_MOD == 'DEV_MODE':
    with open(os.path.join(os.path.dirname(__file__), 'settings_dev.yml'), 'r') as file:
        setting = load(file, Loader=Loader)

print(setting)

