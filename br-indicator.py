#!/usr/bin/env python
#

import pygtk
pygtk.require('2.0')
import gtk
import appindicator

class BrightnessIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator ("brightness-indicator", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon ("indicator-messages-new")
        self.ind.set_icon("distributor-logo")

        # create a menu
        self.menu = gtk.Menu()

        radio = gtk.RadioMenuItem(None, "Radio Menu Item")
	radio.connect("activate",self.setbr, 20)
        radio.show()
        self.menu.append(radio)

        image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        image.connect("activate", self.quit)
        image.show()
        self.menu.append(image)
                    
        self.menu.show()

        self.ind.set_menu(self.menu)

    
    def setbr(self, widget, value):
        print value

    def quit(self, widget, data=None):
        gtk.main_quit()


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    indicator = BrightnessIndicator()
    main()
