#!/usr/bin/env python
#

import pygtk
pygtk.require('2.0')
import gtk
import appindicator
import os

ITEMS_NUM = 11

class BrightnessIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator ("brightness-indicator", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon ("indicator-messages-new")
        self.ind.set_icon("weather-clear")

        # create a menu
        self.menu = gtk.Menu()
        self.items = []
        radio_group = gtk.RadioMenuItem()
        for i in range(ITEMS_NUM):
            radio = gtk.RadioMenuItem(radio_group, str(i))
            radio.connect("activate",self.setbr, i*10)
            radio.show()
            self.items.append(radio)
            self.menu.append(radio)

        image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        image.connect("activate", self.quit)
        image.show()
        self.menu.append(image)

        self.menu.show()


        self.ind.set_menu(self.menu)


    def setbr(self, widget, value):
        command="xbacklight =" + str(value)
        os.popen(command)


    def quit(self, widget, data=None):
        gtk.main_quit()


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    indicator = BrightnessIndicator()
    main()
