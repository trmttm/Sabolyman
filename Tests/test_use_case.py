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

    def test_get_search_result(self):
        from Entities import Card, Action, Person
        card = Card()
        card.set_name('Project A')

        search_result = card.get_search_all_result('Project A')
        self.assertEqual(search_result, 100)

        person1 = Person('Project A')
        action1 = Action()
        action1.set_owner(person1)
        card.add_action(action1)
        search_result = card.get_search_all_result('Project A')
        self.assertEqual(search_result, 105)

        person2 = Person('Project A')
        action2 = Action()
        action2.set_owner(person2)
        card.add_action(action2)
        search_result = card.get_search_all_result('Project A')
        self.assertEqual(search_result, 110)

        description1 = 'I have to do this and that Project A'
        action1.add_description(description1)
        search_result = card.get_search_all_result('Project A')
        self.assertEqual(search_result, 115)

        description2 = 'I have to do this and that Project A'
        action2.add_description(description2)
        search_result = card.get_search_all_result('Project A')
        self.assertEqual(search_result, 120)


if __name__ == '__main__':
    unittest.main()
