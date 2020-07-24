# IEC 60870-5-104 Address Converter

Simple GUI engineering tool to calculate from structured to unstructured **IEC 60870-5-104** addresses and vice versa, i.e. **31.0.1.10.2.4** into **31.0.1.655876**

I have found that a lot of SCADA vendors use one of another and it takes a lot of time to calculate them by hand (and I often forget the formula).

It also has a list with Telegram ASDU Types.

<img src="https://i.ibb.co/1qwZMg0/converter.jpg">

<img src="https://i.ibb.co/YTrXQKN/telegrams.jpg">

If you want to build it, you need to download requirements:

```
# pip install requirements.txt
```
There is a .spec Pyinstaller file attached to create a GUI. Use it as:

```
# pyinstaller main.spec
```
Built program is available in the `dist` folder.

GUI is built on *PySimpleGUI* framework.
