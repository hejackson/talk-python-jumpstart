#!/usr/local/bin/python3

import journal


def print_header():
    print('------------------------------')
    print('         JOURNAL')
    print('------------------------------')


def run_event_loop():
    print('What do you want to do with your journal? ')

    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ').lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry we don't understand '{}'.".format(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    for idx, item in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, item))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


def main():
    print_header()
    run_event_loop()


if __name__ == '__main__':
    main()
