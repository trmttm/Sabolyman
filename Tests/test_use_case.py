import unittest


class MyTestCase(unittest.TestCase):
    def test_add_card(self):
        from Commands import AddCard
        from Entities import Entities

        entities = Entities()
        command = AddCard(entities)
        command.execute()

    def test_add_file(self):
        from Commands import AddFileToCard
        from Entities import Card, File
        card = Card()
        file = File()
        command = AddFileToCard(card, file)
        command.execute()

    def test_add_description(self):
        pass


if __name__ == '__main__':
    unittest.main()
