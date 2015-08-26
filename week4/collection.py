"""
Module ZooPark
"""

import logging

LOG = logging.getLogger(__name__)

AVIARY_CAPACITY = 3

MAX_AVIARIES = 10

class AviaryManagementError(Exception):
    pass

class BaseAnimal(object):
    """
    Basic interface for animal creation
    get_type() => returns either 'Venom' or 'Herbivore'
    """
    COUNT = 0
    def __init__(self, name, age, species, sex):
        self.name = name
        self.sex = sex
        self.age = age
        self.species = species
        BaseAnimal.COUNT += 1
        self._id = BaseAnimal.COUNT


    def get_type(self):
        """
        Method return class type
        """
        return self.__class__.__name__

    @classmethod
    def get_animal_count(cls):
        """
        Classmethod that return BaseAnimal count
        """
        return cls.COUNT

    def __repr__(self):
        """
        Special method for class representing
        """
        return "{}('{}',{},'{}','{}', {})".format(self.get_type(),
            self.name, self.age, self.species, self.sex, self._id)

class Venom(BaseAnimal):
    """
    Class for Venoms
    """
    COUNT = 0

    def __init__(self, name, age, sex, species):
        self.__class__.COUNT += 1
        super(Venom, self).__init__(name=name, age=age,
                                    sex=sex, species=species)

class Herbivore(BaseAnimal):
    """
    Class for herbivore animals
    """
    COUNT = 0

    def __init__(self, name, age, sex, species):
        self.__class__.COUNT += 1
        super(Herbivore, self).__init__(name=name, age=age, sex=sex,
                                        species=species)

class Aviary(object):
    """
    Class for Aviary to contain Animals
    """
    COUNT = 0
    def __init__(self, name, _type):
        self.name = name
        self._type = _type
        self.animals = []
        self.__class__.COUNT += 1
        self._id = self.__class__.COUNT

    def add_animal(self, anml):
        if len(self.animals) < AVIARY_CAPACITY:

            if type(anml) not in [Venom, Herbivore]:

                raise AviaryManagementError("Cannot add animal. Bad param.")
            else:
                if anml.get_type() == self.get_type():
                    self.animals.append(anml)
                    return True
                else:
                    raise AviaryManagementError("Cannot add {0} to {1} aviory."
                                                .format(anml.get_type(), self.get_type()))
        else:
            raise AviaryManagementError("Cannot add animal. Aviary is full")

    @classmethod
    def get_aviary_count(cls):
        """
        Classmethod for aviary count
        """
        return cls.COUNT

    def del_animal(self, anml):
        """
        Method for delete animal
        """
        if anml in self.animals[:]:
            self.animals.remove(anml)

    def count_animal(self, anml):
        """
        Method for count animal
        """
        if type(anml) == Venom:
            Venom.COUNT = Venom.COUNT - 1
        else:
            Herbivore.COUNT = Herbivore.COUNT - 1
        BaseAnimal.COUNT = BaseAnimal.COUNT  - 1

    def get_type(self):
        """
        Method return class type
        """
        return self._type.__name__

    def get_anml_by_id(self, _id):
        """
        Get animal by animal id
        """
        for animal in  self.animals:
            if animal._id == _id:
                return animal
        return None

    def __len__(self):
        return len(self.animals)

    def __repr__(self):
        return "Aviary('{0}', type=>{1}, animals=>{2}, av_id=>{3})".format(self.name, 
                                                            self._type.__name__, 
                                                            self.animals, self._id) 

class Zoo(object):
    """
    Class for representing Zoo
    """

    def __init__(self):
        self.aviaries = []

    def list_aviaries(self):
        """
        List all aviaries in the Zoo
        """
        if len(self.aviaries) > 0:
    	    for aviary in self.aviaries:
                print aviary
        else:
            print "No aviaries"

    def list_all_animals(self):
        for aviary in self.aviaries:
            for animal in aviary.animals:
                print "{} in aviary {}".format(animal, aviary._id)

    def transfer_animal(self, anml, new_aviary, old_aviary):
        """
        Transfer animal from one aviary to another
        """
        try:
            new_aviary.add_animal(anml)
            old_aviary.del_animal(anml)
        except Exception, e:
            print e

    def add_aviary(self, av):
        """
        Add aviary to the Zoo
        """

        if type(av) != Aviary:
            raise AviaryManagementError("Could not add aviary. Bad param")
        if av.get_type() not in [Venom.__name__, Herbivore.__name__]:
            raise AviaryManagementError("Couldn't add aviary. Bad {} type".format(av.get_type()))
        if len(self.aviaries) <= MAX_AVIARIES:
            self.aviaries.append(av)
        else:
            raise AviaryManagementError("Could not add aviary. Maximim {} aviaries".format(MAX_AVIARIES))

    def get_av_by_id(self, _id):
        """
        Get aviary by id
        """
        for aviary in self.aviaries:
            if aviary._id == _id:
                return aviary
        return None

    def del_aviary(self, obj):
        """
        Delete aviary object
        """
        if obj in self.aviaries:
            for animal in obj.animals[:]:
                obj.del_animal(animal)
            self.aviaries.remove(obj)
            Aviary.COUNT = Aviary.COUNT - 1

    def spread_aviary(self, av):
        """
        Spread aviary. If there are another free aviary, transfer animal to it. Else delete animal
        """
        for animal in av.animals[:]:
            for aviary in self.free_aviaries()[:]:
                if aviary != av:
                    if len(aviary.animals) < AVIARY_CAPACITY:
                        if av.get_type() == animal.get_type():
                            self.transfer_animal(animal, aviary, av)
                            break
            else:
                aviary.count_animal(animal)
                aviary.del_animal(animal)

    def free_aviaries(self):
        """
        Method return free aviaries
        """
        free_aviaries = []
        for aviary in self.aviaries[:]:
            if len(aviary) < AVIARY_CAPACITY:
                free_aviaries.append(aviary)
        return free_aviaries       
