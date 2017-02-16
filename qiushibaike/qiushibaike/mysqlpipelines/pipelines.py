from .sql import Sql
from qiushibaike.items import QiushibaikeItem

class QiushibaikePipeline(object):
    def process_item(self, item, spider):
        #deferToThread(self,process_item,item,spider)
        if isinstance(item,QiushibaikeItem):
            id = item['id']
            name = item['name']
            content = item['content']
            agreed_number = item['agreed_number']
            page_number = item['page_number']

            ret = Sql.select_id(id)
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                Sql.insert_item(id, name,content,agreed_number, page_number)
                print('存储完成了一个article！')


