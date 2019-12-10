import urllib.request


def file_downloading(t_url, name):
    urllib.request.urlretrieve(t_url, name)


def word_count(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        stats = {}
        for word in words:
            if word not in stats:
                stats[word] = 1
            else:
                stats[word] += 1
        return len(words), stats


if __name__ == '__main__':
    _url = 'https://norvig.com/big.txt'
    _path = input("Enter path for downloading: ")
    file_downloading(_url, _path)
    filename = 'text.txt'
    word_number, statistic = word_count(filename)
    for key,word in statistic.items():
        print('{0} = {1}'.format(key,word))
    print(f'Слів у файлі text.txt =  {word_number}')
