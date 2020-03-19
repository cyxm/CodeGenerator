# !/usr/bin/python3

import sys
import os

from xml.sax import *
from codegen.translator_code.translator_platform.platform_android import template_android


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


def main():
    arg_length = len(sys.argv)
    if arg_length != 5:
        print("args length error,expect 4")
        return
    ori_path = sys.argv[1]
    target_path = sys.argv[2]

    package_name = sys.argv[3]
    r_name = sys.argv[4]

    validPath = []
    for file in os.listdir(ori_path):
        if not file.endswith(".xml"):
            continue
        fullPath = os.path.join(ori_path, file)
        if os.path.isfile(fullPath):
            validPath.append(fullPath)

    xml_trans = XmlTrans()

    for path in validPath:
        print("start gen path=%s" % path)
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
        str_template = template_android.varTemplateViewHolder
        for part in file_name_list:
            if part == "layout" or part == "page":
                continue
            elif part == "item":
                str_template = template_android.varTemplateViewHolderForRecycle
            viewholder_name += part.capitalize()
        vh_clz_name = "Vh" + viewholder_name
        vh_file_name = vh_clz_name + ".java"

        # 生成变量字符串和构造字符串
        viewholderVar = ""
        viewholderStruct = ""
        for kv in data.items():
            dot_index = kv[1].rfind(".")
            if dot_index >= 0:
                simple_name = kv[1][dot_index + 1:]
                viewholderVar += template_android.varTemplateViewHolderVariable % (
                    simple_name, kv[0])
            else:
                viewholderVar += template_android.varTemplateViewHolderVariable % (
                    kv[1], kv[0])

            viewholderStruct += template_android.varTemplateViewHolderStruct % (
                kv[0], kv[0])
        if viewholderStruct.endswith("\n"):
            viewholderStruct = viewholderStruct[0:-1]

        # 生成import包
        varImportSet = set(data.values())
        import_pack = ""
        print(varImportSet)
        for v in varImportSet:
            if v.find(".") >= 0:
                import_pack += template_android.varTemplateViewHolderImport % v
            else:
                import_pack += template_android.varTemplateViewHolderImport % \
                               template_android.var_map_clz_to_fullpath[v]

        if import_pack.endswith("\n"):
            import_pack = import_pack[0:-1]

        # 生成类
        viewholder_str = str_template.format(
            package_name=package_name,
            r_name=r_name,
            import_pack=import_pack,
            clz_name=vh_clz_name,
            res=file_name_without_suffix,
            vars=viewholderVar,
            finds=viewholderStruct)

        viewholderFilePath = os.path.join(target_path, vh_file_name)
        with open(viewholderFilePath, "w+") as vhFile:
            vhFile.writelines(viewholder_str)
            vhFile.flush()

        print("gen suc path=%s" % path)


if __name__ == '__main__':
    main()
