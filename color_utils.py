def parse_color_code(color_code):
    # Split the color code into level and tones
    level, tones = color_code.split('.')

    # The level is the part to the left of the decimal
    level = int(level)

    # The tones are the part to the right of the decimal
    # Each digit represents a different tone
    primary_tone = int(tones[0])
    secondary_tone = int(tones[1]) if len(tones) > 1 else None

    return level, primary_tone, secondary_tone


tone_mapping = {
    0: 'Clear',
    1: 'Blue',
    2: 'Violet',
    3: 'Gold',
    4: 'Orange',
    6: 'Red',
    7: 'Green'
    # Add other mappings here
}

# Use the mapping
primary_tone_color = tone_mapping[primary_tone]
secondary_tone_color = tone_mapping[secondary_tone] if secondary_tone else None
