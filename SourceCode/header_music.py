###################################################
# header_music.py
# This file contains declarations for music tracks
# DO NOT EDIT THIS FILE!
###################################################


mtf_culture_1                          = 0x00000001
mtf_culture_2                          = 0x00000002
mtf_culture_3                          = 0x00000004
mtf_culture_4                          = 0x00000008
mtf_culture_5                          = 0x00000010
mtf_culture_6                          = 0x00000020
mtf_culture_all                        = 0x0000003F


##mtf_sit_map_travel                 = 0x00000001
##mtf_sit_attack                     = 0x00000002
##mtf_sit_defense                    = 0x00000004
##mtf_sit_raid_attack                = 0x00000010
##mtf_sit_raid_defense               = 0x00000020
##
mtf_looping                            = 0x00000040
mtf_start_immediately                  = 0x00000080
mtf_persist_until_finished             = 0x00000100

mtf_sit_tavern                         = 0x00000200
mtf_sit_fight                          = 0x00000400
mtf_sit_multiplayer_fight              = 0x00000800
mtf_sit_ambushed                       = 0x00001000
mtf_sit_town                           = 0x00002000
mtf_sit_town_infiltrate                = 0x00004000
mtf_sit_killed                         = 0x00008000
mtf_sit_travel                         = 0x00010000
mtf_sit_arena                          = 0x00020000
mtf_sit_siege                          = 0x00040000
mtf_sit_night                          = 0x00080000
mtf_sit_day                            = 0x00100000
mtf_sit_encounter_hostile              = 0x00200000
mtf_sit_main_title                     = 0x00400000
mtf_sit_victorious                     = 0x00800000
mtf_sit_feast                          = 0x01000000
mtf_module_track                       = 0x10000000 ##set this flag for tracks placed under module folder

mtf_situation_global_map = mtf_sit_tavern
mtf_situation_battle = mtf_sit_ambushed
mtf_situation_defeat = mtf_sit_town
mtf_situation_victory_light = mtf_sit_town_infiltrate
mtf_situation_victory_heavy = mtf_sit_siege
mtf_situation_headquarters = mtf_sit_killed
mtf_situation_silence = mtf_sit_travel
mtf_situation_prebattle = mtf_sit_arena
mtf_situation_siege_attacker_preparing = mtf_sit_night
mtf_situation_game_start = mtf_sit_fight
mtf_situation_siege_assault = mtf_sit_feast

mtf_culture_westeurope = mtf_culture_1
mtf_culture_easteurope = mtf_culture_2
mtf_culture_middleeast = mtf_culture_3
mtf_culture_spain = mtf_culture_4
mtf_culture_europe = mtf_culture_westeurope|mtf_culture_easteurope|mtf_culture_spain
