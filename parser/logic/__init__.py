def _lazy_import_hmac_parsers():
    from .hmac_parser import HMAC_SHA1, HMAC_SHA224, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_SHA512_224, HMAC_SHA512_256, HMAC_SHA3_224, HMAC_SHA3_256, HMAC_SHA3_384, HMAC_SHA3_512
    return {"HMAC_SHA1": HMAC_SHA1, "HMAC_SHA224": HMAC_SHA224, "HMAC_SHA256": HMAC_SHA256, "HMAC_SHA384" : HMAC_SHA384, "HMAC_SHA512" : HMAC_SHA512, "HMAC_SHA512_224" : HMAC_SHA512_224, "HMAC_SHA512_256" : HMAC_SHA512_256,
            "HMAC_SHA3_224" : HMAC_SHA3_224, "HMAC_SHA3_256" : HMAC_SHA3_256, "HMAC_SHA3_384" : HMAC_SHA3_384, "HMAC_SHA3_512" : HMAC_SHA3_512}

def _lazy_import_kmac_parsers():
    from .kmac_parser import KMAC128_NO_S, KMAC256_NO_S
    return {"KMAC128_NO_S" : KMAC128_NO_S, "KMAC256_NO_S" : KMAC256_NO_S}

def _lazy_import_cmac_parsers():
    from .cmac_parser import AES_CMAC
    return {"AES_CMAC" : AES_CMAC}

def _lazy_import_gmac_parsers():
    from .gmac_parser import AES_GMAC
    return {"AES_GMAC" : AES_GMAC}

def _lazy_import_hkdf_parsers():
    from .hkdf_parser import HKDF_SHA1, HKDF_SHA256, HKDF_SHA384, HKDF_SHA512 
    return {"HKDF_SHA1" : HKDF_SHA1, "HKDF_SHA256" : HKDF_SHA256, "HKDF_SHA384" : HKDF_SHA384, "HKDF_SHA512" : HKDF_SHA512}

def _lazy_import_pbkdf2_hmac_parsers():
    from .pbkdf2_hmac_parser import PBKDF2_HMAC_SHA1, PBKDF2_HMAC_SHA224, PBKDF2_HMAC_SHA256, PBKDF2_HMAC_SHA384, PBKDF2_HMAC_SHA512
    return {"PBKDF2_HMAC_SHA1" : PBKDF2_HMAC_SHA1, "PBKDF2_HMAC_SHA224" : PBKDF2_HMAC_SHA224, "PBKDF2_HMAC_SHA256" : PBKDF2_HMAC_SHA256, "PBKDF2_HMAC_SHA384" : PBKDF2_HMAC_SHA384, "PBKDF2_HMAC_SHA512" : PBKDF2_HMAC_SHA512}

def _lazy_import_aes_mode_parsers():
    from .aes_modes_parser import AES_CBC_PKCS5 ,AES_GCM
    return {"AES_CBC_PKCS5" : AES_CBC_PKCS5, "AES_GCM" : AES_GCM}

def _lazy_import_chacha20_poly1305_parsers():
    from .chacha20_poly1305_parser import CHACHA20_POLY1305, XCHACHA20_POLY1305
    return {"CHACHA20_POLY1305" : CHACHA20_POLY1305, "XCHACHA20_POLY1305" : XCHACHA20_POLY1305}

# Consolidate everything into a single namespace
_parsers = {}
_parsers.update(_lazy_import_hmac_parsers())
_parsers.update(_lazy_import_kmac_parsers())
_parsers.update(_lazy_import_cmac_parsers())
_parsers.update(_lazy_import_gmac_parsers())
_parsers.update(_lazy_import_hkdf_parsers())
_parsers.update(_lazy_import_pbkdf2_hmac_parsers())
_parsers.update(_lazy_import_aes_mode_parsers())
_parsers.update(_lazy_import_chacha20_poly1305_parsers())

# Make available as package-level imports
globals().update(_parsers)
__all__ = list(_parsers.keys())