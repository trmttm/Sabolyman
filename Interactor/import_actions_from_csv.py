import csv
import datetime

import Utilities
from Commands import AddAction


def execute(e, file):
    with open(file, 'r') as file:
        csvreader = csv.reader(file)
        for n, row in enumerate(csvreader):
            if n > 0:
                print(row)
                command = AddAction(e)
                command.execute()
                new_action = e.active_action

                name, dead_line, start_from, owner, client, days, hour_minutes, scheduled, done, description = row
                new_action.set_name(name)
                new_action.set_dead_line(Utilities.str_to_date_time_no_time(dead_line))
                new_action.set_start_from(Utilities.str_to_date_time_no_time(start_from))
                new_action.set_owner(e.create_new_person(owner))
                new_action.set_client(e.create_new_person(client))
                try:
                    days = int(days)
                    hours_str, minutes_str = hour_minutes.split(':')
                    hours = int(hours_str)
                    minutes = int(minutes_str)
                    seconds = (days * 24 * 60 + hours * 60 + minutes) * 60
                    new_action.set_time_expected(datetime.timedelta(seconds=seconds))
                except:
                    pass
                if scheduled == 'TRUE':
                    new_action.mark_scheduled()
                if done == 'TRUE':
                    new_action.mark_done()
                new_action.add_description(description)
