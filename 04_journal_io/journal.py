import os

def load(name):
    #TODO: take journal name and load file from disk
    journal = []
    return journal


def save(journal, name):
    #create absolute path to new file
    jrl_path = os.path.abspath(os.path.join('./jrl_files/' + name + '.jrl'))
    print('File save location: {}'.format(jrl_path))
    #take list and write each item to new line
   


def add_entry(journal, new_entry):
    updated_journal = journal.append(new_entry)
    return updated_journal


