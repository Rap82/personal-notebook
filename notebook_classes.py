from collections import UserDict, UserList
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Title(Field):
    def __init__(self, value):
        super().__init__(value)


class Content(Field):
    def __init__(self, value):
        super().__init__(value)


class TitleDate(Field):
    def __init__(self, value):
        super().__init__(value)

    def set_date(self, curr_date):
        self._value = datetime.strftime(curr_date, "%d/%m/%Y, %H:%M:%S")
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, curr_date):
        self._value = curr_date
        self.set_date(self._value)


class Record:
    def __init__(self, title_date, title, content, id_counter = 1):
        # self.data = [TitleDate(title_date), Title(title), Content(content)]
        self.id_counter = id_counter
        self.date = TitleDate(title_date)
        self.title = Title(title)
        self.content = Content(content)

    def __str__(self) -> str:
        return f"| {self.date} | {self.title} | {self.content.value[0:10]}"

    def add_content(self):
        pass

    def edit_content(self):
        pass

    def change_title(self):
        pass


class NoteBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.id_counter] = record
    
    def delete_record(self):
        pass

    def find_record(self):
        pass

    def show_all(self):
        pass

    def show_n_records(self):
        pass

    def save_notebook(self):
        pass

    def load_natebook(self):
        pass


def main():
    id_counter = 1
    current_date = datetime.now()
    # print(id_counter, current_date)
    notebook = NoteBook()

    record_title = "Test1"
    record_content = "test teste tet ee."
    record_init = Record(current_date, record_title, record_content, id_counter)
    notebook.add_record(record_init)

    record_title2 = "Test2"
    record_content2 = "wwwww www wqqqw eeee rrtyuy uuii."
    record_init2 = Record(current_date, record_title2, record_content2, id_counter=2)
    notebook.add_record(record_init2)

    record_title3 = "Test3"
    record_content3 = "AA ddddddd sss zxcvvbynm nhynjkukuik yujmumuuimuuimuimui."
    record_init3 = Record(current_date, record_title3, record_content3, id_counter=3)
    notebook.add_record(record_init3)

    # print(notebook.data)
    # Виведення всіх записів у книзі
    for name, record in notebook.data.items():
        print(name, record)

if __name__ == '__main__':
    main()
