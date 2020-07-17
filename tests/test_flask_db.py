from flask_db import db
from model import Course
import unittest



class DBTest(unittest.TestCase):
    #每个单元测试前都可先初始化数据库
    @classmethod
    def setUpClass(self):
        #a = Course(course_name="中", course_type="语文", course_url="www.4399.com", platform_name="bibb")
        #b = Course(course_name="C++", course_type="计算机", course_url="www.metube.com", platform_name="metube")
        #s = [a, b]
        db.init_course_table()
        #db.insert_courses_table()

    #每次测试前都会把表里元素清空
    def setUp(self):
        db.delete_all_course_table()
    # 每次测试都会完查询所有元素
    #插入元素测试

    # 正常插入
    def test_insert1(self):

        a = Course(course_name="hh", course_type="ss", course_url="4399", platform_name="sss")
        self.assertTrue(db.insert_course_table(a))
    # 课程名沒有字
    def test_insert2(self):

        a = Course(course_name="", course_type="", course_url="", platform_name="")
        self.assertTrue(db.insert_course_table(a))
    # 课程名刚好16个字
    def test_insert3(self):

        a = Course(course_name="aaaaaaaaaaaassss", course_type="ss", course_url="4399", platform_name="sss")
        self.assertTrue(db.insert_course_table(a))
    # 课程名超过16个字
    def test_insert4(self):

        a = Course(course_name="aaaaaaaaaaaasssss", course_type="ss", course_url="4399", platform_name="sss")
        self.assertFalse(db.insert_course_table(a))
    # 课程名刚好4个字(中文)
    def test_insert5(self):

        a = Course(course_name="这是一个", course_type="ss", course_url="4399", platform_name="sss")
        self.assertTrue(db.insert_course_table(a))
    # 课程名刚好16个字(中文)
    def test_insert6(self):

        a = Course(course_name="这是一个测试这是一个测试一个测试", course_type="ss", course_url="4399", platform_name="sss")
        self.assertTrue(db.insert_course_table(a))
    # 课程名超过16个字(中文)
    def test_insert7(self):

        a = Course(course_name="这是一个测试这s是一个测试一个测试", course_type="ss", course_url="4399", platform_name="sss")
        self.assertFalse(db.insert_course_table(a))
    # 不正常输入
    def test_insert8(self):

        a = "Cours)"
        self.assertFalse(db.insert_course_table(a))
    # 输入为None
    def test_insert8(self):
        a = None
        self.assertFalse(db.insert_course_table(a))
    #输入已有URL
    def test_insert9(self):
        a = Course(course_name="hh", course_type="ss", course_url="4399", platform_name="sss")
        db.insert_course_table(a)
        self.assertFalse(db.insert_course_table(a))


    # 插入多条元素测试\

    # 正常多条插入
    def test_insertmany1(self):

        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s=[a,b]
        self.assertTrue(db.insert_courses_table(s))
    # 输入数组为空
    def test_insertmany2(self):

        s=[]
        self.assertFalse(db.insert_courses_table(s))
    # 输入数组为None
    def test_insertmany3(self):
        s = None
        self.assertFalse(db.insert_courses_table(s))
    #输入数组其中有一个是课程名超过16位
    def test_insertmany4(self):
        a = Course(course_name="这ssssssssssssssssssssssssssssssssssssssssss一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        self.assertFalse(db.insert_courses_table(s))
    # 输入数组其中有一个是None
    def test_insertmany5(self):
        a = Course(course_name="这一个测试", course_type="ss",course_url="4399", platform_name="")
        b = None
        s = [a, b]
        self.assertFalse(db.insert_courses_table(s))
    #插入相同URL
    def test_insertmany6(self):

        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399d", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s=[a,b]
        self.assertFalse(db.insert_courses_table(s))

    #删除表中所有元素测试

    #表中有元素的删除
    def test_deleteall1(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertTrue(db.delete_all_course_table())
    #表中沒有元素
    def test_deleteall2(self):
        self.assertTrue(db.delete_all_course_table())

    # 删除表中某一元素测试(对象)

    #正常输入
    def test_delete1(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]

        db.insert_courses_table(s)
        self.assertTrue(db.delete_course_table(a))

    #输入新的对象
    def test_delete2(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        c=Course(course_name="这是一个测试", course_type="sss", course_url="sdjw", platform_name="rt")
        self.assertTrue(db.delete_course_table(c))
    #输入为錯誤对象
    def test_delete3(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        c = Course(course_name="测试", course_type="ssds", course_url="sjw", platform_name="t")
        self.assertTrue(db.delete_course_table(c))
    #输入为空
    def test_delete4(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertFalse(db.delete_course_table(None))
    #表为空
    def test_delete5(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        db.delete_all_course_table()
        self.assertTrue(db.delete_course_table(a))

    # 删除表中某一元素测试(id)

    #正常删除
    def test_deleteid1(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.drop_course_table()
        db.init_course_table()
        db.insert_courses_table(s)
        #print(db.select_all_course()[0].id)
        self.assertTrue(db.delete_course_table2(1))
    # 输入不正常
    def test_deleteid2(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.drop_course_table()
        db.init_course_table()
        db.insert_courses_table(s)
        #print(db.select_all_course()[0].id)
        self.assertTrue(db.delete_course_table2(3))
    #输入为空
    def test_deleteid3(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.drop_course_table()
        db.init_course_table()
        db.insert_courses_table(s)
        # print(db.select_all_course()[0].id)
        self.assertFalse(db.delete_course_table2(None))
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.drop_course_table()
        db.init_course_table()
        db.insert_courses_table(s)
        # print(db.select_all_course()[0].id)
        self.assertFalse(db.delete_course_table2(None))

    #更新测试(id)
    #正确输入
    def test_update1(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        c = Course(course_name="这个测试", course_type="sss", course_url="4399", platform_name="r")
        db.drop_course_table()
        db.init_course_table()
        db.insert_courses_table(s)
        self.assertTrue(db.update_course_table(1, c))
    #不正确输入
    def test_update2(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        c = Course(course_name="这个测试", course_type="sss", course_url="4399", platform_name="r")
        db.drop_course_table()
        db.init_course_table()
        db.insert_courses_table(s)
        self.assertTrue(db.update_course_table(3, c))
        #print(db.select_all_course()[3].course_name)
        self.assertFalse(db.update_course_table(None, None))
        self.assertFalse(db.update_course_table(1, None))
        self.assertFalse(db.update_course_table(None, c))


    # 查找课程名测试

    #正确输入
    def test_selectcoursename1(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_course_name(a.course_name)[0].course_name,a.course_name)
        self.assertEqual(db.select_course_name(a.course_name)[1].course_name, a.course_name)
    #输入錯誤
    def test_selectcoursename2(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        c=Course(course_name="这是s测试", course_type="325s", course_url="439d", platform_name="t")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_course_name(c.course_name),[])
    #输入为None
    def test_selectcoursename3(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_course_name(None),None)
    #表为空
    def test_selectcoursename4(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        self.assertEqual(db.select_course_name(a),None)


    # 查找平台类型测试

    #正确输入
    def test_selectcoursetype1(self):
        a = Course(course_name="这是一个测试", course_type="sss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_course_type(a.course_type)[0].course_type,a.course_type)
        self.assertEqual(db.select_course_type(a.course_type)[1].course_type,a.course_type)
    #输入錯誤
    def test_selectcoursetype2(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        c=Course(course_name="这是s测试", course_type="325s", course_url="439d", platform_name="t")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_course_type(c.course_type),[])
    #输入为None
    def test_selectcoursetype3(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_course_type(None),None)

    # 表为空
    def test_selectcoursename4(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        self.assertEqual(db.select_course_type(a), None)


    # 查找平台类型测试

    #正确输入
    def test_selectplatformname1(self):
        a = Course(course_name="这是一个测试", course_type="sss", course_url="4399", platform_name="s")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_platform_name(a.platform_name)[0].course_type,a.course_type)
    #输入錯誤
    def test_selectplatformname2(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        c=Course(course_name="这是s测试", course_type="325s", course_url="439d", platform_name="t")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_platform_name(c.course_type),[])
    #输入为None
    def test_selectplatformname3(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_platform_name(None),None)
    #表为空
    def test_selectcoursename4(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        self.assertEqual(db.select_platform_name(a),None)

    #查找所有
    #正常查找
    def test_selectall1(self):
        a = Course(course_name="这是一个测试", course_type="sss", course_url="4399", platform_name="s")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertEqual(db.select_all_course()[0].course_name,a.course_name)
        #print(db.select_all_course()[0].id)
    #表为空
    def test_selectall2(self):
        self.assertEqual(db.select_all_course(), [])


if __name__=='__main__':
    unittest.main()