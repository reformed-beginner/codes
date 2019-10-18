#!/usr/bin/env python
#%%
import sys
import requests


API_KEY = '{{ YOUR_API_KEY  }}'
API_URL = 'https://api.esv.org/v3/passage/text/'
API_AUDIO_URL = 'https://api.esv.org/v3/passage/audio/'


def get_esv_text(passage):
    params = {
        'q': passage,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    response = requests.get(API_URL, params=params, headers=headers)
    passages = response.json()['passages']
    return passages[0].strip() if passages else 'Error: Passage not found'


def get_esv_audio(passage):
    params = {
        'q': passage,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    response = requests.get(API_AUDIO_URL, params=params, headers=headers).content
    #passages = response.json()['passages']
    f = open('E:\\music\\{}.mp3'.format(passage), 'wb')
    f.write(response)
    f.close()
    return

if __name__ == '__main__':
    passage = ' '.join(sys.argv[1:])
    print(passage)

    if passage:
        print(get_esv_text(passage))
        get_esv_audio(passage)

#%%
