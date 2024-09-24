from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication

from filtres import NuancesGris, Sepia, Flou, InterpolationLineaire

# Membres de l'équipe
# <Nom complet> (usager Github)
# <Nom complet> (usager Github)
# <Nom complet> (usager Github)


class EditeurImage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.etiquette_image = QLabel()
        self.pixmap = QPixmap('ancient_filtres.png')
        self.etiquette_image.setPixmap(self.pixmap)
        self.dict_filtres = {}

    def appliquer_filtres(self):
        # Fait une copy pour s'assurer de ne pas modifier l'original
        pixmap_copy = self.pixmap.copy()
        # On itère à travers tous les filtres contenus dans le dictionnaire
        # La filtre[0] est l'instance du filtre, filtre[1] contient les paramètres passés au filtre
        for filtre in self.dict_filtres.values():
            pixmap_copy = filtre[0].appliquer_filtre(pixmap_copy, filtre[1])
        self.etiquette_image.setPixmap(pixmap_copy)


app = QApplication()
ei = EditeurImage()
ei.show()
app.exec()

