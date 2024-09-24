from abc import ABC, abstractmethod

from PySide6.QtGui import QPixmap, QImage


class AbstractFilter(ABC):

    @abstractmethod
    def appliquer_filtre(self, qpixmap: QPixmap, parametres_filtre: {}) -> QPixmap:
        pass


class Flou(AbstractFilter):

    def appliquer_filtre(self, qpixmap: QPixmap, parametres_filtre: {}) -> QPixmap:
        qimage = qpixmap.toImage()
        # Votre code du filtre ici

        return QPixmap.fromImage(qimage)


class InterpolationLineaire(AbstractFilter):

    def appliquer_filtre(self, qpixmap: QPixmap, parametres_filtre: {}) -> QPixmap:
        qimage = qpixmap.toImage()
        # Votre code du filtre ici

        return QPixmap.fromImage(qimage)


class Sepia(AbstractFilter):

    def appliquer_filtre(self, qpixmap: QPixmap, parametres_filtre: {}) -> QPixmap:
        qimage = qpixmap.toImage()
        # Votre code du filtre ici

        return QPixmap.fromImage(qimage)


class NuancesGris(AbstractFilter):

    def appliquer_filtre(self, qpixmap: QPixmap, parametres_filtre: {}) -> QPixmap:
        qimage = qpixmap.toImage()
        # Votre code du filtre ici

        return QPixmap.fromImage(qimage)