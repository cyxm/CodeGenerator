# !/usr/bin/python3


varTemplateViewHolder = """package {package_name};

import android.view.View;
{import_pack}

import {r_name};

public class {clz_name} {{
{vars}
    public {clz_name}(View v) {{
{finds}
    }}
}}"""

varTemplateViewHolderVariable = "\tpublic %s %s;\n"

varTemplateViewHolderStruct = "\t\t%s = v.findViewById(R.id.%s);\n"

varTemplateViewHolderImport = "import %s;\n"

var_map_clz_to_fullpath = {
    "Button": "android.widget.Button",
    "TextView": "android.widget.TextView",
    "SurfaceView": "android.view.SurfaceView",
    "EditText": "android.widget.EditText",
    "ListView": "android.widget.ListView",
    "LinearLayout": "android.widget.LinearLayout",
    "SeekBar": "android.widget.SeekBar",
    "Spinner": "android.widget.Spinner",
    "Switch": "android.widget.Switch"
}
