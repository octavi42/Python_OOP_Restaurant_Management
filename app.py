from ui import UI
from tests import Tests

def main():
    # Identifizierbar.get_id_count()
    open_app()

def open_app():
    print("app opend")
    ui = UI()
    ui.start()

def start_tests():
    test = Tests()
    test.add_gericht()
    test.suchen_nach_teilname()
    test.suchen_nach_teiladresse()
    test.update_name_kunde()
    test.print_string()
    test.save_bestellung()
    test.load_bestellung()

main()