from mcdreforged.api.rtext import RTextList, RText, RColor
from btr2.config import Configure

conf = Configure()
prefix = conf.prefix

help_head = """
==================§b BTR2 §r==================
"""
help_body = {
    f"§b{prefix}": "§rDisplay help message.",
    f"§b{prefix} upload": "§rUpload the slot1 (by default) to Firebase storage.",
    f"§b{prefix} download": "§rDownload the file and extract in slot1 (by default)."
}

def gen_help_message():
    help_message = RTextList(
        RText(help_head),
        RText("Available Commands:", color=RColor.gold),
    )
    for command, description in help_body.items():
        help_message.append(f"\n  {command} - {description}")
    return help_message

def gen_unknown_argument_message():
    unknown_message = RText("Unknown argument.", color=RColor.red)
    return str(unknown_message)

command_help_message = "Use !!btr2 to upload Slot1 (by default) to firebase."
