# General game states
GENERAL_GAME_STATES = {
  'HELP': 'help',
  'CHARACTER_STATS': 'stats',
}

# Layer States
FIRST_LAYER_STATES = {
  'INITIALISE': 'game_initialise',
  'GAME_START': 'game_start',
  'CHARACTER_CREATION': 'create_character_stats',
  'ROOM_PICKUP_FIRST_LAYER': 'room_pickup_first_layer',
  'ROOM_DOOR_CHOICE_FIRST_LAYER': 'room_door_choice_first_layer'
}
SECOND_LAYER_STATES = {
  'FIGHT_SECOND_LAYER': 'fight_second_layer'
}
END_STATES = {
  'END': 'end_of_game'
}
