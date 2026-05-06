import sys
import os

# Add the directory containing user_configuration_manager to the path
sys.path.insert(0, os.path.dirname(__file__))

# Import the functions from the user_configuration_manager module
from user_configuration_manager import add_setting, update_setting, delete_setting, view_settings, test_settings

def test_add_setting():
    print("Testing add_setting function...")

    # Test 1: Adding a new setting
    settings = {'theme': 'light'}
    result = add_setting(settings, ('volume', 'high'))
    expected = "Setting 'volume' added with value 'high' successfully!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert settings['volume'] == 'high', "Setting was not added to dictionary"
    print("✓ Test 1 passed: Adding new setting")

    # Test 2: Trying to add existing setting
    result = add_setting(settings, ('THEME', 'dark'))
    expected = "Setting 'theme' already exists! Cannot add a new setting with this name."
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ Test 2 passed: Preventing duplicate setting")

    # Test 3: Case conversion
    settings2 = {}
    result = add_setting(settings2, ('LANGUAGE', 'ENGLISH'))
    expected = "Setting 'language' added with value 'english' successfully!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert settings2['language'] == 'english', "Case conversion failed"
    print("✓ Test 3 passed: Case conversion")

def test_update_setting():
    print("\nTesting update_setting function...")

    # Test 1: Updating existing setting
    settings = {'theme': 'light'}
    result = update_setting(settings, ('theme', 'dark'))
    expected = "Setting 'theme' updated to 'dark' successfully!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert settings['theme'] == 'dark', "Setting was not updated"
    print("✓ Test 1 passed: Updating existing setting")

    # Test 2: Trying to update non-existing setting
    result = update_setting(settings, ('volume', 'high'))
    expected = "Setting 'volume' does not exist! Cannot update a non-existing setting."
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ Test 2 passed: Preventing update of non-existing setting")

    # Test 3: Case conversion
    settings2 = {'notifications': 'disabled'}
    result = update_setting(settings2, ('NOTIFICATIONS', 'ENABLED'))
    expected = "Setting 'notifications' updated to 'enabled' successfully!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert settings2['notifications'] == 'enabled', "Case conversion failed"
    print("✓ Test 3 passed: Case conversion")

def test_delete_setting():
    print("\nTesting delete_setting function...")

    # Test 1: Deleting existing setting
    settings = {'theme': 'light', 'volume': 'high'}
    result = delete_setting(settings, 'theme')
    expected = "Setting 'theme' deleted successfully!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert 'theme' not in settings, "Setting was not deleted"
    print("✓ Test 1 passed: Deleting existing setting")

    # Test 2: Trying to delete non-existing setting
    result = delete_setting(settings, 'theme')
    expected = "Setting not found!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ Test 2 passed: Handling non-existing setting deletion")

    # Test 3: Case conversion
    settings2 = {'language': 'english'}  # Note: key should be lowercase to match function behavior
    result = delete_setting(settings2, 'LANGUAGE')
    expected = "Setting 'language' deleted successfully!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert 'language' not in settings2, "Setting was not deleted"
    print("✓ Test 3 passed: Case conversion")

def test_view_settings():
    print("\nTesting view_settings function...")

    # Test 1: Empty settings
    result = view_settings({})
    expected = "No settings available."
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ Test 1 passed: Empty settings")

    # Test 2: Non-empty settings
    settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
    result = view_settings(settings)
    expected = "Current User Settings:\nTheme: dark\nNotifications: enabled\nVolume: high\n"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ Test 2 passed: Non-empty settings with proper formatting")

    # Test 3: Single setting
    settings2 = {'language': 'english'}
    result = view_settings(settings2)
    expected = "Current User Settings:\nLanguage: english\n"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ Test 3 passed: Single setting")

def test_test_settings_exists():
    print("\nTesting test_settings dictionary...")

    # Test that test_settings exists and has some values
    assert isinstance(test_settings, dict), "test_settings should be a dictionary"
    assert len(test_settings) > 0, "test_settings should have at least one setting"
    print("✓ Test passed: test_settings dictionary exists with values")

def run_all_tests():
    print("Running all tests for User Configuration Manager...\n")

    try:
        test_add_setting()
        test_update_setting()
        test_delete_setting()
        test_view_settings()
        test_test_settings_exists()

        print("\n🎉 All tests passed! Your User Configuration Manager is working correctly.")

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False

    return True

if __name__ == "__main__":
    run_all_tests()