"""Tests for normalizing structured AI analysis sections."""

import unittest

from trendradar.ai.analyzer import _coerce_analysis_text


class AnalysisResponseNormalizationTests(unittest.TestCase):
    def test_string_is_preserved(self):
        self.assertEqual(_coerce_analysis_text("summary"), "summary")

    def test_list_is_renderable_text(self):
        self.assertEqual(
            _coerce_analysis_text(["first", {"title": "second"}, 3]),
            'first\n{"title": "second"}\n3',
        )

    def test_null_and_scalar_values_are_safe(self):
        self.assertEqual(_coerce_analysis_text(None), "")
        self.assertEqual(_coerce_analysis_text(42), "42")


if __name__ == "__main__":
    unittest.main()
