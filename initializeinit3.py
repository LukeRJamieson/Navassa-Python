import os
import adrv9001_python_wrappers.analog_devices_adrv9001_profile_types as adrv9001_profile_types
from adrv9001_python_wrappers import flags
flags.DEEP_PRINT = True
initialize_init_clocks_3 = adrv9001_profile_types.adrv9001_ClockSettings_t(38400, 442368000, adrv9001_profile_types.adrv9001_HsDiv_e.ADRV9001_HSDIV_4, 
                                                adrv9001_profile_types.adrv9001_ClkPllMode_e.ADRV9001_CLK_PLL_LP_MODE, 
                                                adrv9001_profile_types.adrv9001_InternalClock_Divisor_e.ADRV9001_INTERNAL_CLOCK_DIV_2, 
                                                adrv9001_profile_types.adrv9001_InternalClock_Divisor_e.ADRV9001_INTERNAL_CLOCK_DIV_6, 
                                                1, True, adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_HIGH, 
                                                adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_HIGH, 
                                                0, 0, 0, adrv9001_profile_types.adrv9001_PllLoMode_e.ADRV9001_INT_LO1 | adrv9001_profile_types.adrv9001_PllLoMode_e.ADRV9001_INT_LO2, 
                                                adrv9001_profile_types.adrv9001_PllLoMode_e.ADRV9001_INT_LO1 | adrv9001_profile_types.adrv9001_PllLoMode_e.ADRV9001_INT_LO2, 
                                                adrv9001_profile_types.adrv9001_ExtLoType_e.ADRV9001_EXT_LO_DIFFERENTIAL, 
                                                adrv9001_profile_types.adrv9001_ExtLoType_e.ADRV9001_EXT_LO_DIFFERENTIAL, 
                                                adrv9001_profile_types.adrv9001_RxRfInputSel_e.ADRV9001_RX_A, 
                                                adrv9001_profile_types.adrv9001_RxRfInputSel_e.ADRV9001_RX_A, 
                                                2, 2, adrv9001_profile_types.adrv9001_RfPllMcs_e.ADRV9001_RFPLLMCS_NOSYNC, 
                                                adrv9001_profile_types.adrv9001_LoSel_e.ADRV9001_LOSEL_LO1, 
                                                adrv9001_profile_types.adrv9001_LoSel_e.ADRV9001_LOSEL_LO1, 
                                                adrv9001_profile_types.adrv9001_LoSel_e.ADRV9001_LOSEL_LO1, 
                                                adrv9001_profile_types.adrv9001_LoSel_e.ADRV9001_LOSEL_LO1, 
                                                adrv9001_profile_types.adrv9001_LoDividerMode_e.ADRV9001_LO_DIV_MODE_LOW_POWER, 
                                                adrv9001_profile_types.adrv9001_LoDividerMode_e.ADRV9001_LO_DIV_MODE_LOW_POWER, 
                                                adrv9001_profile_types.adrv9001_LoDividerMode_e.ADRV9001_LO_DIV_MODE_LOW_POWER, 
                                                adrv9001_profile_types.adrv9001_LoDividerMode_e.ADRV9001_LO_DIV_MODE_LOW_POWER, 
                                                adrv9001_profile_types.adrv9001_LoGenPower_e.ADRV9001_LOGENPOWER_RFPLL_LDO, 
                                                adrv9001_profile_types.adrv9001_LoGenPower_e.ADRV9001_LOGENPOWER_RFPLL_LDO)
initialize_init_rx_rx_channel_cfg_3 = [adrv9001_profile_types.adrv9001_RxChannelCfg_t(None)] * 8
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_gain_comp9_gain_i_0 = [16384] * 6
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_0 = adrv9001_profile_types.adrv9001_RxSincHbTop_t(
                                              adrv9001_profile_types.adrv9001_RxSincGainMuxOutput_e.ADRV9001_RX_SINC_GAIN_MUX_6_DB, 
                                              adrv9001_profile_types.adrv9001_RxSincMux5Output_e.ADRV9001_RX_SINC_MUX5_OUTPUT_ZERO, 
                                              adrv9001_profile_types.adrv9001_RxHBMuxOutput_e.ADRV9001_RX_HB_MUX_OUTPUT_HB1, 
                                              0, initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_gain_comp9_gain_i_0, 
                                              [0] * 6)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_0 = adrv9001_profile_types.adrv9001_RxNbDemConfig_t(
                                                adrv9001_profile_types.adrv9001_RxDpInFifoConfig_t(0, adrv9001_profile_types.adrv9001_RxDpInFifoMode_e.ADRV9001_DP_IN_FIFO_MODE_DETECTING, 
                                                   adrv9001_profile_types.adrv9001_RxDpInFifoInputSel_e.ADRV9001_DP_IN_FIFO_INPUT_DP_SEL), 
                                                adrv9001_profile_types.adrv9001_RxNbNcoConfig_t(0, adrv9001_profile_types.adrv9001_NcoDpConfig_t(0, 0, 0, 0)), 
                                                adrv9001_profile_types.adrv9001_RxWbNbCompPFir_t(
                                                 adrv9001_profile_types.adrv9001_PfirBank_e.ADRV9001_PFIR_BANK_A, 
                                                 adrv9001_profile_types.adrv9001_RxPfirInMuxSel_e.ADRV9001_RP_FIR_IN_MUX_INT_IN, 
                                                 0), 
                                                adrv9001_profile_types.adrv9001_RxResampConfig_t(0, 0, 0), 
                                                adrv9001_profile_types.adrv9001_RxGsOutMuxSel_e.ADRV9001_GS_OUT_MUX_BYPASS, 
                                                adrv9001_profile_types.adrv9001_RxOutSel_e.ADRV9001_RX_OUT_IQ_SEL, 
                                                adrv9001_profile_types.adrv9001_RxRoundMode_e.ADRV9001_RX_ROUNDMODE_IQ, 
                                                adrv9001_profile_types.adrv9001_RxDpArmSel_e.ADRV9001_DP_SEL)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_0 = adrv9001_profile_types.adrv9001_RxDpProfile_t(
                                              adrv9001_profile_types.adrv9001_RxNbDecTop_t(0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                                              adrv9001_profile_types.adrv9001_RxWbDecTop_t(0, 0, 0, 0, 0, 0), 
                                              adrv9001_profile_types.adrv9001_RxDecTop_t(0, 0, 0, 0, 0), 
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_0, 
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_0)
initialize_init_rx_rx_channel_cfg_3_profile_0 = adrv9001_profile_types.adrv9001_RxProfile_t(12500, 0, 0, 0, False, adrv9001_profile_types.adrv9001_RxSignalType_e.ADRV9001_RX_IQ, 
                                            1, 1, 0, 0, 0, 0, 0, adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_HIGH, 
                                            adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_HIGH, 
                                            0, adrv9001_profile_types.adrv9001_AdcType_e.ADRV9001_ADC_HP, 
                                            adrv9001_profile_types.adrv9001_Adc_LowPower_CalMode_e.ADRV9001_ADC_LOWPOWER_PERIODIC, 
                                            adrv9001_profile_types.adrv9001_RxGainTableType_e.ADRV9001_RX_GAIN_CORRECTION_TABLE, 
                                            initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_0, 
                                            adrv9001_profile_types.adrv9001_RxLnaConfig_t(False, adrv9001_profile_types.adrv9001_GpioAnalogPinNibbleSel_e.ADRV9001_GPIO_ANALOG_PIN_NIBBLE_UNASSIGNED, 
                                              adrv9001_profile_types.adrv9001_ExternalLnaPinSel_e.ADRV9001_EXTERNAL_LNA_PIN_RX1_LOWER_RX2_UPPER, 
                                              0, 0, [0] * 4, 0, 0, adrv9001_profile_types.adrv9001_ExternalLnaType_e.ADRV9001_EXTERNAL_LNA_TYPE_SINGLE), 
                                            adrv9001_profile_types.adrv9001_SsiConfig_t(
                                            adrv9001_profile_types.adrv9001_SsiType_e.ADRV9001_SSI_TYPE_DISABLE, 
                                            adrv9001_profile_types.adrv9001_SsiDataFormat_e.ADRV9001_SSI_FORMAT_2_BIT_SYMBOL_DATA, 
                                            adrv9001_profile_types.adrv9001_SsiNumLane_e.ADRV9001_SSI_1_LANE, 
                                            adrv9001_profile_types.adrv9001_SsiStrobeType_e.ADRV9001_SSI_SHORT_STROBE, 
                                            0, 0, adrv9001_profile_types.adrv9001_SsiTxRefClockPin_e.ADRV9001_SSI_TX_REF_CLOCK_PIN_DISABLED, 
                                            False, False, False, 0, False, False, False, False, 
                                            False))
initialize_init_rx_rx_channel_cfg_3[0] = adrv9001_profile_types.adrv9001_RxChannelCfg_t(
                                               initialize_init_rx_rx_channel_cfg_3_profile_0)
initialize_init_rx_rx_channel_cfg_3[1] = adrv9001_profile_types.adrv9001_RxChannelCfg_t(
                                               initialize_init_rx_rx_channel_cfg_3_profile_0)
initialize_init_rx_rx_channel_cfg_3[2] = adrv9001_profile_types.adrv9001_RxChannelCfg_t(
                                               initialize_init_rx_rx_channel_cfg_3_profile_0)
initialize_init_rx_rx_channel_cfg_3[3] = adrv9001_profile_types.adrv9001_RxChannelCfg_t(
                                               initialize_init_rx_rx_channel_cfg_3_profile_0)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dec_top_4 = adrv9001_profile_types.adrv9001_RxNbDecTop_t(1, 10, 0, 1, 1, 1, 1, 1, 1, 1)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_dec_top_4 = adrv9001_profile_types.adrv9001_RxDecTop_t(0, 1, 0, 1, 0)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_gain_comp9_gain_i_4 = [16384] * 6
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_4 = adrv9001_profile_types.adrv9001_RxSincHbTop_t(
                                              adrv9001_profile_types.adrv9001_RxSincGainMuxOutput_e.ADRV9001_RX_SINC_GAIN_MUX_6_DB, 
                                              adrv9001_profile_types.adrv9001_RxSincMux5Output_e.ADRV9001_RX_SINC_MUX5_OUTPUT_SINC3, 
                                              adrv9001_profile_types.adrv9001_RxHBMuxOutput_e.ADRV9001_RX_HB_MUX_OUTPUT_HB1, 
                                              0, initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_gain_comp9_gain_i_4, 
                                              [0] * 6)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_rx_wb_nb_comp_p_fir_4 = adrv9001_profile_types.adrv9001_RxWbNbCompPFir_t(
                                                 adrv9001_profile_types.adrv9001_PfirBank_e.ADRV9001_PFIR_BANK_B, 
                                                 adrv9001_profile_types.adrv9001_RxPfirInMuxSel_e.ADRV9001_RP_FIR_IN_MUX_INT_IN, 
                                                 0)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_4 = adrv9001_profile_types.adrv9001_RxNbDemConfig_t(
                                                adrv9001_profile_types.adrv9001_RxDpInFifoConfig_t(0, adrv9001_profile_types.adrv9001_RxDpInFifoMode_e.ADRV9001_DP_IN_FIFO_MODE_DETECTING, 
                                                   adrv9001_profile_types.adrv9001_RxDpInFifoInputSel_e.ADRV9001_DP_IN_FIFO_INPUT_DP_SEL), 
                                                adrv9001_profile_types.adrv9001_RxNbNcoConfig_t(0, adrv9001_profile_types.adrv9001_NcoDpConfig_t(0, 0, 0, 0)), 
                                                initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_rx_wb_nb_comp_p_fir_4, 
                                                adrv9001_profile_types.adrv9001_RxResampConfig_t(0, 0, 0), 
                                                adrv9001_profile_types.adrv9001_RxGsOutMuxSel_e.ADRV9001_GS_OUT_MUX_BYPASS, 
                                                adrv9001_profile_types.adrv9001_RxOutSel_e.ADRV9001_RX_OUT_IQ_SEL, 
                                                adrv9001_profile_types.adrv9001_RxRoundMode_e.ADRV9001_RX_ROUNDMODE_IQ, 
                                                adrv9001_profile_types.adrv9001_RxDpArmSel_e.ADRV9001_DP_SEL)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_4 = adrv9001_profile_types.adrv9001_RxDpProfile_t(
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dec_top_4, 
                                              adrv9001_profile_types.adrv9001_RxWbDecTop_t(0, 0, 0, 0, 0, 0), 
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_dec_top_4, 
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_4, 
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_4)
initialize_init_rx_rx_channel_cfg_3_profile_rx_ssi_config_4 = adrv9001_profile_types.adrv9001_SsiConfig_t(
                                            adrv9001_profile_types.adrv9001_SsiType_e.ADRV9001_SSI_TYPE_LVDS, 
                                            adrv9001_profile_types.adrv9001_SsiDataFormat_e.ADRV9001_SSI_FORMAT_16_BIT_I_Q_DATA, 
                                            adrv9001_profile_types.adrv9001_SsiNumLane_e.ADRV9001_SSI_2_LANE, 
                                            adrv9001_profile_types.adrv9001_SsiStrobeType_e.ADRV9001_SSI_SHORT_STROBE, 
                                            0, 0, adrv9001_profile_types.adrv9001_SsiTxRefClockPin_e.ADRV9001_SSI_TX_REF_CLOCK_PIN_DISABLED, 
                                            False, False, False, 0, False, False, False, True, False)
initialize_init_rx_rx_channel_cfg_3_profile_4 = adrv9001_profile_types.adrv9001_RxProfile_t(12000, 24000, 24000, 0, False, adrv9001_profile_types.adrv9001_RxSignalType_e.ADRV9001_RX_IQ, 
                                            1, 1, 20000000, 0, 1105920, 40000, 40000, adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_LOW, 
                                            adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_LOW, 
                                            64, adrv9001_profile_types.adrv9001_AdcType_e.ADRV9001_ADC_HP, 
                                            adrv9001_profile_types.adrv9001_Adc_LowPower_CalMode_e.ADRV9001_ADC_LOWPOWER_PERIODIC, 
                                            adrv9001_profile_types.adrv9001_RxGainTableType_e.ADRV9001_RX_GAIN_CORRECTION_TABLE, 
                                            initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_4, 
                                            adrv9001_profile_types.adrv9001_RxLnaConfig_t(False, adrv9001_profile_types.adrv9001_GpioAnalogPinNibbleSel_e.ADRV9001_GPIO_ANALOG_PIN_NIBBLE_UNASSIGNED, 
                                              adrv9001_profile_types.adrv9001_ExternalLnaPinSel_e.ADRV9001_EXTERNAL_LNA_PIN_RX1_LOWER_RX2_UPPER, 
                                              0, 0, [0] * 4, 0, 0, adrv9001_profile_types.adrv9001_ExternalLnaType_e.ADRV9001_EXTERNAL_LNA_TYPE_SINGLE), 
                                            initialize_init_rx_rx_channel_cfg_3_profile_rx_ssi_config_4)
initialize_init_rx_rx_channel_cfg_3[4] = adrv9001_profile_types.adrv9001_RxChannelCfg_t(
                                               initialize_init_rx_rx_channel_cfg_3_profile_4)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_rx_wb_nb_comp_p_fir_5 = adrv9001_profile_types.adrv9001_RxWbNbCompPFir_t(
                                                 adrv9001_profile_types.adrv9001_PfirBank_e.ADRV9001_PFIR_BANK_D, 
                                                 adrv9001_profile_types.adrv9001_RxPfirInMuxSel_e.ADRV9001_RP_FIR_IN_MUX_INT_IN, 
                                                 0)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_5 = adrv9001_profile_types.adrv9001_RxNbDemConfig_t(
                                                adrv9001_profile_types.adrv9001_RxDpInFifoConfig_t(0, adrv9001_profile_types.adrv9001_RxDpInFifoMode_e.ADRV9001_DP_IN_FIFO_MODE_DETECTING, 
                                                   adrv9001_profile_types.adrv9001_RxDpInFifoInputSel_e.ADRV9001_DP_IN_FIFO_INPUT_DP_SEL), 
                                                adrv9001_profile_types.adrv9001_RxNbNcoConfig_t(0, adrv9001_profile_types.adrv9001_NcoDpConfig_t(0, 0, 0, 0)), 
                                                initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_rx_wb_nb_comp_p_fir_5, 
                                                adrv9001_profile_types.adrv9001_RxResampConfig_t(0, 0, 0), 
                                                adrv9001_profile_types.adrv9001_RxGsOutMuxSel_e.ADRV9001_GS_OUT_MUX_BYPASS, 
                                                adrv9001_profile_types.adrv9001_RxOutSel_e.ADRV9001_RX_OUT_IQ_SEL, 
                                                adrv9001_profile_types.adrv9001_RxRoundMode_e.ADRV9001_RX_ROUNDMODE_IQ, 
                                                adrv9001_profile_types.adrv9001_RxDpArmSel_e.ADRV9001_DP_SEL)
initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_5 = adrv9001_profile_types.adrv9001_RxDpProfile_t(
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dec_top_4, 
                                              adrv9001_profile_types.adrv9001_RxWbDecTop_t(0, 0, 0, 0, 0, 0), 
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_dec_top_4, 
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_sinc_h_b_top_4, 
                                              initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_rx_nb_dem_5)
initialize_init_rx_rx_channel_cfg_3_profile_5 = adrv9001_profile_types.adrv9001_RxProfile_t(12000, 24000, 24000, 0, False, adrv9001_profile_types.adrv9001_RxSignalType_e.ADRV9001_RX_IQ, 
                                            1, 1, 20000000, 0, 1105920, 40000, 40000, adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_LOW, 
                                            adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_LOW, 
                                            128, adrv9001_profile_types.adrv9001_AdcType_e.ADRV9001_ADC_HP, 
                                            adrv9001_profile_types.adrv9001_Adc_LowPower_CalMode_e.ADRV9001_ADC_LOWPOWER_PERIODIC, 
                                            adrv9001_profile_types.adrv9001_RxGainTableType_e.ADRV9001_RX_GAIN_CORRECTION_TABLE, 
                                            initialize_init_rx_rx_channel_cfg_3_profile_rx_dp_profile_5, 
                                            adrv9001_profile_types.adrv9001_RxLnaConfig_t(False, adrv9001_profile_types.adrv9001_GpioAnalogPinNibbleSel_e.ADRV9001_GPIO_ANALOG_PIN_NIBBLE_UNASSIGNED, 
                                              adrv9001_profile_types.adrv9001_ExternalLnaPinSel_e.ADRV9001_EXTERNAL_LNA_PIN_RX1_LOWER_RX2_UPPER, 
                                              0, 0, [0] * 4, 0, 0, adrv9001_profile_types.adrv9001_ExternalLnaType_e.ADRV9001_EXTERNAL_LNA_TYPE_SINGLE), 
                                            initialize_init_rx_rx_channel_cfg_3_profile_rx_ssi_config_4)
initialize_init_rx_rx_channel_cfg_3[5] = adrv9001_profile_types.adrv9001_RxChannelCfg_t(
                                               initialize_init_rx_rx_channel_cfg_3_profile_5)
initialize_init_rx_rx_channel_cfg_3[6] = adrv9001_profile_types.adrv9001_RxChannelCfg_t(
                                               initialize_init_rx_rx_channel_cfg_3_profile_0)
initialize_init_rx_rx_channel_cfg_3[7] = adrv9001_profile_types.adrv9001_RxChannelCfg_t(
                                               initialize_init_rx_rx_channel_cfg_3_profile_0)
initialize_init_rx_3 = adrv9001_profile_types.adrv9001_RxSettings_t(192, initialize_init_rx_rx_channel_cfg_3)
initialize_init_tx_tx_profile_3_tx_dp_profile_tx_pre_proc_0 = adrv9001_profile_types.adrv9001_TxPreProc_t(0, 0, 0, 0, 1, adrv9001_profile_types.adrv9001_TxDpPreProcMode_e.ADRV9001_TX_DP_PREPROC_IQ_DATA_WITH_PFIRS, 
                                            adrv9001_profile_types.adrv9001_PfirBank_e.ADRV9001_PFIR_BANK_A, 
                                            adrv9001_profile_types.adrv9001_PfirBank_e.ADRV9001_PFIR_BANK_B)
initialize_init_tx_tx_profile_3_tx_dp_profile_tx_nb_int_top_0 = adrv9001_profile_types.adrv9001_TxNbIntTop_t(1, 1, 1, 1, 1, 1, 1, 1, 10)
initialize_init_tx_tx_profile_3_tx_dp_profile_tx_int_top_0 = adrv9001_profile_types.adrv9001_TxIntTop_t(0, 0, 0, 0, 1, 1)
initialize_init_tx_tx_profile_3_tx_dp_profile_tx_int_top_freq_dev_map_0 = adrv9001_profile_types.adrv9001_TxIntTopFreqDevMap_t(0, 0, 0, 0, 0, 1)
initialize_init_tx_tx_profile_3_tx_dp_profile_tx_iqdm_duc_iqdm_nco_0 = adrv9001_profile_types.adrv9001_NcoDpConfig_t(0, 46080000, 0, 0)
initialize_init_tx_tx_profile_3_tx_dp_profile_tx_iqdm_duc_0 = adrv9001_profile_types.adrv9001_TxIqdmDuc_t(
                                            adrv9001_profile_types.adrv9001_TxDpIqDmDucMode_e.ADRV9001_TX_DP_IQDMDUC_MODE0, 
                                            0, 0, 0, 0, initialize_init_tx_tx_profile_3_tx_dp_profile_tx_iqdm_duc_iqdm_nco_0)
initialize_init_tx_tx_profile_3_tx_dp_profile_0 = adrv9001_profile_types.adrv9001_TxDpProfile_t(
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_pre_proc_0, 
                                              adrv9001_profile_types.adrv9001_TxWbIntTop_t(0, 0, 0, 0, 0, 0), 
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_nb_int_top_0, 
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_int_top_0, 
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_int_top_freq_dev_map_0, 
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_iqdm_duc_0)
initialize_init_tx_tx_profile_3_tx_ssi_config_0 = adrv9001_profile_types.adrv9001_SsiConfig_t(
                                            adrv9001_profile_types.adrv9001_SsiType_e.ADRV9001_SSI_TYPE_LVDS, 
                                            adrv9001_profile_types.adrv9001_SsiDataFormat_e.ADRV9001_SSI_FORMAT_16_BIT_I_Q_DATA, 
                                            adrv9001_profile_types.adrv9001_SsiNumLane_e.ADRV9001_SSI_2_LANE, 
                                            adrv9001_profile_types.adrv9001_SsiStrobeType_e.ADRV9001_SSI_SHORT_STROBE, 
                                            0, 0, adrv9001_profile_types.adrv9001_SsiTxRefClockPin_e.ADRV9001_SSI_TX_REF_CLOCK_PIN_DCLK_OUT_ENABLED, 
                                            False, False, False, 0, False, False, False, True, False)
initialize_init_tx_tx_profile_3_0 = adrv9001_profile_types.adrv9001_TxProfile_t(12000, 24000, 24000, 0, 0, 33000, adrv9001_profile_types.adrv9001_TxSignalType_e.ADRV9001_TX_IQ, 
                                            1, 0, 1000000, 530000, adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_LOW, 
                                            0, 0, 0, 0, initialize_init_tx_tx_profile_3_tx_dp_profile_0, 
                                            initialize_init_tx_tx_profile_3_tx_ssi_config_0)
initialize_init_tx_tx_profile_3_tx_dp_profile_tx_pre_proc_1 = adrv9001_profile_types.adrv9001_TxPreProc_t(0, 0, 0, 0, 1, adrv9001_profile_types.adrv9001_TxDpPreProcMode_e.ADRV9001_TX_DP_PREPROC_IQ_DATA_WITH_PFIRS, 
                                            adrv9001_profile_types.adrv9001_PfirBank_e.ADRV9001_PFIR_BANK_C, 
                                            adrv9001_profile_types.adrv9001_PfirBank_e.ADRV9001_PFIR_BANK_D)
initialize_init_tx_tx_profile_3_tx_dp_profile_1 = adrv9001_profile_types.adrv9001_TxDpProfile_t(
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_pre_proc_1, 
                                              adrv9001_profile_types.adrv9001_TxWbIntTop_t(0, 0, 0, 0, 0, 0), 
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_nb_int_top_0, 
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_int_top_0, 
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_int_top_freq_dev_map_0, 
                                              initialize_init_tx_tx_profile_3_tx_dp_profile_tx_iqdm_duc_0)
initialize_init_tx_tx_profile_3_1 = adrv9001_profile_types.adrv9001_TxProfile_t(12000, 24000, 24000, 0, 0, 33000, adrv9001_profile_types.adrv9001_TxSignalType_e.ADRV9001_TX_IQ, 
                                            1, 0, 1000000, 530000, adrv9001_profile_types.adrv9001_ComponentPowerLevel_e.ADRV9001_COMPONENT_POWER_LEVEL_LOW, 
                                            0, 0, 0, 0, initialize_init_tx_tx_profile_3_tx_dp_profile_1, 
                                            initialize_init_tx_tx_profile_3_tx_ssi_config_0)
initialize_init_tx_tx_profile_3 = [ initialize_init_tx_tx_profile_3_0, initialize_init_tx_tx_profile_3_1  ]
initialize_init_tx_3 = adrv9001_profile_types.adrv9001_TxSettings_t(12, initialize_init_tx_tx_profile_3)
initialize_init_sys_config_pll_modulus_modulus_3 = [8388593] * 5
initialize_init_sys_config_pll_modulus_dm_modulus_3 = [8388593] * 2
initialize_init_sys_config_pll_modulus_3 = adrv9001_profile_types.adrv9001_pllModulus_t(
                                             initialize_init_sys_config_pll_modulus_modulus_3, 
                                             initialize_init_sys_config_pll_modulus_dm_modulus_3)
initialize_init_sys_config_3 = adrv9001_profile_types.adrv9001_DeviceSysConfig_t(
                                                  adrv9001_profile_types.adrv9001_DuplexMode_e.ADRV9001_TDD_MODE, 
                                                  0, adrv9001_profile_types.adrv9001_NumDynamicProfiles_e.ADRV9001_NUM_DYNAMIC_PROFILES_DISABLED, 
                                                  adrv9001_profile_types.adrv9001_McsMode_e.ADRV9001_MCSMODE_DISABLED, 
                                                  adrv9001_profile_types.adrv9001_SsiType_e.ADRV9001_SSI_TYPE_DISABLE, 
                                                  adrv9001_profile_types.adrv9001_AdcType_e.ADRV9001_ADC_HP, 
                                                  380, 0, initialize_init_sys_config_pll_modulus_3, 
                                                  False)
initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_a_coefficients_3 = [ 1, -5, -2, 12, 7, -24, -22, 37, 56, -47, -119, 37, 218, 21, -352, -169, 501, 459, -611, -944, 581, 1659, -252, -2592, -606, 3641, 2295, -4564, -5239, 4868, 10405, -2150, -16860, -7184, 17284, 16170, -15978, -28242, 8754, 41070, 6970, -50243, -31684, 50215, 63113, -35486, -95952, 1919, 122118, 52081, -131402, -124789, 112154, 210975, -51173, -302406, -69399, 388963, 286340, -460206, -731028, 507073, 2617033, 3674001, 2617033, 507073, -731028, -460206, 286340, 388963, -69399, -302406, -51173, 210975, 112154, -124789, -131402, 52081, 122118, 1919, -95952, -35486, 63113, 50215, -31684, -50243, 6970, 41070, 8754, -28242, -15978, 16170, 17284, -7184, -16860, -2150, 10405, 4868, -5239, -4564, 2295, 3641, -606, -2592, -252, 1659, 581, -944, -611, 459, 501, -169, -352, 21, 218, 37, -119, -47, 56, 37, -22, -24, 7, 12, -2, -5, 1, 0  ]
initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_a_3 = adrv9001_profile_types.adrv9001_PfirWbNbBuffer_t(128, adrv9001_profile_types.adrv9001_PfirSymmetric_e.ADRV9001_PFIR_COEF_NON_SYMMETRIC, 
                                                 adrv9001_profile_types.adrv9001_PfirNumTaps_e.ADRV9001_PFIR_128_TAPS | adrv9001_profile_types.adrv9001_PfirNumTaps_e.ADRV9001_PFIR_TAPS_MAX_ID, 
                                                 adrv9001_profile_types.adrv9001_PfirGain_e.ADRV9001_PFIR_GAIN_ZERO_DB, 
                                                 initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_a_coefficients_3)
initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_b_coefficients_3 = [0] * 128
initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_b_coefficients_3[63] = 8388608
initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_b_3 = adrv9001_profile_types.adrv9001_PfirWbNbBuffer_t(128, adrv9001_profile_types.adrv9001_PfirSymmetric_e.ADRV9001_PFIR_COEF_NON_SYMMETRIC, 
                                                 adrv9001_profile_types.adrv9001_PfirNumTaps_e.ADRV9001_PFIR_128_TAPS | adrv9001_profile_types.adrv9001_PfirNumTaps_e.ADRV9001_PFIR_TAPS_MAX_ID, 
                                                 adrv9001_profile_types.adrv9001_PfirGain_e.ADRV9001_PFIR_GAIN_ZERO_DB, 
                                                 initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_b_coefficients_3)
initialize_init_pfir_buffer_pfir_tx_wb_nb_pul_shp_coeff_a_3 = adrv9001_profile_types.adrv9001_PfirWbNbBuffer_t(128, adrv9001_profile_types.adrv9001_PfirSymmetric_e.ADRV9001_PFIR_COEF_NON_SYMMETRIC, 
                                                 adrv9001_profile_types.adrv9001_PfirNumTaps_e.ADRV9001_PFIR_128_TAPS | adrv9001_profile_types.adrv9001_PfirNumTaps_e.ADRV9001_PFIR_TAPS_MAX_ID, 
                                                 adrv9001_profile_types.adrv9001_PfirGain_e.ADRV9001_PFIR_GAIN_ZERO_DB, 
                                                 [0] * 128)
initialize_init_pfir_buffer_pfir_rx_nb_pul_shp_val_coefficients_3 = [0] * 128
initialize_init_pfir_buffer_pfir_rx_nb_pul_shp_val_coefficients_3[63] = 8388608
initialize_init_pfir_buffer_pfir_rx_nb_pul_shp_val_3 = adrv9001_profile_types.adrv9001_PfirPulseBuffer_t(128, adrv9001_profile_types.adrv9001_PfirSymmetric_e.ADRV9001_PFIR_COEF_NON_SYMMETRIC, 
                                                  128, adrv9001_profile_types.adrv9001_PfirGain_e.ADRV9001_PFIR_GAIN_ZERO_DB, 
                                                  initialize_init_pfir_buffer_pfir_rx_nb_pul_shp_val_coefficients_3)
initialize_init_pfir_buffer_pfir_rx_nb_pul_shp_3 = [initialize_init_pfir_buffer_pfir_rx_nb_pul_shp_val_3] * 2
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_hp_val_coefficients_3 = [ -2, 0, 2, -5, 12, -24, 50, -108, 277, -1238, 34839, -1238, 277, -108, 50, -24, 12, -5, 2, 0, -2  ]
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_hp_val_3 = adrv9001_profile_types.adrv9001_PfirMag21Buffer_t(21, initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_hp_val_coefficients_3)
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_hp_3 = [initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_hp_val_3] * 2
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_hp_val_coefficients_3 = [ -70, 229, 35, -832, 234, 1885, -209, -4680, -1265, 11468, 19180, 11468, -1265, -4680, -209, 1885, 234, -832, 35, 229, -70  ]
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_hp_val_3 = adrv9001_profile_types.adrv9001_PfirMag21Buffer_t(21, initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_hp_val_coefficients_3)
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_hp_3 = [initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_hp_val_3] * 2
initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_hp_val_coefficients_3 = [ 41, -241, 750, -1559, 2236, -1920, -262, 4378, -8850, 8452, 26718, 8452, -8850, 4378, -262, -1920, 2236, -1559, 750, -241, 41  ]
initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_hp_val_3 = adrv9001_profile_types.adrv9001_PfirMag21Buffer_t(21, initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_hp_val_coefficients_3)
initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_hp_3 = [initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_hp_val_3] * 2
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_lp_val_coefficients_3 = [ -2, 0, 2, -5, 11, -24, 49, -106, 274, -1227, 34822, -1227, 274, -106, 49, -24, 11, -5, 2, 0, -2  ]
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_lp_val_3 = adrv9001_profile_types.adrv9001_PfirMag21Buffer_t(21, initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_lp_val_coefficients_3)
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_lp_3 = [initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_lp_val_3] * 2
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_lp_val_coefficients_3 = [ -70, 228, 34, -827, 234, 1876, -213, -4661, -1244, 11455, 19144, 11455, -1244, -4661, -213, 1876, 234, -827, 34, 228, -70  ]
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_lp_val_3 = adrv9001_profile_types.adrv9001_PfirMag21Buffer_t(21, initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_lp_val_coefficients_3)
initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_lp_3 = [initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_lp_val_3] * 2
initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_lp_val_coefficients_3 = [ 41, -237, 739, -1536, 2208, -1908, -229, 4283, -8730, 8455, 26600, 8455, -8730, 4283, -229, -1908, 2208, -1536, 739, -237, 41  ]
initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_lp_val_3 = adrv9001_profile_types.adrv9001_PfirMag21Buffer_t(21, initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_lp_val_coefficients_3)
initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_lp_3 = [initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_lp_val_3] * 2
initialize_init_pfir_buffer_pfir_tx_mag_comp1_coefficients_3 = [ 178, -1042, 3271, -6913, 10209, -9581, 1555, 14717, -24411, 7373, 42061, 7373, -24411, 14717, 1555, -9581, 10209, -6913, 3271, -1042, 178  ]
initialize_init_pfir_buffer_pfir_tx_mag_comp1_3 = adrv9001_profile_types.adrv9001_PfirMag21Buffer_t(21, initialize_init_pfir_buffer_pfir_tx_mag_comp1_coefficients_3)
initialize_init_pfir_buffer_pfir_tx_mag_comp_nb_val_coefficients_3 = [ 54, -468, 1339, -836, -3842, 9293, 21689, 9293, -3842, -836, 1339, -468, 54  ]
initialize_init_pfir_buffer_pfir_tx_mag_comp_nb_val_3 = adrv9001_profile_types.adrv9001_PfirMag13Buffer_t(13, initialize_init_pfir_buffer_pfir_tx_mag_comp_nb_val_coefficients_3)
initialize_init_pfir_buffer_pfir_tx_mag_comp_nb_3 = [initialize_init_pfir_buffer_pfir_tx_mag_comp_nb_val_3] * 2
initialize_init_pfir_buffer_pfir_rx_mag_comp_nb_val_3 = adrv9001_profile_types.adrv9001_PfirMag13Buffer_t(13, [0] * 13)
initialize_init_pfir_buffer_pfir_rx_mag_comp_nb_3 = [initialize_init_pfir_buffer_pfir_rx_mag_comp_nb_val_3] * 2
initialize_init_pfir_buffer_3 = adrv9001_profile_types.adrv9001_PfirBuffer_t(
                                             initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_a_3, 
                                             initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_b_3, 
                                             initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_a_3, 
                                             initialize_init_pfir_buffer_pfir_rx_wb_nb_ch_filter_coeff_b_3, 
                                             initialize_init_pfir_buffer_pfir_tx_wb_nb_pul_shp_coeff_a_3, 
                                             initialize_init_pfir_buffer_pfir_tx_wb_nb_pul_shp_coeff_a_3, 
                                             initialize_init_pfir_buffer_pfir_tx_wb_nb_pul_shp_coeff_a_3, 
                                             initialize_init_pfir_buffer_pfir_tx_wb_nb_pul_shp_coeff_a_3, 
                                             initialize_init_pfir_buffer_pfir_rx_nb_pul_shp_3, 
                                             initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_hp_3, 
                                             initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_hp_3, 
                                             initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_hp_3, 
                                             initialize_init_pfir_buffer_pfir_rx_mag_low_tia_low_s_r_lp_3, 
                                             initialize_init_pfir_buffer_pfir_rx_mag_low_tia_high_s_r_lp_3, 
                                             initialize_init_pfir_buffer_pfir_rx_mag_high_tia_high_s_r_lp_3, 
                                             initialize_init_pfir_buffer_pfir_tx_mag_comp1_3, 
                                             initialize_init_pfir_buffer_pfir_tx_mag_comp1_3, 
                                             initialize_init_pfir_buffer_pfir_tx_mag_comp_nb_3, 
                                             initialize_init_pfir_buffer_pfir_rx_mag_comp_nb_3)
initialize_init_3 = adrv9001_profile_types.adrv9001_Init_t(initialize_init_clocks_3, initialize_init_rx_3, 
                                       initialize_init_tx_3, initialize_init_sys_config_3, 
                                       initialize_init_pfir_buffer_3)
