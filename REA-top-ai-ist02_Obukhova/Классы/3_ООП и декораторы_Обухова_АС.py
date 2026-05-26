import random

def is_alive(func):
    def wrapper(*args, **kwargs):
        original = func(*args, **kwargs)
        hero = args[0]
        if hero.health <= 0:
            print(f'{hero.name} мертв и не может действовать!')
            return None
        elif hero.health > 0:
            return original

    return wrapper

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Начало действия: {func.__name__}")
        original = func(*args, **kwargs)
        print(f"[LOG] Действие завершено")
        return original
    return wrapper

def easter_health(func):
    def wrapper(*args, **kwargs):
        original = func(*args, **kwargs)
        hero = args[0]
        hero.health *= 2
        hero.mana *= 1.5
        return original
    return wrapper

def easter_stick(func):
    def wrapper(*args, **kwargs):
        hero = args[0]
        if hero.hero_class == 'волшебник':
            hero.mana += 5
            hero.items['Священный посох'] = {'мана': 5}
        original = func(*args, **kwargs)
        return original
    return wrapper

#Декоратор ульты для героя с рандомной вероятностью ее выпадения, ulta - умножение нанесенного урона
def ult(func, chance = 30, ulta = 3):
    def wrapper(hero, *args, **kwargs):
        damage = args[0]
        if random.randint(1, 20) <= chance:
            critical_damage = int(damage * ulta)
            print(f'{hero.name} нанес критический удар! Урон увеличен в {ulta} раз')
            return func(hero, critical_damage, *args[1:], **kwargs)
        return func(hero, damage, *args[1:], **kwargs)
    return wrapper


class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class.lower()
        if hero_class == "волшебник":
            self.health = 60
            self.mana = 50
        elif hero_class == "воин":
            self.health = 100
            self.mana = 10
        else:
            raise ValueError("Класс героя должен быть 'волшебник' или 'воин'")

        self.spells_names = {}
        self.items = {}

    @is_alive
    @ult
    def attack(self,damage):
        print(f'Герой нанес урон: {damage}')

    @log_action
    def heal(self,amount):
        self.health += amount

    @is_alive
    def cast_spell(self, spell_name):
        if spell_name not in self.spells_names:
            print(f"Заклинание '{spell_name}' не изучено!")
            return
        mana_cost = self.spells_names[spell_name].get('mana_cost')
        if self.mana < mana_cost:
            print(f"Недостаточно маны для заклинания '{spell_name}'! Нужно {mana_cost}, есть {self.mana}")
        self.mana -= mana_cost
        print(spell_name)

    def add_spell(self, spell_name, mana_cost = 0, attack_damage = 0, health_increase = 0):
        self.spells_names[spell_name] = {
            'mana_cost': mana_cost,
            "attack_damage": attack_damage,
            "health_increase": health_increase
        }

    def add_item(self, item_name, param, value):
        if len(self.items) >= 6:
            print(f"Нельзя надеть больше 6 предметов!")

        self.items[item_name] = {param: value}

        if param == "здоровье":
            self.health += value
        if param == "мана":
            self.mana += value

wizard = Hero("Мерлин", "волшебник")
warrior = Hero("Ахиллес", "воин")

@easter_health
@easter_stick
def easter(hero):
    print(f'Применен пасхальный бонус для {hero.hero_class, hero.name}')

print(warrior.health, warrior.items)
print(wizard.health, wizard.items)
easter(warrior)
easter(wizard)
print(warrior.health, warrior.items)
print(wizard.health, wizard.items)

wizard.add_spell("Огненный шар",20, 35, 5)
warrior.add_item("Шлем", "здоровье", 30)

wizard.attack(25)
wizard.cast_spell("Огненный шар")
wizard.heal(10)

warrior.health = 0
warrior.attack(15)
warrior.heal(50)