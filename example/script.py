from anytree import Node

class ObjectGenerator:
    def __repr__(self):
        return "<ObjectGenerator instance>"


def lvl1(
        

):

    node = Node('root')

    lvl2_1(


    )

    lvl2_2()

    lvl3_1(node.name)


def lvl2_1(
        

):

    "hi, I am level 2-1. I have a return value"
    return 1


def lvl2_2(
        
):

    lvl3_1("lvl2_2")

    obj = ObjectGenerator()

    lvl3_2(obj)

    output = "return value with variable"
    return output


def lvl3_1(name):
    f"hi, I am {name}"

def lvl3_2(obj):
    return obj