import PySimpleGUI as sg
from icon import iconWindow
import converter
import telegrams


def converter_layout():
	"""
	Create UI for converting the structured IC 104 address to unstructured ones and vice versa
	:return:
	"""
	col1 = [[sg.Text("IOA3 (HB)", size=(11, 1), font=('Helvetica', 10, "bold"))],
			[sg.Input(key="-IOA3-", size=(10, 1), default_text=0)],
			[sg.Text(size=(10, 2))],
			[sg.Text("Unstructured:", size=(11, 1), font=('Helvetica', 10, "bold"))]]
	col2 = [[sg.Text()],
			[sg.Text()],
			[sg.Button(button_text='', key=("-CONV_TO_UNSTRUCTURED-"), size=(16, 16),
					   image_filename="./static/icons8-down-arrow-30.png", button_color=('lightblue', '#E3F2FD'),
					   border_width=0)]]
	col3 = [[sg.Text("IOA2 (MB)", size=(11, 1), font=('Helvetica', 10, "bold"))],
			[sg.Input(key="-IOA2-", size=(10, 1), default_text=0, )],
			[sg.Text(size=(10, 2))],
			[sg.Input(key="-RESULT-", size=(10, 1), default_text=0)]]
	col4 = [[sg.Text()],
			[sg.Text()],
			[sg.Button(button_text='', key=("-CONV_TO_STRUCTURED-"), size=(16, 16),
					   image_filename="./static/icons8-up-30.png", button_color=('lightblue', '#E3F2FD'),
					   border_width=0)]]
	col5 = [[sg.Text("IOA1 (LB)", size=(11, 1), font=('Helvetica', 10, "bold"))],
			[sg.Input(key="-IOA1-", size=(10, 1), default_text=0)],
			[sg.Text(size=(10, 2))]]

	return [[sg.Column(col1), sg.Column(col2), sg.Column(col3), sg.Column(col4), sg.Column(col5)]]


def telegram_layout():
	"""
	Create UI for telegram information
	:return:
	"""
	layout = [
		[sg.Text("TI", size=(5, 1), pad=(5, 2), font=('Helvetica', 10, "bold")),
		 sg.Text("Description", justification='center', pad=(5, 2), size=(35, 1), font=('Helvetica', 10, "bold")),
		 sg.Text("Code", justification='center', font=('Helvetica', 10, "bold"), size=(15, 1), pad=(5, 2))],
		[sg.Input(pad=(5, 5), key="-TI-", default_text=1, font=('Helvetica', 9), justification="right", size=(5, 1)),
		 sg.Combo(telegrams.get_telegrams_descriptions(), key="-TI_DESC-", enable_events=True, readonly=True, default_value="Single-point information",
				  font=('Helvetica', 9), pad=(5, 5), size=(40, 1)),
		 sg.Combo(telegrams.get_telegrams_codes(), key="-TI_CODE-", enable_events=True, readonly=True, default_value="M_SP_NA_1", font=('Helvetica', 9),
				  pad=(5, 1), size=(15, 1))]]
	return layout


def help_layout():
	"""
	Create UI for settings
	:return:
	"""
	layout = [[sg.Text("1.Converter changes from structured IEC 60870-5-104 i.e. 31.0.1.10.2.4 address \n"
					   "  to unstructured one i.e. 31.0.1.655876 \n"
					   "2. You can also check the Telegram ASDU Types", font=('Helvetica', 9), justification="left")]]

	return layout


def get_structured_address():
	"""
	Method for the UI to get structured address, so different events can call it
	:return:
	"""
	unstruct_address = values["-RESULT-"]
	if not unstruct_address == "":
		struct_address = converter.from_unstructured_to_structured(unstruct_address)
		if len(struct_address) == 3:
			HB = struct_address[0]
			MB = struct_address[1]
			LB = struct_address[2]
			window['-IOA3-'].update(HB)
			window['-IOA2-'].update(MB)
			window['-IOA1-'].update(LB)


def get_unstructured_address():
	"""
	Method for the UI to get unstructured address, so different events can call it
	:return:
	"""
	elements = ['-IOA3-', '-IOA2-', '-IOA1-']
	struct_address = []
	for element in elements:
		if values[element] is not "":
			struct_address.append(values[element])
		else:
			window.find_element(element).update("0")
			struct_address.append("0")
	unstruct = converter.from_structured_to_unstructured(struct_address)
	window.find_element("-RESULT-").update(unstruct)

def get_telegram_values(input_key):
	"""
	Method gets the value of the key of the input and based on that sets to remaining inputs
	:param input_key: KEY of the input for telegram
	:return:
	"""
	if input_key == "-TI-":
		value = int(values["-TI-"])
		result = telegrams.telegrams.get(value, ["Reserved", "-"])
		window.find_element("-TI_DESC-").update(result[0])
		window.find_element("-TI_CODE-").update(result[1])

	if input_key == "-TI_DESC-":
		value = values["-TI_DESC-"]
		for item in telegrams.telegrams:
			if value in telegrams.telegrams[item]:
				result = telegrams.telegrams[item]
				window.find_element("-TI-").update(item)
				window.find_element("-TI_CODE-").update(result[1])
	if input_key == "-TI_CODE-":
		val = values["-TI_CODE-"]
		for item in telegrams.telegrams:
			if val in telegrams.telegrams[item]:
				result = telegrams.telegrams[item]
				window.find_element("-TI-").update(item)
				window.find_element("-TI_DESC-").update(result[0])


# GUI initialization
sg.theme('LightBlue')
sg.SetOptions(icon=iconWindow, font='Helvetica', text_justification='center')

layout = [[sg.TabGroup(
	[[sg.Tab('Converter', layout=converter_layout()), sg.Tab('Telegram', layout=telegram_layout()),
	  sg.Tab('Help', layout=help_layout())]], font=('Helvetica', 9))],
	[sg.Button('', key='Exit', image_filename="./static/exit.png", button_color=('#E3F2FD', '#E3F2FD'))]]

window = sg.Window('IEC 104 Address Converter', layout, location=(500, 500), use_default_focus=True,
				   element_padding=(1, 1), return_keyboard_events=True)

while True:
	event, values = window.read()
	# get element who has focus
	elem = window.find_element_with_focus()
	print(event)
	if elem is not None:
		if elem.Type == sg.ELEM_TYPE_INPUT_TEXT:
			key = elem.Key
			value = values[key]
			if event not in '0123456789':
				# check if event is not normal event
				if event not in window.AllKeysDict:
					if event not in ["Left:37", "Delete:46", "BackSpace:8", "Right:39", "", "	", '\r']:
						elem.update(value[:-1])
			# update values
			else:
				if int(value) < 0:
					elem.update("0")
				if int(value) > 254:
					if elem != window.find_element("-RESULT-"):
						elem.update("254")
					else:
						if int(value) > 16777215:
							elem.update("16777215")

	if event == "-CONV_TO_UNSTRUCTURED-":
		get_unstructured_address()

	if event == "-CONV_TO_STRUCTURED-":
		get_structured_address()

	# desc combobox
	if event == "-TI_DESC-":
		get_telegram_values("-TI_DESC-")

	# code combobox
	if event == "-TI_CODE-":
		get_telegram_values("-TI_CODE-")

	# ENTER key
	if event == '\r':
		key = elem.Key
		if key == "-RESULT-":
			get_structured_address()
		if key == "-IOA1-" or "-IOA2-" or "-IOA3-":
			get_unstructured_address()
		if key == "-TI-":
			get_telegram_values("-TI-")

	# set focus doesnt work unfortunately
	#	elif key == "-TI-":
	# # TAB event
	# if event == "	":
	# 	if elem is not None:
	# 		if elem.Type == sg.ELEM_TYPE_INPUT_TEXT:
	# 			key = elem.Key
	# 			if key == "-IOA3-":
	# 				window.Element('-IOA2-').SetFocus(force=True)
	# 			elif key == "-IOA2-":
	# 				window.Element('-IOA1-').SetFocus(force=True)
	# 			elif key == "-IOA1-":
	# 				window.Element('-RESULT-').SetFocus(force=True)
	# 			elif key == "-RESULT-":
	# 				window.Element('-IOA3-').SetFocus(force=True)

	if event in (None, 'Exit'):
		break

window.close()
