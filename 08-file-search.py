#!/usr/local/bin/python3

import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("Sorry, we can't search that text.")
        return

    matches = search_folder(folder, text)
    for m in matches:
        # print(m)
        print('-------MATCH-------')
        print('file: ' + m.file)
        print('line: {}'.format(m.line))
        print('match: ' + m.text.strip())
        print()


def print_header():
    print('------------------------------')
    print('    FILE SEARCHER APP')
    print('------------------------------')


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()


def search_folder(folder, text):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)

        if os.path.isdir(full_item):
            # matches = search_folder(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #    yield m
            yield from search_folder(full_item, text)

        elif os.path.isfile(full_item):
            # matches = search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #    yield m
            yield from search_file(full_item, text)

    # return all_matches


def search_file(filename, search_text):
    # matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            # if search_text in line.lower()
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                # matches.append(m)
                yield m

    # return matches


if __name__ == '__main__':
    main()
