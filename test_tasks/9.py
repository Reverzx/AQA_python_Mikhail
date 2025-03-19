import random


class Soldier:
    def __init__(self, soldier_id, team):
        self.soldier_id = soldier_id
        self.team = team

    def move_to_hero(self, hero):
        print(f"Солдат {self.soldier_id} следует за героем {hero.hero_id}.")


class Hero:
    def __init__(self, hero_id, team):
        self.hero_id = hero_id
        self.team = team
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f"Герой {self.team} повысил уровень до {self.level}.")


def main():
    global soldier_to_follow
    hero_1 = Hero(hero_id=1, team="Силы Света")
    hero_2 = Hero(hero_id=2, team="Силы Тьмы")

    soldiers_radiant = []
    soldiers_dire = []

    for i in range(1, 15):
        team = random.choice(["Силы Света", "Силы Тьмы"])
        soldier = Soldier(soldier_id=i, team=team)
        if soldier.team == "Силы Света":
            soldiers_radiant.append(soldier)
        else:
            soldiers_dire.append(soldier)

    print(f"В команде сил света {len(soldiers_radiant)} солдат!")
    print(f"В команде сил тьмы {len(soldiers_dire)} солдат!")

    if len(soldiers_radiant) > len(soldiers_dire):
        hero_1.level_up()
    elif len(soldiers_radiant) < len(soldiers_dire):
        hero_2.level_up()
    else:
        print("Количество солдат в обеих командах одинаково")

    if soldiers_radiant:
        soldier_to_follow = soldiers_radiant[0]
        soldier_to_follow.move_to_hero(hero_1)

        # Выводим идентификационные номера героя и солдата
    print(f"Идентификационный номер героя: {hero_1.hero_id}")
    print(f"Идентификационный номер солдата: {soldier_to_follow.soldier_id}")


main()
