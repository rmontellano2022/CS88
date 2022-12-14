test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> g = generator() # what type of object is g?
          >>> g == iter(g) # True or False?
          True
          >>> next(g) # equivalent of g.__next__()
          Starting here
          Before yield
          0
          >>> next(g)
          After yield
          Before yield
          1
          >>> next(g)
          After yield
          Before yield
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
