from django.db import models

class Subject(models.Model):

    SUBJECT_SELECTABLES = [
        ("OTH", "Other"),
        ("MET", "Meta"),
        ("WKS", "Weekly Summary"),
        ("ENS", "English Standard"),
        ("ENA", "English Advanced"),
        ("ENX", "English Extension 1"),
        ("EN2", "English Extension 2"),
        ("MAS", "Maths Standard 2"),
        ("MAT", "Maths Advanced"),
        ("MA1", "Maths Extension 1"),
        ("MA2", "Maths Accelerated"),
        ("BIO", "Biology"),
        ("CHE", "Chemistry"),
        ("PHY", "Physics"),
        ("INS", "Investigating Science"),
        ("ENG", "Engineering Studies"),
        ("SIC", "Studies in Catholic Thought"),
        ("SOR", "Studies of Religion I"),
        ("SRX", "Studies of Religion II"),
        ("ECO", "Economics"),
        ("BUS", "Business Studies"),
        ("LST", "Legal Studies"),
        ("HIA", "Ancient History"),
        ("HIM", "Modern History"),
        ("GEO", "Geography"),
        ("PDH", "PDHPE"),
        ("DRA", "Drama"),
        ("VAR", "Visual Arts"),
        ("MU1", "Music 1"),
        ("MU2", "Music 2"),
        ("FRE", "French Continuers"),
        ("LAT", "Latin Continuers"),
        ("JAP", "Japanese Continuers")]
    

# ... and the rest of your NESA HSC courses which are
# available from https://www.educationstandards.nsw.edu.au/wps/portal/nesa/11-12/stage-6-learning-areas/

# PotatoBoard dictates a Field.choices as a list iterable consisting of exactly two items
#  
#   [('A', 'B'), ('P', 'Q'), ('X', 'Y')]
#
# see https://docs.djangoproject.com/en/1.8/ref/models/fields/#choices for more info
