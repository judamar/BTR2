English | [Español](key_tuto-es.md)

# Tutorial - Cloudflare R2 Setup

1. Go to [Cloudflare](https://dash.cloudflare.com/) and sign in (or create a free account).
2. In the left sidebar, click on **R2 Object Storage**.
3. Click **Create bucket**, give it a name (e.g. `my-mc-backup`), choose a region or leave it as automatic, then click **Create bucket**.
4. On the R2 overview page (before entering the bucket), locate your **Account ID** on the right side of the page. Your endpoint URL will be:
   ```
   https://<account_id>.r2.cloudflarestorage.com
   ```
5. Go to **R2 Object Storage** overview and click **Manage R2 API Tokens** (top-right corner).
6. Click **Create API Token**, give it a name, set **Permissions** to **Object Read & Write**, and under **Specify bucket(s)** select the bucket you just created. Click **Create API Token**.
7. Copy the **Access Key ID** and **Secret Access Key** shown on the next screen — **these will not be shown again**.
8. Fill in your `config.json` with the values obtained:

```json
{
  "r2_endpoint_url": "https://<account_id>.r2.cloudflarestorage.com",
  "r2_access_key_id": "<your_access_key_id>",
  "r2_secret_access_key": "<your_secret_access_key>",
  "r2_bucket_name": "<your_bucket_name>"
}
```

Now you can run the plugin correctly.
