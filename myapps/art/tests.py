from mylog import logger

from django.test import TestCase

# Create your tests here.
class TestDB(TestCase):

    def testConn(self):
        logger.info('开始运行测试方法-testConn-')
        a = None
        # 如果测试断言失败，则会抛出AssertionError
        # 并显示msg指定的消息
        self.assertIsNone(a, 'a 不是None')

    def __del__(self):
        print('--单元测试OVER--')