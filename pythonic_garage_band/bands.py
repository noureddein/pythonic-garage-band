from abc import ABC, abstractclassmethod


class Band:
    instances = []
    solos = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)

    def __str__(self):
        return 'Band'

    def __repr__(self):
        return 'Band'

    @classmethod
    def to_list(cls):
        try:
            cls.instances.append(cls.name)
        except AttributeError:
            return cls.instances
        else:
            return cls.instances

    def play_solos(self):
        return self.solos


class Musician(Band):
    instruments = []

    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo():
        pass


class Guitarist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return 'guitar'

    @classmethod
    def play_solo(cls):
        solo = "face melting guitar solo"
        cls.solos.append(solo)
        return solo


class Bassist(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return 'bass'

    @classmethod
    def play_solo(cls):
        solo = "bom bom buh bom"
        cls.solos.append(solo)
        return solo


class Drummer(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'

    @classmethod
    def play_solo(cls):
        solo = "rattle boom crash"
        cls.solos.append(solo)
        return solo
