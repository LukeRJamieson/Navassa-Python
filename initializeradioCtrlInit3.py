import os
import adrv9001_python_wrappers.analog_devices_eval_client_adrv9001_board as adrv9001_board_types
import adrv9001_python_wrappers.analog_devices_eval_client_adrv9001_device as adrv9001_types
import adrv9001_python_wrappers.analog_devices_adrv9001_profile_types as adrv9001_profile_types
import adrv9001_python_wrappers.analog_devices_eval_client_fpga9001_device as fpga9001_types
from adrv9001_python_wrappers import flags
flags.DEEP_PRINT = True
initialize_radio_ctrl_init_gpio_ctrl_init_cfg_tx_ext_frontend_ctrl_3 = [adrv9001_types.adrv9001_GpioCfg_t()] * 2
initialize_radio_ctrl_init_gpio_ctrl_init_cfg_rx_ext_frontend_ctrl_3 = [adrv9001_types.adrv9001_GpioCfg_t()] * 2
initialize_radio_ctrl_init_gpio_ctrl_init_cfg_ext_pll_chip_enable_3 = [adrv9001_types.adrv9001_GpioCfg_t()] * 2
initialize_radio_ctrl_init_gpio_ctrl_init_cfg_vco_chip_enable_3 = [adrv9001_types.adrv9001_GpioCfg_t()] * 2
initialize_radio_ctrl_init_gpio_ctrl_init_cfg_ext_pll_lock_3 = [adrv9001_types.adrv9001_GpioCfg_t()] * 2
initialize_radio_ctrl_init_gpio_ctrl_init_cfg_channel_power_saving_3 = [adrv9001_types.adrv9001_GpioCfg_t()] * 2
initialize_radio_ctrl_init_gpio_ctrl_init_cfg_fh_update_rx_nco_3 = [adrv9001_types.adrv9001_GpioCfg_t()] * 2
initialize_radio_ctrl_init_gpio_ctrl_init_cfg_rx_interface_gain_seed_save_3 = [adrv9001_types.adrv9001_GpioCfg_t()] * 2
initialize_radio_ctrl_init_rx_carriers_val_3 = adrv9001_types.adrv9001_Carrier_t(
                                  adrv9001_types.adrv9001_LoGenOptimization_e.ADRV9001_LO_GEN_OPTIMIZATION_POWER_CONSUMPTION, 
                                  900000000, 0, adrv9001_profile_types.adrv9001_RxRfInputSel_e.ADRV9001_RX_A)
initialize_radio_ctrl_init_rx_carriers_3 = [initialize_radio_ctrl_init_rx_carriers_val_3] * 2
initialize_radio_ctrl_init_tx_carriers_val_3 = adrv9001_types.adrv9001_Carrier_t(
                                  adrv9001_types.adrv9001_LoGenOptimization_e.ADRV9001_LO_GEN_OPTIMIZATION_POWER_CONSUMPTION, 
                                  910000000, 0, adrv9001_profile_types.adrv9001_RxRfInputSel_e.ADRV9001_RX_A)
initialize_radio_ctrl_init_tx_carriers_3 = [initialize_radio_ctrl_init_tx_carriers_val_3] * 2
initialize_radio_ctrl_init_pll_config_val_3 = adrv9001_types.adrv9001_PllConfig_t(
                                    adrv9001_types.adrv9001_PllCalibration_e.ADRV9001_PLL_CALIBRATION_NORMAL, 
                                    adrv9001_types.adrv9001_PllPower_e.ADRV9001_PLL_POWER_LOW)
initialize_radio_ctrl_init_pll_config_3 = [initialize_radio_ctrl_init_pll_config_val_3] * 2
initialize_radio_ctrl_init_tx_dpd_init_val_model_orders_for_each_tap_3 = [ 31, 127, 31, 30  ]
initialize_radio_ctrl_init_tx_dpd_init_val_3 = adrv9001_types.adrv9001_DpdInitCfg_t(False, adrv9001_types.adrv9001_DpdAmplifier_e.ADRV9001_DPDAMPLIFIER_DEFAULT, 
                                     adrv9001_types.adrv9001_DpdLutSize_e.ADRV9001_DPDLUTSIZE_512, 
                                     adrv9001_types.adrv9001_DpdModel_e.ADRV9001_DPDMODEL_4, 
                                     False, initialize_radio_ctrl_init_tx_dpd_init_val_model_orders_for_each_tap_3, 
                                     8, 0)
initialize_radio_ctrl_init_tx_dpd_init_3 = [initialize_radio_ctrl_init_tx_dpd_init_val_3] * 2
initialize_radio_ctrl_init_rx_enable_delays_3 = [adrv9001_types.adrv9001_ChannelEnablementDelays_t()] * 2
initialize_radio_ctrl_init_tx_enable_delays_3 = [adrv9001_types.adrv9001_ChannelEnablementDelays_t()] * 2
initialize_radio_ctrl_init_fpga9001_ssi_config_rx_strobe_delay_3 = [19] * 2
initialize_radio_ctrl_init_fpga9001_ssi_config_rx_i_data_delay_3 = [19] * 2
initialize_radio_ctrl_init_fpga9001_ssi_config_rx_q_data_delay_3 = [19] * 2
initialize_radio_ctrl_init_fpga9001_ssi_config_tx_clk_delay_3 = [15] * 2
initialize_radio_ctrl_init_rx_mcs_delay_val_3 = adrv9001_types.adrv9001_McsDelay_t(1, 0)
initialize_radio_ctrl_init_rx_mcs_delay_3 = [initialize_radio_ctrl_init_rx_mcs_delay_val_3] * 2
initialize_radio_ctrl_init_tx_mcs_delay_val_3 = adrv9001_types.adrv9001_McsDelay_t(5, 0)
initialize_radio_ctrl_init_tx_mcs_delay_3 = [initialize_radio_ctrl_init_tx_mcs_delay_val_3] * 2
initialize_radio_ctrl_init_rf_pll_loop_filter_cfg_3 = [adrv9001_types.adrv9001_PllLoopFilterCfg_t()] * 2
initialize_radio_ctrl_init_rx_portswitch_config_3 = adrv9001_types.adrv9001_RxPortSwitchCfg_t(890000000, 910000000, 1890000000, 1910000000, 
                                          False, False)
initialize_radio_ctrl_init_3 = adrv9001_board_types.adrv9001_RadioCtrlInit_t(
                                              adrv9001_types.adrv9001_DeviceClockDivisor_e.ADRV9001_DEVICECLOCKDIVISOR_2, 
                                              adrv9001_types.adrv9001_GpioCtrlInitCfg_t(
                                          initialize_radio_ctrl_init_gpio_ctrl_init_cfg_tx_ext_frontend_ctrl_3, 
                                          initialize_radio_ctrl_init_gpio_ctrl_init_cfg_rx_ext_frontend_ctrl_3, 
                                          initialize_radio_ctrl_init_gpio_ctrl_init_cfg_ext_pll_chip_enable_3, 
                                          initialize_radio_ctrl_init_gpio_ctrl_init_cfg_vco_chip_enable_3, 
                                          initialize_radio_ctrl_init_gpio_ctrl_init_cfg_ext_pll_lock_3, 
                                          initialize_radio_ctrl_init_gpio_ctrl_init_cfg_channel_power_saving_3, 
                                          adrv9001_types.adrv9001_GpioCfg_t(
                                  adrv9001_types.adrv9001_GpioPin_e.ADRV9001_GPIO_UNASSIGNED, 
                                  adrv9001_types.adrv9001_GpioPolarity_e.ADRV9001_GPIO_POLARITY_NORMAL, 
                                  adrv9001_types.adrv9001_GpioMaster_e.ADRV9001_GPIO_MASTER_BBIC), 
                                          adrv9001_types.adrv9001_GpioCfg_t(
                                  adrv9001_types.adrv9001_GpioPin_e.ADRV9001_GPIO_UNASSIGNED, 
                                  adrv9001_types.adrv9001_GpioPolarity_e.ADRV9001_GPIO_POLARITY_NORMAL, 
                                  adrv9001_types.adrv9001_GpioMaster_e.ADRV9001_GPIO_MASTER_BBIC), 
                                          initialize_radio_ctrl_init_gpio_ctrl_init_cfg_fh_update_rx_nco_3, 
                                          initialize_radio_ctrl_init_gpio_ctrl_init_cfg_rx_interface_gain_seed_save_3), 
                                              adrv9001_types.adrv9001_SlewRateLimiterCfg_t(False, False, adrv9001_types.adrv9001_SrlTableSel_e.ADRV9001_SRL_TABLE0, 
                                             0, adrv9001_types.adrv9001_SrlStatisticsMode_e.ADRV9001_SRL_STATISTICS_MIN_SLEW_FACTOR_OBSERVED), 
                                              initialize_radio_ctrl_init_rx_carriers_3, 
                                              initialize_radio_ctrl_init_tx_carriers_3, 
                                              initialize_radio_ctrl_init_pll_config_3, 
                                              [False] * 2, initialize_radio_ctrl_init_tx_dpd_init_3, 
                                              initialize_radio_ctrl_init_rx_enable_delays_3, 
                                              initialize_radio_ctrl_init_tx_enable_delays_3, 
                                              adrv9001_types.adrv9001_SsiCalibrationCfg_t([0] * 2, [0] * 2, [0] * 2, [0] * 2, [0] * 2, [0] * 2, 
                                            [0] * 2, [0] * 2, [0] * 2), 
                                              fpga9001_types.fpga9001_SsiCalibrationCfg_t(
                                            initialize_radio_ctrl_init_fpga9001_ssi_config_rx_strobe_delay_3, 
                                            initialize_radio_ctrl_init_fpga9001_ssi_config_rx_i_data_delay_3, 
                                            initialize_radio_ctrl_init_fpga9001_ssi_config_rx_q_data_delay_3, 
                                            initialize_radio_ctrl_init_fpga9001_ssi_config_tx_clk_delay_3, 
                                            [0] * 2, [0] * 2, [0] * 2, [False] * 2), 
                                              [0] * 2, [False] * 2, adrv9001_types.adrv9001_PowerManagementSettings_t(
                                                  [adrv9001_types.adrv9001_LdoPowerSavingMode_e(0)] * 19), 
                                              adrv9001_types.adrv9001_PowerSavingAndMonitorMode_MonitorModeInitCfg_t(
                                                                       adrv9001_types.adrv9001_PowerSavingAndMonitorMode_MonitorModeRssiCfg_t(4, 1, -80000, 10), 
                                                                       adrv9001_types.adrv9001_PowerSavingAndMonitorMode_MonitorModeDmrSearchCfg_t(0, 250, 
                                                                            375, 500, 
                                                                            880000)), 
                                              [adrv9001_types.adrv9001_SsiPowerDown_e(0)] * 2, 
                                              [adrv9001_types.adrv9001_SsiPowerDown_e(0)] * 2, 
                                              initialize_radio_ctrl_init_rx_mcs_delay_3, 
                                              initialize_radio_ctrl_init_tx_mcs_delay_3, 
                                              initialize_radio_ctrl_init_rf_pll_loop_filter_cfg_3, 
                                              initialize_radio_ctrl_init_rx_portswitch_config_3)
