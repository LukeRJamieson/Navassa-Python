from beginTransmittingiqData2 import *
from beginTransmittingiqData4 import *
import numpy as np

import adrv9001_python_wrappers.analog_devices_eval_client_adrv9001_device as adrv9001_types
import adrv9001_python_wrappers.analog_devices_eval_client_fpga9001_device as fpga9001_types
from adrv9001_python_wrappers import flags

def beamForm(adrv9001_device_0: adrv9001_types.Adrv9001Device, fpga9001_device_0: fpga9001_types.Fpga9001Device, phase_delay, phase_cal):
    phaseShiftedArray = begin_transmitting_iq_data_2 * np.exp(1j*np.deg2rad(phase_delay+phase_cal))

    error_code, phaseShiftedArray = fpga9001_device_0.dataChain.Data_Set_16IQInterleaved(
                                                                                        adrv9001_types.common_Port_e.TX, 
                                                                                        adrv9001_types.common_ChannelNumber_e.CHANNEL_1, 
                                                                                        phaseShiftedArray, 
                                                                                        2048)