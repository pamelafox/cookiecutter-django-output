from storages.backends.azure_storage import AzureStorage


class StaticRootAzureStorage(AzureStorage):
    azure_container = "static"
    expiration_secs = None


class MediaRootAzureStorage(AzureStorage):
    azure_container = "media"
    file_overwrite = False
    expiration_secs = 60 * 60 * 24 * 7  # 1 week
