#!/usr/bin/python

from gi.repository import Gtk
import subprocess
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Youtube-dl GUI")


### Wanna create something? Create here.

        # Prompt for Url of video.
        prompt = Gtk.Label()
        prompt.set_text("Enter the URL:")

        # URL input field
        self.url = Gtk.Entry()
        self.url.set_text("Paste the URL here")
        
        # Start download button
        download = Gtk.Button(label="Start!")
        download.connect("clicked", self.startDownload)

        # Folder chooser
        self.location = Gtk.Button(label="Choose folder")
        self.location.connect("clicked", self.filechooser)

        #Display for what's going on!
        self.show = Gtk.Label()
        self.show.set_text("No download process running at the moment.")
        
        # Main grid.
        grid = Gtk.Grid()
        self.add(grid)

### Put your things where you wanna put below.

        # Attaching to the main Grid.
        grid.attach(prompt, 0, 0, 1, 1)
        grid.attach(self.location, 1, 1, 2, 1)
        grid.attach(self.url, 0, 1, 1, 1)
        grid.attach(download, 3, 1, 1, 1)
        grid.attach(self.show, 0, 3, 3, 2)
        #default location
        self.folder = "/home/bibek/music/"

    def startDownload(self, widget):
        arg = self.url.get_text()
        location = self.folder
        pas = "['youtube-dl', '"  + arg + "\" " + "-o '" + location + "/%(title)s.%(ext)s']"
        print(pas)

        self.show.set_text(subprocess.Popen(pas, shell=False, stdout=subprocess.PIPE))

    def filechooser(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self, Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(600, 300)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.folder = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()


        # # Main box
        # main = Gtk.Box(spacing=10)
        # # Header
        # header = Gtk.Box(spacing=10, orientation=Gtk.Orientation.HORIZONTAL)
        # # options
        # options = Gtk.Box(spacing=10, orientation=Gtk.Orientation.HORIZONTAL)
        # #promptgroup
        # promptgroup = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
        
#         # Adding stuffs in box
#         self.add(main)
#         main.pack_start(header, True, True, 0)
#         main.pack_start(options, True, True, 0)
#         header.pack_start(promptgroup, True, True, 0)
#         header.pack_start(self.location, True, True, 0)
#         header.pack_start(download, True, True, 10)
# #        options.pack_start(av, True, True, 0)
# #        options.pack_start(quality, True, True, 0)
#         promptgroup.pack_start(prompt, True, True, 0)
#         promptgroup.pack_start(self.url, True, True, 0)


