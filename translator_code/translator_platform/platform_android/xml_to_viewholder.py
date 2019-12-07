# !/usr/bin/python3

# coding=utf-8

from xml.sax import *
from translator_code.translator_platform.platform_android import template_android

import os
import sys


class AndroidLayoutHandler(ContentHandler):
    idTypeList = {}

    def startElement(self, name, attrs):
        if attrs.get("android:id"):
            widget_id = attrs["android:id"].split("/")[1]
            if self.idTypeList.get(widget_id):
                print("控件ID重复")
                pass
            else:
                self.idTypeList[widget_id] = name
            pass
        pass

    def get_data(self):
        return self.idTypeList


class XmlTrans:

    def __init__(self):
        self.xml_parser = make_parser()
        self.xml_parser.setFeature(handler.feature_namespaces, 0)
        pass

    def set_sax_handler(self, sax_handler):
        self.xml_parser.setContentHandler(sax_handler)
        pass

    def sax_parse(self, file_path):
        self.xml_parser.parse(file_path)
        pass


if __name__ == '__main__':
    ori_path = sys.argv[0]
    target_path = sys.argv[1]
    print(ori_path)

    xml_trans = XmlTrans()

    handler = AndroidLayoutHandler()
    xml_trans.set_sax_handler(handler)

    walkpath = "e:/test"
    for root, dirs, files in os.walk(walkpath):
        # 遍历文件
        for f in files:
            print(os.path.join(root, f))

        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))

    varAndroidResXmlPath = r"e:\test\activity_template_login.xml"
    xml_trans.sax_parse(varAndroidResXmlPath)

    # 获取解析数据
    data = handler.get_data()
    # 生成变量字符串和构造字符串
    viewholderVar = ""
    viewholderStruct = ""
    for kv in data.items():
        viewholderVar += template_android.varTemplateViewHolderVariable % (kv[1], kv[0])
        viewholderStruct += template_android.varTemplateViewHolderStruct % (kv[0], kv[0])

    # 生成类
    viewholderStr = template_android.varTemplateViewHolder % (viewholderVar, viewholderStruct)

    viewholderFilePath = r"e:/test/ViewHolder.java"
    with open(viewholderFilePath, "w+") as vhFile:
        vhFile.writelines(viewholderStr)
    pass
