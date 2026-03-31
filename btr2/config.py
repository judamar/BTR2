from mcdreforged.api.utils.serializer import Serializable

# `Configure` is a class that contains the configuration for the `qb_multi` program


class Configure(Serializable):
    prefix: str = '!!btr2'
    source_path: str = './qb_multi/slot1'
    dest_path: str = './btr2/'
    r2_endpoint_url: str = 'https://<account_id>.r2.cloudflarestorage.com'
    r2_access_key_id: str = ''
    r2_secret_access_key: str = ''
    r2_bucket_name: str = ''
    permission: int = 0
    comp_name: str = 'btr2_comp'
    extension: str = 'zip'
    fb_path: str = 'smp/'
