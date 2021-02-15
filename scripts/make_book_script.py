from bible.models import Book, Bible
from django.db.utils import IntegrityError

books = [
    {
      "_id": "GEN",
      "abbreviation": "Gen",
      "name": "Genesis",
      "nameLong": "The First Book of Moses, called Genesis"
    },
    {
      "_id": "EXO",
      "abbreviation": "Exo",
      "name": "Exodus",
      "nameLong": "The Second Book of Moses, called Exodus"
    },
    {
      "_id": "LEV",
      "abbreviation": "Lev",
      "name": "Leviticus",
      "nameLong": "The Third Book of Moses, called Leviticus"
    },
    {
      "_id": "NUM",
      "abbreviation": "Num",
      "name": "Numbers",
      "nameLong": "The Fourth Book of Moses, called Numbers"
    },
    {
      "_id": "DEU",
      "abbreviation": "Deu",
      "name": "Deuteronomy",
      "nameLong": "The Fifth Book of Moses, called Deuteronomy"
    },
    {
      "_id": "JOS",
      "abbreviation": "Jos",
      "name": "Joshua",
      "nameLong": "The Book of Joshua"
    },
    {
      "_id": "JDG",
      "abbreviation": "Jdg",
      "name": "Judges",
      "nameLong": "The Book of Judges"
    },
    {
      "_id": "RUT",
      "abbreviation": "Rut",
      "name": "Ruth",
      "nameLong": "The Book of Ruth"
    },
    {
      "_id": "1SA",
      "abbreviation": "1Sa",
      "name": "1 Samuel",
      "nameLong": "The First Book of Samuel Otherwise Called The First Book of the Kings"
    },
    {
      "_id": "2SA",
      "abbreviation": "2Sa",
      "name": "2 Samuel",
      "nameLong": "The Second Book of Samuel Otherwise Called The Second Book of the Kings"
    },
    {
      "_id": "1KI",
      "abbreviation": "1Ki",
      "name": "1 Kings",
      "nameLong": "The First Book of the Kings, Commonly Called the Third Book of the Kings"
    },
    {
      "_id": "2KI",
      "abbreviation": "2Ki",
      "name": "2 Kings",
      "nameLong": "The Second Book of the Kings, Commonly Called the Fourth Book of the Kings"
    },
    {
      "_id": "1CH",
      "abbreviation": "1Ch",
      "name": "1 Chronicles",
      "nameLong": "The First Book of the Chronicles"
    },
    {
      "_id": "2CH",
      "abbreviation": "2Ch",
      "name": "2 Chronicles",
      "nameLong": "The Second Book of the Chronicles"
    },
    {
      "_id": "EZR",
      "abbreviation": "Ezr",
      "name": "Ezra",
      "nameLong": "Ezra"
    },
    {
      "_id": "NEH",
      "abbreviation": "Neh",
      "name": "Nehemiah",
      "nameLong": "The Book of Nehemiah"
    },
    {
      "_id": "EST",
      "abbreviation": "Est",
      "name": "Esther",
      "nameLong": "The Book of Esther"
    },
    {
      "_id": "JOB",
      "abbreviation": "Job",
      "name": "Job",
      "nameLong": "The Book of Job"
    },
    {
      "_id": "PSA",
      "abbreviation": "Psa",
      "name": "Psalms",
      "nameLong": "The Book of Psalms"
    },
    {
      "_id": "PRO",
      "abbreviation": "Pro",
      "name": "Proverbs",
      "nameLong": "The Proverbs"
    },
    {
      "_id": "ECC",
      "abbreviation": "Ecc",
      "name": "Ecclesiastes",
      "nameLong": "Ecclesiastes or, the Preacher"
    },
    {
      "_id": "SNG",
      "abbreviation": "Sng",
      "name": "Song of Solomon",
      "nameLong": "The Song of Solomon"
    },
    {
      "_id": "ISA",
      "abbreviation": "Isa",
      "name": "Isaiah",
      "nameLong": "The Book of the Prophet Isaiah"
    },
    {
      "_id": "JER",
      "abbreviation": "Jer",
      "name": "Jeremiah",
      "nameLong": "The Book of the Prophet Jeremiah"
    },
    {
      "_id": "LAM",
      "abbreviation": "Lam",
      "name": "Lamentations",
      "nameLong": "The Lamentations of Jeremiah"
    },
    {
      "_id": "EZK",
      "abbreviation": "Ezk",
      "name": "Ezekiel",
      "nameLong": "The Book of the Prophet Ezekiel"
    },
    {
      "_id": "DAN",
      "abbreviation": "Dan",
      "name": "Daniel",
      "nameLong": "The Book of Daniel"
    },
    {
      "_id": "HOS",
      "abbreviation": "Hos",
      "name": "Hosea",
      "nameLong": "Hosea"
    },
    {
      "_id": "JOL",
      "abbreviation": "Jol",
      "name": "Joel",
      "nameLong": "Joel"
    },
    {
      "_id": "AMO",
      "abbreviation": "Amo",
      "name": "Amos",
      "nameLong": "Amos"
    },
    {
      "_id": "OBA",
      "abbreviation": "Oba",
      "name": "Obadiah",
      "nameLong": "Obadiah"
    },
    {
      "_id": "JON",
      "abbreviation": "Jon",
      "name": "Jonah",
      "nameLong": "Jonah"
    },
    {
      "_id": "MIC",
      "abbreviation": "Mic",
      "name": "Micah",
      "nameLong": "Micah"
    },
    {
      "_id": "NAM",
      "abbreviation": "Nam",
      "name": "Nahum",
      "nameLong": "Nahum"
    },
    {
      "_id": "HAB",
      "abbreviation": "Hab",
      "name": "Habakkuk",
      "nameLong": "Habakkuk"
    },
    {
      "_id": "ZEP",
      "abbreviation": "Zep",
      "name": "Zephaniah",
      "nameLong": "Zephaniah"
    },
    {
      "_id": "HAG",
      "abbreviation": "Hag",
      "name": "Haggai",
      "nameLong": "Haggai"
    },
    {
      "_id": "ZEC",
      "abbreviation": "Zec",
      "name": "Zechariah",
      "nameLong": "Zechariah"
    },
    {
      "_id": "MAL",
      "abbreviation": "Mal",
      "name": "Malachi",
      "nameLong": "Malachi"
    },
    {
      "_id": "MAT",
      "abbreviation": "Mat",
      "name": "Matthew",
      "nameLong": "THE GOSPEL ACCORDING TO ST. MATTHEW"
    },
    {
      "_id": "MRK",
      "abbreviation": "Mrk",
      "name": "Mark",
      "nameLong": "THE GOSPEL ACCORDING TO ST. MARK"
    },
    {
      "_id": "LUK",
      "abbreviation": "Luk",
      "name": "Luke",
      "nameLong": "THE GOSPEL ACCORDING TO ST. LUKE"
    },
    {
      "_id": "JHN",
      "abbreviation": "Jhn",
      "name": "John",
      "nameLong": "THE GOSPEL ACCORDING TO ST. JOHN"
    },
    {
      "_id": "ACT",
      "abbreviation": "Act",
      "name": "Acts",
      "nameLong": "THE ACTS OF THE APOSTLES"
    },
    {
      "_id": "ROM",
      "abbreviation": "Rom",
      "name": "Romans",
      "nameLong": "THE EPISTLE OF PAUL THE APOSTLE TO THE ROMANS"
    },
    {
      "_id": "1CO",
      "abbreviation": "1Co",
      "name": "1 Corinthians",
      "nameLong": "THE FIRST EPISTLE OF PAUL THE APOSTLE TO THE CORINTHIANS"
    },
    {
      "_id": "2CO",
      "abbreviation": "2Co",
      "name": "2 Corinthians",
      "nameLong": "THE SECOND EPISTLE OF PAUL THE APOSTLE TO THE CORINTHIANS"
    },
    {
      "_id": "GAL",
      "abbreviation": "Gal",
      "name": "Galatians",
      "nameLong": "THE EPISTLE OF PAUL THE APOSTLE TO THE GALATIANS"
    },
    {
      "_id": "EPH",
      "abbreviation": "Eph",
      "name": "Ephesians",
      "nameLong": "THE EPISTLE OF PAUL THE APOSTLE TO THE EPHESIANS"
    },
    {
      "_id": "PHP",
      "abbreviation": "Php",
      "name": "Philippians",
      "nameLong": "THE EPISTLE OF PAUL THE APOSTLE TO THE PHILIPPIANS"
    },
    {
      "_id": "COL",
      "abbreviation": "Col",
      "name": "Colossians",
      "nameLong": "THE EPISTLE OF PAUL THE APOSTLE TO THE COLOSSIANS"
    },
    {
      "_id": "1TH",
      "abbreviation": "1Th",
      "name": "1 Thessalonians",
      "nameLong": "THE FIRST EPISTLE OF PAUL THE APOSTLE TO THE THESSALONIANS"
    },
    {
      "_id": "2TH",
      "abbreviation": "2Th",
      "name": "2 Thessalonians",
      "nameLong": "THE SECOND EPISTLE OF PAUL THE APOSTLE TO THE THESSALONIANS"
    },
    {
      "_id": "1TI",
      "abbreviation": "1Ti",
      "name": "1 Timothy",
      "nameLong": "THE FIRST EPISTLE OF PAUL THE APOSTLE TO TIMOTHY"
    },
    {
      "_id": "2TI",
      "abbreviation": "2Ti",
      "name": "2 Timothy",
      "nameLong": "THE SECOND EPISTLE OF PAUL THE APOSTLE TO TIMOTHY"
    },
    {
      "_id": "TIT",
      "abbreviation": "Tit",
      "name": "Titus",
      "nameLong": "THE EPISTLE OF PAUL THE APOSTLE TO TITUS"
    },
    {
      "_id": "PHM",
      "abbreviation": "Phm",
      "name": "Philemon",
      "nameLong": "THE EPISTLE OF PAUL THE APOSTLE TO PHILEMON"
    },
    {
      "_id": "HEB",
      "abbreviation": "Heb",
      "name": "Hebrews",
      "nameLong": "THE EPISTLE OF PAUL THE APOSTLE TO THE HEBREWS"
    },
    {
      "_id": "JAS",
      "abbreviation": "Jas",
      "name": "James",
      "nameLong": "THE GENERAL EPISTLE OF JAMES"
    },
    {
      "_id": "1PE",
      "abbreviation": "1Pe",
      "name": "1 Peter",
      "nameLong": "THE FIRST EPISTLE GENERAL OF PETER"
    },
    {
      "_id": "2PE",
      "abbreviation": "2Pe",
      "name": "2 Peter",
      "nameLong": "THE SECOND EPISTLE GENERAL OF PETER"
    },
    {
      "_id": "1JN",
      "abbreviation": "1Jn",
      "name": "1 John",
      "nameLong": "THE FIRST EPISTLE GENERAL OF JOHN"
    },
    {
      "_id": "2JN",
      "abbreviation": "2Jn",
      "name": "2 John",
      "nameLong": "THE SECOND EPISTLE OF JOHN"
    },
    {
      "_id": "3JN",
      "abbreviation": "3Jn",
      "name": "3 John",
      "nameLong": "THE THIRD EPISTLE OF JOHN"
    },
    {
      "_id": "JUD",
      "abbreviation": "Jud",
      "name": "Jude",
      "nameLong": "THE GENERAL EPISTLE OF JUDE"
    },
    {
      "_id": "REV",
      "abbreviation": "Rev",
      "name": "Revelation",
      "nameLong": "THE REVELATION OF ST. JOHN THE DIVINE"
    }
]

def run():
    for book in books:
        try:
            created_book = Book.objects.create(**book)
            print("Created ", created_book)
        except IntegrityError:
            continue