class MyError(Exception):
    ...
class AnotherError(Exception):
    ...
def UpError():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('there was an error')
    raise exception_
    
try:
    UpError()
except(MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_ = AnotherError('Outher Error ')
    exception_.add_note('Another error there')
    raise exception_ from error
