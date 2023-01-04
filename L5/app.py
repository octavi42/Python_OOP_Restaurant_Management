from ui import UI
from modelle.identifizierbar import Identifizierbar

def main():
    # Identifizierbar.get_id_count()
    open_app()

def open_app():
    print("app opend")
    ui = UI()
    ui.start()

main()