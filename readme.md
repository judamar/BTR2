English | [Español](readme-es.md)

# Backup to R2 (btr2)

[![Github downloads](https://img.shields.io/github/downloads/judamar/BTR2/total?label=Github%20downloads&logo=github)](https://github.com/judamar/BTR2/releases)

This is a plugin for [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) that allows uploading the backup made by [QuickBackupM](https://github.com/TISUnion/QuickBackupM) to [Cloudflare R2](https://www.cloudflare.com/developer-platform/r2/) storage.

Requires `>= v2.0.0a1` [MCDReforged](https://github.com/Fallen-Breath/MCDReforged).

## Description

The BTR2 plugin is a tool for uploading and downloading the backup (Slot1 by default) to [Cloudflare R2](https://www.cloudflare.com/developer-platform/r2/) storage using the S3-compatible API via `boto3`.

## Commands

The BTR2 plugin adds the following commands:

- `!!btr2`: Displays help message.
- `!!btr2 upload`: Compresses the Slot1 (by default) folder and uploads it to R2 storage.
- `!!btr2 download`: Downloads the backup from R2 storage and extracts it into Slot1 (by default).

## Requirements

Install this:

```
pip install boto3
```

## Configuration

You can configure the plugin's behavior in the `config.json` file with the following options:

- **prefix**: Defines the prefix for the plugin's commands.
- **source_path**: Path of the folder to be compressed and uploaded.
- **dest_path**: Path where the downloaded backups will be stored.
- **r2_endpoint_url**: Your R2 endpoint URL (`https://<account_id>.r2.cloudflarestorage.com`), follow this [tutorial](./tutorials/key_tuto.md).
- **r2_access_key_id**: R2 API token Access Key ID.
- **r2_secret_access_key**: R2 API token Secret Access Key.
- **r2_bucket_name**: Name of the R2 bucket to use.
- **permission**: Minimum permission level required to execute commands.
- **comp_name**: Name of the compressed file (without extension).
- **compress**: Whether to compress the backup before uploading. If `false`, files are uploaded individually without compression.
- **extension**: Archive format to use for compression. Supported values:
  - `zip` — ZIP archive (default, widely compatible)
  - `tar` — Uncompressed TAR archive
  - `gztar` — TAR with gzip compression (`.tar.gz`)
  - `bztar` — TAR with bzip2 compression (`.tar.bz2`)
  - `xztar` — TAR with xz compression (`.tar.xz`, best compression ratio)
- **compression_level**: Compression level from `0` (no compression) to `9` (maximum compression). Default is `5`.
- **fb_path**: Path prefix within the R2 bucket where files are stored.

The plugin should work without additional modifications, as long as the R2 configuration is correct.

### Default Configuration:

```json
{
  "prefix": "!!btr2",
  "source_path": "./qb_multi/slot1",
  "dest_path": "./btr2/",
  "r2_endpoint_url": "https://<account_id>.r2.cloudflarestorage.com",
  "r2_access_key_id": "",
  "r2_secret_access_key": "",
  "r2_bucket_name": "",
  "permission": 0,
  "comp_name": "btr2_comp",
  "compress": true,
  "extension": "zip",
  "compression_level": 5,
  "fb_path": "smp/"
}
```

### Extension examples:

| `extension` | Output file | Notes |
|---|---|---|
| `zip` | `btr2_comp.zip` | Default, widely compatible |
| `tar` | `btr2_comp.tar` | No compression, fastest |
| `gztar` | `btr2_comp.tar.gz` | Good balance of speed and size |
| `bztar` | `btr2_comp.tar.bz2` | Better compression than gzip, slower |
| `xztar` | `btr2_comp.tar.xz` | Best compression ratio, slowest |
