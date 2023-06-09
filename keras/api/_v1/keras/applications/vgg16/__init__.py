# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""VGG16 model for Keras.

Reference:
  - [Very Deep Convolutional Networks for Large-Scale Image Recognition]
    (https://arxiv.org/abs/1409.1556) (ICLR 2015)

"""

import sys as _sys

from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import preprocess_input
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.applications.vgg16", public_apis=None, deprecation=True,
      has_lite=False)