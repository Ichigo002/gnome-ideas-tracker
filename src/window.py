
from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/wiktor/IdeaTracker/window.ui')
class IdeatrackerWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'IdeatrackerWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
