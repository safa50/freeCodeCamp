import unittest
from main import Planet

class TestPlanet(unittest.TestCase):

    def test_planet_class_exists(self):
        self.assertTrue(hasattr(Planet, '__init__'))

    def test_init_method_exists(self):
        self.assertTrue(hasattr(Planet, '__init__'))

    def test_init_parameters(self):
        # Check if __init__ has the correct parameters (this is basic, as Python doesn't enforce parameter names in tests easily)
        import inspect
        sig = inspect.signature(Planet.__init__)
        params = list(sig.parameters.keys())
        self.assertEqual(params, ['self', 'name', 'planet_type', 'star'])

    def test_init_raises_typeerror_for_non_string_name(self):
        with self.assertRaises(TypeError) as cm:
            Planet(123, "type", "star")
        self.assertEqual(str(cm.exception), "name, planet type, and star must be strings")

    def test_init_raises_typeerror_for_non_string_planet_type(self):
        with self.assertRaises(TypeError) as cm:
            Planet("name", 123, "star")
        self.assertEqual(str(cm.exception), "name, planet type, and star must be strings")

    def test_init_raises_typeerror_for_non_string_star(self):
        with self.assertRaises(TypeError) as cm:
            Planet("name", "type", 123)
        self.assertEqual(str(cm.exception), "name, planet type, and star must be strings")

    def test_init_raises_valueerror_for_empty_name(self):
        with self.assertRaises(ValueError) as cm:
            Planet("", "type", "star")
        self.assertEqual(str(cm.exception), "name, planet_type, and star must be non-empty strings")

    def test_init_raises_valueerror_for_empty_planet_type(self):
        with self.assertRaises(ValueError) as cm:
            Planet("name", "", "star")
        self.assertEqual(str(cm.exception), "name, planet_type, and star must be non-empty strings")

    def test_init_raises_valueerror_for_empty_star(self):
        with self.assertRaises(ValueError) as cm:
            Planet("name", "type", "")
        self.assertEqual(str(cm.exception), "name, planet_type, and star must be non-empty strings")

    def test_assigns_name(self):
        p = Planet("Earth", "Terrestrial", "Sun")
        self.assertEqual(p.name, "Earth")

    def test_assigns_planet_type(self):
        p = Planet("Earth", "Terrestrial", "Sun")
        self.assertEqual(p.planet_type, "Terrestrial")

    def test_assigns_star(self):
        p = Planet("Earth", "Terrestrial", "Sun")
        self.assertEqual(p.star, "Sun")

    def test_orbit_method_exists(self):
        self.assertTrue(hasattr(Planet, 'orbit'))

    def test_orbit_returns_correct_string(self):
        p = Planet("Earth", "Terrestrial", "Sun")
        self.assertEqual(p.orbit(), "Earth is orbiting around Sun....")

    def test_str_method_exists(self):
        self.assertTrue(hasattr(Planet, '__str__'))

    def test_str_returns_correct_string(self):
        p = Planet("Earth", "Terrestrial", "Sun")
        self.assertEqual(str(p), "Planet: Earth | Type: Terrestrial | Star: Sun")

    def test_instances_created(self):
        # This assumes the instances are created in main.py when imported
        import main
        self.assertTrue(hasattr(main, 'planet_1'))
        self.assertTrue(hasattr(main, 'planet_2'))
        self.assertTrue(hasattr(main, 'planet_3'))
        self.assertIsInstance(main.planet_1, Planet)
        self.assertIsInstance(main.planet_2, Planet)
        self.assertIsInstance(main.planet_3, Planet)

if __name__ == '__main__':
    unittest.main()