import unittest


class MyTestCase(unittest.TestCase):
    def test_add_card(self):
        from view_tkinter import View
        app = View()

        import pickle
        with open('gui.fmide_gui', 'rb') as f:
            view_model = pickle.load(f)

        from Commands import AddCard, RemoveCard
        from Entities import Entities
        from Presenters import Presenters
        entities = Entities()
        presenters = Presenters(app)
        name = 'my_balls'
        command = AddCard(entities)

        app.add_widgets(view_model)
        import datetime
        select_nth = 0
        presenters.update_cards(('Card1',), (datetime.datetime.today(),), select_nth)

        from Entities import EntitiesABC

        def add_new_card(e: EntitiesABC):
            command.execute()

            card_names = e.card_names
            due_dates = e.due_dates
            response_model = card_names, due_dates
            presenters.update_cards(*response_model)

        def delete_selected_cards(e: EntitiesABC):
            indexes = app.get_selected_tree_item_indexes('tree_my_balls')
            next_selection_index = max(min(indexes) - 1, 0)
            RemoveCard(e, indexes).execute()

            card_names = e.card_names
            due_dates = e.due_dates
            response_model = card_names, due_dates, next_selection_index
            presenters.update_cards(*response_model)

        app.bind_command_to_widget(f'btn_{name}_add', lambda: add_new_card(entities))
        app.bind_command_to_widget(f'btn_{name}_delete', lambda: delete_selected_cards(entities))

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
