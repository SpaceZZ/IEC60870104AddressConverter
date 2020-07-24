from _collections import defaultdict

unknown_list = ["Reserved", "-"]
telegrams = defaultdict()
telegrams.default_factory = unknown_list


def fill_telegrams_dict():
	"""
	Fill the telegrams dictionary with the values
	:return:
	"""
	if telegrams is not None:
		telegrams[0] = ["Reserved", "-"]
		telegrams[1] = ["Single-point information", "M_SP_NA_1"]
		telegrams[2] = ["Single-point information with time tag", "M_SP_TA_1"]
		telegrams[3] = ["Double-point information", "M_DP_NA_1"]
		telegrams[4] = ["Double-point information with time tag", "M_DP_TA_1"]
		telegrams[5] = ["Step position information", "M_ST_NA_1"]
		telegrams[6] = ["Step position information with time tag", "M_ST_TA_1"]
		telegrams[7] = ["Bitstring of 32 bit", "M_BO_NA_1"]
		telegrams[8] = ["Bitstring of 32 bit with time tag", "M_BO_TA_1"]
		telegrams[9] = ["Measured value, normalised value", "M_ME_NA_1"]
		telegrams[10] = ["Measured value, normalized value with time tag", "M_ME_TA_1"]
		telegrams[11] = ["Measured value, scaled value", "M_ME_NB_1"]
		telegrams[12] = ["Measured value, scaled value wit time tag", "M_ME_TB_1"]
		telegrams[13] = ["Measured value, short floating point number", "M_ME_NC_1"]
		telegrams[14] = ["Measured value, short floating point number with time tag", "M_ME_TC_1"]
		telegrams[15] = ["Integrated totals", "M_IT_NA_1"]
		telegrams[16] = ["Integrated totals with time tag", "M_IT_TA_1"]
		telegrams[17] = ["Event of protection equipment with time tag", "M_EP_TA_1"]
		telegrams[18] = ["Packed start events of protection equipment with time tag", "M_EP_TB_1"]
		telegrams[19] = ["Packed output circuit information of protection equipment with time tag", "M_EP_TC_1"]
		telegrams[20] = ["Packed single point information with status change detection", "M_PS_NA_1"]
		telegrams[21] = ["Measured value, normalized value without quality descriptor", "M_ME_ND_1"]
		# addresses SDU_TYPE_22..29	22..29	0x16..0x1D	Reserved (standard area)
		telegrams[30] = ["Single-point information with time tag CP56Time2a", "M_SP_TB_1"]
		telegrams[31] = ["Double-point information with time tag CP56Time2a", "M_DP_TB_1"]
		telegrams[32] = ["Step position information with time tag CP56Time2a", "M_ST_TB_1"]
		telegrams[33] = ["Bitstring of 32 bit with time tag CP56Time2a", "M_BO_TB_1"]
		telegrams[34] = ["Measured value, normalised value with time tag CP56Time2a", "M_ME_TD_1"]
		telegrams[35] = ["Measured value, scaled value with time tag CP56Time2a", "M_ME_TE_1"]
		telegrams[36] = ["Measured value, short floating point number with time tag CP56Time2a", "M_ME_TF_1"]
		telegrams[37] = ["Integrated totals with time tag CP56Time2a", "M_IT_TB_1"]
		telegrams[38] = ["Event of protection equipment with time tag CP56Time2a", "M_EP_TD_1"]
		telegrams[39] = ["Packed start events of protection equipment with time tag CP56Time2a", "M_EP_TE_1"]
		telegrams[40] = ["Packed output circuit information of protection equipment with time tag CP56Time2a",
						 "M_EP_TF_1"]
		# ASDU_TYPE_41..44	41..44	0x29..0x2C	Reserved (standard area)
		telegrams[45] = ["Single command", "C_SC_NA_1"]
		telegrams[46] = ["Double command", "C_DC_NA_1"]
		telegrams[47] = ["Regulating step command", "C_RC_NA_1"]
		telegrams[48] = ["Set-point Command, normalised value", "C_SE_NA_1"]
		telegrams[49] = ["Set-point Command, scaled value", "C_SE_NB_1"]
		telegrams[50] = ["Set-point Command, short floating point number", "C_SE_NC_1"]
		telegrams[51] = ["Bitstring 32 bit command", "C_BO_NA_1"]
		# ASDU_TYPE_52..57	52..57	0x34..0x39	Reserved (standard area)
		telegrams[58] = ["Single command with time tag CP56Time2a", "C_SC_TA_1"]
		telegrams[59] = ["Double command with time tag CP56Time2a", "C_DC_TA_1"]
		telegrams[60] = ["Regulating step command with time tag CP56Time2a", "C_RC_TA_1"]
		telegrams[61] = ["Measured value, normalised value command with time tag CP56Time2a", "C_SE_TA_1"]
		telegrams[62] = ["Measured value, scaled value command with time tag CP56Time2a", "C_SE_TB_1"]
		telegrams[63] = ["Measured value, short floating point number command with time tag CP56Time2a", "C_SE_TC_1"]
		telegrams[64] = ["Bitstring of 32 bit command with time tag CP56Time2a", "C_BO_TA_1"]
		# ASDU_TYPE_65..69	65..69	0x41..0x45	Reserved (standard area)
		telegrams[70] = ["End of Initialisation", "M_EI_NA_1"]
		# ASDU_TYPE_71..99	71..99	0x47..0x63	Reserved (standard area)
		telegrams[100] = ["Interrogation command", "C_IC_NA_1"]
		telegrams[101] = ["Counter interrogation command", "C_CI_NA_1"]
		telegrams[102] = ["Read command", "C_RD_NA_1"]
		telegrams[103] = ["Clock synchronisation command", "C_CS_NA_1"]
		telegrams[104] = ["Test command", "C_TS_NA_1"]
		telegrams[105] = ["Reset process command", "C_RP_NA_1"]
		telegrams[106] = ["Delay acquisition command", "C_CD_NA_1"]
		telegrams[107] = ["Test command with time tag CP56Time2a", "C_TS_TA_1"]
		# ASDU_TYPE_108..109	108..109	0x6C..0x6D	Reserved (standard area)
		telegrams[110] = ["Parameter of measured values, normalized value", "P_ME_NA_1"]
		telegrams[111] = ["Parameter of measured values, scaled value", "P_ME_NB_1"]
		telegrams[112] = ["Parameter of measured values, short floating point number", "P_ME_NC_1"]
		telegrams[113] = ["Parameter activation", "P_AC_NA_1"]
		# ASDU_TYPE_114..119	114..119	0x72..0x77	Reserved (standard area)
		telegrams[120] = ["File ready", "F_FR_NA_1"]
		telegrams[121] = ["Section ready", "F_SR_NA_1"]
		telegrams[122] = ["Call directory, select file, call file, call section", "F_SC_NA_1"]
		telegrams[123] = ["Last section, last segment", "F_LS_NA_1"]
		telegrams[124] = ["ACK file, ACK section", "F_FA_NA_1"]
		telegrams[125] = ["Segment", "P_ME_NA_1"]
		telegrams[126] = ["Directory", "F_DR_TA_1"]


def get_telegrams_ids():
	"""
	Function returns telegrams as a list
	:return:
	"""

	if telegrams is not None:
		if not telegrams:
			fill_telegrams_dict()

	return telegrams.keys()


def get_telegrams_descriptions():
	"""
	Function returns descriptions of the telegrams
	:return:
	"""
	if telegrams is not None:
		if not telegrams:
			fill_telegrams_dict()

	_list = [desc for (desc, code) in telegrams.values()]
	return _list


def get_telegrams_codes():
	"""
	Function returns codes of the telegrams
	:return:
	"""
	if telegrams is not None:
		if not telegrams:
			fill_telegrams_dict()

	_list = [code for (desc, code) in telegrams.values()]
	return _list
