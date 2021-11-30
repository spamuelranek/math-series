def fibonacci(n):
  """
  will return the nth position
  of the fibonacci series when n>=1
  """
  if n == 0 or n== 1:
    return n
  else:
    marco = fibonacci(n-1) + fibonacci(n-2)
    return marco

def lucas(n):
  """
  will return the nth postion
  of the lucas series when n>=1
  """
  if n==0:
    return 2
  elif n==1:
    return 1
  else:
    polo = lucas(n-1) + lucas(n-2)
    return polo

def sum_series(n,zero_position = 0, first_postition = 1):
  if n==0:
    return zero_position
  elif n==1:
    return first_postition
  else:
    polo = sum_series(n-1,zero_position, first_postition) + sum_series(n-2,zero_position, first_postition)
    return polo
