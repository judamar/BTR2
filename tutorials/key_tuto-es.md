[English](key_tuto.md) | Español

# Tutorial - Configuración de Cloudflare R2

1. Ve a [Cloudflare](https://dash.cloudflare.com/) e inicia sesión (o crea una cuenta gratuita).
2. En el panel izquierdo, haz clic en **R2 Object Storage**.
3. Haz clic en **Create bucket**, ponle un nombre (por ejemplo, `my-mc-backup`), elige una región o déjala en automático, y haz clic en **Create bucket**.
4. En la página de resumen de R2 (antes de entrar al bucket), localiza tu **Account ID** en el lado derecho de la página. Tu URL de endpoint será:
   ```
   https://<account_id>.r2.cloudflarestorage.com
   ```
5. Ve al resumen de **R2 Object Storage** y haz clic en **Manage R2 API Tokens** (esquina superior derecha).
6. Haz clic en **Create API Token**, ponle un nombre, establece los **Permissions** en **Object Read & Write**, y en **Specify bucket(s)** selecciona el bucket que acabas de crear. Haz clic en **Create API Token**.
7. Copia el **Access Key ID** y el **Secret Access Key** que aparecen en la siguiente pantalla — **no se mostrarán de nuevo**.
8. Rellena tu `config.json` con los valores obtenidos:

```json
{
  "r2_endpoint_url": "https://<account_id>.r2.cloudflarestorage.com",
  "r2_access_key_id": "<tu_access_key_id>",
  "r2_secret_access_key": "<tu_secret_access_key>",
  "r2_bucket_name": "<nombre_de_tu_bucket>"
}
```

Ya puedes correr el plugin de forma correcta.
