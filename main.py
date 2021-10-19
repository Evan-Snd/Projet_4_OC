import sys
from view.view_tournament import Vue

if __name__ == "__main__":
    vue = Vue()
    try:
        while True:
            vue.menu()
    except KeyboardInterrupt:
        print("Le logiciel s'est fermé")
    finally:
        vue.control.save_all()
    sys.exit(0)
