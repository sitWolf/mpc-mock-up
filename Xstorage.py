from whitenoise.storage import CompressedManifestStaticFilesStorage


class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    #manifest_strict = False
    WHITENOISE_MANIFEST_STRICT = False
