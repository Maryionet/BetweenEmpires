# #######################################################################
#	("string-id", "string"),
#	This file was also missing a header, but probably on account 
#	of its simplicity
#
#	Field 1: String ID (string) 
#	Field 2: String Contents (string)
# #######################################################################

strings = [

# #######################################################################
#	These four strings are the only explicitly required strings
# #######################################################################

  ("no_string", "NO STRING!"),
  ("empty_string", " "),
  ("yes", "Yes."),
  ("no", "No."),
  
# #######################################################################
#	But, these may be referenced, so, I have chosen to leave them here.
# #######################################################################

  ("blank_string", " "),
  ("ERROR_string", "{!}ERROR!!!ERROR!!!!ERROR!!!ERROR!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!!"),
  ("noone", "no one"),
  ("s0", "{!}{s0}"),
  ("blank_s1", "{!} {s1}"),
  ("reg1", "{!}{reg1}"),
  ("s50_comma_s51", "{!}{s50}, {s51}"),
  ("s50_and_s51", "{s50} and {s51}"),
  ("s52_comma_s51", "{!}{s52}, {s51}"),
  ("s52_and_s51", "{s52} and {s51}"),
  ("s5_s_party", "{s5}'s Party"),

  ("msg_battle_won", "Battle won! Press tab key to leave..."),

  ("randomize", "Randomize"),
  ("hold_fire", "Hold Fire"),
  ("blunt_hold_fire", "Blunt / Hold Fire"),

  ("finished", "(Finished)"),

  ("delivered_damage", "Delivered {reg60} damage."),

  ("cant_use_inventory_now", "Can't access inventory now."),
  ("cant_use_inventory_arena", "Can't access inventory in the arena."),
  ("cant_use_inventory_disguised", "Can't access inventory while you're disguised."),
  ("cant_use_inventory_tutorial", "Can't access inventory in the training camp."),
  
("province0", "Alsace-Moselle"),
("province1", "Brittany"),
("province2", "Lower Normandy"),
("province3", "Pays de la Loire"),
("province4", "Poitou"),
("province5", "Orleans"),
("province6", "Aquitaine"),
("province7", "Limousin"),
("province8", "Pyrenees"),
("province9", "Languedoc"),
("province10", "Provence"),
("province11", "Rhone"),
("province12", "Burgundy"),
("province13", "Franche-Comte"),
("province14", "Upper Normandy"),
("province15", "Picardie"),
("province16", "Marne"),
("province17", "Ile de France"),
("province18", "Champagne"),
("province19", "Lorraine"),
("province20", "Calais"),
("province21", "Flanders"),
("province22", "Wallonia"),
("province23", "Luxembourg"),
("province24", "North Brabant"),
("province25", "Holland"),
("province26", "Frisia"),
("province27", "Corsica"),
("province28", "Cornwall"),
("province29", "Sussex"),
("province30", "Anglia"),
("province31", "East Midlands"),
("province32", "West Midlands"),
("province33", "Wales"),
("province34", "York"),
("province35", "Scottish Lowlands"),
("province36", "Scottish Highlands"),
("province37", "Ulster"),
("province38", "Leinster"),
("province39", "Connacht"),
("province40", "Munster"),
("province41", "Bern"),
("province42", "Zurich"),
("province43", "Grisons"),
("province44", "Balearic Islands"),
("province45", "Catalonia"),
("province46", "Aragon"),
("province47", "Navarre"),
("province48", "Cantabria"),
("province49", "Leon"),
("province50", "Galicia"),
("province51", "Valencia"),
("province52", "Murcia"),
("province53", "New Castile"),
("province54", "Old Castile"),
("province55", "Extremadura"),
("province56", "Granada"),
("province57", "Seville"),
("province58", "Gibraltar"),
("province59", "Algarve"),
("province60", "Alentejo"),
("province61", "Central Portugal"),
("province62", "Northern Portugal"),
("province63", "Sardinia"),
("province64", "Piedmont"),
("province65", "Lombardy"),
("province66", "Parma"),
("province67", "Veneto"),
("province68", "South Tyrol"),
("province69", "Friuli-Venezia"),
("province70", "Romagna"),
("province71", "Marche-Umbria"),
("province72", "Latium"),
("province73", "Abruzzo"),
("province74", "Campania"),
("province75", "Apulia"),
("province76", "Calabria"),
("province77", "Sicily"),
("province78", "Tuscany"),
("province79", "Baden-Wurttemberg"),
("province80", "North Rhineland"),
("province81", "Westphalia"),
("province82", "Hesse"),
("province83", "Lower Saxony"),
("province84", "Bavaria-Munich"),
("province85", "Bavaria-Regensburg"),
("province86", "Bavaria-Nuremberg"),
("province87", "Schleswig-Holstein"),
("province88", "North Schleswig"),
("province89", "Thuringia"),
("province90", "Anhalt"),
("province91", "Mecklenburg"),
("province92", "Brandenburg"),
("province93", "Saxony"),
("province94", "Pomerania"),
("province95", "Brandenburg-Oder"),
("province96", "Lower Silesia"),
("province97", "Greater Poland"),
("province98", "West Prussia"),
("province99", "Warmia-Masuria"),
("province100", "East Prussia"),
("province101", "Oldenburg"),
("province102", "Central Jutland"),
("province103", "North Jutland"),
("province104", "Zealand and Odense"),
("province105", "Rhineland-Palatinate"),
("province106", "Upper Silesia"),
("province107", "Tyrol"),
("province108", "Austria"),
("province109", "Styria"),
("province110", "Trieste"),
("province111", "Ljubljana"),
("province112", "Central Croatia"),
("province113", "Dalmatia"),
("province114", "Slavonia"),
("province115", "Vojvodina"),
("province116", "Western Transdanubia"),
("province117", "Southern Transdanubia"),
("province118", "Central Transdanubia"),
("province119", "Southern Alfold"),
("province120", "Northern Alfold"),
("province121", "Miskolc"),
("province122", "Banat"),
("province123", "Crisana"),
("province124", "Maramures"),
("province125", "Transylvania"),
("province126", "Bohemia"),
("province127", "Moravia"),
("province128", "Western Slovakia"),
("province129", "Eastern Slovakia"),
("province130", "Sudetenland"),
("province131", "Carpathian Rus"),
("province132", "Galicia"),
("province133", "Lodomeria"),
("province134", "Bukovina"),
("province135", "Herzeg-Bosnia"),
("province136", "Bosnian Krajina"),
("province137", "Eastern Herzeg-Bosnia"),
("province138", "Montenegro"),
("province139", "Northern Albania"),
("province140", "Southern Albania"),
("province141", "Vardar Macedonia"),
("province142", "Kosovo"),
("province143", "Old Serbia"),
("province144", "West Serbia"),
("province145", "East Serbia"),
("province146", "Epirus"),
("province147", "Macedonia"),
("province148", "Thrace"),
("province149", "Thessaly"),
("province150", "West Greece"),
("province151", "Central Greece"),
("province152", "Peloponnesia"),
("province153", "Crete"),
("province154", "Rhodes"),
("province155", "Oltenia"),
("province156", "Muntenia"),
("province157", "South Moldova"),
("province158", "North Moldova"),
("province159", "North Dobruja"),
("province160", "South Dobruja"),
("province161", "Bessarabia"),
("province162", "Moldova"),
("province163", "East Bukovina"),
("province164", "East Thrace"),
("province165", "Burgas"),
("province166", "Varna"),
("province167", "Plovdiv"),
("province168", "Lovech"),
("province169", "Sofia"),
("province170", "Montana"),
("province171", "Odessa"),
("province172", "Vinnytsia"),
("province173", "Tarnopol"),
("province174", "Volhynia"),
("province175", "Zhytomyr"),
("province176", "Kyiv"),
("province177", "Cherkassy"),
("province178", "Kirovohrad"),
("province179", "Mykolaiv"),
("province180", "Kherson"),
("province181", "Zaporizhzhia"),
("province182", "Dnipropetrovsk"),
("province183", "Poltava"),
("province184", "Chernihiv"),
("province185", "Sumy"),
("province186", "Kharkiv"),
("province187", "Aleksandrovka"),
("province188", "Luhansk"),
("province189", "Crimea"),
("province190", "Lublin"),
("province191", "Mazovia"),
("province192", "Podlaskie"),
("province193", "Kielce"),
("province194", "Kalisz"),
("province195", "Plock"),
("province196", "Brest"),
("province197", "Grodno"),
("province198", "Vitebsk"),
("province199", "Minsk"),
("province200", "Mogilev"),
("province201", "Gomel"),
("province202", "Dzukija"),
("province203", "Aukstaitija"),
("province204", "Samogitia"),
("province205", "Courland and Semigalia"),
("province206", "Vidzeme"),
("province207", "Coastal Estonia"),
("province208", "Inland Estonia"),
("province209", "South Karelia"),
("province210", "Karelia"),
("province211", "North Karelia"),
("province212", "Savonia"),
("province213", "Kainuu"),
("province214", "Lapland"),
("province215", "North Ostrobothnia"),
("province216", "South Ostrobothnia"),
("province217", "Central Finland"),
("province218", "Southwest Finland"),
("province219", "Uusimaa"),
("province220", "Finnmark"),
("province221", "Nordland"),
("province222", "Trondelag"),
("province223", "Innlandet"),
("province224", "Viken"),
("province225", "Agder"),
("province226", "Vestland"),
("province227", "More and Romsdal"),
("province228", "Norrbotten"),
("province229", "Vasterbotten"),
("province230", "Jamtland"),
("province231", "Gavleborg"),
("province232", "Stockholm"),
("province233", "Ostergotland"),
("province234", "Vastragotaland"),
("province235", "Jonkoping"),
("province236", "Kalmar"),
("province237", "Skane"),
("province238", "Ingria"),
("province239", "Pskov"),
("province240", "Novgorod"),
("province241", "Tver"),
("province242", "Smolensk"),
("province243", "Moscow"),
("province244", "Belgorod"),
("province245", "Rostov"),
("province246", "Yekaterinodar"),
("province247", "Stavropol"),
("province248", "Dagestan"),
("province249", "Kalmykia-Astrakhan"),
("province250", "Tsaritsyn"),
("province251", "Saratov"),
("province252", "Mordovia"),
("province253", "Nizhny Novgorod"),
("province254", "Yaroslavl"),
("province255", "Vologda"),
("province256", "East Karelia"),
("province257", "Kola"),
("province258", "Severodvinsk"),
("province259", "Arkhangelsk"),
("province260", "Kirov"),
("province261", "Tatarstan"),
("province262", "Samara"),
("province263", "Orenburg"),
("province264", "Bashkortostan"),
("province265", "Perm"),
("province266", "Komi"),
("province267", "North Komi"),
("province268", "Vorkuta"),
("province269", "West Nenetsia"),
("province270", "East Nenetsia"),
("province271", "Yamalo-Nenets"),
("province272", "Khanty-Mansi"),
("province273", "Yekaterinburg"),
("province274", "Chelyabinsk"),
("province275", "Kurgan"),
("province276", "Omsk"),
("province277", "Nizhnevartovskiy"),
("province278", "Nadym-Krasnoselkupskiy"),
("province279", "Tazovskiy"),
("province280", "Taymyr"),
("province281", "Krasnoyarsk"),
("province282", "Tomsk"),
("province283", "Novosibirsk"),
("province284", "Kemerovo"),
("province285", "Altai"),
("province286", "Evenki"),
("province287", "Tuva"),
("province288", "Irkutsk"),
("province289", "Buryatia"),
("province290", "Katangskiy-Bodaybinskiy"),
("province291", "Olenyok"),
("province292", "Mirny"),
("province293", "Verkhoyansk"),
("province294", "Srednekolymsk"),
("province295", "Yakutsk"),
("province296", "Transbaikal"),
("province297", "Amur"),
("province298", "Blagoveshchensk"),
("province299", "Okhotsk"),
("province300", "Khabarovsk"),
("province301", "Birobidzhan"),
("province302", "Primorskiy"),
("province303", "South Sakhalin"),
("province304", "North Sakhalin"),
("province305", "Magadan"),
("province306", "Kamchatka"),
("province307", "Chukotka"),
("province308", "Chechnya"),
("province309", "Astrakhan"),
("province310", "Circassia"),
("province311", "Nikolaevsk"),
("province312", "Taganrog"),
("province313", "Novouzensk"),
("province314", "Bryansk"),
("province315", "Velikie Luki"),
("province316", "Rzhev"),
("province317", "Valdai"),
("province318", "Kaluga"),
("province319", "Tula"),
("province320", "Voronezh"),
("province321", "Abkhazia"),
("province322", "Western Georgia"),
("province323", "Eastern Georgia"),
("province324", "Northern Armenia"),
("province325", "Southern Armenia"),
("province326", "Nakhchivan"),
("province327", "Upper Karabakh"),
("province328", "Ganja"),
("province329", "Baku"),
("province330", "Talysh"),
("province331", "Guryev"),
("province332", "Uralsk"),
("province333", "Mangystau"),
("province334", "Aktobe"),
("province335", "Kostanay"),
("province336", "Petropavl"),
("province337", "Akmolinsk"),
("province338", "Pavlodar"),
("province339", "Abai"),
("province340", "Ust-Kamenogorsk"),
("province341", "Ulytau"),
("province342", "Karaganda"),
("province343", "Kyzylorda"),
("province344", "Shymkent"),
("province345", "Jambyl"),
("province346", "Verny"),
("province347", "Taldy-Kurgan"),
("province348", "Karakalpak"),
("province349", "Khorezm"),
("province350", "Karmana"),
("province351", "Bukhara"),
("province352", "Samarkand"),
("province353", "Tirmidh"),
("province354", "Tashkent"),
("province355", "Fergana"),
("province356", "Transcaspia"),
("province357", "Akhal"),
("province358", "Dashoguz"),
("province359", "Turkmenabad"),
("province360", "Merv"),
("province361", "Jalal-Abad"),
("province362", "Pishpek"),
("province363", "Karakol"),
("province364", "Karotegin"),
("province365", "Badakhshan"),
("province366", "Northwest Anatolia"),
("province367", "Ionia"),
("province368", "Southwest Anatolia"),
("province369", "South Anatolia"),
("province370", "Central Anatolia"),
("province371", "North Anatolia"),
("province372", "Sebastia"),
("province373", "Trebizond"),
("province374", "Southeast Anatolia"),
("province375", "East Anatolia"),
("province376", "West Armenia"),
("province377", "Hatay"),
("province378", "Cyprus"),
("province379", "Al-Hasakah"),
("province380", "Aleppo"),
("province381", "Deir-ez-Zor"),
("province382", "Homs"),
("province383", "Idlib"),
("province384", "Damascus"),
("province385", "Lebanon"),
("province386", "Al-Anbar"),
("province387", "Nineveh"),
("province388", "Kurdistan"),
("province389", "Diyala"),
("province390", "Baghdad"),
("province391", "Najaf"),
("province392", "Maysan"),
("province393", "Basrah"),
("province394", "Kuwait"),
("province395", "Afyonkarahisar"),
("province396", "Samsun"),
("province397", "Van"),
("province398", "Ankara"),
("province399", "Israel"),
("province400", "West Bank"),
("province401", "Washington"),
("province402", "Oregon"),
("province403", "California"),
("province404", "Idaho"),
("province405", "Nevada"),
("province406", "Arizona"),
("province407", "Utah"),
("province408", "New Mexico"),
("province409", "Colorado"),
("province410", "Wyoming"),
("province411", "Montana"),
("province412", "North Dakota"),
("province413", "South Dakota"),
("province414", "Nebraska"),
("province415", "Kansas"),
("province416", "Oklahoma"),
("province417", "Louisiana"),
("province418", "Arkansas"),
("province419", "Missouri"),
("province420", "Iowa"),
("province421", "Minnesota"),
("province422", "North Michigan"),
("province423", "Wisconsin"),
("province424", "Illinois"),
("province425", "Kentucky"),
("province426", "Tennessee"),
("province427", "Mississippi"),
("province428", "Alabama"),
("province429", "Florida"),
("province430", "Georgia"),
("province431", "South Carolina"),
("province432", "North Carolina"),
("province433", "Virginia"),
("province434", "West Virginia"),
("province435", "Ohio"),
("province436", "South Michigan"),
("province437", "Akmolinsk"),
("province438", "Pavlodar"),
("province439", "Abai"),
("province440", "Ust-Kamenogorsk"),
("province441", "Ulytau"),
("province442", "Karaganda"),
("province443", "Kyzylorda"),
("province444", "Shymkent"),
("province445", "Jambyl"),
("province446", "Verny"),
("province447", "Taldy-Kurgan"),
("province448", "Karakalpak"),
("province449", "Khorezm"),
("province450", "South Azerbaijan"),
("province451", "Ardabil"),
("province452", "East Kurdistan"),
("province453", "Qazvin"),
("province454", "Luristan"),
("province455", "Qom"),
("province456", "Tehran"),
("province457", "Khuzestan"),
("province458", "Najafabad"),
("province459", "Esfahan"),
("province460", "Semnan"),
("province461", "North Khorasan"),
("province462", "Razavi Khorasan"),
("province463", "South Khorasan"),
("province464", "Yazd"),
("province465", "Fars"),
("province466", "Bushehr"),
("province467", "Sirjan"),
("province468", "Kerman"),
("province469", "Hormozgan"),
("province470", "Sistan"),
("province471", "Baluchestan"),
("province472", "Al-Mafraq"),
("province473", "Amman"),
("province474", "Aqaba"),
("province475", "Al-Jawf"),
("province476", "Turayf"),
("province477", "Rafha"),
("province478", "Ha'il"),
("province479", "Riyadh"),
("province480", "Eastern Arabia"),
("province481", "Tabuk"),
("province482", "Medina"),
("province483", "Mecca"),
("province484", "Najran"),
("province485", "North Yemen"),
("province486", "Aden"),
("province487", "West Hadhramaut"),
("province488", "East Hadhramaut"),
("province489", "Dhofar"),
("province490", "Al-Wusta"),
("province491", "Ad-Dakhiliyah"),
("province492", "Muscat"),
("province493", "Abu Dhabi"),
("province494", "Dubai"),
("province495", "Qatar"),
("province496", "Hovd"),
("province497", "Khovsgol"),
("province498", "Gobi-Altay"),
("province499", "Arkhangai"),
("province500", "Urga"),
("province501", "Western Gobi"),
("province502", "Bayan Tumen"),
("province503", "Eastern Gobi"),
("province504", "Daxing'anling"),
("province505", "Xing'an"),
("province506", "Hailar"),
("province507", "North Heihe"),
("province508", "South Heihe"),
("province509", "Hinggan"),
("province510", "Tongliao"),
("province511", "Qiqihar"),
("province512", "Mudanjang"),
("province513", "Hegang"),
("province514", "Jiamusi"),
("province515", "Harbin"),
("province516", "Jinzhou"),
("province517", "Dalian"),
("province518", "Jilin"),
("province519", "Port Arthur"),
("province520", "Herat"),
("province521", "Helmand"),
("province522", "Daykundi"),
("province523", "Bamiyan"),
("province524", "Balkh"),
("province525", "Baghlan"),
("province526", "Kabul"),
("province527", "South Badakhshan"),

]
