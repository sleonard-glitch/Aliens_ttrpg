import random
import csv
from Alien_Stat_Card import\
    Soldier as Gun_Bunny, Marshal as Law_Dog, Agent as Company_Stooge, Kid as Newt, Medic as Doc, \
    Officer as Big_Damn_Hero, Pilot as Leaf_On_The_Wind, Roughneck as Shares, Scientist as Dr_Jekyll

careers = ['Colonial Marine', 'Colonial Marshel', 'Company Agent', 'Kid', 'Medic', 'Officer', 'Pilot', 'Roughneck']
names = []
pc_count = 4


def get_marshal():
    colonial_marshal = Law_Dog.character_creator()
    attributes = {}
    print("Colonial Marshal...")
    # print(colonial_marshal)
    for var in range(len(colonial_marshal)):
        print(var, colonial_marshal[var])
        print(isinstance(var, list))
        print(isinstance(var, tuple))
        print(isinstance(var, dict))
        print(isinstance(var, float))
        print(isinstance(var, str))
        print(isinstance(var, int))

    # for i in colonial_marshal:
    #     print(i)
        # if isinstance((i, dict)):
        #     print('True')
    for i in range(8):
        for cm in colonial_marshal[i]:
    #         for c in cm.values():
    #             if isinstance(c, dict):
    #                 print("dict")
            # else:
            for k, v in cm.items():
                # print('dict: ', k)
                print(k, v)
        # print(cm)
        # for k, v in cm:
        #     print("k: ", k)
        #     print("v: ", v)
            # attributes.update({k, v})
    print(attributes)


def get_marine():
    colonial_marine = Gun_Bunny.character_creator()
    print("Colonial Marine...")
    for c in range(8):
        print(colonial_marine[c])
    print()


def get_agent():
    company_agent = Company_Stooge.character_creator()
    print("Company Agent...")
    for c in range(8):
        print(company_agent[c])
    print()


def get_kid():
    kid = Newt.character_creator()
    print("Kid...")
    for c in range(8):
        print(kid[c])
    print()


def get_medic():
    medic = Doc.character_creator()
    print("Medic...")
    for c in range(8):
        print(medic[c])
    print()


def get_officer():
    officer = Big_Damn_Hero.character_creator()
    print("Officer...")
    for c in range(8):
        print(officer[c])
    print()


def get_pilot():
    pilot = Leaf_On_The_Wind.character_creator()
    print("Pilot...")
    for c in range(8):
        print(pilot[c])
    print()


def get_roughneck():
    roughneck = Shares.character_creator()
    print("Roughneck...")
    for c in range(8):
        print(roughneck[c])
    print()


def get_scientist():
    scientist = Dr_Jekyll.character_creator()
    print("Scientist...")
    for c in range(8):
        print(scientist[c])
    print()


get_marshal()
# get_agent()
# get_kid()
# get_marine()
# get_medic()
# get_officer()
# get_pilot()
# get_roughneck()
# get_scientist()



# get_soldiers = input("How Many ")
# colonial_marine = gun_bunny.character_creator()
# for i in range(int(get_soldiers)):
#     for c in range(8):
#         print(colonial_marine[c])
#     print()


# def go():
#     n = 0
#     while n < pc_count < 5:
#         test = gun_bunny.soldier_creator()
#         name = test[0]
#         if name not in names:
#             names.append(name)
#             n = n + 1
#         else:
#             continue
#     return names
#
# print(go())