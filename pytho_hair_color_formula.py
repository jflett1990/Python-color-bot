import csv
import logging
import configparser
from abc import ABC, abstractmethod

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Abstract strategies
class HairColorFormulaStrategy(ABC):
    @abstractmethod
    def choose_developer(self, natural_level, desired_level, hair_condition):
        pass

    @abstractmethod
    def get_grey_coverage_formula(self, grey_percentage):
        pass

    @abstractmethod
    def choose_push_tone(self, desired_tone):
        pass

# Concrete strategies
class DefaultHairColorFormulaStrategy(HairColorFormulaStrategy):
    def choose_developer(self, natural_level, desired_level, hair_condition):
        if natural_level <= desired_level:
            return "10 vol"
        elif natural_level + 1 <= desired_level:
            return "20 vol"
        elif natural_level + 2 <= desired_level:
            return "30 vol"
        else:
            return "40 vol"

    def get_grey_coverage_formula(self, grey_percentage):
        if grey_percentage <= 25:
            return "1"
        elif grey_percentage <= 50:
            return "2"
        else:
            return "3"

    def choose_push_tone(self, desired_tone):
        if desired_tone == "neutral":
            return ""
        elif desired_tone == "warm":
            return "W"
        else:
            return "C"

class HairColorFormula:
    def __init__(self, natural_level, desired_level, desired_tone, grey_percentage, coverage_type, hair_condition, desired_result, desired_color, formula_strategy):
        self.natural_level = natural_level
        self.desired_level = desired_level
        self.desired_tone = desired_tone
        self.grey_percentage = grey_percentage
        self.coverage_type = coverage_type
        self.hair_condition = hair_condition
        self.desired_result = desired_result
        self.desired_color = desired_color

        self.formula_strategy = formula_strategy
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def create_formula(self):
        try:
            developer = self.formula_strategy.choose_developer(self.natural_level, self.desired_level, self.hair_condition)
            formula = grey_coverage_formulas.get(str(coverage_type), {}).get(grey_percentage, 11)

            push_tone = self.formula_strategy.choose_push_tone(self.desired_tone)
            formula = f"{developer} {formula} {push_tone}"
            return formula
        except Exception as e:
            logging.error(f"Error occurred while creating formula: {e}")
            return None

# Unit tests
class HairColorFormulaTest(unittest.TestCase):
    def test_create_formula(self):
        formula_strategy = DefaultHairColorFormulaStrategy()
        hair_color_formula = HairColorFormula(1, 5, 'neutral', 25, 'full', 'normal', 'vibrant', 'blue', formula_strategy)
        expected_formula = "30 vol W"
        actual_formula = hair_color_formula.create_formula()
        self.assertEqual
