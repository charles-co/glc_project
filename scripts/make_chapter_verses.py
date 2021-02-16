import os
import requests
import time
from django.db.utils import IntegrityError
from bible.models import Chapter, Verse


def run():
    chapters = Chapter.objects.all()
    passed = False
    key = os.environ.get('BIBLE_KEY')
    for chapter in chapters:
        cid = chapter._id
        if False:#cid !='LAM.3' and passed == False:
            continue
        else:
            passed = True
            url = "https://api.scripture.api.bible/v1/bibles/de4e12af7f28f599-01/chapters/{}/verses".format(cid)
            response = requests.get(url,
                                headers = {'api-key': key})
            if response.status_code == 200:
                print('success')
                kwargs = []
                datas = response.json()['data']

                for i, data in enumerate(datas):
                    data.pop('orgId')
                    data.pop('bookId')
                    data.pop('chapterId')
                    data.pop('bibleId')
                    temp_data = data
                    temp_data['_id'] = data['id']
                    temp_data.pop('id')
                    kwargs.append(temp_data)
                # verse = ['LAM.3.'+ str(x) for x in range(1, 67)]
                # import pdb; pdb.set_trace()
                Verse.objects.bulk_create([Verse(**data, chapter=chapter) for data in kwargs])
            print("-" * 50)
        time.sleep(2)
    print("completed !!!!!")

