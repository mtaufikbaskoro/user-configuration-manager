# User Configuration Manager

A simple Python utility for managing user application settings and configurations.

## Overview

This project created for me to learn about managing list, tuple, and dictionary in python. It helps me understand on how to inserting tuple to existing dictionary and updating existing dictionary to another format (example: when i want to make key and value as lowercase).

## Features

- **View Settings**: Display all current configuration settings in a formatted manner
- **Add Setting**: Add new configuration key-value pairs
- **Update Setting**: Modify the value of existing settings
- **Delete Setting**: Remove specific settings from the configuration

## Functions

### `view_settings(settings)`
Displays all current user settings in a readable format.

**Parameters:**
- `settings` (dict): Dictionary containing the current settings

**Returns:**
- String representation of all settings or a message indicating no settings are available

**Example:**
```python
settings = {'theme': 'dark', 'language': 'english'}
print(view_settings(settings))
# Output:
# Current User Settings:
# Theme: dark
# Language: english
```

### `add_setting(settings, setting_pair)`
Adds a new configuration setting to the settings dictionary.

**Parameters:**
- `settings` (dict): Dictionary to store settings
- `setting_pair` (tuple): Tuple containing (key, value)

**Returns:**
- Success message if setting was added
- Error message if setting already exists

**Example:**
```python
add_setting(settings, ('theme', 'dark'))
# Output: Setting 'theme' added with value 'dark' successfully!
```

### `update_setting(settings, setting_pair)`
Updates the value of an existing setting.

**Parameters:**
- `settings` (dict): Dictionary containing settings
- `setting_pair` (tuple): Tuple containing (key, new_value)

**Returns:**
- Success message if setting was updated
- Error message if setting doesn't exist

**Example:**
```python
update_setting(settings, ('theme', 'light'))
# Output: Setting 'theme' updated to 'light' successfully!
```

### `delete_setting(settings, setting_key)`
Removes a setting from the configuration.

**Parameters:**
- `settings` (dict): Dictionary containing settings
- `setting_key` (str): Key of the setting to delete

**Returns:**
- Success message if setting was deleted
- Error message if setting doesn't exist

**Example:**
```python
delete_setting(settings, 'theme')
# Output: Setting 'theme' deleted successfully!
```

## Usage

```python
# Initialize a settings dictionary
test_settings = {
    'theme': 'dark'
}

# Add a new setting
print(add_setting(test_settings, ('notification', 'enable')))

# Delete a setting
print(delete_setting(test_settings, 'notification'))

# View all settings
print(view_settings(test_settings))
```

## Notes

- All keys and values are automatically converted to lowercase for consistency
- Settings are case-insensitive for lookups
- The system prevents duplicate settings with the same key
- Each operation returns informative messages for success or error cases

## Installation

No external dependencies required. Simply run the Python script:

```bash
python main.py
```

## License

This project is part of the freeCodeCamp Python Learning course.
