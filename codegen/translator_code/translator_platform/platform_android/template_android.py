# !/usr/bin/python3


varTemplateViewHolder = """package {package_name};

import android.view.View;
{import_pack}

import {r_name};

public class {clz_name} {{

    public static int LAYOUT_RES = R.layout.{res};

{vars}
    public {clz_name}(View v) {{
{finds}
    }}
}}"""

varTemplateViewHolderForRecycle = """package {package_name};

import android.view.View;
import com.chad.library.adapter.base.BaseViewHolder;
{import_pack}

import {r_name};

public class {clz_name} extends BaseViewHolder {{
{vars}
    public {clz_name}(View v) {{
        super(v);
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
    "SeekBar": "android.widget.SeekBar",
    "Spinner": "android.widget.Spinner",
    "Switch": "android.widget.Switch",
    "LinearLayout": "android.widget.LinearLayout",
    "FrameLayout": "android.widget.FrameLayout"
}
