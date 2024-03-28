# Context Manager with function
# Creating and using context managers

from contextlib import contextmanager

@contextmanager
def my_open (file_path, mode):
    try:
        print('Opening file')
        file = open(file_path, mode, encoding='utf8')
        yield file
    except Exception as e:
        print('there was an error', e)
    finally:
        print('Closing file')
        file.close()
        
with my_open('aula150.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n', 'try error')
    file.write('Line 4\n')
    print('With', file)
