# We have to wrap the standard input so we can mock it during tests
def get_input(i): #pragma: no cover
    """ Simple wrapper to default input() """
    return input(i)
