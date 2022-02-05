import os
import base64
import json
import asyncio
import aiohttp

GITHUB_API_USER_NAME = os.environ['GITHUB_API_USER_NAME']
GITHUB_API_TOKEN = os.environ['GITHUB_API_TOKEN']
basic_user_and_password = base64.b64encode('{}:{}'.format(GITHUB_API_USER_NAME, GITHUB_API_TOKEN).encode('utf-8'))
AUTH_HEADER = {'Authorization': 'Basic ' + basic_user_and_password.decode('utf-8')}

class GitHubDownloader:
    def __init__(self, urls):
        self.urls = urls
        self.results = []

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        future = asyncio.ensure_future(self.fetch())
        loop.run_until_complete(future)

    async def fetch(self):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in self.urls:
                task = asyncio.ensure_future(self.download(url, session))
                tasks.append(task)
            self.results = await asyncio.gather(*tasks)

    async def download(self, url, session):
        headers = {}
        headers.update(AUTH_HEADER)
        async with session.get(url, headers=headers) as response:
            return await response.json()