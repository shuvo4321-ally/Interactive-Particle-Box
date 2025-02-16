'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_depth_bounds_test'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_depth_bounds_test',error_checker=_errors._error_checker)
GL_DEPTH_BOUNDS_EXT=_C('GL_DEPTH_BOUNDS_EXT',0x8891)
GL_DEPTH_BOUNDS_TEST_EXT=_C('GL_DEPTH_BOUNDS_TEST_EXT',0x8890)
@_f
@_p.types(None,_cs.GLclampd,_cs.GLclampd)
def glDepthBoundsEXT(zmin,zmax):pass
