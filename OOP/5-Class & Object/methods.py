class Phone:
    price = 16000
    color = "golden"
    brand = "iPhone"
    model = 7

    def call(self):
        print("calling someone")

    def send_sms(self, number, sms):
        return f"sending sms to {number} and message: {sms}"


my_phone = Phone()

my_phone.call()

print(my_phone.send_sms(1517824769, "I called you"))
