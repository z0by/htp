from collection import BaseAnimal, Venom, Herbivore, Zoo, Aviary
import sys
import os


def select_type():
    _str = """
    ----------------------
    Choose type:
    ----------------------
    1. Venom
    2. Herbivore
    
    """
    print _str
    ans = int(raw_input("Enter type number: "))
    if ans == 1:
        return Venom
    elif ans == 2:
        return Herbivore
    else:
        print "Error. Enter wrong type number"
        
def add_aviary():
    print """
    ----------------------
    Add Aviary
    ----------------------"""
    _name = raw_input("Enter aviary name: ")
    _type = select_type()
    aviary = Aviary(_name,_type)
    zoo.add_aviary(aviary)
    print aviary,"added\n"
    print
    raw_input("Press Enter to continue...")

def list_aviaries():
    print """
    ----------------------
    List aviaries:
    ----------------------\n
    """      
    zoo.list_aviaries()
    print
    raw_input("Press Enter to continue...")

def list_free_aviaries():
    print """
    ----------------------
    List free aviaries:
    ----------------------
    """
    free_aviaries =  zoo.free_aviaries()
    if free_aviaries:
        for aviary in free_aviaries:
            print aviary
    else:
        print "No free aviaries"
    print
    raw_input("Press Enter to continue...")

def spread_aviary():
    print """
    ----------------------
    Spread aviary:
    ----------------------
    """
    av_id = int(raw_input("Enter aviary id to spread: "))
    av = zoo.get_av_by_id(av_id)
    if av:
        zoo.spread_aviary(av)
        print " {}  spreaded".format(av)
    else:
        print 
        print "Can't spread aviary\n"
    print
    raw_input("Press Enter to continue...")

def delete_aviary():
    print """
    ----------------------
    Delete aviary:
    ----------------------
    """
    av_id=int(raw_input("Enter aviary id to delete: "))
    for aviary in zoo.aviaries[:]:
        if aviary._id == av_id:
            zoo.del_aviary(aviary)
            print "{} deleted".format(aviary)
            break
    else:
        print 
        print "No aviary to delete\n"
    print
    raw_input("Press Enter to continue...")


def add_animal():
    print """
    ----------------------
    Add animal:
    ----------------------
    """    
    _type = select_type()
    _name = raw_input("Enter name: ")
    _sex =  raw_input("Enter sex(type M or F): ")
    _age = int(raw_input("Enter age: "))
    _species = raw_input("Enter species: ")
    aviary_id = int(raw_input("Enter aviary id: "))
    animal  = _type(_name, _age, _species, _sex)
    for aviary in zoo.aviaries:
        if aviary._id == aviary_id:
            aviary.add_animal(animal)
            print
            print "Animal  {} added\n".format(animal)
            break
    else:
        print
        print "Cannot add animal to aviary with id = {}\n".format(aviary_id) 
    raw_input("Press Enter to continue...")

def list_all_animals():
    print """
    ----------------------
    List animal:
    ----------------------
    """ 
    zoo.list_all_animals()
    print 
    raw_input("Press Enter to continue...")

def transfer_animal():
    print """
    ----------------------
    Transfer animal:
    ----------------------
    """ 
    anml_id=int(raw_input("Enter animal id to transfer: "))
    av_id=int(raw_input("Enter av id to transfered: "))
    for aviary in zoo.aviaries[:]:
        if aviary._id == av_id:
            new_aviary = aviary
    for old_aviary in zoo.aviaries[:]:
        for animal in old_aviary.animals[:]:
            if animal._id == anml_id:
                zoo.transfer_animal(animal, old_aviary, new_aviary )
                print "Aviry  {} deleted".format(aviary)
                break
    else:
        print 
        print "No aviary to delete\n"
    print
    raw_input("Press Enter to continue...")

def delete_animal():
    print """
    ----------------------
    Delete animal:
    ----------------------
    """ 
    ans=int(raw_input("Enter aviary id"))
    for aviary in zoo.aviaries[:]:
        for animal in aviary.animals[:]:
            if animal._id == ans:
                aviary.count_animal(animal)
                aviary.del_animal(animal)

                print "Animal  {} deleted".format(aviary)
                break
    else:
        print 
        print "No animal to delete\n"
    print
    raw_input("Press Enter to continue...")
def stats():
    all_anml =  BaseAnimal.get_animal_count()
    v_anml = Venom.get_animal_count()
    h_anml = Herbivore.get_animal_count()
    all_av =  Aviary.get_aviary_count()
    free_av = len(zoo.free_aviaries())
    FVcount = 0
    FHcount = 0
    for aviary in zoo.free_aviaries()[:]:
        if aviary.get_type() == Venom.__name__:
            FVcount += 1 
        else:
            FHcount += 1

    print """
    STATS
    ----------------------------
    All animals:             {0}
    Venom animals            {1}
    Herbivore animals        {2}
    ----------------------------
    All aviaries             {3}
    Free  aviaries           {4}
    Free Venom aviaries      {5}
    Free Herbivore aviaries  {6}
    """.format(all_anml, v_anml, h_anml, all_av, free_av, FVcount, FHcount)

    print
    raw_input("Press Enter to continue...")

def error():
    print
    print "Enter correct option\n"
    raw_input("Press Enter to continue...")

def switch(choose):
    return {
        '1': add_aviary,
        '2': list_aviaries,
        '3': list_free_aviaries,
        '4': spread_aviary,
        '5': delete_aviary,
        '6': add_animal,
        '7': list_all_animals,
        '8': transfer_animal,
        '9': delete_animal,
        '10': stats,
        '11': sys.exit,
        'q': sys.exit,
       
    }.get(choose, error)


def main_menu():
    _main ="""
    ZooPark
    ----------------------
    1.Add aviary
    2.List all aviaries
    3.List free aviaries
    4.Spread aviary
    5.Delete aviary
    6.Add animal
    7.List animals
    8.Transfer animal
    9.Delete animal
    10.Stats
    11.Exit/Quit
    ---------------------
    """
    while True:
        print _main
        ans=raw_input("What would you like to do? ")
        switch(ans)()

if __name__ == '__main__':
    zoo = Zoo()
    main_menu()
