from tkinter import Frame, Label, Button

from misc import font, bg


class IndicatorBoard(Frame):
    """Contains all rotor indicators"""

    def __init__(self, master, tk_master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.enigma = self.master.enigma

        self.indicators = []
        for index in range(3):
            indicator = RotorIndicator(self, index)
            self.indicators.append(indicator)
            indicator.pack(side='left')

    def update_indicators(self):
        """Update all indicators"""
        [indicator.update_indicator() for indicator in self.indicators]


class RotorIndicator(Frame):
    """Rotor indicator for indicating or rotating a rotor"""
    def __init__(self, master, index):
        Frame.__init__(self, self, bg=bg)
        self.index = index

        self.enigma = master.enigma

        cfg = dict(font=font, width=1)

        Button(self, text='+', command=lambda: self.rotate(1), **cfg).pack(
            side='top')

        self.indicator = Label(self, bd=1, relief='sunken', width=2)

        Button(self, text='-', command=lambda: self.rotate(-1), **cfg).pack(
            side='bottom')

        self.indicator.pack(side='top', pady=10, padx=20)

        self.enigma = enigma_instance
        self.update_indicator()

    def rotate(self, places=0):
        """Rotates the rotor with the selected index backward"""
        self.master.master.playback.play('click')
        self.enigma.rotors[self.index].rotate(places)
        self.update_indicator()

    def update_indicator(self, event=None):
        """Updates what is displayed on the indicator"""
        raw = self.enigma.rotors[self.index].position
        self.indicator.config(text=raw)
