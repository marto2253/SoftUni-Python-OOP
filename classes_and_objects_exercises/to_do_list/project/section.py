from .task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.name} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        else:
            for t in self.tasks:
                if t.name == task_name:
                    t.completed = True
                    return f"Completed task {task_name}"

    def clean_section(self):
        counter = 0
        for t in self.tasks:
            if t.completed:
                del t
        return f"Cleared {counter} tasks."

    def view_section(self):
        result = ''

        result += f'{self.name}:\n'
        joined = "\n".join([i.details() for i in self.tasks])
        result += f'{joined}'

        return result.strip()


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
