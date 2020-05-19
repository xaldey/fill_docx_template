from docxtpl import DocxTemplate
from datetime import datetime, date, time
date_stamp = datetime.today().strftime('%Y-%m-%d---%H-%M')
path_templates = 'templates'
name_template = 'test.docx'
results_path = 'results'
name_result_doc = str(date_stamp) + '_test.docx'
print(name_result_doc)
doc = DocxTemplate(path_templates + '/' + name_template)
context = { 'EMITENT' : 'ООО Ромашка', 'address1' : 'г. Москва, ул. Долгоруковская, д. 0', 'участник': 'ООО Участник',
            'адрес_участника': 'г. Москва, ул. Полевая, д. 0', 'director': 'И.И. Иванов'}
doc.render(context)
doc.save(results_path + '/' + name_result_doc)