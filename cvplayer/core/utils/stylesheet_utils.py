from pkg_resources import resource_filename

def load_css(css_path):
    readed_file = open(resource_filename(__name__, css_path),"r")
    return readed_file.read()

def set_style_sheet(widget, css_path):
    qcss = load_css(css_path)
    widget.setStyleSheet (qcss)

