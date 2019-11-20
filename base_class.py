class Base(object):
    def __init__(self, **kwargs):
        self.__init_values = kwargs
        self.__init_values['Class'] = type(self).__name__

    def get_init_values(self):
        """
        Returns the initialization values of the problem
        :rtype: dict
        """
        return self.__init_values

    def __str__(self):
        """
        Converts problem into a string
        :rtype: str
        """
        s = ' | '.join(['{}: {}'.format(key, item)
                         for key, item in self.__init_values.items() if not key == 'problem'])
        if 'problem' in self.__init_values:
            s += ('\n' + str(self.__init_values['problem']))
        return s
