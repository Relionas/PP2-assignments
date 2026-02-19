class Phone:
    def call(self):
        print("Calling via GSM...")

class SmartPhone(Phone):
    def call(self):
        print("Calling via Telegram...")

phone = SmartPhone()
phone.call()