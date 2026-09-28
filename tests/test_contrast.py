import importlib.util
import unittest
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "skills/game-tool-visual-director/scripts/contrast.py"
spec = importlib.util.spec_from_file_location("visual_contrast", path)
contrast = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contrast)


class ContrastTests(unittest.TestCase):
    def test_known_extremes(self):
        self.assertEqual(contrast.measure("#000", "#fff")["ratio"], 21)
        self.assertEqual(contrast.measure("#fff", "#fff")["ratio"], 1)

    def test_rounding_cannot_turn_failure_into_pass(self):
        passing = contrast.measure("#767676", "#FFFFFF")
        failing = contrast.measure("#777777", "#FFFFFF")
        self.assertTrue(passing["threshold_matches"]["4.5:1"])
        self.assertEqual(round(failing["ratio"], 1), 4.5)
        self.assertFalse(failing["threshold_matches"]["4.5:1"])

    def test_transparency_and_unresolved_color_spaces_rejected(self):
        for value in ("#ffffff80", "rgba(0,0,0,0.5)", "oklch(60% 0.1 20)", "#zzzzzz"):
            with self.assertRaises(ValueError):
                contrast.measure(value, "#fff")


if __name__ == "__main__":
    unittest.main()
