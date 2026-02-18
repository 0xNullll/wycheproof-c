def _lazy_import_hmac_parsers():
    from .hmac_parser import HMACSHA1, HMACSHA224, HMACSHA256, HMACSHA384, HMACSHA512, HMACSHA3_224, HMACSHA3_256, HMACSHA3_384, HMACSHA3_512
    return {"HMACSHA1": HMACSHA1, "HMACSHA224": HMACSHA224, "HMACSHA256": HMACSHA256, "HMACSHA384" : HMACSHA384, "HMACSHA512" : HMACSHA512,
            "HMACSHA3_224" : HMACSHA3_224, "HMACSHA3_256" : HMACSHA3_256, "HMACSHA3_384" : HMACSHA3_384, "HMACSHA3_512" : HMACSHA3_512}


# Consolidate everything into a single namespace
_parsers = {}
_parsers.update(_lazy_import_hmac_parsers())

# Make available as package-level imports
globals().update(_parsers)
__all__ = list(_parsers.keys())