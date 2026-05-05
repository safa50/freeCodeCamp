def add_setting(settings, item):
    key, value = item
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, item):
    key, value = item
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    # del settings[key]
    settings.pop(key)
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")

    return "\n".join(lines) + "\n"


# Sample dictionary for testing user configuration preferences
# The tests will check that this dictionary exists with some values.
test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': 'enabled'
}

# Example usage - uncomment these lines to see the functions in action
if __name__ == "__main__":
    print("Initial settings:")
    print(view_settings(test_settings))

    print("\nAdding a new setting:")
    result = add_setting(test_settings, ('volume', 'high'))
    print(result)
    print(view_settings(test_settings))

    print("\nUpdating an existing setting:")
    result = update_setting(test_settings, ('theme', 'light'))
    print(result)
    print(view_settings(test_settings))

    print("\nDeleting a setting:")
    result = delete_setting(test_settings, 'notifications')
    print(result)
    print(view_settings(test_settings))
