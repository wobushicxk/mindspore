from mindspore import context, ops
context.set_context(mode=context.GRAPH_MODE, device_target='CPU')

import mindspore.nn as nn
from mindspore import Tensor

