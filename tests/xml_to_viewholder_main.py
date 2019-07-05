# !/usr/bin/python3


from codegen.translator_code.translator_platform.platform_android.xml_to_viewholder import *

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
        viewholderVar += template_android.varTemplateViewHolderVariable % (kv[1], kv[0])
        viewholderStruct += template_android.varTemplateViewHolderStruct % (kv[0], kv[0])
    if viewholderStruct.endswith("\n"):
        viewholderStruct = viewholderStruct[0:-1]

    # 生成类
    viewholderStr = template_android.varTemplateViewHolder.format(clz_name=vh_clz_name,
                                                                    vars=viewholderVar,
                                                                    finds=viewholderStruct)

    viewholderFilePath = os.path.join(target_path, vh_file_name)
    with open(viewholderFilePath, "w+") as vhFile:
        vhFile.writelines(viewholderStr)
        vhFile.flush()

    print("gen suc path=%s" % path)
