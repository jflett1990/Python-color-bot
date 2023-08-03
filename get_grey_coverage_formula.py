def get_grey_coverage_formula(grey_percentage, coverage_type):
    # Map the grey coverage formulas
    grey_coverage_formulas = {
        'full': {
            25: '30g Natural, 10g Intense Natural, 60mL 20vol',
            50: '20g Natural, 20g Intense Natural, 60mL 20vol',
            75: '10g Natural, 30g Intense Natural, 30mL 10vol, 30mL 20vol',
            100: '10g Natural, 30g Intense Natural, 60mL 10vol'
        },
        'blended': {
            25: '40g Pre-Blended, 60mL 20vol',
            50: '10g Natural, 30g Pre-Blended, 60mL 20vol',
            75: '20g Natural, 20g Pre-Blended, 60mL 20vol',
            100: '20g Natural, 20g Pre-Blended, 30mL 10vol, 30mL 20vol'
        }
    }

    # Get the appropriate formula
    formula = grey_coverage_formulas.get(coverage_type, {}).get(grey_percentage, '')
    return formula
