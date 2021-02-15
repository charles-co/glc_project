from bible.models import Book, Bible
from django.db.utils import IntegrityError

bibles = [{
    "_id": "65eec8e0b60e656b-01",
    "dblId": "65eec8e0b60e656b",
    "name": "Free Bible Version",
    "abbreviation": "FBV"
  },
  {
    "_id": "c315fa9f71d4af3a-01",
    "dblId": "c315fa9f71d4af3a",
    "name": "Geneva Bible",
    "abbreviation": "enggnv"
  },
  {
    "_id": "de4e12af7f28f599-01",
    "dblId": "de4e12af7f28f599",
    "name": "King James (Authorised) Version",
    "abbreviation": "engKJV"
  },
  {
    "_id": "de4e12af7f28f599-02",
    "dblId": "de4e12af7f28f599",
    "name": "King James (Authorised) Version 2",
    "abbreviation": "engKJV"
  },
  {
    "_id": "01b29f4b342acc35-01",
    "dblId": "01b29f4b342acc35",
    "name": "Literal Standard Version",
    "abbreviation": "LSV"
  },
  {
    "_id": "40072c4a5aba4022-01",
    "dblId": "40072c4a5aba4022",
    "name": "Revised Version 1885",
    "abbreviation": "engRV"
  },
  {
    "_id": "06125adad2d5898a-01",
    "dblId": "06125adad2d5898a",
    "name": "The Holy Bible, American Standard Version",
    "abbreviation": "ASV"
}]

def run():
    for bible in bibles:
        try:
            created_bible = Bible.objects.create(**bible)
            print("Created ", created_bible)
        except IntegrityError:
            continue