import configparser
import os

dash_cfg = os.getcwd() + "/config/settings_private.ini"


def read_config(public=True):
    config = configparser.ConfigParser()
    if public == False:
        config.read(os.getcwd() + "/config/private_settings.ini")
        dash_cfg = os.getcwd() + "/config/private_dashboard.cfg"
        return dash_cfg, config
    elif public == True:
        config.read(os.getcwd() + "/config/public_settings.ini")
        dash_cfg = os.getcwd() + "/config/public_dashboard.cfg"
        return dash_cfg, config


dash_cfg, config = read_config(public=False)
