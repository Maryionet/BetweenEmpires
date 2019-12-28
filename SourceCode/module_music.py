from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

tracks = [
("bogus", "cant_find_this.ogg", 0, 0),

("main_menu", "main_menu.ogg", mtf_sit_main_title|mtf_start_immediately, mtf_situation_global_map),

("game_start1", "game_start1.ogg", mtf_situation_game_start|mtf_start_immediately, mtf_situation_global_map),

("battle_generic01", "battle_generic01.ogg", mtf_situation_battle, 0),

("victory_heavy01", "victory_heavy01.ogg", mtf_situation_victory_heavy|mtf_situation_victory_light, mtf_situation_global_map),
("victory_heavy02", "victory_heavy02.ogg", mtf_situation_victory_heavy|mtf_situation_victory_light, mtf_situation_global_map),
("victory_heavy03", "victory_heavy03.ogg", mtf_situation_victory_heavy|mtf_situation_victory_light, mtf_situation_global_map),
("victory_heavy04", "victory_heavy04.ogg", mtf_situation_victory_heavy|mtf_situation_victory_light, mtf_situation_global_map),

("globalmap_generic01", "globalmap_generic01.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic01b", "globalmap_generic01b.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic02", "globalmap_generic02.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic03", "globalmap_generic03.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic03b", "globalmap_generic03b.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic04", "globalmap_generic04.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic04b", "globalmap_generic04b.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic05", "globalmap_generic05.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic05b", "globalmap_generic05b.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic06", "globalmap_generic06.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic07", "globalmap_generic07.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic08", "globalmap_generic08.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic09", "globalmap_generic09.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic10", "globalmap_generic10.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic11", "globalmap_generic11.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic12", "globalmap_generic12.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic13", "globalmap_generic13.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic14", "globalmap_generic14.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic15", "globalmap_generic15.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic16", "globalmap_generic16.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic17", "globalmap_generic17.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic18", "globalmap_generic18.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic19", "globalmap_generic19.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic20", "globalmap_generic20.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic21", "globalmap_generic21.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic22", "globalmap_generic22.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic23", "globalmap_generic23.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic24", "globalmap_generic24.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic25", "globalmap_generic25.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic26", "globalmap_generic26.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic27", "globalmap_generic27.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic28", "globalmap_generic28.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic29", "globalmap_generic29.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic30", "globalmap_generic30.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic31", "globalmap_generic31.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic32", "globalmap_generic32.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic33", "globalmap_generic33.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic34", "globalmap_generic34.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic35", "globalmap_generic35.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic36", "globalmap_generic36.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic37", "globalmap_generic37.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic38", "globalmap_generic38.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic39", "globalmap_generic39.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic40", "globalmap_generic40.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic41", "globalmap_generic41.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic42", "globalmap_generic42.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic43", "globalmap_generic43.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic44", "globalmap_generic44.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic45", "globalmap_generic45.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic46", "globalmap_generic46.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic47", "globalmap_generic47.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic48", "globalmap_generic48.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic49", "globalmap_generic49.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic50", "globalmap_generic50.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic51", "globalmap_generic51.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic52", "globalmap_generic52.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),
("globalmap_generic53", "globalmap_generic53.ogg", mtf_culture_europe|mtf_situation_global_map, mtf_culture_middleeast),

("globalmap_easteurope01", "globalmap_easteurope01.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope02", "globalmap_easteurope02.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope02b", "globalmap_easteurope02b.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope03", "globalmap_easteurope03.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope04", "globalmap_easteurope04.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope05", "globalmap_easteurope05.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope05b", "globalmap_easteurope05b.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope06", "globalmap_easteurope06.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope06b", "globalmap_easteurope06b.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope07", "globalmap_easteurope07.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope08", "globalmap_easteurope08.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope09", "globalmap_easteurope09.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope10", "globalmap_easteurope10.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope11", "globalmap_easteurope11.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope12", "globalmap_easteurope12.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope13", "globalmap_easteurope13.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope14", "globalmap_easteurope14.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope15", "globalmap_easteurope15.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope16", "globalmap_easteurope16.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope17", "globalmap_easteurope17.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_easteurope18", "globalmap_easteurope18.ogg", mtf_culture_easteurope|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),

("globalmap_middleeast01", "globalmap_middleeast01.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast01b", "globalmap_middleeast01b.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast02", "globalmap_middleeast02.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast03", "globalmap_middleeast03.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast04", "globalmap_middleeast04.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast04b", "globalmap_middleeast04b.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast05", "globalmap_middleeast05.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast06", "globalmap_middleeast06.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast07", "globalmap_middleeast07.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast08", "globalmap_middleeast08.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast09", "globalmap_middleeast09.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast10", "globalmap_middleeast10.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast11", "globalmap_middleeast11.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast12", "globalmap_middleeast12.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast13", "globalmap_middleeast13.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast14", "globalmap_middleeast14.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast15", "globalmap_middleeast15.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast16", "globalmap_middleeast16.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast17", "globalmap_middleeast17.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast18", "globalmap_middleeast18.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast19", "globalmap_middleeast19.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast20", "globalmap_middleeast20.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast21", "globalmap_middleeast21.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast22", "globalmap_middleeast22.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast23", "globalmap_middleeast23.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast24", "globalmap_middleeast24.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),
("globalmap_middleeast25", "globalmap_middleeast25.ogg", mtf_culture_middleeast|mtf_situation_global_map, 0),

("globalmap_spain01", "globalmap_spain01.ogg", mtf_culture_spain|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_spain02", "globalmap_spain02.ogg", mtf_culture_spain|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_spain03", "globalmap_spain03.ogg", mtf_culture_spain|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_spain04", "globalmap_spain04.ogg", mtf_culture_spain|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
("globalmap_spain05", "globalmap_spain05.ogg", mtf_culture_spain|mtf_situation_global_map, mtf_culture_middleeast|mtf_culture_europe),
]
