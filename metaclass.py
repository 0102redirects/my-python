#coding:utf-8
class ObjectCreator(object):
    pass

my_object = ObjectCreator()

print ObjectCreator


def echo(o):
    print o

echo(ObjectCreator)      # 你可以将类做为参数传给函数
print hasattr(ObjectCreator, 'new_attribute')
ObjectCreator.new_attribute = 'foo'  # 你可以为类增加属性
print hasattr(ObjectCreator, 'new_attribute')
print ObjectCreator.new_attribute
ObjectCreatorMirror = ObjectCreator  # 你可以将类赋值给一个变量
print ObjectCreatorMirror()
