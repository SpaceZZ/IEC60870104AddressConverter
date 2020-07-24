"""
Converter for the changing the IEC 60870-104 addressing from structured IOA to unstructured IOA
and other way around
"""


def from_unstructured_to_structured(unstruct):
	"""
	Method converts the unstructured address (i.e. 800) to structured address - IOA3 - High Byte, IOA2 Medium Byte,
	IOA1 Low Byte.
	This is big Endian notation convention
	TODO implement big endian notation
	:param unstruct: string with unstructured address
	:return: list with 3 elements [HB, MB, LB] in DECIMAL notation
	"""
	_unstruct = int(unstruct)

	if _unstruct < 0:
		# this should not be possible, requires positive addressing
		return ["0", "0", "0"]

	result = hex(_unstruct)
	result = normalize_hex_3_bytes(result)
	HB = int(result[0:2], 16)
	MB = int(result[2:4], 16)
	LB = int(result[4:6], 16)

	return [HB, MB, LB]


def from_structured_to_unstructured(struct):
	"""
	Method converts the structured address (i.e. IOA3 - 0, IOA2 - 3, IOA3 - 32) to unstructured address - 800.
	:param struct: List with HB, MB , LB
	:return: unstructured integer with result
	"""
	unstruct = 0
	if len(struct) == 3:
		HB = hex(int(struct[0]))
		HB = normalize_hex_1_byte(HB)
		MB = hex(int(struct[1]))
		MB = normalize_hex_1_byte(MB)
		LB = hex(int(struct[2]))
		LB = normalize_hex_1_byte(LB)
		unstruct = HB + MB + LB
		unstruct = int(unstruct, 16)
	return unstruct


def normalize_hex_1_byte(hex_string):
	"""
	Normalizes to the correct 1 byte system
	:param hex_string:
	:return:
	"""
	hex_string = hex_string.replace("0x", "")
	if len(hex_string) < 2:
		hex_string = "0" + hex_string
	return hex_string


def normalize_hex_3_bytes(hex_string):
	"""
	Normalizes the usage of the hex_string
	:param hex_string:
	:return:
	"""
	if "0x" in hex_string:
		hex_string = hex_string[2:]

	# 3 bytes
	if len(hex_string) < 6:
		diff = 6 - len(hex_string)
		hex_string = ("0" * diff) + hex_string

	return hex_string
