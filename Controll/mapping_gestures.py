from .Actions.simple_actions import low_light, disable_light, bright_light
def map_command_to_gesture(gesture):
    mapping_dictionary = {
        "FIVE": low_light,
        "FIST": disable_light,
        "HARD": bright_light,
        "FUCK": exit
    }
    
    mapping_dictionary.get(gesture, "No gesture in mapping dictionary")()