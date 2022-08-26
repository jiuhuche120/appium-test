import os

import pytest

reports_json_path = os.path.join(os.path.dirname(__file__), 'reports/json_reports')
reports_html_path = os.path.join(os.path.dirname(__file__), 'reports/html_reports')
if __name__ == '__main__':
    # --clean-alluredir 每次执行之前删除上一次的json文件
    pytest.main(['-s', '-v', '--alluredir=%s' % reports_json_path, '--clean-alluredir'])
    # 　执行命令，将json文件转换成html报告输出
    os.system('allure generate %s -o %s --clean' % (reports_json_path, reports_html_path))
