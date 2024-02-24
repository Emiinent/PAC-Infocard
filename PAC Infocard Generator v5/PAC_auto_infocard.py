import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st
from tkinter import messagebox
import webbrowser

apCount = 0
regCount = 0
apIndex = 0
regIndex = 0
rarity_colors = {}
ap_value_list = []
reg_value_list = []
apEntry = []
regEntry = []
ultimate_ability = {
    "name": '',
    "description": '',
    "ap_value": [],
    "reg_value": []
}

html = ""
# Dictionary mapping rarities to their corresponding rgb values
rarity_colors = {
    'Common': 'rgb(159, 159, 159)',
    'Uncommon': 'rgb(59, 201, 94)',
    'Rare': 'rgb(65, 191, 204)',
    "Epic": 'rgb(202, 108, 238)',
    'Ultra': 'rgb(229, 59, 59)',
    'Unique': 'rgb(255, 255, 255)',
    'Legendary': 'rgb(230, 203, 73)',
    'Hatch': 'rgb(185, 145, 90)',
    'Special': 'rgb(150, 127, 255)'
}

def generate_pokemon_card(name, rarity_label, stars, types, stats, passive_ability, ultimate_ability, portrait_url, passive_box_height=None, ultimate_box_height=None):
    # Construct the rarity tier section with stars
    rarity_tier = ''.join(f'<img src="assets/ui/star.svg" height="16">' for _ in range(stars))

    # Construct the types section
    types_section = ''
    for i in types:
        
        for t, url in types_data:
            if t == i:
                # If it's an asset URL, construct the image tag using the asset URL
                types_section += f'<img src="{url}" alt="{t.capitalize()}" title="{t.capitalize()}" class="synergy-icon" style="width: 40px; height: 40px;">'

        #for n, url2 in types_data_custom:
            #if n == i:
                # If it's an asset URL, construct the image tag using the asset URL
                #types_section += f'<img src="{url2}" alt="{n.capitalize()}" title="{n.capitalize()}" class="synergy-icon" style="width: 32px; height: 32px; margin-top: 4px; margin-right: 4px;">'

     

    
    # Construct the stats section
    stats_section = ''.join(f'<div><img src="assets/icons/{stat.upper()}.png" alt="{stat.upper()}" title="{stat.capitalize()}"><p>{value}</p></div>' for stat, value in stats.items())
    
# Define a dictionary mapping status names to their corresponding image filenames
    item_images = {
    'Fossil Stone' : 'FOSSIL_STONE',
    'Twisted Spoon' : 'TWISTED_SPOON',
    'Magnet' : 'MAGNET',
    'Black Glasses' : 'BLACK_GLASSES',
    'Miracle Seed' : 'MIRACLE_SEED',
    'Charcoal' : 'CHARCOAL',
    'Never Melt Ice' : 'NEVER_MELT_ICE',
    'Heart Scale' : 'HEART_SCALE',
    'Mystic Water' : 'MYSTIC_WATER',
    'Old Amber' : 'OLD_AMBER',
    'Dawn Stone' : 'DAWN_STONE',
    'Thunder Stone' : 'THUNDER_STONE',
    'Dusk Stone' : 'DUSK_STONE',
    'Leaf Stone' : 'LEAF_STONE',
    'Fire Stone' : 'FIRE_STONE',
    'Ice Stone' : 'ICE_STONE',
    'Moon Stone' : 'MOON_STONE',
    'Water Stone' : 'WATER_STONE',
    'Choice Specs' : 'CHOICE_SPECS',
    'Upgrade' : 'UPGRADE',
    'Reaper Cloth' : 'REAPER_CLOTH',
    'Pokemonomicon' : 'POKEMONOMICON',
    'Shell Bell' : 'SHELL_BELL',
    'Power Lens' : 'POWER_LENS',
    'Lucky Egg' : 'LUCKY_EGG',
    'Soul Dew' : 'SOUL_DEW',
    'Xray Vision' : 'XRAY_VISION',
    'Razor Fang' : 'RAZOR_FANG',
    'Leftovers' : 'LEFTOVERS',
    'Fire Gem' : 'FIRE_GEM',
    'Choice Scarf' : 'CHOICE_SCARF',
    'Defensive Ribbon' : 'DEFENSIVE_RIBBON',
    'Blue Orb' : 'BLUE_ORB',
    'Wonder Box' : 'WONDER_BOX',
    'Cleanse Tag' : 'CLEANSE_TAG',
    'Razor Claw' : 'RAZOR_CLAW',
    'Wide Lens' : 'WIDE_LENS',
    'Fluffy Tail' : 'FLUFFY_TAIL',
    'Scope Lens' : 'SCOPE_LENS',
    'Kings Rock' : 'KINGS_ROCK',
    'Gracidea Flower' : 'GRACIDEA_FLOWER',
    'Shiny Charm' : 'SHINY_CHARM',
    'Flame Orb' : 'FLAME_ORB',
    'Star Dust' : 'STAR_DUST',
    'Red Orb' : 'RED_ORB',
    'Amulet Coin' : 'AMULET_COIN',
    'Max Revive' : 'MAX_REVIVE',
    'Mana Scarf' : 'MANA_SCARF',
    'Electirizer' : 'ELECTIRIZER',
    'Magmarizer' : 'MAGMARIZER',
    'Exp Share' : 'EXP_SHARE',
    'Light Ball' : 'LIGHT_BALL',
    'Toxic Orb' : 'TOXIC_ORB',
    'Hard Stone' : 'HARD_STONE',
    'Metal Coat' : 'METAL_COAT',
    'Swift Wing' : 'SWIFT_WING',
    'Macho Brace' : 'MACHO_BRACE',
    'Incense' : 'INCENSE',
    'Metronome' : 'METRONOME',
    'Big Nugget' : 'BIG_NUGGET',
    'Smoke Ball' : 'SMOKE_BALL',
    'Delta Orb' : 'DELTA_ORB',
    'Aqua Egg' : 'AQUA_EGG',
    'Aguav Berry' : 'AGUAV_BERRY',
    'Apicot Berry' : 'APICOT_BERRY',
    'Aspear Berry' : 'ASPEAR_BERRY',
    'Babiri Berry' : 'BABIRI_BERRY',
    'Cheri Berry' : 'CHERI_BERRY',
    'Chesto Berry' : 'CHESTO_BERRY',
    'Ganlon Berry' : 'GANLON_BERRY',
    'Jaboca Berry' : 'JABOCA_BERRY',
    'Lansat Berry' : 'LANSAT_BERRY',
    'Leppa Berry' : 'LEPPA_BERRY',
    'Liechi Berry' : 'LIECHI_BERRY',
    'Lum Berry' : 'LUM_BERRY',
    'Oran Berry' : 'ORAN_BERRY',
    'Pecha Berry' : 'PECHA_BERRY',
    'Persim Berry' : 'PERSIM_BERRY',
    'Petaya Berry' : 'PETAYA_BERRY',
    'Rawst Berry' : 'RAWST_BERRY',
    'Rowap Berry' : 'ROWAP_BERRY',
    'Salac Berry' : 'SALAC_BERRY',
    'Sitrus Berry' : 'SITRUS_BERRY',
  
}

    multi_data_banana = {
    'Grassy Field' : 'grassy_field_banana',
    'Electric Field' : 'electric_field_banana',
    'Fairy Field' : 'fairy_field_banana',
    'Psychic Field' : 'psychic_field_banana',
    'Special Defense' : 'special_defense_banana',
    'Rune Protect' : 'rune_banana',
    'Attack Speed' : 'attack_speed_banana',
    'TypePoison' : 'poi_banana'
    
    }
    
    
    
    # Define a dictionary mapping status names to their corresponding image filenames
    status_images = {
        'RuneProtect' : 'RUNE_PROTECT',
        'Burn': 'BURN',
        'Silence': 'SILENCE',
        'Confusion': 'CONFUSION',
        'Freeze': 'FREEZE',
        'Paralyzed': 'PARALYSIS',
        'Poison': 'POISONNED',
        'Sleep': 'SLEEP',
        'Wound': 'WOUND',
        'Charmed': 'CHARM',
        'Curse' : 'CURSE',
        'Flinch' : 'FLINCH',
        'Protect' : 'PROTECT',
        'Resurection' : 'RESURECTION',
        'Armor Reduction' : 'ARMOR_REDUCTION',
        'Armour Reduction' : 'ARMOR_REDUCTION'
        #'ElectricField' : 'ELECTRIC_FIELD',
        #'GrassField' : 'GRASS_FIELD',
        #'FairyField' : 'FAIRY_FIELD',
        #'PsychicField' : 'PSYCHIC_FIELD',
        
      
    }

    # Define a dictionary mapping Weather names to their corresponding image filenames
    weather_images = {
        'Zenith' : 'sun',
        'Rain' : 'rain',
        'Snow' : 'snow',
        'Night' : 'night',
        'Windy' : 'windy',
        'Misty' : 'misty',
        'Storm' : 'storm',
        'Sandstorm' : 'sandstorm',
        'Calm' : 'neutral',
        
    }

      # Define a dictionary mapping Weather names to their corresponding image filenames
    stats_images = {
       'HP' : 'HP',
        'Shield' : 'SHIELD',
        'Defense' : 'DEF',
        'Special Def' : 'SP_DEF',
        'PP' : 'PP',
        'Attack' : 'ATK',
        'Range' : 'RANGE',
        'ATK Speed' : 'ATK_SPEED',
        'Crit Chance' : 'CRIT_CHANCE',
        'Crit Damage' : 'CRIT_DAMAGE'
    }
    
        

    

    # Define a dictionary mapping Types names to their corresponding image filenames
    type_images = {
        'TypeNormal' : 'NORMAL',
        'TypeGrass' : 'GRASS',
        'TypeFire' : 'FIRE',
        'TypeWater' : 'WATER',
        'TypeElectric' : 'ELECTRIC',
        'TypeFighting' : 'FIGHTING',
        'TypePsychic' : 'PSYCHIC',
        'TypeDark' : 'DARK',
        'TypeSteel' : 'STEEL',
        'TypeGround' : 'GROUND',
        #'poi_banana' : 'POISON',
        'TypeDragon' : 'DRAGON',
        'TypeField' : 'FIELD',
        'TypeMonster' : 'MONSTER',
        'TypeHuman' : 'HUMAN',
        'TypeAquatic' : 'AQUATIC',
        'TypeBug' : 'BUG',
        'TypeFlying' : 'FLYING',
        'TypeFlora' : 'FLORA',
        'TypeRock' : 'ROCK',
        'TypeGhost' : 'GHOST',
        'TypeFairy' : 'FAIRY',
        'TypeIce' : 'ICE',
        'TypeFossil' : 'FOSSIL',
        'TypeSound' : 'SOUND',
        'TypeArtificial' : 'ARTIFICIAL',
        'TypeBaby' : 'BABY'
    }

    multi_data = {
    'grassy_field_banana' : 'html_grassy_field',
    'electric_field_banana' : 'html_electric_field',
    'fairy_field_banana' : 'html_fairy_field',
    'psychic_field_banana' : 'html_psychic_field',
    'special_defense_banana' : 'html_special_defense',
    'rune_banana' : 'html_rune_protect',
    'attack_speed_banana' : 'html_attack_speed'
    
    }

         # First, replace the placeholders with their corresponding banana placeholders
    for status, banana_placeholder in multi_data_banana.items():
        passive_ability = passive_ability.replace(status, banana_placeholder)
        ultimate_ability['description'] = ultimate_ability['description'].replace(status, banana_placeholder)
    print(ultimate_ability['description'])

    


    # Define a dictionary mapping Custom names to their corresponding image filenames
    custom_images = {
        'Money' : '"assets/icons/money.svg" style="width: 13.64px; height: 13.64px; margin-right: 3px">',
        'TypeWild' : '"https://i.ibb.co/s6qTY4S/Wild-Downsized.png" style="width: 20px; height: 20px; margin-right: 3px">Wild</span>',
        'poi_banana' : '"https://pokemon-auto-chess.com/assets/types/POISON.svg" style="width: 20px; height: 20px; margin-right: 3px">Poison</span>'
   }

     
    # Replace Types placeholders in ability descriptions with corresponding icons
    for status, image_filename in type_images.items():
        passive_ability = passive_ability.replace(status, f'<img src="assets/types/{image_filename.upper()}.svg" style="width: 20px; height: 20px; margin-right: 3px">{status[4:]}</span>')
        ultimate_ability['description'] = ultimate_ability['description'].replace(status, f'<img src="assets/types/{image_filename.upper()}.svg" style="width: 20px; height: 20px; margin-right: 3px">{status[4:]}</span>')

        # Replace status effect placeholders in ability descriptions with corresponding icons
    for status, image_filename in status_images.items():
        passive_ability = passive_ability.replace(status, f'<img src="assets/icons/{image_filename.upper()}.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">{status}</span>')
        ultimate_ability['description'] = ultimate_ability['description'].replace(status, f'<img src="assets/icons/{image_filename.upper()}.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">{status}</span>')
    print(ultimate_ability['description'])
         
         

        # Replace Stats placeholders in ability descriptions with corresponding custom icons
    for status, image_filename in stats_images.items():
        passive_ability = passive_ability.replace(status, f'<img src="assets/icons/{image_filename.upper()}.png" style="width: 20px; height: 20px; margin-right: 3px"><span class="stat-label">{status}</span>')
        ultimate_ability['description'] = ultimate_ability['description'].replace(status, f'<img src="assets/icons/{image_filename.upper()}.png" style="width: 20px; height: 20px; margin-right: 3px"><span class="stat-label">{status}</span>')
    print(ultimate_ability['description'])
    

    
   

        # Replace Items placeholders in ability descriptions with corresponding icons
    for status, image_filename in item_images.items():
        passive_ability = passive_ability.replace(status, f'<img src="assets/item/{image_filename.upper()}.png" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">{status}</span>')
        ultimate_ability['description'] = ultimate_ability['description'].replace(status, f'<img src="assets/item/{image_filename.upper()}.png" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">{status}</span>')
    print(ultimate_ability['description'])
        
        # Replace Weather placeholders in ability descriptions with corresponding icons
    for status, image_filename in weather_images.items():
        passive_ability = passive_ability.replace(status, f'<img src="assets/icons/weather/{image_filename.lower()}.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">{status}</span>')
        ultimate_ability['description'] = ultimate_ability['description'].replace(status, f'<img src="assets/icons/weather/{image_filename.lower()}.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">{status}</span>')
    print(ultimate_ability['description'])

    # Replace Types placeholders in ability descriptions with corresponding custom icons
    for status, image_url in custom_images.items():
        passive_ability = passive_ability.replace(status, f'<img src={image_url}')
        ultimate_ability['description'] = ultimate_ability['description'].replace(status, f'<img src={image_url}')
    print(ultimate_ability['description'])

    
        # Then, replace the banana placeholders with their corresponding HTML
    for banana_placeholder, html_variable in multi_data.items():
        passive_ability = passive_ability.replace(banana_placeholder, globals()[html_variable])
        ultimate_ability['description'] = ultimate_ability['description'].replace(banana_placeholder, globals()[html_variable])
    print(ultimate_ability['description'])


        # Replace AP value in passive with highlighted text
    for a in range(passive_ability.count("APValues")):
        passive_ability = passive_ability.replace("APValues", f'<img src="assets/icons/AP.png" style="width: 20px; height: 20px; margin-right: 3px" alt="Ability Power" title="Scales with Ability Power">{trackAPIndex()}',1)
    # Replace Regular values in ultimate ability with highlighted text
    for b in range(passive_ability.count("RegValues")):
        passive_ability = passive_ability.replace("RegValues", f'{trackRegIndex()}',1)

    # Replace AP value in ultimate ability with highlighted text
    for h in range(ultimate_ability['description'].count("APValues")):
        ultimate_ability['description'] = ultimate_ability['description'].replace("APValues", f'<img src="assets/icons/AP.png" style="width: 20px; height: 20px; margin-right: 3px" alt="Ability Power" title="Scales with Ability Power">{trackAPIndex()}',1)
    # Replace Regular values in ultimate ability with highlighted text
    for q in range(ultimate_ability['description'].count("RegValues")):
        ultimate_ability['description'] = ultimate_ability['description'].replace("RegValues", f'{trackRegIndex()}',1)
    
    #ultimate_ability['description'] = ultimate_ability['description'].replace("AP", f'<img src="assets/icons/AP.png" alt="Ability Power" title="Scales with Ability Power"><span class="ability-value" style="color: rgb(255, 165, 0); font-weight: bold;">{trackAPIndex()}</span>')
    #Highlight damage types in passive ability descriptions:
    passive_ability = passive_ability.replace("special damage", '<span class="damage-special">special damage</span>')
    passive_ability = passive_ability.replace("physical damage", '<span class="damage-physical">physical damage</span>')
    passive_ability = passive_ability.replace("true damage", '<span class="damage-true">true damage</span>')

    # Highlight "special damage" in ultimate ability description
    ultimate_ability['description'] = ultimate_ability['description'].replace("special damage", '<span class="damage-special">special damage</span>')
    ultimate_ability['description'] = ultimate_ability['description'].replace("physical damage", '<span class="damage-physical">physical damage</span>')
    ultimate_ability['description'] = ultimate_ability['description'].replace("true damage", '<span class="damage-true">true damage</span>')

    if passive_ability:
        passive_html = f"""<div class="game-pokemon-detail-passive">{passive_ability}</div>"""
    else:
        passive_html = ""

    # Construct the HTML for the Pokémon card
    global html
    html = f"""
    <div class="game-pokemon-detail-tooltip">
        <div class="game-pokemon-detail in-shop">
            <img class="game-pokemon-detail-portrait" src="{portrait_url}" style="border-color: {rarity_colors.get(rarity_label)};">
            <div class="game-pokemon-detail-entry">
                <p class="game-pokemon-detail-entry-name">{name}</p>
                <p class="game-pokemon-detail-entry-rarity" style="color: {rarity_colors.get(rarity_label)};">{rarity_label}</p>
                <p class="game-pokemon-detail-entry-tier">{rarity_tier}</p>
            </div>
            <div class="game-pokemon-detail-types">{types_section}</div>
            <div class="game-pokemon-detail-stats">{stats_section}</div>
            {passive_html}
            <div class="game-pokemon-detail-ult"><div class="ability-name">{ultimate_ability['name']}</div><div class="ability-description">{ultimate_ability['description']}</div></div>
        </div>
    </div>
    """
    return html

def trackAPIndex():
    global apIndex
    global ap_value_list
    
    apTextList = []
    starsCalc = []
    print('apIndex: ',apIndex)
    if int(stars.get())>len(ultimate_ability['ap_value'][apIndex]):
        starsCalc = len(ultimate_ability['ap_value'][apIndex])-1
    else:
        starsCalc = int(stars.get())-1
            
    for i in range(len(ultimate_ability['ap_value'][apIndex])):
        if starsCalc == i: 
            apTextList.append(f"""<span class="ability-value" style="color: rgb(209, 114, 255); font-weight: bold;"><span class>{ultimate_ability['ap_value'][apIndex][i]}</span>""")
        else:
            apTextList.append(f"""<span class="ability-value" style="color: rgb(68, 0, 147); font-weight: bold;"><span class>{ultimate_ability['ap_value'][apIndex][i]}</span>""")
        apTextList.append("</span>")
        if i != len(ultimate_ability['ap_value'][apIndex])-1:
            
            apTextList.append('<span class style="color: rgb(68, 0, 147); font-weight: bold;">/</span>')
    
    apIndex += 1
    
    return ''.join(apTextList)

def trackRegIndex():
    global regIndex
    global reg_value_list
    
    regTextList = []
    starsCalcReg = []

    if int(stars.get())>len(ultimate_ability['reg_value'][regIndex]):
        starsCalcReg = len(ultimate_ability['reg_value'][regIndex])-1
    else:
        starsCalcReg = int(stars.get())-1
    
    for k in range(len(ultimate_ability['reg_value'][regIndex])):

        if starsCalcReg == k:
            regTextList.append(f"""<span class="ability-value" style="color: rgb(255,255,255); font-weight: bold;"><span class>{ultimate_ability['reg_value'][regIndex][k]}</span>""")
        else:
            regTextList.append(f"""<span class="ability-value" style="color: rgb(171, 171, 171); font-weight: bold;"><span class>{ultimate_ability['reg_value'][regIndex][k]}</span>""")
        regTextList.append("</span>")
        if k != len(ultimate_ability['reg_value'][regIndex])-1:
            
            regTextList.append('<span class style="color: rgb(171, 171, 171); font-weight: bold;">/</span>')
        
    regIndex += 1
    
    return ''.join(regTextList)


html_grassy_field = '<img src="assets/icons/GRASS_FIELD.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">Grassy Field</span>'
html_electric_field = '<img src="assets/icons/ELECTRIC_FIELD.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">Electric Field</span>'
html_fairy_field = '<img src="assets/icons/FAIRY_FIELD.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">Fairy Field</span>'
html_psychic_field = '<img src="assets/icons/PSYCHIC_FIELD.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">Psychic Field</span>'
html_special_defense = '<img src="assets/icons/SP_DEF.png" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">Special Defense</span>'
html_rune_protect = '<img src="assets/icons/RUNE_PROTECT.svg" style="width: 20px; height: 20px; margin-right: 3px"><span class="status-label">Rune Protect</span>'
html_attack_speed = '<img src="assets/icons/ATK_SPEED.png" style="width: 20px; height: 20px; margin-right: 3px"><span class="stat-label">Attack Speed</span>'

    

types_data = [
    ('Normal', 'assets/types/NORMAL.svg'),
    ('Grass', 'assets/types/GRASS.svg'),
    ('Fire', 'assets/types/FIRE.svg'),
    ('Water', 'assets/types/WATER.svg'),
    ('Electric', 'assets/types/ELECTRIC.svg'),
    ('Fighting', 'assets/types/FIGHTING.svg'),
    ('Psychic', 'assets/types/PSYCHIC.svg'),
    ('Dark', 'assets/types/DARK.svg'),
    ('Steel', 'assets/types/STEEL.svg'),
    ('Ground', 'assets/types/GROUND.svg'),
    ('Poison', 'assets/types/POISON.svg'),
    ('Dragon', 'assets/types/DRAGON.svg'),
    ('Field', 'assets/types/FIELD.svg'),
    ('Monster', 'assets/types/MONSTER.svg'),
    ('Human', 'assets/types/HUMAN.svg'),
    ('Aquatic', 'assets/types/AQUATIC.svg'),
    ('Bug', 'assets/types/BUG.svg'),
    ('Flying', 'assets/types/FLYING.svg'),
    ('Flora', 'assets/types/FLORA.svg'),
    ('Rock', 'assets/types/ROCK.svg'),
    ('Ghost', 'assets/types/GHOST.svg'),
    ('Fairy', 'assets/types/FAIRY.svg'),
    ('Ice', 'assets/types/ICE.svg'),
    ('Fossil', 'assets/types/FOSSIL.svg'),
    ('Sound', 'assets/types/SOUND.svg'),
    ('Artificial', 'assets/types/ARTIFICIAL.svg'),
    ('Baby', 'assets/types/BABY.svg'),
    ('Wild', 'https://i.ibb.co/s6qTY4S/Wild-Downsized.png'),
    ]


# Copy code to clipboard
def copycode():
    m.clipboard_clear()
    m.clipboard_append(html)
    m.update()

# Generate HTML for the Pokémon card
def submit():
    global ultimate_ability
    global apIndex
    global regIndex
    #ultimate_ability['ap_value'] = []
    #ultimate_ability['reg_value'] = []
    types = []
    typesTemp = [type1.get(), type2.get(), type3.get(), type4.get()]
    for i in range(4):
        if typesTemp[i] != 'None' and typesTemp[i]:
            types.append(typesTemp[i])
    stats = {
        "HP":int(hp.get()),
        "DEF":int(defence.get()),
        "ATK":int(atk.get()),
        "PP":int(pp.get()),
        "SPE_DEF":int(spe_def.get()),
        "RANGE":int(atk_range.get())
    }
    passive_ability = passiveText.get(1.0,tk.END)

    ultimate_ability['name'] = ult_name.get()
    ultimate_ability['description'] = ultDescText.get(1.0,tk.END)
    ultimate_ability['ap_value'].clear()
    ultimate_ability['reg_value'].clear()
    print('reg value 1: ',ultimate_ability['reg_value'])
    
    global ap_value_list
    global apEntry
    ap_value_list.clear()
    apIndex = 0
    
    for w in apEntry:
        ap_value_list.append(str(w.get()))

    for i in range(len(ap_value_list)):
        ap_split_list= ap_value_list[i].split('/')

        ultimate_ability['ap_value'].append(ap_split_list)

    global reg_value_list
    global regEntry
    reg_value_list.clear()
    regIndex = 0
    
    for n in regEntry:
        reg_value_list.append(str(n.get()))

    for d in range(len(reg_value_list)):
        reg_split_list = reg_value_list[d].split('/')
        
        ultimate_ability['reg_value'].append(reg_split_list)

    ap_value_count = 0
    
    for j in range(len(ultimate_ability['ap_value'])):
        if ultimate_ability['ap_value'][j] != ['']:
            ap_value_count += 1
            
    if passive_ability.count("APValues") + ultimate_ability['description'].count("APValues") > ap_value_count:
        messagebox.showerror("Error", "'APValues' terms must appear as often as their corresponding values. Delete unused 'APValues' terms.")
        return
    if passive_ability.count("APValues") + ultimate_ability['description'].count("APValues") < ap_value_count:
        messagebox.showerror("Error", "'APValues' terms must appear as often as their corresponding values. Delete text from unused fields.")
        return

    reg_value_count = 0
    
    for t in range(len(ultimate_ability['reg_value'])):
        if ultimate_ability['reg_value'][t] != ['']:
            reg_value_count += 1

    if passive_ability.count("RegValues") + ultimate_ability['description'].count("RegValues") > reg_value_count:
        messagebox.showerror("Error", "'RegValues' terms must appear as often as their corresponding values. Delete unused 'RegValues' terms.")
        return

    if passive_ability.count("RegValues") + ultimate_ability['description'].count("RegValues") < reg_value_count:
        messagebox.showerror("Error", "'RegValues' terms must appear as often as their corresponding values. Delete text from unused fields.")
        return
    
    print('\nreg value ',ultimate_ability['reg_value'])
    textOutput.delete('1.0', tk.END)
    html = generate_pokemon_card(name.get(), rarity_label.get(), int(stars.get()), types, stats, passive_ability, ultimate_ability, portrait_url.get())
    
    # Print the HTML
    print(html)
    textOutput.insert(tk.END, html)
    
    #ap_value_list = []
    #apEntry = []
    #apIndex = 0
    #ap_split_list = []
    
    #ap_value_list = []
    #apIndex = 0

def apInsert(textbox):
    global apCount
    global ap_value_list
    global apEntry
    apLabels = []
    
    textbox.insert("insert","APValues")

    newAPEntry = tk.Entry(m,bg='#7c8ea1', fg='#ffffff', font=defaultFontTuple)
    newAPEntry.place(x=220, y=450+20*apCount, width=80)
    apEntry.append(newAPEntry)

    """newAPLabel = tk.Label(m, text="yay")
    newAPLabel.place(x=205, y=450+20*apCount)
    apLabels.append(newAPLabel)
    if(textbox == passiveText):
        newAPLabel.configure(text="Passive:")
    else:
        newAPLabel.configure(text="Ability:")
        
    """
    apCount += 1

def regInsert(textbox):
    global regCount
    global reg_value_list
    global regEntry
    textbox.insert("insert","RegValues")

    newRegEntry = tk.Entry(m,bg='#7c8ea1', fg='#ffffff', font=defaultFontTuple)
    newRegEntry.place(x=70, y=450+20*regCount,width=80)
    regEntry.append(newRegEntry)

    regCount += 1

def openTutorial():
    webbrowser.open_new('https://www.youtube.com/watch?v=SJc6qBy21EI')

def openPastebin():
    webbrowser.open_new('https://pastebin.com/CtyA20eR')
    
    
m = tk.Tk()
m.geometry('950x580')
m.configure(background='#54596b')
m.title('PAC Infocard Generator')

def on_enter(e):
    e.widget['background'] = '#1195ec'

def on_leave(e):
    e.widget['background'] = '#61738a'

defaultFontTuple = ('Calibri',11,"bold")
comboboxStyle = ttk.Style()
comboboxStyle.theme_create('comboboxStyle', parent='alt',
                           settings = {'TCombobox':
                                       {'configure':
                                        {'selectbackground': '#7c8ea1',
                                         'fieldbackground': '#7c8ea1',
                                         'background': '#7c8ea1',
                                         'foreground': '#ffffff',
                                         }}}
                           )

comboboxStyle.theme_use('comboboxStyle')

portrait_url = tk.StringVar()
name = tk.StringVar()
rarity_label = tk.StringVar()
stars = tk.StringVar()
type1 = tk.StringVar()
type2 = tk.StringVar()
type3 = tk.StringVar()
type4 = tk.StringVar()
hp = tk.StringVar()
defence = tk.StringVar()
atk = tk.StringVar()
pp = tk.StringVar()
spe_def = tk.StringVar()
atk_range = tk.StringVar()
ult_name = tk.StringVar()
passive_text = tk.StringVar()

developerLabel = tk.Label(text='Developed by Emii and Windchilled',font=('Calibri',12,'bold'), background='#54596b', fg='#ffffff')
developerLabel.place(x=690,y=10)

copyHTMLButton = tk.Button(m, text='Copy HTML', bg='#61738a', fg='#ffffff', relief="ridge", command=copycode)
copyHTMLButton.place(x=710, y=340, width=90)
copyHTMLButton.bind("<Enter>", on_enter)
copyHTMLButton.bind("<Leave>", on_leave)

submitButton = tk.Button(m, text='Submit', bg='#61738a', fg='#ffffff',relief='ridge', command=submit)
submitButton.place(x=550, y=340, width=90)
submitButton.bind("<Enter>", on_enter)
submitButton.bind("<Leave>", on_leave)

templateImage = tk.PhotoImage(file='autocardTemplate.png')
cardTemplate = tk.Label(m, image = templateImage, background='#54596b')
cardTemplate.place(x=30,y=70)

formatKeyImage = tk.PhotoImage(file='formattingKey2.png')
formatKeyImage = formatKeyImage.subsample(4,4)
formatKey = tk.Label(m, image = formatKeyImage, background='#54596b')
formatKey.place(x=460,y=390)

portraitURLEntry = tk.Entry(m, bg='#7c8ea1', fg='#ffffff', font=defaultFontTuple, textvariable = portrait_url)
portraitURLEntry.place(x=37, y=35, height = 25, width = 500)

portraitURLLabel = tk.Label(m, bg='#54596b', fg='#ffffff', font=defaultFontTuple, text='Input Portrait URL:')
portraitURLLabel.place(x=37,y=10)

nameEntry = tk.Entry(m,bg='#7c8ea1', fg='#ffffff',font=defaultFontTuple, textvariable = name)
nameEntry.place(x=140, y=90, height = 25, width=100)

typeValues = ('None', 'Artificial', 'Aquatic', 'Baby', 'Bug', 'Dark', 'Dragon',
              'Electric','Fairy','Field','Fighting','Fire','Flora','Flying',
              'Fossil','Ghost','Grass','Ground','Human','Ice','Light','Monster','Normal',
              'Poison','Psychic','Rock','Sound','Steel','Water','Wild')

typeCombobox1 = ttk.Combobox(m, width = 8, height=20, textvariable = type1)
typeCombobox1['values'] = typeValues
typeCombobox1.place(x=270, y=90, height=19)
typeCombobox1.configure(font=('TKDefaultFont',9,'bold'))

typeCombobox2 = ttk.Combobox(m, width=8, height = 20, textvariable = type2)
typeCombobox2['values'] = typeValues
typeCombobox2.place(x=270, y=108, height=19)
typeCombobox2.configure(font=('TKDefaultFont',9,'bold'))

typeCombobox3 = ttk.Combobox(m, width=8, height = 20, textvariable = type3)
typeCombobox3['values'] = typeValues
typeCombobox3.place(x=270, y=126, height=19)
typeCombobox3.configure(font=('TKDefaultFont',9,'bold'))

typeCombobox4 = ttk.Combobox(m, width=8, height = 20, textvariable = type4)
typeCombobox4['values'] = typeValues
typeCombobox4.place(x=270, y=144, height=19)
typeCombobox4.configure(font=('TKDefaultFont',9,'bold'))

rarityCombobox = ttk.Combobox(m, width = 11, textvariable= rarity_label)
rarityCombobox['values'] = ('Common',
                            'Uncommon',
                            'Rare',
                            'Epic',
                            'Ultra',
                            'Unique',
                            'Legendary',
                            'Hatch',
                            'Special')
rarityCombobox.place(x=140, y=119)
rarityCombobox.configure(font=('TKDefaultFont',9,'bold'))

starsCombobox = ttk.Combobox(m, width=2, textvariable=stars)
starsCombobox['values'] = (1,2,3,4)
starsCombobox.place(x=158, y=142)
starsCombobox.configure(font=('TKDefaultFont',9,'bold'))

hpEntry = tk.Entry(m, bg='#7c8ea1', fg='#ffffff',font=("Calibri",12,"bold"), textvariable = hp)
hpEntry.place(x=80, y=180, height = 25, width=40)

defEntry = tk.Entry(m, bg='#7c8ea1', fg='#ffffff',font=("Calibri",12,"bold"), textvariable = defence)
defEntry.place(x=182, y=180, height = 25, width=40)

atkEntry = tk.Entry(m, bg='#7c8ea1', fg='#ffffff',font=("Calibri",12,"bold"),textvariable = atk)
atkEntry.place(x=283, y=180, height = 25, width=40)

ppEntry = tk.Entry(m, bg='#7c8ea1', fg='#ffffff',font=("Calibri",12,"bold"),textvariable = pp)
ppEntry.place(x=80, y=213, height = 25, width=40)

spe_defEntry = tk.Entry(m,bg='#7c8ea1', fg='#ffffff', font=("Calibri",12,"bold"),textvariable = spe_def)
spe_defEntry.place(x=182, y=213, height = 25, width=40)

rangeEntry = tk.Entry(m,bg='#7c8ea1', fg='#ffffff', font=("Calibri",12,"bold"),textvariable = atk_range)
rangeEntry.place(x=283, y=213, height = 25, width=40)

passiveText = st.ScrolledText(m,wrap=tk.WORD, bg='#54596b', fg='#ffffff', font=defaultFontTuple)
passiveText.place(x=50,y=250,width=280,height=45)

ultNameEntry = tk.Entry(m, bg='#54596b', fg='#ffffff', font=("Calibri",13,"bold"), textvariable = ult_name)
ultNameEntry.place(x=50,y=307,width=140,height=30)

ultDescText = st.ScrolledText(m,bg='#7c8ea1', fg='#ffffff', font=defaultFontTuple, wrap=tk.WORD)
ultDescText.place(x=50,y=348,width=280,height=45)

textOutput = st.ScrolledText(m,bg='#7c8ea1', fg='#ffffff', width=45,height=15)
textOutput.place(x=490, y=80)

apValuePassiveButton = tk.Button(m, text='AP Values',relief="ridge", bg='#61738a', fg='#ffffff', command=lambda: apInsert(passiveText))
apValuePassiveButton.place(x=370,y=275,width=70)
apValuePassiveButton.bind("<Enter>", on_enter)
apValuePassiveButton.bind("<Leave>", on_leave)

apValueUltButton = tk.Button(m, text='AP Values', relief="ridge",bg='#61738a', fg='#ffffff', command=lambda: apInsert(ultDescText))
apValueUltButton.place(x=370,y=369,width=70)
apValueUltButton.bind("<Enter>", on_enter)
apValueUltButton.bind("<Leave>", on_leave)

regValuePassiveButton = tk.Button(m, text='Values',relief="ridge", bg='#61738a', fg='#ffffff', command=lambda: regInsert(passiveText))
regValuePassiveButton.place(x=370,y=245,width=70)
regValuePassiveButton.bind("<Enter>", on_enter)
regValuePassiveButton.bind("<Leave>", on_leave)

regValueUltButton = tk.Button(m, text='Values',relief="ridge", bg='#61738a', fg='#ffffff', command=lambda: regInsert(ultDescText))
regValueUltButton.place(x=370,y=340,width=70)
regValueUltButton.bind("<Enter>", on_enter)
regValueUltButton.bind("<Leave>", on_leave)

tutorialButton = tk.Button(m, text='Watch Tutorial', relief="ridge", bg='#61738a', fg='#ffffff', command=openTutorial)
tutorialButton.place(x=550,y=540)
tutorialButton.bind("<Enter>", on_enter)
tutorialButton.bind("<Leave>", on_leave)

PastebinButton = tk.Button(m, text='Open Keyword List', relief="ridge", bg='#61738a', fg='#ffffff', command=openPastebin)
PastebinButton.place(x=700,y=540)
PastebinButton.bind("<Enter>", on_enter)
PastebinButton.bind("<Leave>", on_leave)

#valuesBgLabel = tk.Label(m, bg='#7c8ea1')
#valuesBgLabel.place(x=50, y=420, width=100, height=120)

regValueLabel = tk.Label(m,bg='#54596b', fg='#ffffff', font=defaultFontTuple, text='Values:')
regValueLabel.place(x=70,y=420)

apValueLabel = tk.Label(m,bg='#54596b', fg='#ffffff', font=defaultFontTuple, text='AP Values:')
apValueLabel.place(x=220,y=420)



m.mainloop()
