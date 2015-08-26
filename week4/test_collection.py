import unittest
import collection

class TestBaseAnimal(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        reload(collection)

    def test_init(self):
        animal = collection.BaseAnimal('Alex', 20, 'Lion', 'M')

        self.assertEqual(animal.name, 'Alex')
        self.assertEqual(animal.sex, 'M')
        self.assertEqual(animal.age, 20)
        self.assertEqual(animal.species, 'Lion')

    def test_get_type(self):
        animal = collection.BaseAnimal('Alex', 20, 'Lion', 'M')
        result = animal.get_type()

        self.assertEqual(result, 'BaseAnimal')


class TestVenom(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        reload(collection)

    def test_init(self):
        animal = collection.Venom('Alex', 20, 'M','Lion')
        self.assertEqual(animal.name, 'Alex')
        self.assertEqual(animal.sex, 'M')
        self.assertEqual(animal.age, 20)
        self.assertEqual(animal.species, 'Lion')

    def test_get_type(self):
        animal = collection.Venom('Alex', 20, 'M', 'Lion')
        result = animal.get_type()

        self.assertEqual(result, 'Venom')


class TestAviary(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        reload(collection)

    def test_init(self):
        aviary = collection.Aviary('Lions', 'Venom')

        self.assertEqual(aviary.name, 'Lions')
        self.assertEqual(aviary._type, 'Venom')

    def test_get_aviary_count(self):
        aviary1 = collection.Aviary('Lions', 'Venom')
        aviary2 = collection.Aviary('Tigers', 'Venom')
        aviary3 = collection.Aviary('Zebras', 'Herbivore')
        aviary4 = collection.Aviary('Elephants', 'Herbivore')

        self.assertEqual(collection.Aviary.get_aviary_count(), 4)

if __name__ == "__main__":
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestBaseAnimal))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestVenom))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestAviary))
    test_suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
