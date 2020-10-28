from treelib import Tree, Node
import hashlib
import time
import random

__root__ = Tree()
# 一个10层的root树
__root_tree__ = __root__.create_node(tag='ROOT', identifier='ROOT', data=10)


def add_node(name, identifier=None, auto_generated=True, patent=__root_tree__):
    """
    默认产生一个节点为10的树枝

    情况：
        1、如果auto_generated is True ，配置自动生成id，id名称策略为：
            见同类下方法：random_uid(str) -> str

        2、如果identifier is None，同上

        3、节点uid不允许重复，如遇重复，则

    :param name:树枝的名字和id都一样

    :param auto_generated:默认自动生成uid

    :param identifier:uid

    :param patent:为空时默认使用根节点

    :return:返回新节点
    """
    if auto_generated or identifier is None:
        identifier = random_uid()
        return __root__.create_node(tag=name, identifier=identifier, parent=patent, data=10)
    else:
        return __root__.create_node(tag=name, identifier=identifier, parent=patent, data=10)


def random_uid(uid="system"):
    """
    随机生成uid，解决起名难的问题

    :param uid:可以跟随自己心情填写，将根据这个名称随机起名
                不写也可以

    :return:
    """
    count = __root__.size()
    uni = int(random.uniform(0, count))
    _nodes = __root__.all_nodes()[uni]
    md = hashlib.md5()
    _uuid = time.time()
    _tt = str(int(_uuid) + int(random.random() * 99999 ** 3 + 1))
    _patent = _nodes.identifier
    md.update(str(_patent).encode('utf-8'))
    md.update(bytes(_tt.encode('utf-8')))
    first = md.hexdigest()
    second = md.hexdigest()
    md.update(str(first + second).encode('utf-8'))
    return '%s_%s' % (uid, md.hexdigest())


def find_node(uuid):
    """
    根据uuid查找节点
    :param uuid:
    :return:
    """
    return __root__.get_node(nid=uuid)


def root():
    """
    返回这个树的root
    :return:
    """
    return __root__


def root_tree():
    """
    获得树根
    :return:
    """
    return __root_tree__


def show(node=__root__):
    """
    显示节点的位置关系

    :param node:节点

    :return:
    """
    node.show()


if __name__ == '__main__':
    for i in range(200000):
        print(i)
        uuid = random_uid()
        try:
            node = add_node(name=uuid, identifier=uuid, auto_generated=True)
        except Exception as e:
            node = find_node(uuid)
            print(e)
