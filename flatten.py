#!/usr/bin/env python3

import sys
import os
import ujson as json


def flatten_keys(obj, sep:str = ".", include_values:bool = False) -> list:
    '''
    This method takes a dict (usually representing a JSON object) and will flatten the keys
    so that each key is separated by its child key with a period. You can specify a different
    separator using the separator parameter. The values for all flattened keys can be included
    by setting the include_values key to True (default is False).
    '''

    all_keys = []

    def _recurse(obj, name):

        if isinstance(obj, dict):
            for k in obj.keys():
                appended_name = f"{name}{sep}{k}"
                if isinstance(obj[k], dict):
                    _recurse(obj[k], appended_name)
                else:
                    if include_values:
                        all_keys.append(f"{appended_name} = {obj[k]}")
                    else:
                        all_keys.append(appended_name)
        else:
            if include_values:
                all_keys.append(f"{name} = {obj}")
            else:
                all_keys.append(name)

    for k in obj.keys():
        name = _recurse(obj[k], k)

    return all_keys


if __name__ == "__main__":
    '''
    This is an example of taking a Youtube channel JSON object and extracting and flattening
    all keys within the JSON object.
    '''

    yt_channel = '''{
  "id": "UCDCZverF1jgqUi911TZv5WQ",
  "etag": "aIFgOr-NlPOrY8ZBW2oU5JCmgl8",
  "kind": "youtube#channel",
  "status": {
    "isLinked": true,
    "privacyStatus": "public",
    "longUploadsStatus": "longUploadsUnspecified"
  },
  "snippet": {
    "title": "Jeremia Novianto",
    "customUrl": "@jeremianovianto2882",
    "localized": {
      "title": "Jeremia Novianto",
      "description": "somebody who's trying to learn film making"
    },
    "thumbnails": {
      "high": {
        "url": "https://yt3.ggpht.com/ytc/AOPolaTHZ8k0GKA6ypIS5wcP12NFIGmagz_CMnxsoGBm=s800-c-k-c0x00ffffff-no-rj",
        "width": 800,
        "height": 800
      },
      "medium": {
        "url": "https://yt3.ggpht.com/ytc/AOPolaTHZ8k0GKA6ypIS5wcP12NFIGmagz_CMnxsoGBm=s240-c-k-c0x00ffffff-no-rj",
        "width": 240,
        "height": 240
      },
      "default": {
        "url": "https://yt3.ggpht.com/ytc/AOPolaTHZ8k0GKA6ypIS5wcP12NFIGmagz_CMnxsoGBm=s88-c-k-c0x00ffffff-no-rj",
        "width": 88,
        "height": 88
      }
    },
    "description": "somebody who's trying to learn film making",
    "publishedAt": "2017-08-05T08:17:50Z"
  },
  "statistics": {
    "viewCount": "82779",
    "videoCount": "14",
    "subscriberCount": "224",
    "hiddenSubscriberCount": false
  },
  "topicDetails": {
    "topicIds": [
      "/m/07yv9",
      "/m/019_rr"
    ],
    "topicCategories": [
      "https://en.wikipedia.org/wiki/Vehicle",
      "https://en.wikipedia.org/wiki/Lifestyle_(sociology)"
    ]
  },
  "contentDetails": {
    "relatedPlaylists": {
      "likes": "",
      "uploads": "UUDCZverF1jgqUi911TZv5WQ"
    }
  },
  "brandingSettings": {
    "image": {
      "bannerExternalUrl": "https://lh3.googleusercontent.com/CbglvXhAxj0w4Dm3dUAh932Cr-wStLnMELbkhAFJZR-TSmHR8wSXAa6NkNgIPGJd_YCREXU96g"
    },
    "channel": {
      "title": "Jeremia Novianto",
      "description": "somebody who's trying to learn film making"
    }
  },
  "contentOwnerDetails": {}
}
'''
    if not os.isatty(0):
        for line in sys.stdin:
            j = json.loads(line)
            flattened_list = flatten_keys(j)
            for keyname in flattened_list:
                print(f" - {keyname}")
    else:
        yt_channel_json = json.loads(yt_channel)
        flattened_list = flatten_keys(obj=yt_channel_json, sep=".", include_values=False)
        print(f"Original JSON string: \n{yt_channel}")
        for keyname in flattened_list:
            print(f" - {keyname}")
