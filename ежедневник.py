from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QCalendarWidget, QTimeEdit, QListWidget
from PyQt5.QtCore import QDate, QTime

class DailyPlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.calendar = QCalendarWidget(self)
        self.time_edit = QTimeEdit(self)
        self.event_input = QLineEdit(self)
        self.add_button = QPushButton('Добавить', self)
        self.event_list = QListWidget(self)

        self.calendar.setSelectedDate(QDate.currentDate())
        self.time_edit.setTime(QTime.currentTime())

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel('Название события:'))
        input_layout.addWidget(self.event_input)

        datetime_layout = QHBoxLayout()
        datetime_layout.addWidget(QLabel('Дата:'))
        datetime_layout.addWidget(self.calendar)
        datetime_layout.addWidget(QLabel('Время:'))
        datetime_layout.addWidget(self.time_edit)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.add_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(datetime_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.event_list)

        self.setLayout(main_layout)

        self.add_button.clicked.connect(self.add_event)

    def add_event(self):
        event_name = self.event_input.text()
        event_date = self.calendar.selectedDate().toString('dd.MM.yyyy')
        event_time = self.time_edit.time().toString('hh:mm')

        event_str = f'{event_date} {event_time} - {event_name}'
        self.event_list.addItem(event_str)

        self.event_list.sortItems()

        self.event_input.setText('')

if __name__ == '__main__':
    app = QApplication([])
    planner = DailyPlanner()
    planner.show()
    app.exec_()
    
