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
("province436", "Indiana"),
("province437", "South Michigan"),
("province438", "Maryland"),
("province439", "Pennsylvania"),
("province440", "New Jersey"),
("province441", "New York"),
("province442", "Massachusetts"),
("province443", "Vermont"),
("province444", "Maine"),
("province445", "North Texas"),
("province446", "South Texas"),
("province447", "South Alaska"),
("province448", "North Alaska"),
("province449", "Hawaii"),
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
("province528", "Khyber"),
("province529", "Punjab"),
("province530", "Quetta"),
("province531", "Balochistan"),
("province532", "Sindh"),
("province533", "Chongjin"),
("province534", "Pyongyang"),
("province535", "Kaesong"),
("province536", "Hanseong"),
("province537", "Daejeon"),
("province538", "Busan"),
("province539", "Sinai"),
("province540", "Cairo"),
("province541", "El Alamein"),
("province542", "Aswan"),
("province543", "Upper Egypt"),
("province544", "Greenland"),
("province545", "West Iceland"),
("province546", "East Iceland"),
("province547", "British Columbia"),
("province548", "Yukon"),
("province549", "Alberta"),
("province550", "Saskatchewan"),
("province551", "Manitoba"),
("province552", "Ontario"),
("province553", "Toronto"),
("province554", "Quebec"),
("province555", "New Brunswick"),
("province556", "Nova Scotia"),
("province557", "North Quebec"),
("province558", "Newfoundland and Labrador"),
("province559", "Northwest Territories"),
("province560", "Nunavut"),
("province561", "Aksai Chin"),
("province562", "Jammu and Kashmir"),
("province563", "East Punjab"),
("province564", "Delhi"),
("province565", "Jaipur"),
("province566", "Jodhpur"),
("province567", "Udaipur"),
("province568", "Kutch"),
("province569", "Kathiawar"),
("province570", "Bombay"),
("province571", "Rampur"),
("province572", "Agra"),
("province573", "Awadh"),
("province574", "Varanasi"),
("province575", "Nagpur"),
("province576", "Jabalpur"),
("province577", "Aurangabad"),
("province578", "Gulbarga"),
("province579", "Hyderabad"),
("province580", "Mysore"),
("province581", "Mangalore"),
("province582", "Goa"),
("province583", "Madras"),
("province584", "Tamil Nadu"),
("province585", "Travancore"),
("province586", "Ceylon"),
("province587", "Godavari"),
("province588", "Bastar"),
("province589", "Odisha"),
("province590", "Nerbudda"),
("province591", "Chota"),
("province592", "West Bengal"),
("province593", "East Bengal"),
("province594", "Chittagong"),
("province595", "Sikkim"),
("province596", "Assam"),
("province597", "Itanagar"),
("province598", "Manipur"),
("province599", "Mizoram"),
("province600", "Karnali"),
("province601", "Kathmandu"),
("province602", "Bhutan"),
("province603", "Anand"),
("province604", "Arakan"),
("province605", "Pegu"),
("province606", "Tenasserim"),
("province607", "Shan"),
("province608", "Chin"),
("province609", "Kachin"),
("province610", "Chiang Mai"),
("province611", "Khon Kaen"),
("province612", "Bangkok"),
("province613", "Samut Songkhram"),
("province614", "Surat Thani"),
("province615", "Pattani"),
("province616", "Peking"),
("province617", "Chengde"),
("province618", "Xilinhot"),
("province619", "Cangzhou"),
("province620", "Zhangjiakou"),
("province621", "Hohhot"),
("province622", "Dongying"),
("province623", "Tsingtao"),
("province624", "Bayan Nur"),
("province625", "Taiyuan"),
("province626", "Shijiazhuang"),
("province627", "Kumul"),
("province628", "Bayanhot"),
("province629", "Jiuquan"),
("province630", "Altay"),
("province631", "Urumqi"),
("province632", "Karamay"),
("province633", "Kashgar"),
("province634", "Korla"),
("province635", "East Bayingolin"),
("province636", "Kargilik"),
("province637", "Keriya"),
("province638", "Hotan"),
("province639", "Luang Prabang"),
("province640", "Vientiane"),
("province641", "Champasak"),
("province642", "Sen Monorom"),
("province643", "Phnompenh"),
("province644", "Hanoi"),
("province645", "Hue"),
("province646", "Da Nang"),
("province647", "Saigon"),
("province648", "Cochinchina"),
("province649", "Perak"),
("province650", "Terengganu"),
("province651", "Malacca"),
("province652", "Johor"),
("province653", "Singapore"),
("province654", "Kuching"),
("province655", "Sarawak"),
("province656", "Brunei"),
("province657", "Sabah"),
("province658", "South Mindanao"),
("province659", "North Mindanao"),
("province660", "Palawan"),
("province661", "Visayas"),
("province662", "Luzon"),
("province663", "Aceh"),
("province664", "North Sumatra"),
("province665", "Siak"),
("province666", "Deli"),
("province667", "West Sumatra"),
("province668", "South Sumatra"),
("province669", "Oosthaven"),
("province670", "West Java"),
("province671", "Central Java"),
("province672", "Yogyakarta"),
("province673", "Surakarta"),
("province674", "East Java"),
("province675", "Bali"),
("province676", "South Baja California"),
("province677", "North Baja California"),
("province678", "Sonora"),
("province679", "Chihuahua"),
("province680", "Coahuila de Zaragoza"),
("province681", "Nueva Leon"),
("province682", "Tamaulipas"),
("province683", "San Luis Potosi"),
("province684", "Zacatecas"),
("province685", "Durango"),
("province686", "Sinaloa"),
("province687", "Nayarit"),
("province688", "Jalisco"),
("province689", "Guanajuato"),
("province690", "Michoacan de Ocampo"),
("province691", "Puebla"),
("province692", "Veracruz-Llave"),
("province693", "Guerrero"),
("province694", "Oaxaca"),
("province695", "Chiapas"),
("province696", "Tabasco"),
("province697", "Campeche"),
("province698", "Yucatan"),
("province699", "Quintana Roo"),
("province700", "West Lesser Sunda Islands"),
("province701", "East Lesser Sunda Islands"),
("province702", "West Timor"),
("province703", "East Timor"),
("province704", "Banjar"),
("province705", "Central Borneo"),
("province706", "Ketapang"),
("province707", "Pontianak"),
("province708", "Singkawang"),
("province709", "East Borneo"),
("province710", "Bulungan"),
("province711", "Southwest Celebes"),
("province712", "Southease Celebes"),
("province713", "Central Celebes"),
("province714", "North Celebes"),
("province715", "South Moluccas"),
("province716", "North Moluccas"),
("province717", "West New Guinea"),
("province718", "Haidong"),
("province719", "Jingzi"),
("province720", "Maken"),
("province721", "Xihai"),
("province722", "Tianjun"),
("province723", "Dulan"),
("province724", "Golmud"),
("province725", "Da Qaidam"),
("province726", "Magnai"),
("province727", "South Golmud"),
("province728", "Zadoi"),
("province729", "Nangqen"),
("province730", "Zogang"),
("province731", "Lhorong"),
("province732", "Banbar"),
("province733", "Lhasa"),
("province734", "Shigatse"),
("province735", "Nagqu"),
("province736", "Coqen"),
("province737", "Gerze"),
("province738", "Senge Tsangpo"),
("province739", "Rutog"),
("province740", "Dege"),
("province741", "Cyrenaica"),
("province742", "Fezzan"),
("province743", "Tripolitania"),
("province744", "Gabes"),
("province745", "Tunis"),
("province746", "Tamanrasset"),
("province747", "Bechar"),
("province748", "Constantine"),
("province749", "Algiers"),
("province750", "Laghouat"),
("province751", "Oran"),
("province752", "Fes"),
("province753", "Tangier"),
("province754", "Ceuta and Melilla"),
("province755", "Rabat"),
("province756", "Agadir"),
("province757", "Northwestern Australia"),
("province758", "Southwestern Australia"),
("province759", "Northern Territory"),
("province760", "South Australia"),
("province761", "Queensland"),
("province762", "New South Wales"),
("province763", "Victoria"),
("province764", "Tasmania"),
("province765", "Aotearoa"),
("province766", "Kaikoura"),
("province767", "Te Wahi Pounamu"),
("province768", "Hokkaido"),
("province769", "Hakodate"),
("province770", "Tohoku"),
("province771", "Sendai"),
("province772", "Edo"),
("province773", "Shizuoka"),
("province774", "Kyoto"),
("province775", "Wakayama"),
("province776", "Shikoku"),
("province777", "Hiroshima"),
("province778", "Nagato"),
("province779", "North Kyushu"),
("province780", "South Kyushu"),
("province781", "Ryukyu Islands"),
("province782", "Northern Sudan"),
("province783", "Darfur"),
("province784", "Kurdufan"),
("province785", "Central Sudan"),
("province786", "Eastern Sudan"),
("province787", "El Ghazal"),
("province788", "Upper Nile"),
("province789", "Equatoria"),
("province790","province790"),
("province791","province791"),
("province792","province792"),
("province793","province793"),
("province794","province794"),
("province795","province795"),
("province796","province796"),
("province797","province797"),
("province798","province798"),
("province799","province799"),
("province800","province800"),
("province801","province801"),
("province802","province802"),
("province803","province803"),
("province804","province804"),
("province805","province805"),
("province806","province806"),
("province807","province807"),
("province808","province808"),
("province809","province809"),
("province810","province810"),
("province811","province811"),
("province812","province812"),
("province813","province813"),
("province814","province814"),
("province815","province815"),
("province816","province816"),
("province817","province817"),
("province818","province818"),
("province819","province819"),
("province820","province820"),
("province821","province821"),
("province822","province822"),
("province823","province823"),
("province824","province824"),
("province825","province825"),
("province826","province826"),
("province827","province827"),
("province828","province828"),
("province829","province829"),
("province830","province830"),
("province831","province831"),
("province832","province832"),
("province833","province833"),
("province834","province834"),
("province835","province835"),
("province836","province836"),
("province837","province837"),
("province838","province838"),
("province839","Northwest Eritrea"),
("province840","Southeast Eritrea"),
("province841","Djibouti"),
("province842","Tigray"),
("province843","Amhara"),
("province844","Afar"),
("province845","Benishangul-Gumuz"),
("province846","Addis Ababa"),
("province847","Awasa"),
("province848","Oromiya"),
("province849","West Somalia"),
("province850","Somaliland"),
("province851","North Somalia"),
("province852","South Somalia"),
("province853","Socotra"),
("province854","Turkana"),
("province855","Nyanza"),
("province856","Nairobi"),
("province857","Marsabil"),
("province858","Meru"),
("province859","Garissa"),
("province860","Mombasa"),
("province861","Aozou"),
("province862","Borkou"),
("province863","Ennedi"),
("province864","Kanem"),
("province865","Batha"),
("province866","Baghirmi"),
("province867","Dar Sila"),
("province868","Logone"),
("province869","Borno"),
("province870","Kano"),
("province871","Sokoto"),
("province872","Taraba"),
("province873","Nasarawa"),
("province874","Kwara"),
("province875","Imo"),
("province876","Oyo"),
("province877","Maroua"),
("province878","N'Gamdere"),
("province879","Bertua"),
("province880","Yaunde"),
("province881","Bafoussam"),
("province882","Agadez"),
("province883","Zinder"),
("province884","Tahoua"),
("province885","Niamey"),
("province886","Timbuktu"),
("province887","Segou"),
("province888","Sikasso"),
("province889","Bamako"),
("province890","El Aiun"),
("province889","Ausert"),
("province889","Tiris Zemmour"),
("province889","Adrar"),
("province889","Tagant"),
("province895","Chargui"),
("province896","Antsiranana"),
("province897","Comoros"),
("province898","Mahajanga"),
("province899","Antananarivo"),
("province900","Toliara"),
("province901","Reunion"),
("province902","Mauritius"),
("province903","Kerguelen Islands"),
("province904","Seychelles"),
("province905","East New Guinea"),
("province906","Solomon Islands"),
("province907","Vanuatu"),
("province908","New Caledionia"),
("province909","Fiji"),
("province910","Tonga"),
("province911","Samoa"),
("province912","Tuvalu"),
("province913","Kiribati"),
("province914","Marshall Islands"),
("province915","Micronesia"),
("province916","Caroline Islands"),
("province917","Northern Mariana"),
("province918","West Cuba"),
("province919","Bahamas"),
("province920","Andros"),
("province921","East Cuba"),
("province922","Jamaica"),
("province923","West Hispaniola"),
("province924","East Hispaniola"),
("province925","Puerto Rico"),
("province926","Anguila"),
("province927","Guadeloupe"),
("province928","Dominica"),
("province929","Martinique"),
("province930","St. Lucia"),
("province931","Trinidad and Tobago"),
("province932","Margarita Island"),
("province933","Curacao"),
("province934","Chetumal"),
("province935","Belize"),
("province936","Toledo"),
("province937","North Guatemala"),
("province938","Puerto Barrios"),
("province939","Central Guatemala"),
("province940","South Guatemala"),
("province941","Santa Barbara"),
("province942","Puerto Lempira"),
("province943","Olancho"),
("province944","El Salvador"),
("province945","Managua"),
("province946","Mosquito Coast"),
("province947","Bonanza"),
("province948","El Tortuguero"),
("province949","Alajuela"),
("province950","San Jose"),
("province951","West Panama"),
("province952","East Panama"),
("province953","Louga"),
("province954","Tambacounda"),
("province955","Gambia"),
("province956","Sedhiou"),
("province957","Guinea-Bissau"),
("province958","Konakri"),
("province959","Upper Guinea"),
("province960","South Guinea"),
("province961","Sierra Leone"),
("province962","Liberia"),
("province963","Greensville"),
("province964","Ouagadougou"),
("province965","Fada N'Gouma"),
("province966","Woroba"),
("province967","Bas-Sassandra"),
("province968","Zanzan"),
("province969","Abidjan"),
("province970","Western Gold Coast"),
("province971","Eastern Gold Coast"),
("province972","Ashanti"),
("province973","North Ashanti"),
("province974","Lome"),
("province975","Bassar"),
("province976","Abomey"),
("province977","Djougou"),
("province978","province978"),
("province979","province979"),
("province980","province980"),
("province981","province981"),
("province982","province982"),
("province983","province983"),
("province984","province984"),
("province985","province985"),
("province986","province986"),
("province987","province987"),
("province988","province988"),
("province989","province989"),
("province990","province990"),
("province991","province991"),
("province992","province992"),
("province993","province993"),
("province994","province994"),
("province995","province995"),
("province996","province996"),
("province997","province997"),
("province998","province998"),
("province999","province999"),
("province1000","province1000"),
("province1001","province1001"),
("province1002","province1002"),
("province1003","province1003"),
("province1004","province1004"),
("province1005","province1005"),
("province1006","province1006"),
("province1007","province1007"),
("province1008","province1008"),
("province1009","province1009"),
("province1010","province1010"),
("province1011","province1011"),
("province1012","province1012"),
("province1013","province1013"),
("province1014","province1014"),
("province1015","province1015"),
("province1016","province1016"),
("province1017","province1017"),
("province1018","province1018"),
("province1019","province1019"),
("province1020","province1020"),
("province1021","province1021"),
("province1022","province1022"),
("province1023","province1023"),
("province1024","province1024"),
("province1025","province1025"),
("province1026","province1026"),
("province1027","province1027"),
("province1028","province1028"),
("province1029","province1029"),
("province1030","province1030"),
("province1031","province1031"),
("province1032","province1032"),
("province1033","province1033"),
("province1034","province1034"),
("province1035","province1035"),
("province1036","province1036"),
("province1037","province1037"),
("province1038","province1038"),
("province1039","province1039"),
("province1040","province1040"),
("province1041","province1041"),
("province1042","province1042"),
("province1043","province1043"),
("province1044","province1044"),
("province1045","province1045"),
("province1046","province1046"),
("province1047","province1047"),
("province1048","province1048"),
("province1049","province1049"),
("province1050","province1050"),
("province1051","province1051"),
("province1052","province1052"),
("province1053","province1053"),
("province1054","province1054"),
("province1055","province1055"),
("province1056","province1056"),
("province1057","province1057"),
("province1058","province1058"),
("province1059","province1059"),
("province1060","province1060"),
("province1061","province1061"),
("province1062","province1062"),
("province1063","province1063"),
("province1064","province1064"),
("province1065","province1065"),
("province1066","province1066"),
("province1067","province1067"),
("province1068","province1068"),
("province1069","province1069"),
("province1070","province1070"),
("province1071","province1071"),
("province1072","province1072"),
("province1073","province1073"),
("province1074","province1074"),
("province1075","province1075"),
("province1076","province1076"),
("province1077","province1077"),
("province1078","province1078"),
("province1079","province1079"),
("province1080","province1080"),
("province1081","province1081"),
("province1082","province1082"),
("province1083","province1083"),
("province1084","province1084"),
("province1085","province1085"),
("province1086","province1086"),
("province1087","province1087"),
("province1088","province1088"),
("province1089","province1089"),
("province1090","province1090"),
("province1091","province1091"),
("province1092","province1092"),
("province1093","province1093"),
("province1094","province1094"),
("province1095","province1095"),
("province1096","province1096"),
("province1097","province1097"),
("province1098","province1098"),
("province1099","province1099"),
("province1100","province1100"),
("province1101","province1101"),
("province1102","province1102"),
("province1103","province1103"),
("province1104","province1104"),
("province1105","province1105"),
("province1106","province1106"),
("province1107","province1107"),
("province1108","province1108"),
("province1109","province1109"),
("province1110","province1110"),
("province1111","province1111"),
("province1112","province1112"),
("province1113","province1113"),
("province1114","province1114"),
("province1115","province1115"),
("province1116","province1116"),
("province1117","province1117"),
("province1118","province1118"),
("province1119","province1119"),
("province1120","province1120"),
("province1121","province1121"),
("province1122","province1122"),
("province1123","province1123"),
("province1124","province1124"),
("province1125","province1125"),
("province1126","province1126"),
("province1127","province1127"),
("province1128","province1128"),
("province1129","province1129"),
("province1130","province1130"),
("province1131","province1131"),
("province1132","province1132"),
("province1133","province1133"),
("province1134","province1134"),
("province1135","province1135"),
("province1136","province1136"),
("province1137","province1137"),
("province1138","province1138"),
("province1139","province1139"),
("province1140","province1140"),
("province1141","province1141"),
("province1142","province1142"),
("province1143","province1143"),
("province1144","province1144"),
("province1145","province1145"),
]
