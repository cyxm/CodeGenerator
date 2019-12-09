# !/usr/bin/python3

import sys
import os

from xml.sax import *
from . import template_android


class AndroidLayoutHandler(ContentHandler):

    def __init__(self):
        super().__init__()
        self.idTypeList = {}

    def startElement(self, name, attrs):
        if attrs.get("android:id"):
            widget_id = attrs["android:id"].split("/")[1]
            if self.idTypeList.get(widget_id):
                print("控件ID重复 ID=%s" % widget_id)
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
    ori_path = sys.argv[1]
    target_path = sys.argv[2]

    validPath = []
    for file in os.listdir(ori_path):
        if not file.endswith(".xml"):
            continue
        fullPath = os.path.join(ori_path, file)
        if os.path.isfile(fullPath):
            validPath.append(fullPath)

    xml_trans = XmlTrans()

    for path in validPath:
        # 解析
        handler = AndroidLayoutHandler()
        xml_trans.set_sax_handler(handler)
        xml_trans.sax_parse(path)

        # 获取解析数据
        data = handler.get_data()

        # 处理名称
        fileName = os.path.basename(path)
        file_name_without_suffix = fileName.split(".")[0]
        file_name_list = file_name_without_suffix.split("_")
        viewholder_name = ""
        for part in file_name_list:
            if part == "activity" or part == "frag" or part == "fragment":
                continue
            viewholder_name += part.title()
        vh_clz_name = "Vh" + viewholder_name
        vh_file_name = vh_clz_name + ".java"

        # 生成变量字符串和构造字符串
        viewholderVar = ""
        viewholderStruct = ""
        for kv in data.items():
            viewholderVar += template_android.varTemplateViewHolderVariable % (
                kv[1], kv[0])
            viewholderStruct += template_android.varTemplateViewHolderStruct % (
                kv[0], kv[0])
        if viewholderStruct.endswith("\n"):
            viewholderStruct = viewholderStruct[0:-1]

        # 生成类
        viewholderStr = template_android.varTemplateViewHolder.format(
            clz_name=vh_clz_name,
            vars=viewholderVar,
            finds=viewholderStruct)

        viewholderFilePath = os.path.join(target_path, vh_file_name)
        with open(viewholderFilePath, "w+") as vhFile:
            vhFile.writelines(viewholderStr)
            vhFile.flush()

        print("gen suc path=%s" % path)
