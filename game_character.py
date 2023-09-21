import random


class MixinPlay:
    def play_game(self):
        return f"Я играю "


class MixinFall:
    def fall(self):
        return f"Я упал"


class MixinStay:
    def stay(self):
        return f"Я умею стоять, я - {self.name}"


class MixinTalkable:
    def talkable(self):
        return f"Я умею говорить, я - {self.name}"


class MixinWalk:

    def walk(self):
        print(f'Я могу сам бегать')


class Character:

    def __init__(self, name: str, hp: int, xp: int, attack_power: int):
        self.name: str = name
        self.hp: int = hp
        self.xp: int = xp
        self.attack_power: int = attack_power

    def show_person(self):
        return (f"Я {self.name},\n "
                f"у меня {self.hp} здоровья,\n"
                f" сейчас{self.xp} опята \n"
                f", а ударить я могу с силой {self.attack_power}\n")


class FunkoPop(MixinPlay, MixinStay, MixinFall):
    pass


class Playable(MixinPlay, MixinStay, MixinFall, MixinTalkable, MixinWalk):
    pass


class Pudge(Character):
    def __int__(self, name: str = 'Pudge', hp: int = 170, xp: int = 0,
                attack_power: int = 250, close: str = "фартук"):
        Character.__init__(self, name, hp, xp, attack_power)
        self.close = close

    def show_close(self):
        return f"У меня есть {self.close}"


class PudgePlayable(Pudge, Playable):
    def stink(self):
        return "Я ВОНЯЮ ВСЕГДА"

    def hook(self):
        return "СЕЙЧАС БУДЕТ МЯСО"


class PudgeFunkoPop(Pudge, FunkoPop):
    def hanger(self):
        return "А у меня есть крюк, и больше ниукого нет хааххахахахх"


class Hoodwink(Character):
    def __int__(self, name: str = 'HOODWINK', hp: int = 120, xp: int = 10,
                attack_power: int = 53, weapon: str = "луч"):
        Character.__init__(self, name, hp, xp, attack_power)
        self.weapon = weapon

    def weapon_attack(self):
        return f"Я могу есть {self.weapon}"


class HoodwinkPlayable(Hoodwink, Playable):
    def run(self):
        return "Я очень быстро бегаю, быстрее всех"

    def voice(self):
        return "У меня очень ну очень милый голос"


class HoodwinkFunkoPop(Hoodwink, FunkoPop):
    def body(self):
        return "круглая белка стала квадратной игрушкой"


class ArtemMarandich(Character):
    def __int__(self, name: str = 'Artem Marandich', hp: int = 10000, xp: int = -100,
                attack_power: int = 1, intelligence: str = "сто одна поговорка"):
        Character.__init__(self, name, hp, xp, attack_power)
        self.intelligence = intelligence

    def can_say(self):
        return f"Я могу сказть {self.intelligence}"


class ArtemMarandichPlayable(ArtemMarandich, Playable):
    def word(self):
        return f"Я могу {(self.intelligence) * 10}"


class ArtemMarandichFunkoPop(ArtemMarandich, FunkoPop):
    def game_of_hide_and_seek(self):
        return "коллекционка"
