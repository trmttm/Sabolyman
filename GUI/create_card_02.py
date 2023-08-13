import WidgetNames
from stacker import Stacker
from stacker import widgets as w

from .components.action_notes import ACTION_NOTES
from .components.action_properties import ACTION_PROPERTIES
from .components.action_resources import ACTION_RESOURCES


def get_view_model(parent: str = 'root'):
    stacker = create_stacker(parent)
    view_model = stacker.view_model
    return view_model


def create_stacker(parent):
    from GUI.list_of_actions.list_of_actions import LIST_OF_ACTIONS
    from GUI.list_of_recources.list_of_resources import LIST_OF_RESOURCES
    import datetime
    data = {'date': datetime.datetime(2023, 8, 13, 23, 59), 'ask_user_for_duration':lambda :print('Hi'), 'card_states': ({'card_name': 'Machida refinance', 'action_ids': ('032de6fe-adcc-445a-963e-311fc93dc847',), 'action_names': ('Identify next action',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'NISA 2023', 'action_ids': ('b2c16987-f163-473c-a7e6-b70de39590b5',), 'action_names': ('Study Rakuten SPU',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'Open Rakuten Securities', 'action_ids': ('a5c65f56-92fc-4c74-b7f4-c150757e4a3a',), 'action_names': ('Rakuten Shoken to complete process',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'Apply NISA', 'action_ids': ('78abee20-551e-4adc-b93b-1e71ded43dab',), 'action_names': ('Apply NISA',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'Rina Inveset', 'action_ids': ('d8eda381-4bfc-4a11-8225-cb626382f13d',), 'action_names': ('Place order',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'Furusato nozei 活用', 'action_ids': ('2eca41d1-9c9d-4271-af74-26f07cc40c7c', '9fed3f12-05eb-46f3-9919-f89f9cc707d3', 'c3cc9a73-10a5-442d-98c9-e7007db8c369'), 'action_names': ('制度の勉強', '管理表作成', '実行'), 'done_or_not': (False, False, False), 'scheduled_or_not_': (False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 0, 0), datetime.datetime(2023, 8, 12, 0, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0))}, {'card_name': 'Monthly - July', 'action_ids': ('f7aef8eb-cb1c-41cf-bec3-c92f588b74d7',), 'action_names': ('Invest',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'Nissei Pension', 'action_ids': ('8b2e0066-294c-41fc-9321-4497dc176b21',), 'action_names': ('ID process with Renesus HR',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(seconds=900),)}, {'card_name': '2023 Summer vacation', 'action_ids': ('e936915e-eb08-48c6-b9aa-65a5d1fabef5', '36309449-62ba-4cf9-a9b0-c637d4b1ec1b', 'bc83e582-5386-4ad1-80df-fdb53e565ae1', '0ed7d434-ee63-409e-bf9e-d7a2f2bd740f', 'd9c39a17-00f8-4bef-a732-fbf804fb7df0', '16042793-1acd-4c0b-8eee-38614349c91b', '1c6d060a-44bd-452b-9fca-095e683ec722', 'a3f9513c-82c7-406b-b4df-eaed090febd3', 'cd2b68b9-ebd7-402a-aad4-2d79842c57db'), 'action_names': ('Prevent Sabolyman Crash', 'Better resource management (share the latest resources)', 'Read Eat that frog again', "Read Microsoft programmer's book again", 'Significantly enhance Sabolyman GUI (read notes)', 'Plan and complete all the Study items', 'SBLM in iPad', 'Kanji flash card', 'Kings interhigh'), 'done_or_not': (False, False, False, False, False, False, False, False, False), 'scheduled_or_not_': (False, False, False, False, False, False, False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0))}, {'card_name': 'Malini home work - Semiconductor process', 'action_ids': ('a806a4d5-1d8a-4cce-8870-1901e1475e4c', '87e3cac6-bc71-461f-be41-96f911ed5de8', 'fa5422cd-cc21-46dd-985a-8c7d6bb8f69a'), 'action_names': ('High level flow chart by Blue book', 'Read 2 remaining books for the second time.', 'Get information from internal resources, too'), 'done_or_not': (False, False, False), 'scheduled_or_not_': (False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0))}, {'card_name': 'Master Eagle Valuation', 'action_ids': ('3e049662-9faf-488a-b7de-1b740bc88eee', 'f1941d38-41a0-4108-9c7f-6f5f05276bea'), 'action_names': ('Create fmIDE template', 'Copy cell formats'), 'done_or_not': (False, False), 'scheduled_or_not_': (False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(0))}, {'card_name': 'Sabolyman', 'action_ids': ('e9688cb2-a002-4e95-8cdd-bfcfc7e53396', 'e4d75f10-adeb-45bb-80bf-755f88954375', '45a73040-0d72-4be2-9861-6cb9d585e5a4', 'aed469c4-97a0-451f-8510-218e94496f8d', '155844a1-afc4-43a4-95b5-2a4c6d0d457e', '428dd8e6-e42d-4cc8-a5c4-8e1d9c3fcfeb', 'f636a3ff-8b75-4bb7-8563-edebe2582f9c', '3ddb51c9-37aa-47d3-80b8-92eb13b8f6e3', '0868749a-0b20-4192-876f-00c652a03727', 'e936915e-eb08-48c6-b9aa-65a5d1fabef5'), 'action_names': ('fix iMac crash bug', 'Command Macro', 'Related People', 'Feature Scheduler', 'Feature Contact', 'Goal is to create Notes', 'Learning from Monday.com', 'View Calendar', 'Itinerary auto creation', 'Prevent Sabolyman Crash'), 'done_or_not': (False, False, False, False, False, False, False, False, False, False), 'scheduled_or_not_': (False, False, False, False, False, False, False, False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600), datetime.timedelta(0), datetime.timedelta(0))}, {'card_name': 'fmIDE', 'action_ids': ('a5394f34-fd67-4b6b-8722-bcd5c83c7723', '28447c09-51cb-44a9-9db9-608dcf3e5533', 'aacc99f8-c941-4d85-af51-2941d424f01d', '11b75a52-d418-495b-b6fb-e46c0ae7ba5e', 'f53499c9-7aee-47a0-bb7e-706cacc526d1', '25f76630-5c6b-4272-a827-68856dde9618', '91331227-30e7-4425-a1ac-ba3e07eb9633', '2a3fa118-1017-4d90-90cd-7e8501252f46', '76f33e03-646b-47d9-9c45-1092ed6d334d', '86140ab8-a443-4871-94bb-d54598f20941', 'df2cb1c0-5068-4576-b50e-c643370be451', '07b1ae76-5976-4591-a195-1294b5027757'), 'action_names': ('Upon hovering over button...', 'Add option to fold modules', 'Maximize user experience', 'Support multiple languages', 'Module explanation', 'Sheet: How to use', 'Sheet: Dashboard', 'Create many patterns of transactions', 'Articles', 'Bug Accounts tree', 'Segregate Monthly vs Annua;', 'Plug vs Socket vs IDの整理'), 'done_or_not': (False, False, False, False, False, False, False, False, False, False, False, False), 'scheduled_or_not_': (False, False, False, False, False, False, False, False, False, False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(seconds=3600), datetime.timedelta(0), datetime.timedelta(0))}, {'card_name': 'Keyboard short cut is no longer working', 'action_ids': ('ea5de915-a2ca-4092-8456-8f0acab5bc8e',), 'action_names': ('Update so that keyboard shortcut can be set dynamically, like Sabolyman',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'Misc', 'action_ids': ('4766f8e7-01dc-417f-9bc1-6187d8a2dff1', '380c0f8b-121e-4d61-8d2a-844ce37951d6'), 'action_names': ('Use library!', 'Clean messanine and Kura'), 'done_or_not': (False, False), 'scheduled_or_not_': (False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 0, 0), datetime.datetime(2023, 8, 12, 0, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(seconds=7200))}, {'card_name': 'for Kids', 'action_ids': ('0e0bdd27-880e-458b-ba80-2cb2aa5f9379', 'd9be8a0c-6cde-4fdd-bd22-1443ec4c68a1', 'a39a182d-7d23-4b1f-98c0-df2e5221a527', '793ca999-ee87-40a3-b597-2a2f53247394'), 'action_names': ('Job description and record', 'Penalty system', 'Automate flashcard Kanji', 'Daily todo list'), 'done_or_not': (False, False, False, False), 'scheduled_or_not_': (False, False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 0, 0), datetime.datetime(2023, 8, 12, 0, 0), datetime.datetime(2023, 8, 12, 0, 0), datetime.datetime(2023, 8, 12, 0, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(seconds=900), datetime.timedelta(seconds=900), datetime.timedelta(0), datetime.timedelta(0))}, {'card_name': 'Subscription Management ', 'action_ids': ('cab9a577-6f55-47a9-ad8c-18c253722999',), 'action_names': ('Apple app shows all the subscriptions',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'Private Web App', 'action_ids': ('2572216d-20c3-4476-80c9-2437307d8aa7', 'e8b6a945-3605-4df9-8f2a-0acf733536d7', '41bdec19-3fa0-4a21-a203-7fdd3d8551cc', 'aa7904e7-f3c2-42b1-93f1-30f5c7a43ea6'), 'action_names': ('Sabolyman', 'Optimized Auto shopping', 'Share calendar', 'Implement convenient APIs'), 'done_or_not': (False, False, False, False), 'scheduled_or_not_': (False, False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600))}, {'card_name': 'Education', 'action_ids': ('d9a5d3f8-e857-46af-b97f-4ade16b29052',), 'action_names': ('Flash card Kanji',), 'done_or_not': (False,), 'scheduled_or_not_': (False,), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0),), 'owners': ('Taro Yamaka',), 'duration': (datetime.timedelta(0),)}, {'card_name': 'Kings inter high', 'action_ids': ('80dd0dc9-d6a6-49c0-ad31-c19c3f1d514c', '6e9ae01b-cb21-4097-8907-989519069df5', '14828539-75da-4ed1-982c-d245d5b15323'), 'action_names': ('Re-enroll', 'Decide subjects', 'Make payments'), 'done_or_not': (False, False, False), 'scheduled_or_not_': (False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0))}, {'card_name': 'Fun stuff', 'action_ids': ('67fb2ea9-0001-4afd-9a00-0e92e3143ab6', 'b8d91b2e-a629-4ef7-b78d-88040a594f16', '9d3a847d-bcb6-4edd-b7d9-b27bf4cc2a35', '673d0b09-5820-4de9-8a01-7f0a9d96b491', '8cde4c92-e5f4-4f15-bf10-b7ef458b9851'), 'action_names': ('Books', 'Movies', 'Games', 'Road bike', 'Community'), 'done_or_not': (False, False, False, False, False), 'scheduled_or_not_': (False, False, False, False, False), 'action_due_dates': (datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0), datetime.datetime(2023, 8, 12, 17, 0)), 'owners': ('Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka', 'Taro Yamaka'), 'duration': (datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0), datetime.timedelta(0))})}

    wn = WidgetNames
    stacker = Stacker(specified_parent=parent)
    stacker.vstack(
        w.PanedWindow('a', stacker).is_horizontal().stackers(
            w.PanedWindow('b', stacker).is_vertical().stackers(
                LIST_OF_ACTIONS(data, stacker),
                w.Label('place_holder_01').text('Place holder 01'),

            ),
            w.PanedWindow('c', stacker).is_vertical().stackers(
                w.PanedWindow('d', stacker).is_horizontal().stackers(
                    stacker.vstack(
                        get_card_property_entry(stacker),
                        get_actions_tree(stacker),
                        w.Spacer().adjust(-1)
                    ),
                    stacker.vstack(
                        ACTION_PROPERTIES(stacker, wn),
                        w.PanedWindow('e', stacker).is_vertical().stackers(
                            ACTION_NOTES(wn),
                            ACTION_RESOURCES(stacker),
                        ),
                        w.Spacer().adjust(-1),
                    )
                ),
                LIST_OF_RESOURCES(stacker),
            ),
        ),
    )
    return stacker


def get_actions_tree(stacker: Stacker):
    wn = WidgetNames
    return stacker.vstack(
        stacker.hstack(
            w.TreeView(wn.tree_card_actions).padding(10, 10),
        ),
        stacker.hstack(
            w.Spacer(),
            w.Button(wn.button_delete_selected_actions).text('X').width(1),
            w.Button(wn.button_move_down_selected_actions).text('↓').width(1),
            w.Button(wn.button_move_up_selected_actions).text('↑').width(1),
            w.Button(wn.button_add_new_action).text('+').width(1),
            w.Button(wn.button_display_resources).text('Resources'),
            w.Spacer(),
        ),
        w.Spacer().adjust(-2),
    )


def get_card_property_entry(stacker: Stacker):
    wn = WidgetNames
    return stacker.vstack(
        stacker.hstack(
            w.Label('lbl_name').text('Card').width(10).padding(10, 0),
            w.Entry(wn.entry_card_name).default_value('New Card Name', ).padding(5, 0),
            w.Spacer().adjust(-1),
        ),
        stacker.hstack(
            w.Label('lbl_dead_line').text('Deadline').width(10).padding(10, 0),
            w.Label(wn.label_card_dead_line).text('2022/5/30 15:00', ).padding(5, 0),
            w.Label('lbl_date_created1').text('Created:').width(6).padding(0, 0),
            w.Label(WidgetNames.label_date_created).text('2022/5/30 15:00').padding(10, 0),
            w.Spacer(),
        ),
        stacker.hstack(
            w.Label(wn.label_card_importance).text('Priority').width(12).padding(10, 0),
            w.Button(wn.button_importance_down).text('-').width(1).padding(10, 0),
            w.Entry(wn.entry_card_importance).default_value(5).width(3),
            w.Button(wn.button_importance_up).text('+').width(1).padding(10, 0),
        ),
        stacker.hstack(
            w.Label('lbl_action_name').text('Action').width(10).padding(10, 0),
            w.Entry(wn.entry_action_name).default_value('Action Name', ).padding(10, 0),
            w.Spacer().adjust(-1),
        ),
        w.Spacer(),
    )
