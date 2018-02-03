class Tools:
    def __init__(self, text):
        self.text = text
    def change_space_to_plus(self):
        return self.text.replace(' ', '+')

    def remove_spaces_enter_tab(self):
        for i in " \t\n\r":
            self.text = self.text.replace(i, '')
        return self.text
