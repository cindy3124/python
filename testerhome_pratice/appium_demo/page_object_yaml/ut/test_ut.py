import yaml


# 测试yaml文件的加载
class TestYaml(object):
    def test_yaml(self):
        dict = yaml.load(open("../data/LoginPage.yaml", 'r'))
        print(dict)
        for step in dict["loginByPasswd"]:
            print(step['locator'])


