class DemoClass:

    my_class_att = 0

    def __init__(self, name):
        """
        Initialize the instance variables
        :param name: name assigned to instance
        """
        self.my_instance_name_att = name
        self._my_private_att = 'z'
        self.__my_mangled_private_att = 'mz'


    def __str__(self):
        """
        convert class data to string
        :return: string
        """
        return "data : {} : {} : {} : {} ".format(self.my_class_att, self.my_instance_name_att, self._my_private_att, self.__my_mangled_private_att)


if __name__== '__main__':
    print("Class {} : ".format(DemoClass.my_class_att))
    #print("{} : {} : {} ".format(DemoClass.my_class_att, DemoClass.my_instance_att, DemoClass._my_private_att))

    a = DemoClass('A')
    b = DemoClass('B')

    print("Instantiation:")
    print(a)
    print(b)

    print("Set b:")
    b.my_instance_name_att = 'C'
    print(a)
    print(b)

    print(" Set class att:")
    DemoClass.my_class_att = 42
    print(a)
    print(b)

    print("set as instance att (don't do this):")
    a.my_class_att = 99
    print(a)
    print(b)

    print(" Set class att (but above busted the link):")
    DemoClass.my_class_att = 'Squirrels'
    print(a)
    print(b)

    a._my_private_att = 'not really private (convention only)'
    a._DemoClass__my_mangled_private_att = 'mangled is still not really private (convention only)'
    print(a)

    print("Get directory of attributes:")
    print(dir(a))

