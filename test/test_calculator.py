from app.calculator import add,subtract

'''
  from app->folder
  calculator -> fileName
  import add,subtract(function)
  '''
def test_add():
  assert add(2,3) == 5

def test_substract():
  assert subtract(5,3) == 2
