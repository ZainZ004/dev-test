import pyttsx
import time
engine = pyttsx.init()
engine.read("English test")
engine.runAndwait()
engine.read("中文测试")
engine.runAndwait()
