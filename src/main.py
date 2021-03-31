from gui import *
from json_reader import *


class MainWindow(QtWidgets.QMainWindow, Ui_BBN):

    def __init__(self, *args, **kwargs):

        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Utility vars
        self.lang_selected_1 = 'None'
        self.lang_selected_2 = 'None'
        self.current_key = 'None'
        self.current_answers = ['None']

        # READER
        self.reader = Reader()
        self.num_units = 0

        # Initial setup
        self.initial_setup()

        # Choose lang_1
        self.chckBox_spanish_left.clicked.connect(self.refresh_available_langs_spanish_left)
        self.chckBox_russian_left.clicked.connect(self.refresh_available_langs_russian_left)
        self.chckBox_german_left.clicked.connect(self.refresh_available_langs_german_left)

        # Choose lang_2
        self.chckBox_spanish_right.clicked.connect(self.refresh_available_langs_spanish_right)
        self.chckBox_russian_right.clicked.connect(self.refresh_available_langs_russian_right)
        self.chckBox_german_right.clicked.connect(self.refresh_available_langs_german_right)

        # Display group_box_exercises
        self.chkBox_unit_1.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_2.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_3.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_4.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_5.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_6.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_7.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_8.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_9.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_10.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_11.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_12.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_13.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_14.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_15.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_16.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_17.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_18.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_19.clicked.connect(self.display_group_box_exercises)
        self.chkBox_unit_20.clicked.connect(self.display_group_box_exercises)

        # Display answer/question boxes and answer button_answer
        self.radBut_words.toggled.connect(self.display_quest_answe_button)
        self.radBut_sentences.toggled.connect(self.display_quest_answe_button)

        # Verify answer
        self.button_answer.clicked.connect(self.verify_answer)
        self.Answer.returnPressed.connect(self.verify_answer)

###############################################################################
#    INITIAL SETUP
###############################################################################

    def initial_setup(self):

        self.group_box_units.hide()
        self.group_box_exercises.hide()
        self.group_box_lang_selected_1.hide()
        self.group_box_lang_selected_2.hide()
        self.button_answer.hide()

        for i in range(1,21):
            var = 'self.chkBox_unit_' + str(i) + '.hide()'
            eval(var)

###############################################################################
#    LEFT LANG SELECTOR
###############################################################################

    def refresh_available_langs_spanish_left(self):

        if self.chckBox_spanish_left.isChecked():
            self.chckBox_russian_left.hide()
            self.chckBox_german_left.hide()
            self.chckBox_spanish_right.hide()
        else:
            if self.chckBox_german_right.isChecked():
                self.chckBox_russian_left.show()
            elif self.chckBox_russian_right.isChecked():
                self.chckBox_german_left.show()
            else:
                self.chckBox_russian_left.show()
                self.chckBox_german_left.show()
                self.chckBox_spanish_right.show()

        if self.chckBox_spanish_left.isChecked() and self.chckBox_russian_right.isChecked():
            self.valid_combination_langs_selected('spanish', 'russian')
        elif self.chckBox_spanish_left.isChecked() and self.chckBox_german_right.isChecked():
            self.valid_combination_langs_selected('spanish', 'german')
        else:
            self.no_combination_langs_selected()

        if self.chckBox_spanish_left.isChecked():
            self.lang_selected_1 = 'Spanish'
        else:
            self.lang_selected_1 = 'None'

    def refresh_available_langs_russian_left(self):

        if self.chckBox_russian_left.isChecked():
            self.chckBox_spanish_left.hide()
            self.chckBox_german_left.hide()
            self.chckBox_russian_right.hide()
        else:
            if self.chckBox_german_right.isChecked():
                self.chckBox_spanish_left.show()
            elif self.chckBox_spanish_right.isChecked():
                self.chckBox_german_left.show()
            else:
                self.chckBox_spanish_left.show()
                self.chckBox_german_left.show()
                self.chckBox_russian_right.show()

        if self.chckBox_russian_left.isChecked() and self.chckBox_spanish_right.isChecked():
            self.valid_combination_langs_selected('russian', 'spanish')
        elif self.chckBox_russian_left.isChecked() and self.chckBox_german_right.isChecked():
            self.valid_combination_langs_selected('russian', 'german')
        else:
            self.no_combination_langs_selected()

        if self.chckBox_russian_left.isChecked():
            self.lang_selected_1 = 'Russian'
        else:
            self.lang_selected_1 = 'None'

    def refresh_available_langs_german_left(self):

        if self.chckBox_german_left.isChecked():
            self.chckBox_spanish_left.hide()
            self.chckBox_russian_left.hide()
            self.chckBox_german_right.hide()
        else:
            if self.chckBox_russian_right.isChecked():
                self.chckBox_spanish_left.show()
            elif self.chckBox_spanish_right.isChecked():
                self.chckBox_russian_left.show()
            else:
                self.chckBox_spanish_left.show()
                self.chckBox_russian_left.show()
                self.chckBox_german_right.show()

        if self.chckBox_german_left.isChecked() and self.chckBox_spanish_right.isChecked():
            self.valid_combination_langs_selected('german', 'spanish')
        elif self.chckBox_german_left.isChecked() and self.chckBox_russian_right.isChecked():
            self.valid_combination_langs_selected('german', 'russian')
        else:
            self.no_combination_langs_selected()

        if self.chckBox_german_left.isChecked():
            self.lang_selected_1 = 'German'
        else:
            self.lang_selected_1 = 'None'

###############################################################################
#    RIGHT LANG SELECTOR
###############################################################################

    def refresh_available_langs_spanish_right(self):

        if self.chckBox_spanish_right.isChecked():
            self.chckBox_russian_right.hide()
            self.chckBox_german_right.hide()
            self.chckBox_spanish_left.hide()
        else:
            if self.chckBox_russian_left.isChecked():
                self.chckBox_german_right.show()
            elif self.chckBox_german_left.isChecked():
                self.chckBox_russian_right.show()
            else:
                self.chckBox_german_right.show()
                self.chckBox_russian_right.show()
                self.chckBox_spanish_left.show()

        if self.chckBox_spanish_right.isChecked() and self.chckBox_russian_left.isChecked():
            self.valid_combination_langs_selected('russian', 'spanish')
        elif self.chckBox_spanish_right.isChecked() and self.chckBox_german_left.isChecked():
            self.valid_combination_langs_selected('german', 'spanish')
        else:
            self.no_combination_langs_selected()

        if self.chckBox_spanish_right.isChecked():
            self.lang_selected_2 = 'Spanish'
        else:
            self.lang_selected_2 = 'None'

    def refresh_available_langs_russian_right(self):

        if self.chckBox_russian_right.isChecked():
            self.chckBox_spanish_right.hide()
            self.chckBox_german_right.hide()
            self.chckBox_russian_left.hide()
        else:
            if self.chckBox_spanish_left.isChecked():
                self.chckBox_german_right.show()
            elif self.chckBox_german_left.isChecked():
                self.chckBox_spanish_right.show()
            else:
                self.chckBox_german_right.show()
                self.chckBox_spanish_right.show()
                self.chckBox_russian_left.show()

        if self.chckBox_russian_right.isChecked() and self.chckBox_spanish_left.isChecked():
            self.valid_combination_langs_selected('spanish', 'russian')
        elif self.chckBox_russian_right.isChecked() and self.chckBox_german_left.isChecked():
            self.valid_combination_langs_selected('german', 'russian')
        else:
            self.no_combination_langs_selected()

        if self.chckBox_russian_right.isChecked():
            self.lang_selected_2 = 'Russian'
        else:
            self.lang_selected_2 = 'None'

    def refresh_available_langs_german_right(self):

        if self.chckBox_german_right.isChecked():
            self.chckBox_spanish_right.hide()
            self.chckBox_russian_right.hide()
            self.chckBox_german_left.hide()
        else:
            if self.chckBox_russian_left.isChecked():
                self.chckBox_spanish_right.show()
            elif self.chckBox_spanish_left.isChecked():
                self.chckBox_russian_right.show()
            else:
                self.chckBox_spanish_right.show()
                self.chckBox_russian_right.show()
                self.chckBox_german_left.show()

        if self.chckBox_german_right.isChecked() and self.chckBox_spanish_left.isChecked():
            self.valid_combination_langs_selected('spanish', 'german')
        elif self.chckBox_german_right.isChecked() and self.chckBox_russian_left.isChecked():
            self.valid_combination_langs_selected('russian', 'german')
        else:
            self.no_combination_langs_selected()

        if self.chckBox_german_right.isChecked():
            self.lang_selected_2 = 'German'
        else:
            self.lang_selected_2 = 'None'

###############################################################################
#    LANG SELECTOR AUXILIAR FUNCTIONS
###############################################################################

    def valid_combination_langs_selected(self, lang_1, lang_2):

        self.group_box_units.show()
        self.reader.read_json_words(lang_1, lang_2)
        self.reader.read_json_sentences(lang_1, lang_2)
        self.display_units_available()

    def no_combination_langs_selected(self):

        self.group_box_units.hide()
        self.group_box_exercises.hide()
        self.uncheck_all_units()
        self.group_box_lang_selected_1.hide()
        self.group_box_lang_selected_2.hide()
        self.button_answer.hide()

###############################################################################
#    DISPLAY NUMBER OF UNITS AVAILABLE
###############################################################################

    def display_units_available(self):

        if self.reader.list_words[0] == []:
            self.num_units = 0
        else:
            self.num_units = len(self.reader.list_words)

        for i in range(1,self.num_units+1):
            var = 'self.chkBox_unit_' + str(i) + '.show()'
            eval(var)

        for i in range(self.num_units+1,21):
            var = 'self.chkBox_unit_' + str(i) + '.hide()'
            eval(var)

    def uncheck_all_units(self):

        for i in range(1,21):
            var = 'self.chkBox_unit_' + str(i) + '.setChecked(False)'
            eval(var)

###############################################################################
#    DISPLAY EXERCISES AVAILABLE
###############################################################################

    def display_group_box_exercises(self):

        if self.chkBox_unit_1.isChecked() or \
           self.chkBox_unit_2.isChecked() or \
           self.chkBox_unit_3.isChecked() or \
           self.chkBox_unit_4.isChecked() or \
           self.chkBox_unit_5.isChecked() or \
           self.chkBox_unit_6.isChecked() or \
           self.chkBox_unit_7.isChecked() or \
           self.chkBox_unit_8.isChecked() or \
           self.chkBox_unit_9.isChecked() or \
           self.chkBox_unit_10.isChecked() or \
           self.chkBox_unit_11.isChecked() or \
           self.chkBox_unit_12.isChecked() or \
           self.chkBox_unit_13.isChecked() or \
           self.chkBox_unit_14.isChecked() or \
           self.chkBox_unit_15.isChecked() or \
           self.chkBox_unit_16.isChecked() or \
           self.chkBox_unit_17.isChecked() or \
           self.chkBox_unit_18.isChecked() or \
           self.chkBox_unit_19.isChecked() or \
           self.chkBox_unit_20.isChecked():
            self.group_box_exercises.show()
        else:
            self.group_box_exercises.hide()

        self.reset_exercises()
        self.group_box_lang_selected_1.hide()
        self.group_box_lang_selected_2.hide()
        self.button_answer.hide()

    def reset_exercises(self):

            self.buttonGroup_exercises.setExclusive(False)
            self.radBut_words.setChecked(False)
            self.radBut_sentences.setChecked(False)
            self.buttonGroup_exercises.setExclusive(True)

###############################################################################
#    DISPLAY QUESTION/ANSWER GROUPS
###############################################################################

    def display_quest_answe_button(self):

        self.group_box_lang_selected_1.show()
        self.group_box_lang_selected_2.show()
        self.button_answer.show()

        self.group_box_lang_selected_1.setTitle(self.lang_selected_1)
        self.group_box_lang_selected_2.setTitle(self.lang_selected_2)

        units=[]

        if self.chkBox_unit_1.isChecked():
            units.append(1)
        if self.chkBox_unit_2.isChecked():
            units.append(2)
        if self.chkBox_unit_3.isChecked():
            units.append(3)
        if self.chkBox_unit_4.isChecked():
            units.append(4)
        if self.chkBox_unit_5.isChecked():
            units.append(5)
        if self.chkBox_unit_6.isChecked():
            units.append(6)
        if self.chkBox_unit_7.isChecked():
            units.append(7)
        if self.chkBox_unit_8.isChecked():
            units.append(8)
        if self.chkBox_unit_9.isChecked():
            units.append(9)
        if self.chkBox_unit_10.isChecked():
            units.append(10)
        if self.chkBox_unit_11.isChecked():
            units.append(11)
        if self.chkBox_unit_12.isChecked():
            units.append(12)
        if self.chkBox_unit_13.isChecked():
            units.append(13)
        if self.chkBox_unit_14.isChecked():
            units.append(14)
        if self.chkBox_unit_15.isChecked():
            units.append(15)
        if self.chkBox_unit_16.isChecked():
            units.append(16)
        if self.chkBox_unit_17.isChecked():
            units.append(17)
        if self.chkBox_unit_18.isChecked():
            units.append(18)
        if self.chkBox_unit_19.isChecked():
            units.append(19)
        if self.chkBox_unit_20.isChecked():
            units.append(20)

        if self.radBut_words.isChecked():
            self.reader.choose_units(units, 'words')
        if self.radBut_sentences.isChecked():
            self.reader.choose_units(units, 'sentences')

        self.next_question()

###############################################################################
#    ANSWER, VERIFICATION
###############################################################################

    def verify_answer(self):

        if self.Answer.text().lower() in [x.lower() for x in self.current_answers]:
            self.next_question()
            self.Answer.setText('')
        else:
            self.Answer.setText('')

    def next_question(self):

        try:
            self.current_answers, self.current_key = self.reader.pop_random_next_combination()
            self.Question.setText(self.current_key)
        except:
            self.current_key = ' <<-_=-=_->>'
            self.current_answers = []
            self.Question.setText(self.current_key)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
