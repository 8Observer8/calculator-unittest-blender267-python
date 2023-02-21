bl_info = {
    "name": "Unit Testing",
    "category": "3D View"
}

import os, sys
import bpy
import unittest

filepath = bpy.context.space_data.text.filepath
dir = os.path.dirname(filepath)

class MyPanel(bpy.types.Panel):
    bl_label = "Testing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
    def draw(self, context):
        col = self.layout.column()
        col.operator("unit_tests.run", "Run Unit Tests")

class UnitTestOperator(bpy.types.Operator):
    bl_idname = "unit_tests.run"
    bl_label = "Run Unit Tests"
    bl_description = "This is a button to run unit tests"
    
    def execute(self, context):
        testsuite = unittest.TestLoader().discover(os.path.join(dir, "tests"), "test*.py")
        unittest.TextTestRunner(verbosity=1).run(testsuite)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(MyPanel)
    bpy.utils.register_class(UnitTestOperator)

def unregister():
    bpy.utils.unregister_class(MyPanel)
    bpy.utils.unregister_class(UnitTestOperator)

if __name__ == "__main__":
    register()
