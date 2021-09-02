'''module for notes'''
from datetime import datetime
import csv
import unittest


class Note:
    '''Class for one Note'''
    def __init__(self, name, data, tags,
                current_time = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')):
        self.name = name
        self.data = data
        self.tags = tags.split()
        self.current_time = current_time

    def add_tag(self, tag):
        '''function for adding tag'''
        self.tags.append(tag)

    def change_name(self, name):
        '''function for changing name'''
        if not name:
            print('Note name cannot be empty')
        else:
            self.name = name
            self.current_time = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')

    def change_data(self, data):
        '''function for changing note'''
        self.data = data
        self.current_time = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')

    def change_tag(self):
        '''function for changing tag'''
        print(self.tags)
        user_input = input('Choose tag to change: ')
        if user_input in self.tags:
            user_input2 = input('Enter new tag: ')
            index_to_change = self.tags.index(user_input)
            self.tags[index_to_change] = user_input2
            self.current_time = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
            print('Tag successfully changed!')

    def print_note(self):
        '''function for printing note'''
        print("|{:<20}|{:^15}|{:^25}|{}|".format(self.current_time,self.name, ' '
            .join(self.tags), self.data))
        print(' {:‾^105}'.format(''))

class NoteList:
    '''class for notebook'''

    def __init__(self):
        self.data = []
        self.load_notelist()

    def add_note(self, note):
        '''function for adding note into notebook'''
        self.data.append(note)

    def delete_note(self, note_name):
        '''function for deleting note from notebook'''
        for note in self.data:
            if note.name == note_name:
                self.data.remove(note)
                break

    def find(self, search_value):
        '''function for finding value in notes'''
        find_flag = False
        for i in self.data:
            if search_value in i.name or search_value in i.data:
                i.print_note()
                find_flag = True
        if not find_flag:
            print('Data was not founded in the notes ')
        return find_flag

    def find_tags(self, search_value):
        '''function for finding notes by tag'''
        find_flag = False
        for i in self.data:
            if search_value in i.tags:
                i.print_note()
                find_flag = True

        if not find_flag:
            print('Tag was not founded in the notes')
        return find_flag

    def save_notelist(self):
        '''function for saving notelist into csv'''
        with open('notes.csv', 'w', newline='', encoding="utf-8") as file:
            field_names = ['time', 'name', 'tags', 'note']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            dict_to_write = {}
            for note in self.data:
                dict_to_write['time'] = note.current_time
                dict_to_write['name'] = note.name
                dict_to_write['tags'] = ' '.join(note.tags)
                dict_to_write['note'] = note.data
                writer.writerow(dict_to_write)

    def load_notelist(self):
        '''function for loading notelist. Also used in init func'''
        try:
            with open('notes.csv', 'r', newline = '', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    new_note = Note(row['name'], row['note'], row['tags'], row['time'])
                    self.data.append(new_note)
        except FileNotFoundError:
            self.data = []

    def print_notelist(self):
        '''function for printing notelist'''
        print(' {:_^105}'.format(''))
        for note in self.data:
            note.print_note()

class TestNote(unittest.TestCase):
    '''class for tests'''

    def setUp(self):
        '''func for tests'''
        self.note1 = Note('name1', 'data1', 'tag1')
        self.note2 = Note('name2', 'data2', 'tag1 tag2 tag3')

    def test_init(self):
        '''func for tests'''
        self.assertEqual(self.note1.name, 'name1')
        self.assertEqual(self.note1.data, 'data1')
        self.assertEqual(self.note1.tags, ['tag1'])
        self.assertEqual(self.note2.name, 'name2')
        self.assertEqual(self.note2.tags, ['tag1', 'tag2', 'tag3'])

    def test_add_tag(self):
        '''func for tests'''
        self.note1.add_tag('tag2')
        self.assertEqual(self.note1.tags, ['tag1', 'tag2'])

    def test_change_data(self):
        '''func for tests'''
        self.note1.change_name('')
        self.assertEqual(self.note1.name, 'name1')
        self.note1.change_name('name_changed')
        self.assertEqual(self.note1.name, 'name_changed')

    def test_change_data2(self):
        '''func for tests'''
        self.note1.change_data('')
        self.assertEqual(self.note1.data, '')
        self.note1.change_data('data changed')
        self.assertEqual(self.note1.data, 'data changed')

class TestNoteList(unittest.TestCase):
    '''func for tests'''

    def setUp(self):
        '''func for tests'''
        self.notelist = NoteList()
        self.note1 = Note('name1', 'data1', 'tag1')
        self.note2 = Note('name2', 'data2', 'tag1 tag2 tag3')
        self.notelist.add_note(self.note1)
        self.notelist.add_note(self.note2)

    def test_add_note(self):
        '''func for tests'''
        self.note1 = Note('name1', 'data1', 'tag1')
        self.note2 = Note('name2', 'data2', 'tag1 tag2 tag3')
        self.notelist.add_note(self.note1)
        self.assertEqual(self.notelist.data[-1], self.note1)
        self.notelist.add_note(self.note2)
        self.assertEqual(self.notelist.data[-1], self.note2)

    def test_delete_note(self):
        '''func for tests'''
        self.notelist.delete_note('name2')
        self.assertEqual(self.notelist.data[-1], self.note1)

    def test_find(self):
        '''func for tests'''
        self.assertTrue(self.notelist.find('data2'))
        self.assertFalse(self.notelist.find('name3'))
        self.assertTrue(self.notelist.find('name'))

    def test_find_tags(self):
        '''func for tests'''
        self.assertTrue(self.notelist.find_tags('tag1'))
        self.assertFalse(self.notelist.find_tags('tagggg'))
        self.assertTrue(self.notelist.find_tags('tag3'))

if __name__ == '__main__':
    unittest.main()
