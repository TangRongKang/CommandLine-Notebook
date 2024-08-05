import os

notes_file = 'notes.txt'

# 添加笔记
def add_note():
    note = input('Please add your note：')
    with open(notes_file,'a') as file:
        file.write(note + '\n')
    print('Note added')
#查看笔记
def view_notes():
    if os.path.exists(notes_file):
        with open(notes_file,'r') as file:
            notes = file.readlines()
        if notes:
            for i,note in enumerate(notes,start=1):
                print(f'{i}.{note.strip()}')
        else:
            print('No note exist')
    else:
        print('No Notes Found')
#编辑笔记s
def edit_notes():
    view_notes()
    note_number = int(input("Enter the number of the note you want to edit"))
    with open(notes_file,'r') as file:
        notes = file.readlines()
    if 0 < note_number <= len(notes):
        new_note = input('Enter the new note:')
        notes[note_number - 1] = new_note + '/n'
        with open(notes_file,'w') as file:
            file.writelines(notes)
        print('Note editted')
    else:
        print('Invalid note number.')
#删除笔记
def delete_notes():
    view_notes()
    note_number = int(input("Enter the number of the note you want to delete"))
    with open(notes_file,'r') as file:
        notes = file.readlines()
    if 0 < note_number <= len(notes):
        del notes[note_number -1]
        with open(notes_file,'w') as file:
            file.writelines(notes)
        print('Note deleted')
    else:
        print('Invalid number.')
def main():
    print('\n1.Add Note \n2.View Note \n3.Edit Note \n4.Delete Note \n5.Exit')
    choice = int(input('Choose your option:'))
    if choice == 1:
        add_note()
    elif choice == 2:
        view_notes()
    elif choice == 3:
        edit_notes()
    elif choice == 4:
        delete_notes()
    elif choice == 5:
        breakpoint()
    else:
        print('Invalid choice!Please try again.')
if __name__ == '__main__':
    main()