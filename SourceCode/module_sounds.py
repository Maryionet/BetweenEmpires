from header_sounds import *

sounds = [
 ("click", sf_2d|sf_vol_3,["drum_3.ogg"]),
 ("tutorial_1", sf_2d|sf_vol_7,["tutorial_1.ogg"]),
 ("tutorial_2", sf_2d|sf_vol_7,["tutorial_2.ogg"]),
 ("gong", sf_2d|sf_priority_9|sf_vol_7, ["s_cymbals.ogg"]),
 ("quest_taken", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_completed", sf_2d|sf_priority_9|sf_vol_8, ["quest_completed.ogg"]),
 ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_6, ["quest_succeeded.ogg"]),
 ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, ["quest_concluded.ogg"]),
 ("quest_failed", sf_2d|sf_priority_9|sf_vol_7, ["quest_failed.ogg"]),
 ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, ["quest_cancelled.ogg"]),
 ("rain",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["rain_1.ogg"]),
 ("money_received",sf_2d|sf_priority_10|sf_vol_4, ["coins_dropped_1.ogg"]),
 ("money_paid",sf_2d|sf_priority_10|sf_vol_10, ["coins_dropped_2.ogg"]),
 ("sword_clash_1", sf_priority_5|sf_vol_8,["sword_clank_metal_09.ogg","sword_clank_metal_09b.ogg","sword_clank_metal_10.ogg","sword_clank_metal_10b.ogg","sword_clank_metal_12.ogg","sword_clank_metal_12b.ogg","sword_clank_metal_13.ogg","sword_clank_metal_13b.ogg"]),
 ("sword_clash_2", sf_priority_5|sf_vol_9,["s_swordClash2.wav"]),
 ("sword_clash_3", sf_priority_5|sf_vol_9,["s_swordClash3.wav"]),
 ("sword_swing", sf_vol_8|sf_priority_2,["melee_swing1.wav","melee_swing2.wav","melee_swing3.wav","melee_swing4.wav","melee_swing5.wav","melee_swing6.wav"]),
 ("footstep_grass", sf_vol_2|sf_priority_1,["footstep_grass1.wav","footstep_grass2.wav","footstep_grass3.wav","footstep_grass4.wav","footstep_grass5.wav","footstep_grass6.wav","footstep_grass7.wav","footstep_grass8.wav","footstep_grass9.wav","footstep_grass10.wav","footstep_grass11.wav","footstep_grass12.wav","footstep_grass13.wav","footstep_grass14.wav","footstep_grass15.wav","footstep_grass16.wav","footstep_grass17.wav","footstep_grass18.wav","footstep_grass19.wav","footstep_grass20.wav","footstep_grass21.wav","footstep_grass22.wav","footstep_grass23.wav","footstep_grass24.wav","footstep_grass25.wav","footstep_grass26.wav","footstep_grass27.wav","footstep_grass28.wav","footstep_grass29.wav","footstep_grass30.wav","footstep_grass31.wav","footstep_grass32.wav"]),
 ("footstep_wood", sf_vol_5|sf_priority_1,["footstep_wood_1.ogg","footstep_wood_2.ogg","footstep_wood_4.ogg"]),
# ("footstep_wood", sf_vol_3|sf_priority_1,["footstep_stone_1.ogg","footstep_stone_3.ogg","footstep_stone_4.ogg"]),
 ("footstep_water", sf_vol_4|sf_priority_3,["water_walk_1.ogg","water_walk_2.ogg","water_walk_3.ogg","water_walk_4.ogg"]),
 ("footstep_horse",sf_priority_3|sf_vol_8, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
# ("footstep_horse",0, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
# ("footstep_horse_1f",sf_priority_3|sf_vol_8, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
 ("footstep_horse_2b",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav"]),
 ("footstep_horse_2f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2f.wav"]),
 ("footstep_horse_3b",sf_priority_3|sf_vol_8, ["s_footstep_horse_3b.wav"]),
 ("footstep_horse_3f",sf_priority_3|sf_vol_8, ["s_footstep_horse_3f.wav"]),
 ("footstep_horse_4b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav"]),
 ("footstep_horse_4f",sf_priority_3|sf_vol_8, ["s_footstep_horse_4f.wav"]),
 ("footstep_horse_5b",sf_priority_3|sf_vol_8, ["s_footstep_horse_5b.wav"]),
 ("footstep_horse_5f",sf_priority_3|sf_vol_8, ["s_footstep_horse_5f.wav"]),
 ("jump_begin", sf_vol_6|sf_priority_9,["jump_begin.ogg"]),
 ("jump_end", sf_vol_5|sf_priority_9,["jump_end.ogg"]),
 ("jump_begin_water", sf_vol_3|sf_priority_9,["jump_begin_water.ogg"]),
 ("jump_end_water", sf_vol_3|sf_priority_9,["jump_end_water.ogg"]),
 ("horse_jump_begin", sf_vol_6|sf_priority_9,["horse_jump_begin.ogg"]),
 ("horse_jump_end", sf_vol_7|sf_priority_9,["horse_jump_end.ogg"]),
 ("horse_jump_begin_water", sf_vol_6|sf_priority_9,["jump_begin_water.ogg"]),
 ("horse_jump_end_water", sf_vol_6|sf_priority_9,["jump_end_water.ogg"]),

 ("release_bow",sf_vol_4, ["release_bow_1.ogg"]),
 ("release_crossbow",sf_vol_7, ["none.ogg"]),
 ("throw_javelin",sf_vol_5, ["throw_javelin_2.ogg"]),
 ("throw_axe",sf_vol_7, ["throw_axe_1.ogg"]),
 ("throw_knife",sf_vol_5, ["throw_knife_1.ogg"]),
 ("throw_stone",sf_vol_7, ["throw_stone_1.ogg"]),

 ("reload_crossbow",sf_vol_3, ["none.ogg"]),
 ("reload_crossbow_continue",sf_vol_6, ["none.ogg"]),
 ("pull_bow",sf_vol_5, ["pull_bow_1.ogg"]),
 ("pull_arrow",sf_vol_5, ["pull_arrow.ogg"]),

 ("arrow_pass_by",sf_priority_7, ["arrow_pass_by_1.ogg","arrow_pass_by_2.ogg","arrow_pass_by_3.ogg","arrow_pass_by_4.ogg"]),
 ("bolt_pass_by",sf_priority_7, ["bullet_pass1.wav","bullet_pass2.wav","bullet_pass3.wav","bullet_pass4.wav","bullet_pass5.wav","bullet_pass6.wav","bullet_pass7.wav","bullet_pass8.wav","bullet_pass9.wav","bullet_pass10.wav","bullet_pass11.wav","bullet_pass12.wav","bullet_pass13.wav","bullet_pass14.wav","bullet_pass15.wav","bullet_pass16.wav","bullet_pass17.wav","bullet_pass18.wav","bullet_pass19.wav","bullet_pass20.wav","bullet_pass21.wav","bullet_pass22.wav","bullet_pass23.wav","bullet_pass24.wav","bullet_pass25.wav","bullet_pass26.wav","bullet_pass27.wav","bullet_pass28.wav","bullet_pass29.wav","bullet_pass30.wav","bullet_pass31.wav","bullet_pass32.wav"]),
 ("javelin_pass_by",sf_priority_7, ["javelin_pass_by_1.ogg","javelin_pass_by_2.ogg"]),
 ("stone_pass_by",sf_vol_9|sf_priority_7, ["stone_pass_by_1.ogg"]),
 ("axe_pass_by",sf_priority_7, ["axe_pass_by_1.ogg"]),
 ("knife_pass_by",sf_priority_7, ["knife_pass_by_1.ogg"]),
 ("bullet_pass_by",sf_priority_7, ["bullet_pass1.wav","bullet_pass2.wav","bullet_pass3.wav","bullet_pass4.wav","bullet_pass5.wav","bullet_pass6.wav","bullet_pass7.wav","bullet_pass8.wav","bullet_pass9.wav","bullet_pass10.wav","bullet_pass11.wav","bullet_pass12.wav","bullet_pass13.wav","bullet_pass14.wav","bullet_pass15.wav","bullet_pass16.wav","bullet_pass17.wav","bullet_pass18.wav","bullet_pass19.wav","bullet_pass20.wav","bullet_pass21.wav","bullet_pass22.wav","bullet_pass23.wav","bullet_pass24.wav","bullet_pass25.wav","bullet_pass26.wav","bullet_pass27.wav","bullet_pass28.wav","bullet_pass29.wav","bullet_pass30.wav","bullet_pass31.wav","bullet_pass32.wav"]),
 
 ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_7, ["bullet_hit_ground1.wav","bullet_hit_ground2.wav","bullet_hit_ground3.wav","bullet_hit_ground4.wav","bullet_hit_ground5.wav"]),
 ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_bullet_hit_ground",sf_priority_7|sf_vol_7, ["bullet_hit_ground1.wav","bullet_hit_ground2.wav","bullet_hit_ground3.wav","bullet_hit_ground4.wav","bullet_hit_ground5.wav"]),

 ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_7,  ["bullet_hit_ground1.wav","bullet_hit_ground2.wav","bullet_hit_ground3.wav","bullet_hit_ground4.wav","bullet_hit_ground5.wav"]),
 ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_10, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_7, ["bullet_hit_ground1.wav","bullet_hit_ground2.wav","bullet_hit_ground3.wav","bullet_hit_ground4.wav","bullet_hit_ground5.wav"]),


 ("draw_sword",sf_priority_2|sf_vol_4, ["draw_sword.ogg"]),
 ("put_back_sword",sf_priority_1|sf_vol_4, ["put_back_sword.ogg"]),
 ("draw_greatsword",sf_priority_2|sf_vol_4, ["draw_greatsword.ogg"]),
 ("put_back_greatsword",sf_priority_1|sf_vol_4, ["put_back_sword.ogg"]),
 ("draw_axe",sf_priority_2|sf_vol_4, ["draw_mace.ogg"]),
 ("put_back_axe",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_greataxe",sf_priority_2|sf_vol_4, ["draw_greataxe.ogg"]),
 ("put_back_greataxe",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_spear",sf_priority_2|sf_vol_4, ["draw_spear.ogg"]),
 ("put_back_spear",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_crossbow",sf_priority_2|sf_vol_4, ["rifle_deploy1.wav","rifle_deploy2.wav","rifle_deploy3.wav"]),
 ("put_back_crossbow",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_revolver",sf_priority_2|sf_vol_4, ["pistol_deploy1.wav","pistol_deploy2.wav","pistol_deploy3.wav"]),
 ("put_back_revolver",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_dagger",sf_priority_2|sf_vol_4, ["draw_dagger.ogg"]),
 ("put_back_dagger",sf_priority_1|sf_vol_4, ["put_back_dagger.ogg"]),
 ("draw_bow",sf_priority_2|sf_vol_4, ["draw_bow.ogg"]),
 ("put_back_bow",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_shield",sf_priority_2|sf_vol_4, ["draw_shield.ogg"]),
 ("put_back_shield",sf_priority_1|sf_vol_4, ["put_back_shield.ogg"]),
 ("draw_other",sf_priority_2|sf_vol_4, ["draw_other.ogg"]),
 ("put_back_other",sf_priority_1|sf_vol_4, ["draw_other2.ogg"]),

 ("body_fall_small",sf_priority_5|sf_vol_9, ["body_fall_small_1.ogg","body_fall_small_2.ogg"]),
 ("body_fall_big",sf_priority_6|sf_vol_8, ["body_fall_1.ogg","body_fall_2.ogg","body_fall_3.ogg"]),
# ("body_fall_very_big",sf_priority_9|sf_vol_10, ["body_fall_very_big_1.ogg"]),
 ("horse_body_fall_begin",sf_priority_6|sf_vol_10, ["horse_body_fall_begin_1.ogg"]),
 ("horse_body_fall_end",sf_priority_6|sf_vol_10, ["horse_body_fall_end_1.ogg","body_fall_2.ogg","body_fall_very_big_1.ogg"]),
 
## ("clang_metal",sf_priority_9, ["clang_metal_1.ogg","clang_metal_2.ogg","s_swordClash1.wav","s_swordClash2.wav","s_swordClash3.wav"]),
 ("hit_wood_wood",sf_priority_7|sf_vol_12, ["hit_wood_wood_1.ogg","hit_wood_wood_2.ogg","hit_wood_wood_3.ogg","hit_wood_wood_4.ogg","hit_wood_metal_4.ogg","hit_wood_metal_5.ogg","hit_wood_metal_6.ogg"]),#dummy
 ("hit_metal_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_3.ogg","hit_metal_metal_4.ogg",
                                              "hit_metal_metal_5.ogg","hit_metal_metal_6.ogg","hit_metal_metal_7.ogg","hit_metal_metal_8.ogg",
                                              "hit_metal_metal_9.ogg","hit_metal_metal_10.ogg",
                                              "clang_metal_1.ogg","clang_metal_2.ogg"]),
 ("hit_wood_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_1.ogg","hit_metal_metal_2.ogg","hit_wood_metal_7.ogg"]),
# ("clang_metal", sf_priority_9,["sword_clank_metal_09.ogg","sword_clank_metal_10.ogg","sword_clank_metal_12.ogg","sword_clank_metal_13.ogg"]),
## ("shield_hit_cut",sf_priority_5, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg"]),
 ("shield_hit_wood_wood",sf_priority_7|sf_vol_9, ["shield_hit_wood_wood_1.ogg","shield_hit_wood_wood_2.ogg","shield_hit_wood_wood_3.ogg"]),
 ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_hit_metal_metal_1.ogg","shield_hit_metal_metal_2.ogg","shield_hit_metal_metal_3.ogg","shield_hit_metal_metal_4.ogg"]),
 ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg","shield_hit_cut_10.ogg"]), #(shield is wood)
 ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_hit_metal_wood_1.ogg","shield_hit_metal_wood_2.ogg","shield_hit_metal_wood_3.ogg"]),#(shield is metal)
 ("shield_broken",sf_priority_9, ["shield_broken.ogg"]),
 ("man_hit",sf_priority_7|sf_vol_7, ["manhit1.wav","manhit2.wav","manhit3.wav","manhit4.wav","manhit5.wav","manhit6.wav","manhit7.wav","manhit8.wav","manhit9.wav","manhit10.wav","manhit11.wav","manhit12.wav","manhit13.wav","manhit14.wav","manhit15.wav","manhit16.wav","manhit17.wav","manhit18.wav","manhit19.wav","manhit20.wav","manhit21.wav","manhit22.wav","manhit23.wav","manhit24.wav","manhit25.wav","manhit26.wav","manhit27.wav","manhit28.wav","manhit29.wav","manhit30.wav","manhit31.wav","manhit32.wav"]),
 ("man_die",sf_priority_10|sf_vol_8,  []),# ["man_fall_1.ogg","man_fall_2.ogg","man_fall_3.ogg","man_fall_4.ogg"]),
 ("woman_hit",sf_priority_7|sf_vol_2, ["womanhit1.wav","womanhit2.wav","womanhit3.wav","womanhit4.wav","womanhit5.wav","womanhit6.wav","womanhit7.wav","womanhit8.wav","womanhit9.wav","womanhit10.wav","womanhit11.wav","womanhit12.wav","womanhit13.wav","womanhit14.wav","womanhit15.wav","womanhit16.wav","womanhit17.wav","womanhit18.wav","womanhit19.wav","womanhit20.wav","womanhit21.wav","womanhit22.wav","womanhit23.wav","womanhit24.wav","womanhit25.wav","womanhit26.wav","womanhit27.wav","womanhit28.wav","womanhit29.wav","womanhit30.wav","womanhit31.wav","womanhit32.wav"]),
 ("woman_die",sf_priority_10|sf_vol_9, []),
 ("woman_yell",sf_priority_8|sf_vol_9, []),
 ("hide",0, ["s_hide.wav"]),
 ("unhide",0, ["s_unhide.wav"]),
 ("neigh",0, ["horse_exterior_whinny_01.ogg","horse_exterior_whinny_02.ogg","horse_exterior_whinny_03.ogg","horse_exterior_whinny_04.ogg","horse_exterior_whinny_05.ogg","horse_whinny.ogg"]),
 ("gallop",sf_vol_4, ["horse_gallop_3.ogg","horse_gallop_4.ogg","horse_gallop_5.ogg"]),
 ("battle",sf_vol_4, ["battle.ogg"]),
# ("bow_shoot_player",sf_priority_10|sf_vol_10, ["bow_shoot_4.ogg"]),
# ("bow_shoot",sf_priority_4, ["bow_shoot_4.ogg"]),
# ("crossbow_shoot",sf_priority_4, ["bow_shoot_2.ogg"]),
 ("arrow_hit_body",sf_priority_4, ["arrow_hit_body_1.ogg","arrow_hit_body_2.ogg","arrow_hit_body_3.ogg"]),
 ("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_lo_dmg_1.ogg","sword_hit_lo_armor_lo_dmg_2.ogg","sword_hit_lo_armor_lo_dmg_3.ogg"]),
 ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["meleeimpact1.wav","meleeimpact2.wav","meleeimpact3.wav","meleeimpact4.wav","meleeimpact5.wav","meleeimpact6.wav","meleeimpact7.wav","meleeimpact8.wav","meleeimpact9.wav","meleeimpact10.wav","meleeimpact11.wav","meleeimpact12.wav","meleeimpact13.wav","meleeimpact14.wav","meleeimpact15.wav","meleeimpact16.wav","meleeimpact17.wav"]),
 ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_hit_high_armor_low_damage.ogg","metal_hit_high_armor_low_damage_2.ogg","metal_hit_high_armor_low_damage_3.ogg"]),
 ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_hi_armor_hi_dmg_1.ogg","sword_hit_hi_armor_hi_dmg_2.ogg","sword_hit_hi_armor_hi_dmg_3.ogg"]),
 ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_hit_low_1.ogg","blunt_hit_low_2.ogg","blunt_hit_low_3.ogg"]),
 ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["wooden_hit_high_armor_low_damage.ogg","wooden_hit_high_armor_low_damage_2.ogg"]),
 ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("mp_arrow_hit_target",sf_2d|sf_priority_15|sf_vol_9, ["mp_arrow_hit_target.ogg"]),
 ("blunt_hit",sf_priority_5|sf_vol_9, ["punch_1.ogg","punch_4.ogg","punch_4.ogg","punch_5.ogg"]),
 ("player_hit_by_arrow",sf_priority_10|sf_vol_10, ["player_hit_by_arrow.ogg"]),
 ("pistol_shot",sf_priority_10|sf_vol_10, ["fl_pistol.wav"]),
 ("man_grunt",sf_priority_8|sf_vol_7,  ["maneffort1.wav","maneffort2.wav","maneffort3.wav","maneffort4.wav","maneffort5.wav","maneffort6.wav","maneffort7.wav","maneffort8.wav","maneffort9.wav","maneffort10.wav","maneffort11.wav","maneffort12.wav","maneffort13.wav","maneffort14.wav","maneffort15.wav","maneffort16.wav","maneffort17.wav","maneffort18.wav","maneffort19.wav","maneffort20.wav","maneffort21.wav","maneffort22.wav","maneffort23.wav","maneffort24.wav"]),
 ("man_breath_hard",sf_priority_3|sf_vol_8, ["man_ugh_1.ogg","man_ugh_2.ogg","man_ugh_4.ogg","man_ugh_7.ogg","man_ugh_12.ogg","man_ugh_13.ogg","man_ugh_17.ogg"]),
 ("man_stun",sf_priority_3|sf_vol_8, ["man_stun_1.ogg"]),
 ("man_grunt_long",sf_priority_6|sf_vol_2,  ["maneffort1.wav","maneffort2.wav","maneffort3.wav","maneffort4.wav","maneffort5.wav","maneffort6.wav","maneffort7.wav","maneffort8.wav","maneffort9.wav","maneffort10.wav","maneffort11.wav","maneffort12.wav","maneffort13.wav","maneffort14.wav","maneffort15.wav","maneffort16.wav","maneffort17.wav","maneffort18.wav","maneffort19.wav","maneffort20.wav","maneffort21.wav","maneffort22.wav","maneffort23.wav","maneffort24.wav"]),
 ("man_yell",sf_priority_5|sf_vol_5,["yell1.wav","yell2.wav","yell3.wav","yell4.wav","yell5.wav","yell6.wav","yell7.wav","yell8.wav","yell9.wav","yell10.wav","yell11.wav","yell12.wav","yell13.wav","yell14.wav","yell15.wav","yell16.wav","yell17.wav","yell18.wav","yell19.wav","yell20.wav","yell21.wav","yell22.wav","yell23.wav","yell24.wav","yell25.wav","yell26.wav","yell27.wav","yell28.wav","yell29.wav","yell30.wav","yell31.wav","yell32.wav"]),
 
 ("man_warcry",sf_priority_5, ["man_insult_2.ogg","man_insult_3.ogg","man_insult_7.ogg","man_insult_9.ogg","man_insult_13.ogg","man_insult_15.ogg","man_insult_16.ogg"]),

 ("encounter_looters",sf_2d|sf_vol_8, ["encounter_river_pirates_5.ogg","encounter_river_pirates_6.ogg","encounter_river_pirates_9.ogg","encounter_river_pirates_10.ogg","encounter_river_pirates_4.ogg"]),

 ("encounter_bandits",sf_2d|sf_vol_8, ["encounter_bandit_2.ogg","encounter_bandit_9.ogg","encounter_bandit_12.ogg","encounter_bandit_13.ogg","encounter_bandit_15.ogg","encounter_bandit_16.ogg","encounter_bandit_10.ogg",]),
 ("encounter_farmers",sf_2d|sf_vol_8, ["encounter_farmer_2.ogg","encounter_farmer_5.ogg","encounter_farmer_7.ogg","encounter_farmer_9.ogg"]),
 ("encounter_sea_raiders",sf_2d|sf_vol_8, ["encounter_sea_raider_5.ogg","encounter_sea_raider_9.ogg","encounter_sea_raider_9b.ogg","encounter_sea_raider_10.ogg"]),
 ("encounter_steppe_bandits",sf_2d|sf_vol_8, ["encounter_steppe_bandit_3.ogg","encounter_steppe_bandit_3b.ogg","encounter_steppe_bandit_8.ogg","encounter_steppe_bandit_10.ogg","encounter_steppe_bandit_12.ogg"]),
 ("encounter_nobleman",sf_2d|sf_vol_8, ["encounter_nobleman_1.ogg"]),
 ("encounter_vaegirs_ally",sf_2d|sf_vol_8, ["encounter_vaegirs_ally.ogg","encounter_vaegirs_ally_2.ogg"]),
 ("encounter_vaegirs_neutral",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("encounter_vaegirs_enemy",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("sneak_town_halt",sf_2d, ["sneak_halt_1.ogg","sneak_halt_2.ogg"]),
 ("horse_walk",sf_priority_3|sf_vol_5, ["horse_walk_1.ogg","horse_walk_2.ogg","horse_walk_3.ogg","horse_walk_4.ogg"]),
 ("horse_trot",sf_priority_4|sf_vol_6, ["horse_trot_1.ogg","horse_trot_2.ogg","horse_trot_3.ogg","horse_trot_4.ogg"]),
 ("horse_canter",sf_priority_4|sf_vol_7, ["horse_canter_1.ogg","horse_canter_2.ogg","horse_canter_3.ogg","horse_canter_4.ogg"]),
 ("horse_gallop",sf_priority_5|sf_vol_8, ["horse_gallop_6.ogg","horse_gallop_7.ogg","horse_gallop_8.ogg","horse_gallop_9.ogg"]),
 ("horse_breath",sf_priority_1|sf_vol_4, ["horse_breath_4.ogg","horse_breath_5.ogg","horse_breath_6.ogg","horse_breath_7.ogg"]),
 ("horse_snort",sf_priority_1|sf_vol_2, ["horse_snort_1.ogg","horse_snort_2.ogg","horse_snort_3.ogg","horse_snort_4.ogg","horse_snort_5.ogg"]),
 ("horse_low_whinny",sf_vol_12, ["horse_whinny-1.ogg","horse_whinny-2.ogg"]),
 ("block_fist",0, ["block_fist_3.ogg","block_fist_4.ogg"]),
 ("man_hit_blunt_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_blunt_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_victory",sf_priority_5|sf_vol_10, ["man_victory_3.ogg","man_victory_4.ogg","man_victory_5.ogg","man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","man_victory_54.ogg","man_victory_57.ogg","man_victory_71.ogg"]),
 ("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("dummy_hit",sf_priority_9, ["shield_hit_cut_3.ogg","shield_hit_cut_5.ogg"]),
 ("dummy_destroyed",sf_priority_9, ["shield_broken.ogg"]),
 ("gourd_destroyed",sf_priority_9, ["shield_broken.ogg"]),#TODO
 ("cow_moo", sf_2d|sf_priority_9|sf_vol_8, ["cow_moo_1.ogg"]),
 ("cow_slaughter", sf_2d|sf_priority_9|sf_vol_8, ["cow_slaughter.ogg"]),
 ("distant_dog_bark", sf_2d|sf_priority_3|sf_vol_8, ["d_dog1.ogg","d_dog2.ogg","d_dog3.ogg","d_dog7.ogg"]),
 ("distant_owl", sf_2d|sf_priority_3|sf_vol_9, ["d_owl2.ogg","d_owl3.ogg","d_owl4.ogg"]),
 ("distant_chicken", sf_2d|sf_priority_3|sf_vol_8, ["d_chicken1.ogg","d_chicken2.ogg"]),
 ("distant_carpenter", sf_2d|sf_priority_3|sf_vol_3, ["d_carpenter1.ogg","d_saw_short3.ogg"]),
 ("distant_blacksmith", sf_2d|sf_priority_3|sf_vol_4, ["d_blacksmith2.ogg"]),
 ("arena_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["arena_loop11.ogg"]),
 ("town_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["town_loop_3.ogg"]),
 ("tutorial_fail", sf_2d|sf_vol_7,["cue_failure.ogg"]),
 ("your_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_taken.ogg"]),
 ("enemy_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["enemy_flag_taken.ogg"]),
 ("flag_returned", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_returned.ogg"]),
 ("team_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["you_scored_a_point.ogg"]),
 ("enemy_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["enemy_scored_a_point.ogg"]),
 #INVASION MODE START
 ("ccoop_spawn_companion_0",sf_2d|sf_vol_8, ["encounter_farmer_2.ogg"]),
 ("ccoop_spawn_companion_1",sf_2d|sf_vol_8, ["encounter_farmer_5.ogg"]),
 ("ccoop_spawn_companion_2",sf_2d|sf_vol_8, ["encounter_farmer_7.ogg"]),
 ("ccoop_spawn_companion_3",sf_2d|sf_vol_8, ["encounter_farmer_9.ogg"]),
 ("ccoop_nobleman_taunt",sf_2d|sf_vol_8, ["encounter_nobleman_1.ogg"]),
 ("ccoop_looter_taunt_0",sf_2d|sf_vol_8, ["encounter_river_pirates_5.ogg"]),
 ("ccoop_looter_taunt_1",sf_2d|sf_vol_8, ["encounter_river_pirates_6.ogg"]),
 ("ccoop_looter_taunt_2",sf_2d|sf_vol_8, ["encounter_river_pirates_9.ogg"]),
 ("ccoop_looter_taunt_3",sf_2d|sf_vol_8, ["encounter_river_pirates_10.ogg"]),
 ("ccoop_looter_taunt_4",sf_2d|sf_vol_8, ["encounter_river_pirates_4.ogg"]),
 ("ccoop_bandit_taunt_0",sf_2d|sf_vol_8, ["encounter_bandit_2.ogg"]),
 ("ccoop_bandit_taunt_1",sf_2d|sf_vol_8, ["encounter_bandit_9.ogg"]),
 ("ccoop_bandit_taunt_2",sf_2d|sf_vol_8, ["encounter_bandit_12.ogg"]),
 ("ccoop_bandit_taunt_3",sf_2d|sf_vol_8, ["encounter_bandit_13.ogg"]),
 ("ccoop_bandit_taunt_4",sf_2d|sf_vol_8, ["encounter_bandit_15.ogg"]),
 ("ccoop_bandit_taunt_5",sf_2d|sf_vol_8, ["encounter_bandit_16.ogg"]),
 ("ccoop_bandit_taunt_6",sf_2d|sf_vol_8, ["encounter_bandit_10.ogg"]),
 ("ccoop_sea_raider_taunt_0",sf_2d|sf_vol_8, ["encounter_sea_raider_5.ogg"]),
 ("ccoop_sea_raider_taunt_1",sf_2d|sf_vol_8, ["encounter_sea_raider_9.ogg"]),
 ("ccoop_sea_raider_taunt_2",sf_2d|sf_vol_8, ["encounter_sea_raider_9b.ogg"]),
 ("ccoop_sea_raider_taunt_3",sf_2d|sf_vol_8, ["encounter_sea_raider_10.ogg"]),
 ("sounds_end", sf_2d|sf_priority_10|sf_vol_10, ["enemy_scored_a_point.ogg"]),
 #INVASION MODE END
 
 ("shot_pistol1", sf_priority_14|sf_vol_15, ["shot_pistol1_1.wav", "shot_pistol1_2.wav", "shot_pistol1_3.wav", "shot_pistol1_4.wav", "shot_pistol1_5.wav"]),
 ("shot_caplockpistol", sf_priority_14|sf_vol_15, ["shot_caplockpistol1.wav", "shot_caplockpistol2.wav", "shot_caplockpistol3.wav", "shot_caplockpistol5.wav"]),
 ("shot_caplock", sf_priority_14|sf_vol_15, ["shot_caplock1.wav", "shot_caplock2.wav", "shot_caplock3.wav", "shot_caplock4.wav", "shot_caplock5.wav"]),
 ("shot_rifle1", sf_priority_14|sf_vol_15, ["rifle_shot1_01.wav", "rifle_shot1_02.wav", "rifle_shot1_03.wav", "rifle_shot1_04.wav", "rifle_shot1_05.wav", "rifle_shot1_06.wav", "rifle_shot1_07.wav", "rifle_shot1_08.wav", "rifle_shot1_09.wav", "rifle_shot1_10.wav"]),
 ("shot_rifle2", sf_priority_14|sf_vol_15, ["rifle_shot2_01.wav", "rifle_shot2_02.wav", "rifle_shot2_03.wav", "rifle_shot2_04.wav", "rifle_shot2_05.wav", "rifle_shot2_06.wav", "rifle_shot2_07.wav", "rifle_shot2_08.wav"]),

("mandeath1",sf_priority_10|sf_vol_11, ["mandeath1.wav","mandeath2.wav","mandeath3.wav","mandeath4.wav","mandeath5.wav","mandeath6.wav","mandeath7.wav","mandeath8.wav","mandeath9.wav","mandeath10.wav","mandeath11.wav","mandeath12.wav","mandeath13.wav","mandeath14.wav","mandeath15.wav","mandeath16.wav","mandeath17.wav","mandeath18.wav","mandeath19.wav","mandeath20.wav","mandeath21.wav","mandeath22.wav","mandeath23.wav","mandeath24.wav","mandeath25.wav","mandeath26.wav","mandeath27.wav","mandeath28.wav","mandeath29.wav","mandeath30.wav","mandeath31.wav","mandeath32.wav"]),
("mandeath2",sf_priority_10|sf_vol_11, ["mandeath33.wav","mandeath34.wav","mandeath35.wav","mandeath36.wav","mandeath37.wav","mandeath38.wav","mandeath39.wav","mandeath40.wav","mandeath41.wav","mandeath42.wav","mandeath43.wav","mandeath44.wav","mandeath45.wav","mandeath46.wav","mandeath47.wav","mandeath48.wav","mandeath49.wav","mandeath50.wav","mandeath51.wav","mandeath52.wav","mandeath53.wav","mandeath54.wav","mandeath55.wav","mandeath56.wav","mandeath57.wav","mandeath58.wav","mandeath59.wav","mandeath60.wav","mandeath61.wav","mandeath62.wav","mandeath63.wav","mandeath64.wav"]),
("mandeath3",sf_priority_10|sf_vol_11, ["mandeath65.wav","mandeath66.wav","mandeath67.wav","mandeath68.wav","mandeath69.wav","mandeath70.wav","mandeath71.wav","mandeath72.wav","mandeath73.wav","mandeath74.wav","mandeath75.wav","mandeath76.wav","mandeath77.wav","mandeath78.wav","mandeath79.wav","mandeath80.wav","mandeath81.wav","mandeath82.wav","mandeath83.wav","mandeath84.wav","mandeath85.wav","mandeath86.wav","mandeath87.wav","mandeath88.wav","mandeath89.wav","mandeath90.wav","mandeath91.wav","mandeath92.wav","mandeath93.wav","mandeath94.wav","mandeath95.wav","mandeath96.wav"]),
("mandeath4",sf_priority_10|sf_vol_11, ["mandeath97.wav","mandeath98.wav","mandeath99.wav","mandeath100.wav","mandeath101.wav","mandeath102.wav","mandeath103.wav","mandeath104.wav","mandeath105.wav","mandeath106.wav","mandeath107.wav","mandeath108.wav","mandeath109.wav","mandeath110.wav","mandeath111.wav","mandeath112.wav","mandeath113.wav","mandeath114.wav","mandeath115.wav","mandeath116.wav","mandeath117.wav","mandeath118.wav","mandeath119.wav","mandeath120.wav","mandeath121.wav","mandeath122.wav","mandeath123.wav","mandeath124.wav","mandeath125.wav","mandeath126.wav","mandeath127.wav","mandeath128.wav"]),
("mandeath5",sf_priority_10|sf_vol_11, ["mandeath129.wav","mandeath130.wav","mandeath131.wav","mandeath132.wav","mandeath133.wav","mandeath134.wav","mandeath135.wav","mandeath136.wav","mandeath137.wav","mandeath138.wav","mandeath139.wav","mandeath140.wav","mandeath141.wav","mandeath142.wav","mandeath143.wav","mandeath144.wav","mandeath145.wav","mandeath146.wav","mandeath147.wav","mandeath148.wav","mandeath149.wav","mandeath150.wav","mandeath151.wav","mandeath152.wav","mandeath153.wav","mandeath154.wav","mandeath155.wav","mandeath156.wav","mandeath157.wav","mandeath158.wav","mandeath159.wav","mandeath160.wav"]),
("mandeath6",sf_priority_10|sf_vol_11, ["mandeath161.wav","mandeath162.wav","mandeath163.wav","mandeath164.wav","mandeath165.wav","mandeath166.wav","mandeath167.wav","mandeath168.wav","mandeath169.wav","mandeath170.wav","mandeath171.wav","mandeath172.wav"]),

("rifle_shot_reflection_small", sf_priority_1|sf_vol_15, ["rifle_shot_reflection_small1.wav", "rifle_shot_reflection_small2.wav", "rifle_shot_reflection_small3.wav", "rifle_shot_reflection_small4.wav"]),
("rifle_shot_reflection", sf_priority_1|sf_vol_15, ["rifle_shot_reflection1.wav", "rifle_shot_reflection2.wav", "rifle_shot_reflection3.wav", "rifle_shot_reflection4.wav"]),
("rifle_shot_far1", sf_2d|sf_priority_1|sf_vol_12, ["rifle_shot_far1_1.wav", "rifle_shot_far1_2.wav", "rifle_shot_far1_3.wav", "rifle_shot_far1_4.wav", "rifle_shot_far1_5.wav", "rifle_shot_far1_6.wav", "rifle_shot_far1_7.wav", "rifle_shot_far1_8.wav", "rifle_shot_far1_9.wav", "rifle_shot_far1_10.wav", "rifle_shot_far1_11.wav", "rifle_shot_far1_12.wav", "none"]),

("bugle_open_fire", sf_priority_12|sf_vol_15, ["bugle_open_fire1.wav", "bugle_open_fire2.wav"]),
("bugle_stop_fire", sf_priority_12|sf_vol_15, ["bugle_stop_fire1.wav", "bugle_stop_fire2.wav"]),
("bugle_run", sf_priority_12|sf_vol_15, ["bugle_run1.wav"]),
("bugle_walk", sf_priority_12|sf_vol_15, ["bugle_walk1.wav"]),
("bugle_retreat", sf_priority_12|sf_vol_15, ["bugle_retreat1.wav"]),
("bugle_stop_retreat", sf_priority_12|sf_vol_15, ["bugle_stop_retreat1.wav"]),
("bugle_cavalry_charge", sf_priority_12|sf_vol_15, ["bugle_cavalry_charge1.wav", "bugle_cavalry_charge2.wav"]),

("winch_shot", sf_priority_14|sf_vol_15, ["winch_shot1.wav", "winch_shot2.wav", "winch_shot3.wav", "winch_shot4.wav"]),
("shot_spencer", sf_priority_14|sf_vol_15, ["shot_spencer1.wav", "shot_spencer2.wav", "shot_spencer3.wav", "shot_spencer4.wav"]),
("shot_pistol2", sf_priority_14|sf_vol_15, ["shot_pistol2_1.wav", "shot_pistol2_2.wav", "shot_pistol2_3.wav"]),
("shot_boltaction1", sf_priority_14|sf_vol_15, ["shot_boltaction1_1.wav", "shot_boltaction1_2.wav", "shot_boltaction1_3.wav", "shot_boltaction1_4.wav", "shot_boltaction1_5.wav", "shot_boltaction1_6.wav", "shot_boltaction1_7.wav"]),

("voice_all_chargewarcry1",sf_priority_14|sf_vol_14, ["voice_all_chargewarcry01.wav","voice_all_chargewarcry02.wav","voice_all_chargewarcry03.wav","voice_all_chargewarcry04.wav","voice_all_chargewarcry05.wav","voice_all_chargewarcry06.wav","voice_all_chargewarcry07.wav","voice_all_chargewarcry08.wav","voice_all_chargewarcry09.wav","voice_all_chargewarcry10.wav","voice_all_chargewarcry11.wav","voice_all_chargewarcry12.wav","voice_all_chargewarcry13.wav","voice_all_chargewarcry14.wav","voice_all_chargewarcry15.wav","voice_all_chargewarcry16.wav","voice_all_chargewarcry17.wav","voice_all_chargewarcry18.wav","voice_all_chargewarcry19.wav","voice_all_chargewarcry20.wav","voice_all_chargewarcry21.wav","voice_all_chargewarcry22.wav","voice_all_chargewarcry23.wav","voice_all_chargewarcry24.wav","voice_all_chargewarcry25.wav","voice_all_chargewarcry26.wav","voice_all_chargewarcry27.wav","voice_all_chargewarcry28.wav","voice_all_chargewarcry29.wav","voice_all_chargewarcry30.wav","voice_all_chargewarcry31.wav","voice_all_chargewarcry32.wav"]),
("voice_all_chargewarcry2",sf_priority_14|sf_vol_14, ["voice_all_chargewarcry33.wav","voice_all_chargewarcry34.wav","voice_all_chargewarcry35.wav","voice_all_chargewarcry36.wav","voice_all_chargewarcry37.wav","voice_all_chargewarcry38.wav","voice_all_chargewarcry39.wav","voice_all_chargewarcry40.wav","voice_all_chargewarcry41.wav","voice_all_chargewarcry42.wav","voice_all_chargewarcry43.wav","voice_all_chargewarcry44.wav","voice_all_chargewarcry45.wav","voice_all_chargewarcry46.wav","voice_all_chargewarcry47.wav","voice_all_chargewarcry48.wav","voice_all_chargewarcry49.wav","voice_all_chargewarcry50.wav","voice_all_chargewarcry51.wav","voice_all_chargewarcry52.wav","voice_all_chargewarcry53.wav","voice_all_chargewarcry54.wav","voice_all_chargewarcry55.wav","voice_all_chargewarcry56.wav","voice_all_chargewarcry57.wav","voice_all_chargewarcry58.wav","voice_all_chargewarcry59.wav","voice_all_chargewarcry60.wav","voice_all_chargewarcry61.wav","voice_all_chargewarcry62.wav","voice_all_chargewarcry63.wav","voice_all_chargewarcry64.wav"]),
("voice_all_chargewarcry3",sf_priority_14|sf_vol_14, ["voice_all_chargewarcry65.wav","voice_all_chargewarcry66.wav","voice_all_chargewarcry67.wav","voice_all_chargewarcry68.wav","voice_all_chargewarcry69.wav","voice_all_chargewarcry70.wav","voice_all_chargewarcry71.wav","voice_all_chargewarcry72.wav","voice_all_chargewarcry73.wav","voice_all_chargewarcry74.wav","voice_all_chargewarcry75.wav","voice_all_chargewarcry76.wav","voice_all_chargewarcry77.wav","voice_all_chargewarcry78.wav","voice_all_chargewarcry79.wav","voice_all_chargewarcry80.wav","voice_all_chargewarcry81.wav","voice_all_chargewarcry82.wav","voice_all_chargewarcry83.wav","voice_all_chargewarcry84.wav","voice_all_chargewarcry85.wav","voice_all_chargewarcry86.wav","voice_all_chargewarcry87.wav","voice_all_chargewarcry88.wav","voice_all_chargewarcry89.wav","voice_all_chargewarcry90.wav","voice_all_chargewarcry91.wav","voice_all_chargewarcry92.wav","voice_all_chargewarcry93.wav","voice_all_chargewarcry94.wav","voice_all_chargewarcry95.wav","voice_all_chargewarcry96.wav"]),
("voice_all_chargewarcry4",sf_priority_14|sf_vol_14, ["voice_all_chargewarcry97.wav","voice_all_chargewarcry98.wav","voice_all_chargewarcry99.wav","voice_all_chargewarcry100.wav","voice_all_chargewarcry101.wav","voice_all_chargewarcry102.wav","voice_all_chargewarcry103.wav","voice_all_chargewarcry104.wav","voice_all_chargewarcry105.wav","voice_all_chargewarcry106.wav","voice_all_chargewarcry107.wav","voice_all_chargewarcry108.wav","voice_all_chargewarcry109.wav","voice_all_chargewarcry110.wav","voice_all_chargewarcry111.wav","voice_all_chargewarcry112.wav","voice_all_chargewarcry113.wav","voice_all_chargewarcry114.wav","voice_all_chargewarcry115.wav","voice_all_chargewarcry116.wav","voice_all_chargewarcry117.wav","yell33.wav","voice_all_whistle1.wav","voice_all_whistle2.wav","voice_all_whistle3.wav"]),
("voice_all_chargewarcry5",sf_priority_14|sf_vol_14,["yell1.wav","yell2.wav","yell3.wav","yell4.wav","yell5.wav","yell6.wav","yell7.wav","yell8.wav","yell9.wav","yell10.wav","yell11.wav","yell12.wav","yell13.wav","yell14.wav","yell15.wav","yell16.wav","yell17.wav","yell18.wav","yell19.wav","yell20.wav","yell21.wav","yell22.wav","yell23.wav","yell24.wav","yell25.wav","yell26.wav","yell27.wav","yell28.wav","yell29.wav","yell30.wav","yell31.wav","yell32.wav"]),

("rifle_shot_far2", sf_2d|sf_priority_1|sf_vol_12, ["rifle_shot_far2_01.wav", "rifle_shot_far2_02.wav", "rifle_shot_far2_03.wav", "rifle_shot_far2_04.wav", "rifle_shot_far2_05.wav", "rifle_shot_far2_06.wav", "rifle_shot_far2_07.wav", "rifle_shot_far2_08.wav", "rifle_shot_far2_09.wav", "rifle_shot_far2_10.wav", "rifle_shot_far2_11.wav", "rifle_shot_far2_12.wav", "rifle_shot_far2_13.wav","rifle_shot_far2_14.wav","rifle_shot_far2_15.wav","rifle_shot_far2_16.wav","none"]),
("rifle_shot_far3", sf_2d|sf_priority_1|sf_vol_15, ["rifle_shot_far2_01.wav", "rifle_shot_far2_02.wav", "rifle_shot_far2_03.wav", "rifle_shot_far2_04.wav", "rifle_shot_far2_05.wav", "rifle_shot_far2_06.wav", "rifle_shot_far2_07.wav", "rifle_shot_far2_08.wav", "rifle_shot_far2_09.wav", "rifle_shot_far2_10.wav", "rifle_shot_far2_11.wav", "rifle_shot_far2_12.wav", "rifle_shot_far2_13.wav","rifle_shot_far2_14.wav","rifle_shot_far2_15.wav","rifle_shot_far2_16.wav","none"]),

]
