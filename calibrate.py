# This file contains code automatically generated by a machine.
# It has not been independently verified by any human.
# The generation process is deterministic and tested (not generative AI),
# but not every scenario or risk has been captured in unit tests.
# All code is provided as-is for example purposes only.
# The customer assumes all risks related to the use of this code.


# 
# Silicon Revision: Presumed C0
# 
# Tx / Rx optimal carrier frequencies: 30 MHz to 6 GHz
# External LO optimal frequencies: 60 MHz to 12 GHz
# 
# FPGA: v0.0.0
# Device Driver API: v0.0.0
# Device Driver Client: v68.13.7
# Firmware: v0.22.30
# Profile Generator: v0.53.6.0
# Stream Generator Assembly: v0.7.11.0
# Transceiver Evaluation Software: v0.26.0
# ADRV9001 Plugin: v0.26.0

import os
import adrv9001_python_wrappers.analog_devices_adrv9001_profile_types as adrv9001_profile_types
import adrv9001_python_wrappers.analog_devices_eval_client_adrv9001_device as adrv9001_types
from adrv9001_python_wrappers import flags
flags.DEEP_PRINT = True


def build_str_buff(size, s):
	buff = [0] * size
	ba = bytearray(s, 'utf8')
	for i, v in enumerate(ba):
		buff[i] = v
	return buff



def calibrate(adrv9001_device_0: adrv9001_types.Adrv9001Device):
	input("Preparing to calibrate. Turn your signal source OFF, then press Enter.")

	init_cals_chan_init_cal_mask_1 = [adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_TX_QEC | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_TX_LO_LEAKAGE | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_TX_LB_PD | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_TX_BBAF | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_TX_BBAF_GD | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_TX_ATTEN_DELAY | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_TX_DAC | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_TX_PATH_DELAY | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_RX_HPADC_FLASH | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_RX_LPADC | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_RX_TIA_CUTOFF | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_RX_GROUP_DELAY | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_RX_QEC_FIC | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_RX_RF_DC_OFFSET | adrv9001_profile_types.adrv9001_InitCalibrations_e.ADRV9001_INIT_CAL_RX_GAIN_PATH_DELAY] * 2
	init_cals_1 = adrv9001_profile_types.adrv9001_InitCals_t(
                                           adrv9001_profile_types.adrv9001_InitCalibrations_e(0), 
                                           init_cals_chan_init_cal_mask_1, adrv9001_profile_types.adrv9001_InitCalMode_e.ADRV9001_INIT_CAL_MODE_ALL, 
                                           False)
	error_flag_1 = 0
	error_code, error_flag_1 = adrv9001_device_0.cals.InitCals_Run(init_cals_1, 300000, 
                                                                error_flag_1)

	read_data_2 = 0
	error_code, read_data_2 = adrv9001_device_0.spi.Byte_Read(11, read_data_2)

	print("Byte_Read parameter 'readData' read back as '" + str(read_data_2) + "'\n")

	internal_path_delays_ns_3 = [0] * 6
	error_code, internal_path_delays_ns_3 = adrv9001_device_0.cals.InternalPathDelay_Get(
                                                                                      adrv9001_types.common_Port_e.TX, 
                                                                                      adrv9001_types.common_ChannelNumber_e.CHANNEL_1, 
                                                                                      internal_path_delays_ns_3, 
                                                                                      6)

	printStr = "[ " + "\n" + str(internal_path_delays_ns_3[0])
	for internal_path_delays_ns_3_indexer in range(1, 6):
		printStr = printStr + ", " + "\n" + str(internal_path_delays_ns_3[internal_path_delays_ns_3_indexer])

	printStr = printStr + " ]"
	print("InternalPathDelay_Get parameter 'internalPathDelays_ns' read back as '" + printStr + "'\n")

	internal_path_delays_ns_4 = [0] * 6
	error_code, internal_path_delays_ns_4 = adrv9001_device_0.cals.InternalPathDelay_Get(
                                                                                      adrv9001_types.common_Port_e.TX, 
                                                                                      adrv9001_types.common_ChannelNumber_e.CHANNEL_2, 
                                                                                      internal_path_delays_ns_4, 
                                                                                      6)

	printStr = "[ " + "\n" + str(internal_path_delays_ns_4[0])
	for internal_path_delays_ns_4_indexer in range(1, 6):
		printStr = printStr + ", " + "\n" + str(internal_path_delays_ns_4[internal_path_delays_ns_4_indexer])

	printStr = printStr + " ]"
	print("InternalPathDelay_Get parameter 'internalPathDelays_ns' read back as '" + printStr + "'\n")

	error_code = adrv9001_device_0.tx.DataPath_Loopback_Set(
                                                         adrv9001_types.common_ChannelNumber_e.CHANNEL_1, 
                                                         False)

	error_code = adrv9001_device_0.ssi.Loopback_Set(
                                                 adrv9001_types.common_ChannelNumber_e.CHANNEL_1, 
                                                 adrv9001_profile_types.adrv9001_SsiType_e.ADRV9001_SSI_TYPE_LVDS, 
                                                 False)

	error_code = adrv9001_device_0.tx.DataPath_Loopback_Set(
                                                         adrv9001_types.common_ChannelNumber_e.CHANNEL_2, 
                                                         False)

	error_code = adrv9001_device_0.ssi.Loopback_Set(
                                                 adrv9001_types.common_ChannelNumber_e.CHANNEL_2, 
                                                 adrv9001_profile_types.adrv9001_SsiType_e.ADRV9001_SSI_TYPE_LVDS, 
                                                 False)

	error_code = adrv9001_device_0.auxdac.Configure(
                                                 adrv9001_types.adrv9001_AuxDac_e.ADRV9001_AUXDAC0, 
                                                 False)

	error_code = adrv9001_device_0.auxdac.Configure(
                                                 adrv9001_types.adrv9001_AuxDac_e.ADRV9001_AUXDAC1, 
                                                 False)

	error_code = adrv9001_device_0.auxdac.Configure(
                                                 adrv9001_types.adrv9001_AuxDac_e.ADRV9001_AUXDAC2, 
                                                 False)

	error_code = adrv9001_device_0.auxdac.Configure(
                                                 adrv9001_types.adrv9001_AuxDac_e.ADRV9001_AUXDAC3, 
                                                 False)

	print("Calibrations complete.")

