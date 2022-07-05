# A dictonary of most common file extensions
extensions = {
    "Html": [".html5", ".html", ".htm", ".xhtml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv", ".m4v"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx",".csv"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PlainText": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    # "Python": [".py"],
    "Xml": [".xml"],
    "Exe": [".exe",".djvu",".msi",".bat"],
    "Shell": [".sh", ".bat"],
    "Android": [".apk"]
}

#Returns a category of file by using the dictionary Extensions
def return_category(file_type):
    for category, extension_list in extensions.items():
        for suffix in extension_list:
            if suffix == file_type:
                return category