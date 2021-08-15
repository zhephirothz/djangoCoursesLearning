import csv  # https://docs.python.org/3/library/csv.html
import urllib.request
import io

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso

url = 'https://www.dj4e.com/assn/dj4e_load/whc-sites-2018-clean.csv'
response = urllib.request.urlopen(url)

def run():
    reader = csv.reader(io.TextIOWrapper(response))
    next(reader)

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    print(reader)

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            lt = float(row[4])
        except:
            lt = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            ah = float(row[6])
        except:
            ah = None


        site = Site(
            name=row[0],
            description=row[1],
            justification=row[2],
            year=y,
            longtitude=lt,
            latitude=lat,
            area_hectares=ah,
            category=c,
            state=s,
            region=r,
            iso=i
        )
        site.save()
