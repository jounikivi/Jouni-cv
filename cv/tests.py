from datetime import date
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Koulutus, Taidot, TietojaMinusta, Tyokokemus


@override_settings(SECRET_KEY="test-secret-key")
class ModelStringRepresentationTests(TestCase):
    """Ensure __str__ methods return expected strings."""

    def test_tietoja_minusta_str(self):
        obj = TietojaMinusta(otsikko="Otsikko", kuvaus="Kuvaus")
        self.assertEqual(str(obj), "Otsikko")

    def test_tyokokemus_str(self):
        obj = Tyokokemus(
            yritys="Yritys",
            tehtava="Tehtävä",
            kuvaus="Kuvaus",
            alkupvm=date(2020, 1, 1),
            loppupvm=date(2021, 1, 1),
        )
        self.assertEqual(str(obj), "Tehtävä at Yritys")

    def test_koulutus_str(self):
        obj = Koulutus(
            oppilaitos="Oppilaitos",
            tutkinto="Tutkinto",
            kuvaus="Kuvaus",
            aloitusvuosi=date(2018, 1, 1),
            valmistumisvuosi=date(2020, 1, 1),
        )
        self.assertEqual(str(obj), "Tutkinto at Oppilaitos")

    def test_taidot_str(self):
        obj = Taidot(taito="Python", taso=5)
        self.assertEqual(str(obj), "Python 5")


GIF_BYTES = (
    b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF!\xF9\x04\x01"
    b"\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02L\x01\x00;"
)


@override_settings(MEDIA_ROOT=tempfile.gettempdir(), SECRET_KEY="test-secret-key")
class HomeViewTests(TestCase):
    """Verify context and response of the home view."""

    def setUp(self):
        self.tietoa = TietojaMinusta.objects.create(
            otsikko="Minusta",
            kuvaus="Kuvaus",
            kuva=SimpleUploadedFile("test.gif", GIF_BYTES, content_type="image/gif"),
        )
        self.tyokokemus = Tyokokemus.objects.create(
            yritys="Yritys",
            tehtava="Tehtävä",
            kuvaus="Kuvaus",
            alkupvm=date(2020, 1, 1),
            loppupvm=date(2021, 1, 1),
        )
        self.koulutus = Koulutus.objects.create(
            oppilaitos="Oppilaitos",
            tutkinto="Tutkinto",
            kuvaus="Kuvaus",
            aloitusvuosi=date(2018, 1, 1),
            valmistumisvuosi=date(2020, 1, 1),
        )
        self.taito = Taidot.objects.create(taito="Python", taso=3)

    def test_home_context_and_response(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cv/home.html")
        self.assertEqual(response.context["tietoa"], self.tietoa)
        self.assertEqual(list(response.context["tyokokemukset"]), [self.tyokokemus])
        self.assertEqual(list(response.context["koulutukset"]), [self.koulutus])
        self.assertEqual(list(response.context["taidot"]), [self.taito])
