[English](readme.md) | Español

# Backup to R2 (btr2)

[![Descargas en Github](https://img.shields.io/github/downloads/judamar/BTR2/total?label=Descargas%20en%20Github&logo=github)](https://github.com/judamar/BTR2/releases)

Este es un complemento para [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) que permite subir la copia de seguridad realizada por [QuickBackupM](https://github.com/TISUnion/QuickBackupM) al almacenamiento [Cloudflare R2](https://www.cloudflare.com/developer-platform/r2/).

Requiere `>= v2.0.0a1` de [MCDReforged](https://github.com/Fallen-Breath/MCDReforged).

## Descripción

El complemento BTR2 es una herramienta para subir y descargar la copia de seguridad (Slot1 por defecto) al almacenamiento [Cloudflare R2](https://www.cloudflare.com/developer-platform/r2/) usando la API compatible con S3 mediante `boto3`.

## Comandos

El complemento BTR2 añade los siguientes comandos:

- `!!btr2`: Muestra el mensaje de ayuda.
- `!!btr2 upload`: Comprime la carpeta Slot1 (por defecto) y la sube al almacenamiento R2.
- `!!btr2 download`: Descarga la copia de seguridad desde el almacenamiento R2 y la extrae en Slot1 (por defecto).

## Requisitos

Instala lo siguiente:

```
pip install boto3
```

## Configuración

Puedes configurar el comportamiento del complemento en el archivo `config.json` con las siguientes opciones:

- **prefix**: Define el prefijo para los comandos del complemento.
- **source_path**: Ruta de la carpeta que se comprimirá y subirá.
- **dest_path**: Ruta donde se almacenarán las copias de seguridad descargadas.
- **r2_endpoint_url**: URL del endpoint de R2 (`https://<account_id>.r2.cloudflarestorage.com`), sigue este [tutorial](./tutorials/key_tuto-es.md).
- **r2_access_key_id**: Access Key ID del token de API de R2.
- **r2_secret_access_key**: Secret Access Key del token de API de R2.
- **r2_bucket_name**: Nombre del bucket de R2 a utilizar.
- **permission**: Nivel mínimo de permiso requerido para ejecutar los comandos.
- **comp_name**: Nombre del archivo comprimido (sin extensión).
- **compress**: Si se debe comprimir la copia de seguridad antes de subirla. Si es `false`, los archivos se suben individualmente sin comprimir.
- **extension**: Formato de archivo a usar para la compresión. Valores soportados:
  - `zip` — Archivo ZIP (por defecto, amplia compatibilidad)
  - `tar` — Archivo TAR sin compresión
  - `gztar` — TAR con compresión gzip (`.tar.gz`)
  - `bztar` — TAR con compresión bzip2 (`.tar.bz2`)
  - `xztar` — TAR con compresión xz (`.tar.xz`, mejor ratio de compresión)
- **compression_level**: Nivel de compresión del `0` (sin compresión) al `9` (máxima compresión). Por defecto es `5`.
- **fb_path**: Prefijo de ruta dentro del bucket de R2 donde se almacenan los archivos.

El complemento debería funcionar sin modificaciones adicionales, siempre que la configuración de R2 sea correcta.

### Configuración por defecto:

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

### Ejemplos de extensión:

| `extension` | Archivo generado | Notas |
|---|---|---|
| `zip` | `btr2_comp.zip` | Por defecto, amplia compatibilidad |
| `tar` | `btr2_comp.tar` | Sin compresión, más rápido |
| `gztar` | `btr2_comp.tar.gz` | Buen equilibrio entre velocidad y tamaño |
| `bztar` | `btr2_comp.tar.bz2` | Mejor compresión que gzip, más lento |
| `xztar` | `btr2_comp.tar.xz` | Mejor ratio de compresión, más lento |
