def student_info(*args, **kwargs):  # *args are used to say that we gonna take anything as parameter
    # **kwargs states that we gonna take anything that is keyvalue, e.g. 'name' = 'idrees'
    print(args)
    print(kwargs)
course = ['math', 'art']
info = {'name' : 'john', 'age': 22}
student_info(course, info)