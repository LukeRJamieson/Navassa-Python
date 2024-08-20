import os
from adrv9001_python_wrappers import flags
flags.DEEP_PRINT = True
begin_transmitting_iq_data_2 = [ 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886, 29204, 0, 20650, 20650, 0, 29204, 44886, 20650, 36332, 0, 44886, 44886, 0, 36332, 20650, 44886  ]
