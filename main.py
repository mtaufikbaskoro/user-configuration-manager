def view_settings(settings):
    if not settings:
        return 'No settings available.'
    configuration = 'Current User Settings:\n'
    for key, value in settings.items():
        configuration += f'{key.title()}: {value}\n'
    return configuration

def add_setting(settings, setting_pair):
    key = setting_pair[0].lower()
    value = setting_pair[-1].lower()

    settings_lower = {k.lower(): v.lower() for k, v in settings.items()}
    settings.clear()
    settings.update(settings_lower)

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
        

def update_setting(settings, setting_pair):
    key = setting_pair[0].lower()
    value = setting_pair[-1].lower()

    settings_lower = {k.lower(): v.lower() for k, v in settings.items()}
    settings.clear()
    settings.update(settings_lower)

    if not key in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings, setting_key):
    key = setting_key.lower()

    if not key in settings:
        return f"Setting not found!"
    
    del settings[key]
    return f"Setting '{key}' deleted successfully!"

test_settings = {
    'theme': 'dark'
}

print(add_setting(test_settings, ('notification', 'enable')))
print(delete_setting(test_settings, 'notification'))
print(view_settings(test_settings))