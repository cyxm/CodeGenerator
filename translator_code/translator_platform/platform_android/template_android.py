# !/usr/bin/python3

varTemplateViewHolder = """class ViewHolder {
%s
    ViewHolder(View v) {
%s
    }
}"""

varTemplateViewHolderVariable = "\tpublic %s %s;\n"

varTemplateViewHolderStruct = "\t\t%s = v.findViewById(R.id.%s);\n"
