import random
import csv


class Soldier(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name():
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Strength'
        attribute_2_t = 'Wits'
        attribute_3_t = 'Empathy'
        attribute_4_t = 'Agility'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        attributes = {}
        attributes.update({"Attributes": attribute})
        return attributes

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Close Combat', 'Stamina', 'Ranged Combat']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        final_skills = {}
        final_skills.update({'Skills': final_skill})
        return final_skills

    @staticmethod
    def get_money():
        d6 = random.randint(1, 6)
        starting_cash = d6 * 100
        cash = {}
        cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        starting_gear = {
            'M41A Pulse Rifle': 'a',        'M56A2 Smart Gun': 'a',
            'M313 Motion Tracker': 'b',     'G2 Electroshock Grenades': 'b',
            'IRC MK.35 Pressure Suit': 'c', 'M3 Personnel Armor': 'c',
            'Signal Flare': 'd',            'Deck of Cards': 'd'
            }
        gear = {}
        k_list = []
        v_list = []
        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue
        gear.update({"Starting Gear": k_list})
        return gear

    @staticmethod
    def get_career_talent():
        career_talents = ['Banter', 'Overkill', 'Past the Limit']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Bullet that you survived',
            'Lost friend\'s dog tags',
            'Trophy from a deafeted enemy',
            'Small bottle of hot sauce'
        ]

        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Crew Cut',
            'Arm Tattoo',
            'Scar',
            'Cold eyes',
            'Cocky grin',
            'Personalized body armor'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})
        return appearance

    @staticmethod
    def character_creator():
        return Soldier.get_name(), Soldier.get_attributes(), Soldier.get_skill(), Soldier.get_money(), \
               Soldier.get_gear(), Soldier.get_career_talent(), Soldier.get_signature_item(), Soldier.get_appearance()


class Marshal(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name(Marshal_dict = {}):
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Wits'
        attribute_2_t = 'Empathy'
        attribute_3_t = 'Agility'
        attribute_4_t = 'Strength'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        # attributes = {}
        # attributes.update({"Attributes": attribute})
        return attribute

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Observation', 'Manipulation', 'Ranged Combat']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        # final_skills = {}
        # final_skills.update({'Skills': final_skill})
        return final_skill

    @staticmethod
    def get_money():
        d6 = random.randint(1, 6)
        starting_cash = d6 * 100
        cash = {}
        cash.update({"Cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        d6 = random.randint(1, 6)
        starting_gear = {
            '.357 Magnum Revolver': 'a',            'Armat Model 37A2 12 gauge pump-action': 'a',
            'Binoculars': 'b',                      'Hi-beam flashlight': 'b',
            'Personal medkit': 'c',                 'Stun baton': 'c',
            str(d6) + ' doses Neversleep pills':    'd', 'Hand radio': 'd'
            }
        gear1 = {}
        gear2 = {}
        k_list = []
        v_list = []

        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue
        # print(k_list)
        gear1.update({"Gear Slot 2": k_list[0]})
        gear2.update({"Gear Slot 3": k_list[1]})
        return gear1, gear2

    @staticmethod
    def get_career_talent():
        career_talents = ['Authority', 'Investigator', 'Subdue']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Photo of a loved one',
            'Dented flask with an inscription on the front',
            'News clipping of an unsolved case',
            'Gold Shariff\'s badge'
        ]
        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Chewing a toothpick',
            'Cigarette',
            'Impressive mustache',
            'Worn cap',
            'Scar across face',
            'Graying hair',
            'Crew cut',
            'Inquisitive gaze',
            'Old lether jacket'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})

        return appearance

    @staticmethod
    def character_creator():

        return Marshal.get_name(), Marshal.get_attributes(), Marshal.get_skill(), Marshal.get_money(), \
             Marshal.get_gear(), Marshal.get_career_talent(), Marshal.get_signature_item(), Marshal.get_appearance()



Marshal.character_creator()


class Agent(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name():
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Wits'
        attribute_2_t = 'Empathy'
        attribute_3_t = 'Agility'
        attribute_4_t = 'Strength'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        attributes = {}
        attributes.update({"Attributes": attribute})
        return attributes

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Observation', 'Manipulation', 'Comtech']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        final_skills = {}
        final_skills.update({'Skills': final_skill})
        return final_skills

    @staticmethod
    def get_money():
        dice = []
        for i in range(2):
            d6 = random.randint(1, 6)
            dice.append(d6)
        starting_cash = sum(dice) * 100
        cash = {}
        cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        d6 = random.randint(1, 6)
        starting_gear = {
            'Leather briefcase': 'a',                                       'Chrome briefcase': 'a',
            'Gold-plated pen': 'b',                                         'Rolex watch': 'b',
            'Data transmitter card with corporate clearence level': 'c',    'M4A3 Service Pistol': 'c',
            str(d6) + ' doses Neversleep pills': 'd',                       str(d6) + ' doses Naproleve pills': 'd'
            }
        gear = {}
        k_list = []
        v_list = []

        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue

            gear.update({"Starting Gear": k_list})
        return gear

    @staticmethod
    def get_career_talent():
        career_talents = ['Cunning', 'Personal Safety', 'Take Control']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Letter of corporate authorization',
            'Divorce papers',
            'Employee of the year award',
            'Calfskin gloves'
        ]
        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Icy glare',
            'Disarming smile',
            'Expensive Rolex',
            'Unique signet ring',
            'Tanned',
            'Elaborate hairstyle',
            'Emotional stare',
            'Monogrammed silk tie'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})

        return appearance

    @staticmethod
    def character_creator():
        return Agent.get_name(), Agent.get_attributes(), Agent.get_skill(), Agent.get_money(), \
               Agent.get_gear(), Agent.get_career_talent(), Agent.get_signature_item(), Agent.get_appearance()


class Kid(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name():
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Agility'
        attribute_2_t = 'Strnegth'
        attribute_3_t = 'Wits'
        attribute_4_t = 'Empathy'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        attributes = {}
        attributes.update({"Attributes": attribute})
        return attributes

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Mobility', 'Survival', 'Observation']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        final_skills = {}
        final_skills.update({'Skills': final_skill})
        return final_skills

    @staticmethod
    def get_money():
        number_of_dice = 1
        dice = []
        for i in range(number_of_dice):
            d6 = random.randint(1, 6)
            dice.append(d6)
        starting_cash = sum(dice)
        cash = {}
        cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        d6 = random.randint(1, 6)
        #  str(d6) + ' doses Neversleep pills': 'd',
        starting_gear = {
            'Fishing line': 'a', 'Laser pointer': 'a',
            'Magnet': 'b', 'Radio-controlled car': 'b',
            'Yo-yo': 'c', 'Electronic handheld game': 'c',
            'Personal locator beacon': 'd', 'Coloring pens': 'd'
            }
        gear = {}
        k_list = []
        v_list = []

        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue

            gear.update({"Starting Gear": k_list})
        return gear

    @staticmethod
    def get_career_talent():
        career_talents = ['Beneath Notice', 'Dodge', 'Nimble']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Lunchbox covered in stickers',
            'Favorite doll or action figure',
            'Bracelett made by older sibling',
            'Comic book'
        ]
        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Grubby and unkempt',
            'Trendy sneakers that light up',
            'Denim jeans, torn at the knees',
            'T-Shirt with band logo',
            'Cargo shorts',
            'Ponytail',
            'Bored expression',
            'Baseball cap'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})

        return appearance

    @staticmethod
    def character_creator():
        return Kid.get_name(), Kid.get_attributes(), Kid.get_skill(), Kid.get_money(), \
               Kid.get_gear(), Kid.get_career_talent(), Kid.get_signature_item(), Kid.get_appearance()


class Medic(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name():
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Empathy'
        attribute_2_t = 'Agility'
        attribute_3_t = 'Strength'
        attribute_4_t = 'Wits'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        attributes = {}
        attributes.update({"Attributes": attribute})
        return attributes

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Mobility', 'Observation', 'Medical Aid']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        final_skills = {}
        final_skills.update({'Skills': final_skill})
        return final_skills

    @staticmethod
    def get_money():
        number_of_dice = 1
        dice = []
        for i in range(number_of_dice):
            d6 = random.randint(1, 6)
            dice.append(d6)
        starting_cash = sum(dice) * 100
        cash = {}
        cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        d6 = random.randint(1, 6)
        #  str(d6) + ' doses Neversleep pills': 'd',
        starting_gear = {
            'Surgical kit': 'a',                        'IRC MK.50 compression suit': 'a',
            str(d6) + ' doses Naproleve pills': 'b',    str(d6) + ' doses Neversleep pills': 'b',
            'Personal medkit': 'c',                     str(d6) + ' doses experimental X-Drugs': 'c',
            'Samani E-Series watch': 'd',               'Hand radio': 'd'
            }
        gear = {}
        k_list = []
        v_list = []

        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue

            gear.update({"Starting Gear": k_list})
        return gear

    @staticmethod
    def get_career_talent():
        career_talents = ['Calming Presence', 'Compassion', 'Field Surgeon']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Framed medical certificate',
            'Letter from son or daughter',
            'Last psych evaluation: "All clear at last"',
            'Stethoscope'
        ]
        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Sympathetic smile',
            'Short, tidy hair',
            'Warm, caring eyes',
            'Dark bags under eyes',
            'Fidgeting hands',
            'Calm and gentle voice',
            'Cold, unsympathetic stare',
            'Spectacles',
            'White coat'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})

        return appearance

    @staticmethod
    def character_creator():
        return Medic.get_name(), Medic.get_attributes(), Medic.get_skill(), Medic.get_money(), \
               Medic.get_gear(), Medic.get_career_talent(), Medic.get_signature_item(), Medic.get_appearance()


class Officer(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name():
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Empathy'
        attribute_2_t = 'Agility'
        attribute_3_t = 'Strength'
        attribute_4_t = 'Wits'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        attributes = {}
        attributes.update({"Attributes": attribute})
        return attributes

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Ranged Combat', 'Command', 'Manipulation']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        final_skills = {}
        final_skills.update({'Skills': final_skill})
        return final_skills

    @staticmethod
    def get_money():
        number_of_dice = 2
        dice = []
        for i in range(number_of_dice):
            d6 = random.randint(1, 6)
            dice.append(d6)
        starting_cash = sum(dice) * 100
        cash = {}
        cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        d6 = random.randint(1, 6)
        #  str(d6) + ' doses Neversleep pills': 'd',
        starting_gear = {
            'M4A3 Service Pistol': 'a', 'Rexim RXF-M5 EVA Pistol': 'a',
            'Samani E-Series watch': 'b', 'Binoculars': 'b',
            'M314 motion tracker': 'c', 'IRC MK.50 compression suit': 'c',
            'Seegson P-DAT': 'd', 'IFF transponder': 'd'
            }
        gear = {}
        k_list = []
        v_list = []

        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue

            gear.update({"Starting Gear": k_list})
        return gear

    @staticmethod
    def get_career_talent():
        career_talents = ['Field Commander', 'Influence', 'Pull Rank']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Ship\'s cat',
            'Letter of recommendation',
            'ICC Commercial Flight Officer license',
            'Log book'
        ]
        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Hair in a crew cut, or tied-back',
            'Serious, intense expression',
            'Spotless uniform',
            'Overworked and "strung-out"',
            'Stiff body posture',
            'Relaxed and soothing voice',
            'Jumpsuit with mission patch',
            'Impatiently taps a foot'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})

        return appearance

    @staticmethod
    def character_creator():
        return Officer.get_name(), Officer.get_attributes(), Officer.get_skill(), Officer.get_money(), \
               Officer.get_gear(), Officer.get_career_talent(), Officer.get_signature_item(), Officer.get_appearance()


class Pilot(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name():
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Agility'
        attribute_2_t = 'Strength'
        attribute_3_t = 'Wits'
        attribute_4_t = 'Empathy'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        attributes = {}
        attributes.update({"Attributes": attribute})
        return attributes

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Piloting', 'Ranged Combat', 'Comtech']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        final_skills = {}
        final_skills.update({'Skills': final_skill})
        return final_skills

    @staticmethod
    def get_money():
        number_of_dice = 1
        dice = []
        for i in range(number_of_dice):
            d6 = random.randint(1, 6)
            dice.append(d6)
        starting_cash = sum(dice) * 100
        cash = {}
        cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        d6 = random.randint(1, 6)
        #  str(d6) + ' doses Neversleep pills': 'd',
        starting_gear = {
            'M4A3 service pistol': 'a',                 'PR-PUT uplink terminal': 'a',
            'Hand radio': 'b',                          str(d6) + ' flares': 'b',
            'Maintenance jack': 'c',                    'Seegson P-DAT': 'c',
            'Seegson system diagnostic device': 'd',    'IRC M.50 compression suit': 'd'
            }
        gear = {}
        k_list = []
        v_list = []

        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue

            gear.update({"Starting Gear": k_list})
        return gear

    @staticmethod
    def get_career_talent():
        career_talents = ['Full Throttle', ' Like the Back of Your Hand', 'Reckless']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Dashboard dancer',
            'Pilot\'s logbook',
            'Pilot\'s shades',
            'Plastic dinosaurs'
        ]
        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Arrogant walk',
            'Steely blue eyes',
            'Multi-pocket flight suit',
            'Sunglasses',
            'Previous mission patches',
            'Deadpan expression',
            'Chews gum',
            'Skeptical look'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})

        return appearance

    @staticmethod
    def character_creator():
        return Pilot.get_name(), Pilot.get_attributes(), Pilot.get_skill(), Pilot.get_money(), \
               Pilot.get_gear(), Pilot.get_career_talent(), Pilot.get_signature_item(), Pilot.get_appearance()


class Roughneck(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name():
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Strength'
        attribute_2_t = 'Wits'
        attribute_3_t = 'Empathy'
        attribute_4_t = 'Agility'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        attributes = {}
        attributes.update({"Attributes": attribute})
        return attributes

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Heavy Machinery', 'Stamina', 'Close Combat']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        final_skills = {}
        final_skills.update({'Skills': final_skill})
        return final_skills

    @staticmethod
    def get_money():
        number_of_dice = 1
        dice = []
        for i in range(number_of_dice):
            d6 = random.randint(1, 6)
            dice.append(d6)
        starting_cash = sum(dice) * 100
        cash = {}
        cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        d6 = random.randint(1, 6)
        #  str(d6) + ' doses Neversleep pills': 'd',
        starting_gear = {
            'Cutting torch': 'a',                   'Watsumi DV-303 bolt gun': 'a',
            str(d6) + ' doses Hydr8tion': 'b',      'Maintenance jack': 'b',
            'Stash of hard liquor': 'c',            'IRC MK.50 compression suit': 'c',
            'Hi-beam flashlight': 'd',              'Seegson C-Series magnetic tape recorder': 'd'
            }
        gear = {}
        k_list = []
        v_list = []

        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue

            gear.update({"Starting Gear": k_list})
        return gear

    @staticmethod
    def get_career_talent():
        career_talents = ['Resilient', 'The Long Haul', 'True Grit']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Tool belt',
            'Photo of partner',
            'Crucifix or other religious symbol',
            'Pet rat'
        ]
        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Tattoos',
            'Scar',
            'Broken nose',
            'Mirthless eyes',
            'Smirking face',
            'Loud laugh',
            'Bruised and calloused hands',
            'Eyes hidden behind safety goggles',
            'Filthy boots that clomp loudly when you walk',
            'Wild hair'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})

        return appearance

    @staticmethod
    def character_creator():
        return Roughneck.get_name(), Roughneck.get_attributes(), Roughneck.get_skill(), Roughneck.get_money(), \
               Roughneck.get_gear(), Roughneck.get_career_talent(), Roughneck.get_signature_item(), \
               Roughneck.get_appearance()


class Scientist(object):

    def __init__(self):
        pass

    @staticmethod
    def get_name():
        name_getter = csv.reader(open(r'Names.txt', 'r'))
        names = sum([i for i in name_getter], [])  # To flatten the list
        names = random.choice(names)
        name = {}
        name.update({"Name": names})
        return name

    @staticmethod
    def get_attributes():
        attribute = {}
        key_attribute_t = 'Wits'
        attribute_2_t = 'Empathy'
        attribute_3_t = 'Agiity'
        attribute_4_t = 'Strength'
        key_attribute = random.randint(4, 5)
        attribute.update({key_attribute_t: key_attribute})
        attribute_2 = random.randint(2, 4)
        attribute.update({attribute_2_t: attribute_2})
        if key_attribute + attribute_2 == 9:
            attribute_3 = random.randint(2, 3)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 8:
            attribute_3 = random.randint(2, 4)
            attribute.update({attribute_3_t: attribute_3})
            if attribute_3 == 2:
                attribute_4 = 4
                attribute.update({attribute_4_t: attribute_4})
            elif attribute_3 == 3:
                attribute_4 = 3
                attribute.update({attribute_4_t: attribute_4})
            else:
                attribute_4 = 2
                attribute.update({attribute_4_t: attribute_4})
        elif key_attribute + attribute_2 == 7:
            attribute_3 = random.randint(3, 4)
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
            attribute.update({attribute_4_t: attribute_4})
        else:
            attribute_3 = 4
            attribute.update({attribute_3_t: attribute_3})
            attribute_4 = 4
            attribute.update({attribute_4_t: attribute_4})

        attributes = {}
        attributes.update({"Attributes": attribute})
        return attributes

    @staticmethod
    def skill_values():
        skill_getter = csv.reader(open(r'Skills.txt', 'r'))
        data = sum([i for i in skill_getter], [])  # To flatten the list
        skill = random.choice(data)
        return skill

    @staticmethod
    def get_skill():
        key_skills = ['Observation', 'Survival', 'Comtech']
        final_skill = {}
        skills_list = []
        skill_total = 10
        while skill_total >= 1:
            skill = Soldier.skill_values()
            if skill not in skills_list:
                if skill in key_skills and skill_total > 2:
                    skills_list.append(skill)
                    v = random.randint(1, 3)
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
                else:
                    skills_list.append(skill)
                    v = 1
                    s = skill
                    final_skill.update({s: v})
                    skill_total = skill_total - v
        final_skills = {}
        final_skills.update({'Skills': final_skill})
        return final_skills

    @staticmethod
    def get_money():
        number_of_dice = 1
        dice = []
        for i in range(number_of_dice):
            d6 = random.randint(1, 6)
            dice.append(d6)
        starting_cash = sum(dice) * 100
        cash = {}
        cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
        return cash

    @staticmethod
    def get_gear():
        n = 0
        d6 = random.randint(1, 6)
        #  str(d6) + ' doses Neversleep pills': 'd',
        starting_gear = {
            'Digital video camera': 'a', 'Hand radio': 'a',
            'Seegson P-Dat': 'b', 'Neuro visor': 'b',
            'Seegson System Diagnostic Device': 'c', 'Personal Data Transmitter': 'c',
            'M314 motion tracker': 'd', 'Personal medkit': 'd'
            }
        gear = {}
        k_list = []
        v_list = []

        while 0 <= n < 2:
            k, v = random.choice(list(starting_gear.items()))
            if v not in v_list and k not in k_list:
                v_list.append(v)
                k_list.append(k)
                n = n + 1
            else:
                continue

            gear.update({"Starting Gear": k_list})
        return gear

    @staticmethod
    def get_career_talent():
        career_talents = ['Analysis', 'Breakthrough', 'Inquisitive']
        career_talent = {}
        career_talent.update({"Career talent": random.choice(career_talents)})
        return career_talent

    @staticmethod
    def get_signature_item():
        signature_items = [
            'Albert Einstein Award',
            'Unfinished scientific paper',
            'Blackmail letter',
            'Specimen collecting kit'
        ]
        signature_item = {}
        signature_item.update({"Signature Item": random.choice(signature_items)})
        return signature_item

    @staticmethod
    def get_appearance():
        appearance_list = [
            'Unkempt, untidy appearance',
            'Stained lab coat',
            'Nervous manner',
            'Hands constantly shoved in pockets',
            'Tidy. well-trimmed hair',
            'Thoughtful gaze',
            'Clears throat before speaking',
            'Bleary, overworked eyes'
        ]
        appearance = {}
        appearance.update({"Appearance": random.choice(appearance_list)})

        return appearance

    @staticmethod
    def character_creator():
        return Scientist.get_name(), Scientist.get_attributes(), Scientist.get_skill(), Scientist.get_money(), \
               Scientist.get_gear(), Scientist.get_career_talent(), Scientist.get_signature_item(), \
               Scientist.get_appearance()


# class z(object):
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_name():
#         name_getter = csv.reader(open(r'Names.txt', 'r'))
#         names = sum([i for i in name_getter], [])  # To flatten the list
#         names = random.choice(names)
#         name = {}
#         name.update({"Name": names})
#         return name
#
#     @staticmethod
#     def get_attributes():
#         attribute = {}
#         key_attribute_t = ''
#         attribute_2_t = ''
#         attribute_3_t = ''
#         attribute_4_t = ''
#         key_attribute = random.randint(4, 5)
#         attribute.update({key_attribute_t: key_attribute})
#         attribute_2 = random.randint(2, 4)
#         attribute.update({attribute_2_t: attribute_2})
#         if key_attribute + attribute_2 == 9:
#             attribute_3 = random.randint(2, 3)
#             attribute.update({attribute_3_t: attribute_3})
#             attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
#             attribute.update({attribute_4_t: attribute_4})
#         elif key_attribute + attribute_2 == 8:
#             attribute_3 = random.randint(2, 4)
#             attribute.update({attribute_3_t: attribute_3})
#             if attribute_3 == 2:
#                 attribute_4 = 4
#                 attribute.update({attribute_4_t: attribute_4})
#             elif attribute_3 == 3:
#                 attribute_4 = 3
#                 attribute.update({attribute_4_t: attribute_4})
#             else:
#                 attribute_4 = 2
#                 attribute.update({attribute_4_t: attribute_4})
#         elif key_attribute + attribute_2 == 7:
#             attribute_3 = random.randint(3, 4)
#             attribute.update({attribute_3_t: attribute_3})
#             attribute_4 = (14 - (key_attribute + attribute_2 + attribute_3))
#             attribute.update({attribute_4_t: attribute_4})
#         else:
#             attribute_3 = 4
#             attribute.update({attribute_3_t: attribute_3})
#             attribute_4 = 4
#             attribute.update({attribute_4_t: attribute_4})
#
#         attributes = {}
#         attributes.update({"Attributes": attribute})
#         return attributes
#
#     @staticmethod
#     def skill_values():
#         skill_getter = csv.reader(open(r'Skills.txt', 'r'))
#         data = sum([i for i in skill_getter], [])  # To flatten the list
#         skill = random.choice(data)
#         return skill
#
#     @staticmethod
#     def get_skill():
#         key_skills = ['', '', '']
#         final_skill = {}
#         skills_list = []
#         skill_total = 10
#         while skill_total >= 1:
#             skill = Soldier.skill_values()
#             if skill not in skills_list:
#                 if skill in key_skills and skill_total > 2:
#                     skills_list.append(skill)
#                     v = random.randint(1, 3)
#                     s = skill
#                     final_skill.update({s: v})
#                     skill_total = skill_total - v
#                 else:
#                     skills_list.append(skill)
#                     v = 1
#                     s = skill
#                     final_skill.update({s: v})
#                     skill_total = skill_total - v
#         final_skills = {}
#         final_skills.update({'Skills': final_skill})
#         return final_skills
#
#     @staticmethod
#     def get_money():
#         number_of_dice = 1
#         dice = []
#         for i in range(number_of_dice):
#             d6 = random.randint(1, 6)
#             dice.append(d6)
#         starting_cash = sum(dice) * 100
#         cash = {}
#         cash.update({"Starting cash": '$' + str(starting_cash) + ".00 Cash"})
#         return cash
#
#     @staticmethod
#     def get_gear():
#         n = 0
#         d6 = random.randint(1, 6)
#         #  str(d6) + ' doses Neversleep pills': 'd',
#         starting_gear = {
#             '': 'a', '': 'a',
#             '': 'b', '': 'b',
#             '': 'c', '': 'c',
#             '': 'd', '': 'd'
#             }
#         gear = {}
#         k_list = []
#         v_list = []
#
#         while 0 <= n < 2:
#             k, v = random.choice(list(starting_gear.items()))
#             if v not in v_list and k not in k_list:
#                 v_list.append(v)
#                 k_list.append(k)
#                 n = n + 1
#             else:
#                 continue
#
#             gear.update({"Starting Gear": k_list})
#         return gear
#
#     @staticmethod
#     def get_career_talent():
#         career_talents = ['', '', '']
#         career_talent = {}
#         career_talent.update({"Career talent": random.choice(career_talents)})
#         return career_talent
#
#     @staticmethod
#     def get_signature_item():
#         signature_items = [
#             '',
#             '',
#             '',
#             ''
#         ]
#         signature_item = {}
#         signature_item.update({"Signature Item": random.choice(signature_items)})
#         return signature_item
#
#     @staticmethod
#     def get_appearance():
#         appearance_list = [
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             ''
#         ]
#         appearance = {}
#         appearance.update({"Appearance": random.choice(appearance_list)})
#
#         return appearance
#
#     @staticmethod
#     def character_creator():
#         return z.get_name(), z.get_attributes(), z.get_skill(), z.get_money(), \
#                z.get_gear(), z.get_career_talent(), z.get_signature_item(), z.get_appearance()