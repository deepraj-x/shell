import requests
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool

def check_url_protocol(url, protocol='http'):
    return f'{protocol}://{url}/themes.php'

def check(url):
    try:
        protocols = ['http', 'https']
        for protocol in protocols:
            shel = check_url_protocol(url, protocol)
            response = requests.get(shel, headers={'User-Agent': UserAgent().safari}, timeout=10)
            if '<input type="password" name="password">' in response.text:
                print(f'Found      {shel}')
                with open('Shells.txt', 'a') as file:
                    file.write(f'{shel}\n')
                return

        print(f'Not Found {url}')

    except Exception as e:
        pass

def main():
    try:
        file_path = input('Your List: ')
        with open(file_path, 'r', errors='ignore') as file:
            urls = file.read().splitlines()

        pool = Pool(100)
        pool.map(check, urls)

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()