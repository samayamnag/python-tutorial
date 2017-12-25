def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print('display function ran')


@decorator_function
def display_info(name, email):
    print('display_info function ran with two arguments ({}, {})'.format(name, email))


# display = decorator_function(display)
display()
display_info('Nag', 'nag.samayam@gmail.com')
