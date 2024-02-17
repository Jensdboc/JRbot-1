map_card_value_to_integer = {
    'deuce': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'jack': 11,
    'queen': 12,
    'king': 13,
    'ace': 14
}


suits = ['diamonds', 'clubs', 'hearts', 'spades']

game_states = {
    "Starting": 0,
    "Playing": 1,
    "Finished": 2
}

player_places = [
    (99, 280),
    (23, 179),
    (23, 75),
    (144, 18),
    (270, 18),
    (406, 18),
    (477, 118),
    (477, 222),
    (361, 280)
]

right_panel_player_places = [
    (545, 120),
    (545, 150),
    (545, 180),
    (545, 210),
    (545, 240),
    (545, 270),
    (545, 300),
    (545, 330),
    (545, 360),
    (545, 390)
]

right_panel_credit_places = [
    (595, 120),
    (595, 150),
    (595, 180),
    (595, 210),
    (595, 240),
    (595, 270),
    (595, 300),
    (595, 330),
    (595, 360),
    (595, 390)
]

cross_places = [
    [(198, 243), (341, 243), (341, 325), (198, 325)],
    [(98, 272), (187, 272), (187, 324), (98, 324)],
    [(15, 180), (70, 180), (70, 265), (15, 265)],
    [(15, 72), (70, 72), (70, 160), (15, 160)],
    [(96, 12), (187, 12), (187, 64), (96, 64)],
    [(224, 12), (314, 12), (314, 64), (224, 64)],
    [(358, 12), (449, 12), (449, 64), (358, 64)],
    [(469, 74), (526, 74), (526, 160), (469, 160)],
    [(469, 177), (526, 177), (526, 264), (469, 264)],
    [(358, 272), (449, 272), (449, 324), (358, 324)],
]

card_places_center = [
    (76, 119),
    (156, 119),
    (236, 119),
    (316, 119),
    (396, 119)
]

own_card_size = (72, 85)
open_card_size = (70, 97)
background_size = (768, 432)
avatar_size = (42, 40)
right_panel_avatar_size = (32, 27)
right_panel_start = (545, 29)

order_of_card_combinations = ['royal_flush', 'straight_flush', 'four_of_a_kind', 'full_house', 'flush', 'straight', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']

other_players_card_size = (47, 58)
other_players_card_rotations = [0, 0, 90, 90, 0, 0, 0, 270, 270, 0]
other_players_card_places_offsets = [
    (0, 0),
    (other_players_card_size[0], 0),
    (0, -other_players_card_size[0]),
    (0, -other_players_card_size[0]),
    (other_players_card_size[0], 0),
    (other_players_card_size[0], 0),
    (other_players_card_size[0], 0),
    (0, other_players_card_size[0]),
    (0, other_players_card_size[0]),
    (other_players_card_size[0], 0)
]
other_players_card_places = [
    (0, 0),
    (97, 270),
    (15, 220),
    (144, 18),
    (270, 18),
    (406, 18),
    (477, 118),
    (477, 222),
    (361, 280)
]
