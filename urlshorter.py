from __future__ import with_statement
import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen

def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' +
                   urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')
# urlencode избавляется от спецсимволов, urlopen открывает ссылку
def main():
    url = input('Enter url: ')
    print('Short var:', make_tiny(url))

if __name__ == '__main__':
    main()
