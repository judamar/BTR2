import shutil
import boto3
from mcdreforged.api.all import *
from btr2.config import *
from btr2.UI import *
import os

conf = Configure
# It defines the path where the zip file will be saved
out_path = conf.dest_path+conf.comp_name
unknown_argument_msg = gen_unknown_argument_message()


def print_msg(server: PluginServerInterface, msg: str, prefix='[BTR2] '):
    msg = RTextList(prefix, msg)
    server.logger.info(msg)
    server.say(msg)


@new_thread("BTR2 Check Folder")
# It checks if the folder exists, if not, it creates it.
def check_folder(server: PluginServerInterface):
    if not os.path.exists(conf.dest_path):
        os.makedirs(conf.dest_path)
        server.logger.info("dest_path folder created")


# It compresses the source code of the plugin into a zip file.
def compress_qb(server: PluginServerInterface):
    print_msg(server, f"§a[+]§r Compressing {conf.source_path}")
    try:
        shutil.make_archive(out_path, conf.extension, conf.source_path,
                            compresslevel=conf.compression_level)
        print_msg(server, "§a[+]§r Success§r")
    except Exception as error:
        print_msg(server, f"§c[-] Compression failed§r {error}")


# It extracts the source code of the plugin from the zip file.
def extract_qb(server: PluginServerInterface):
    print_msg(server, f"§a[+]§r Extracting")
    try:
        shutil.rmtree(conf.source_path)
        os.makedirs(conf.source_path)
        shutil.unpack_archive(conf.dest_path + conf.comp_name +
                              '.' + conf.extension, conf.source_path, conf.extension)
        os.remove(out_path + "." + conf.extension)
        print_msg(server, "§a[+]§r Success")
        print_msg(server, f"§a[+]§r Ready to restore the {conf.source_path}")
    except Exception as error:
        print_msg(server, f"§c[-] Extraction failed§r {error}")


def _get_r2_client():
    return boto3.client(
        's3',
        endpoint_url=conf.r2_endpoint_url,
        aws_access_key_id=conf.r2_access_key_id,
        aws_secret_access_key=conf.r2_secret_access_key,
        region_name='auto',
    )


def upload_to_r2(server: PluginServerInterface):  # It uploads the zip file to R2 Storage
    print_msg(server, f"§a[+]§r Uploading to R2 {conf.fb_path}§r")
    try:
        s3 = _get_r2_client()
        if conf.compress:
            file = out_path + "." + conf.extension
            object_key = conf.fb_path + conf.comp_name + "." + conf.extension
            s3.upload_file(file, conf.r2_bucket_name, object_key)
            os.remove(file)
        else:
            for dirpath, _dirnames, filenames in os.walk(conf.source_path):
                for filename in filenames:
                    local_file = os.path.join(dirpath, filename)
                    relative = os.path.relpath(local_file, conf.source_path)
                    object_key = conf.fb_path + conf.comp_name + \
                        "/" + relative.replace(os.sep, "/")
                    s3.upload_file(local_file, conf.r2_bucket_name, object_key)
        print_msg(server, "§a[+]§r Success")
    except Exception as error:
        print_msg(server, f"§c[-] Uploading failed§r {error}")


# It downloads the zip file from R2 Storage
def download_from_r2(server: PluginServerInterface):
    print_msg(server, f"§a[+]§r Downloading from R2 {conf.fb_path}§r")
    try:
        s3 = _get_r2_client()
        if conf.compress:
            file = conf.comp_name + "." + conf.extension
            object_key = conf.fb_path + conf.comp_name + "." + conf.extension
            s3.download_file(conf.r2_bucket_name, object_key,
                             conf.dest_path + file)
        else:
            prefix = conf.fb_path + conf.comp_name + "/"
            paginator = s3.get_paginator('list_objects_v2')
            for page in paginator.paginate(Bucket=conf.r2_bucket_name, Prefix=prefix):
                for obj in page.get('Contents', []):
                    relative = obj['Key'][len(prefix):]
                    local_file = os.path.join(
                        conf.source_path, *relative.split("/"))
                    os.makedirs(os.path.dirname(local_file), exist_ok=True)
                    s3.download_file(conf.r2_bucket_name,
                                     obj['Key'], local_file)
        print_msg(server, "§a[+]§r Success")
    except Exception as error:
        print_msg(server, f"§c[-] ERROR§r {error}")


@new_thread("BTR2 Upload")
def upload(server: PluginServerInterface):
    if conf.compress:
        compress_qb(server)
    upload_to_r2(server)


@new_thread("BTR2 Download")
def download(server: PluginServerInterface):
    download_from_r2(server)
    if conf.compress:
        extract_qb(server)

# |REGISTER COMMANDS|


def register_command(server: PluginServerInterface):
    def get_literal_node(literal):
        lvl = conf.permission
        return Literal(literal).requires(lambda src: src.has_permission(lvl)).on_error(RequirementNotMet, lambda src: src.reply("Permission denied"), handled=True)

    server.register_command(
        Literal(conf.prefix).
        runs(lambda src: src.reply(gen_help_message())).
        on_error(UnknownArgument, lambda src, _: print_msg(server, unknown_argument_msg), handled=True).
        then(
            get_literal_node('upload').runs(
                lambda src, ctx: upload(src.get_server()))
        ).
        then(
            get_literal_node('download').runs(
                lambda src, ctx: download(src.get_server()))
        )
    )


def on_load(server: PluginServerInterface, old_module):
    global conf  # do conf global
    check_folder(server)  # check folder
    # load config.json file to conf
    conf = server.load_config_simple('config.json', target_class=Configure)
    msg = 'Plugin btr2 loaded, use {}'.format(
        conf.prefix)  # message showed when server start
    server.logger.info(msg)  # displays message
    register_command(server)  # register command
    # when !!help it shows help message
    server.register_help_message(conf.prefix, {'en_us': command_help_message})
