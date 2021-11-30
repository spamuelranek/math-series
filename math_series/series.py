def fibonacci(n):
  """
  will return the nth position
  of the fibonacci series when n>=1
  """
  if n == 0 or n== 1:
    return str(n)
  else:
    marco = fibonacci(n-1) + fibonacci(n-2)
    return str(marco)

def lucas(n):
  """
  will return the nth postion
  of the lucas series when n>=1
  """
  if n==0:
    return str(2)
  elif n==1:
    return str(1)
  else:
    polo = lucas(n-1) + lucas(n-2)
    return polo