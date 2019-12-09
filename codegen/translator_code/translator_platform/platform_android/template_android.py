# !/usr/bin/python3


varTemplateViewHolder = """class {clz_name} {{
{vars}
    {clz_name}(View v) {{
{finds}
    }}
}}"""

varTemplateViewHolderVariable = "\tpublic %s %s;\n"

varTemplateViewHolderStruct = "\t\t%s = v.findViewById(R.id.%s);\n"
