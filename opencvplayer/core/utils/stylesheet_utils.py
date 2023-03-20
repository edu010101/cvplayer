def load_css(css_path):
    readed_file = open(css_path,"r")
    return readed_file.read()

def set_style_sheet(widget, css_path):
    qcss = load_css(css_path)
    widget.setStyleSheet (qcss)

