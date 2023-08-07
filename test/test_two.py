import unittest

from sqlalchemy import inspect

from model import ResumeSend, ResumeSendBasic


class TestTwo(unittest.TestCase):

    def test_cls_method(self):
        d = {"a": "4", "m": 45}
        # print(d.keys())
        # print(ResumeSend.get_columns())
        # resumeSendBasic = ResumeSendBasic(cname='412', mguid='123456', salary=12)
        # print(resumeSendBasic.model_dump(include=ResumeSend.get_columns()))
        resume_send = ResumeSend()
        setattr(resume_send, 'cname', 'test')
        # resume_send['cname'] = 'test'
        print(resume_send.cname)

    def test_cls(self):
        # ResumeSend.get_cls()
        # resume_send1 = ResumeSend(cname='12', mguid='123', jobname='python', salary=100)
        # resume_send1.equal("salary", 15)
        # resume_send1.like("cname", 'test')
        # print(resume_send1.get_sql_list())
        # print(ResumeSend.cname)
        # print(resume_send1.__table__.primary_key.columns)
        inspector = inspect(ResumeSend)
        print(inspector.primary_key, type(inspector.primary_key[0]), *inspector.primary_key)
        print(inspector, inspector.columns)

    def test_init(self):
        resume_send1 = ResumeSend(cname='12', mguid='123', jobname='python', salary=100)
        print('cname', resume_send1.cname)
        print(resume_send1.__table__.columns)
        resume_send1.equal(resume_send1.cname, '12')
        resume_send1.cname = '15'
        resume_send2 = ResumeSend(cname='22')
        print('cname', resume_send1.cname, resume_send2.cname)
        print('_equal_conditions', resume_send1._equal_conditions, resume_send2._equal_conditions)

    def test_table(self):
        resume_send = ResumeSend(cname='12', mguid='123', jobname='python', salary=100)
        c = resume_send.__table__.columns
        print(resume_send.cname, type(c))
        print(type(resume_send.cname))
        # column = getattr(resume_send, 'salary')
        # print(column)
        resume_send.equal(ResumeSend.salary, 100)
        resume_send.like(ResumeSend.jobname, 'python')
        conditions = resume_send.where_condition()
        sql = resume_send.get_sql_select()
        print(conditions)
        print(sql)
        print(resume_send.get_sql_list(currentPage=1, pagesize=10))
