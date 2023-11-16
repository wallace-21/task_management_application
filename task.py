#!/usr/bin/python3

""" Define a class description """


class Task:
    """ a class that handles the tasks for the application """

    def __init__(self, title, description, due_date, status="Incomplete"):
        """ interface of the task manager """

        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def display_task_details(self):
        """ things to be displayed on the interface """

        print(f"Title: {self.title}".format(self.title))
        print(f"Description: {self.description}".format({self.description))
        print(f"Due Date: {self.due_date}".format(self.due_date))
        print(f"Status: {self.status}".format(self.status))
