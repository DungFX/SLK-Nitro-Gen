import requests
import random
import string
import time

print("""
╔═══╗╔╗   ╔╗╔═╗    ╔═╗ ╔╗╔══╗╔════╗╔═══╗╔═══╗    ╔═══╗╔═══╗╔═╗ ╔╗
║╔═╗║║║   ║║║╔╝    ║║╚╗║║╚╣╠╝║╔╗╔╗║║╔═╗║║╔═╗║    ║╔═╗║║╔══╝║║╚╗║║
║╚══╗║║   ║╚╝╝     ║╔╗╚╝║ ║║ ╚╝║║╚╝║╚═╝║║║ ║║    ║║ ╚╝║╚══╗║╔╗╚╝║
╚══╗║║║ ╔╗║╔╗║     ║║╚╗║║ ║║   ║║  ║╔╗╔╝║║ ║║    ║║╔═╗║╔══╝║║╚╗║║
║╚═╝║║╚═╝║║║║╚╗    ║║ ║║║╔╣╠╗ ╔╝╚╗ ║║║╚╗║╚═╝║    ║╚╩═║║╚══╗║║ ║║║
╚═══╝╚═══╝╚╝╚═╝    ╚╝ ╚═╝╚══╝ ╚══╝ ╚╝╚═╝╚═══╝    ╚═══╝╚═══╝╚╝ ╚═╝

""")
time.sleep(2)
print("Auto Tạo Nitro Link")
time.sleep(0.3)
print("Join discord.gg/slkcommunity Để Cập Nhật\n")
time.sleep(0.2)

num = int(input('Bạn Muốn Gen Và Check Bao Nhiêu: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Mã nitro của bạn đang được tạo, hãy kiên nhẫn nếu bạn nhập số cao!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Có | {nitro} ")
            break
        else:
            print(f" Không | {nitro} ")