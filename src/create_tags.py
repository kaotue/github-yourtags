import json
import time
import os
import asyncio
import github_api
from calc_time import calc_time

EXCEPT_TAGS = os.environ.get('EXCEPT_TAGS', 'html').split(',')
print(f'{EXCEPT_TAGS=}')

@calc_time
def run(user_name: str) -> list:

    urls = [f'https://api.github.com/users/{user_name}/repos']
    downloader = github_api.GitHubDownloader(urls)
    downloader.run()
    if not downloader.results:
        return None

    print(downloader.results)
    urls = [x.get('languages_url') for x in downloader.results[0]]
    downloader = github_api.GitHubDownloader(urls)
    downloader.run()

    tags = []
    for result in downloader.results:
        # print(f'{result=}')
        if not result:
            continue
        for k, v in result.items():
            tag = next((x for x in tags if x['name'] == k), None)
            if k.lower() in EXCEPT_TAGS:
                continue
            if tag:
                tag['count'] = tag['count'] + 1
                tag['value'] = tag['value'] + v
            else:
                tags.append({
                    'name': k,
                    'count': 1,
                    'value': v
                })
    if not tags:
        return None
    # set_point_to_tags(tags)
    # sort by count and point
    # tags = sorted(tags, key=lambda x: (x['value'], x['count']), reverse=True)
    return tags

def set_point_to_tags(tags: dict):
    sum_count = sum([x['count'] for x in tags])
    for tag in tags:
        tag['point'] = round((tag['count'] / sum_count) * 100, 2)