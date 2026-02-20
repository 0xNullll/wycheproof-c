import os
from logic import (
    hmac_parser,
    kmac_parser,
    cmac_parser,
    gmac_parser,
    hkdf_parser,
    pbkdf2_hmac_parser,
    aes_modes_parser,
    chacha20_poly1305_parser
)

def get_target_files(directory_path, prefixes, suffix, exclusion=None):
    """
    Fetch target files matching specific prefixes and suffix in the directory.
    Optionally exclude files containing specific substrings.

    :param directory_path: Directory where JSON test vectors are stored
    :param prefixes: Tuple of prefixes to filter files
    :param suffix: Suffix to filter files
    :param exclusion: Tuple of substrings to exclude files containing them
    :return: List of matching file names
    """
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return []

    if isinstance(prefixes, str):
        prefixes = (prefixes,)
    if exclusion and isinstance(exclusion, str):
        exclusion = (exclusion,)

    all_files = os.listdir(directory_path)

    matching_files = [
        f for f in all_files
        if f.endswith(suffix) and any(f == p + suffix for p in prefixes)
    ]
    if exclusion:
        matching_files = [f for f in matching_files if not any(excl in f for excl in exclusion)]

    return matching_files


# Parser metadata
PARSERS = [
    # name, parser_class, prefixes, suffix, output_c_header, optional exclusion
    ("HMAC-SHA1", hmac_parser.HMAC_SHA1, ("hmac_sha1",), "_test.json", "./parsed_vectors/tv_hmac_sha1.h", None),
    ("HMAC-SHA224", hmac_parser.HMAC_SHA224, ("hmac_sha224",), "_test.json", "./parsed_vectors/tv_hmac_sha224.h", None),
    ("HMAC-SHA256", hmac_parser.HMAC_SHA256, ("hmac_sha256",), "_test.json", "./parsed_vectors/tv_hmac_sha256.h", None),
    ("HMAC-SHA384", hmac_parser.HMAC_SHA384, ("hmac_sha384",), "_test.json", "./parsed_vectors/tv_hmac_sha384.h", None),
    ("HMAC-SHA512", hmac_parser.HMAC_SHA512, ("hmac_sha512",), "_test.json", "./parsed_vectors/tv_hmac_sha512.h", None),
    ("HMAC-SHA512_224", hmac_parser.HMAC_SHA512_224, ("hmac_sha512_224",), "_test.json", "./parsed_vectors/tv_hmac_sha512_224.h", None),
    ("HMAC-SHA512_256", hmac_parser.HMAC_SHA512_256, ("hmac_sha512_256",), "_test.json", "./parsed_vectors/tv_hmac_sha512_256.h", None),
    ("HMAC-SHA3_224", hmac_parser.HMAC_SHA3_224, ("hmac_sha3_224",), "_test.json", "./parsed_vectors/tv_hmac_sha3_224.h", None),
    ("HMAC-SHA3_256", hmac_parser.HMAC_SHA3_256, ("hmac_sha3_256",), "_test.json", "./parsed_vectors/tv_hmac_sha3_256.h", None),
    ("HMAC-SHA3_384", hmac_parser.HMAC_SHA3_384, ("hmac_sha3_384",), "_test.json", "./parsed_vectors/tv_hmac_sha3_384.h", None),
    ("HMAC-SHA3_512", hmac_parser.HMAC_SHA3_512, ("hmac_sha3_512",), "_test.json", "./parsed_vectors/tv_hmac_sha3_512.h", None),
    ("KMAC128_NO_CUSTOMIZATION", kmac_parser.KMAC128_NO_S, ("kmac128_no_customization_test",), "_test.json", "./parsed_vectors/tv_kmac128_no_customization.h", None),
    ("KMAC256_NO_CUSTOMIZATION", kmac_parser.KMAC256_NO_S, ("kmac256_no_customization_test",), "_test.json", "./parsed_vectors/tv_kmac256_no_customization.h", None),
    ("AES-CMAC", cmac_parser.AES_CMAC, ("aes_cmac_test",), "_test.json", "./parsed_vectors/tv_aes_cmac.h", None),
    ("AES-GMAC", gmac_parser.AES_GMAC, ("aes_gmac_test",), "_test.json", "./parsed_vectors/tv_aes_gmac.h", None),
    ("HKDF-SHA1", hkdf_parser.HKDF_SHA1, ("hkdf_sha1",), "_test.json", "./parsed_vectors/tv_hkdf_sha1.h", None),
    ("HKDF-SHA256", hkdf_parser.HKDF_SHA256, ("hkdf_sha256",), "_test.json", "./parsed_vectors/tv_hkdf_sha256.h", None),
    ("HKDF-SHA384", hkdf_parser.HKDF_SHA384, ("hkdf_sha384",), "_test.json", "./parsed_vectors/tv_hkdf_sha384.h", None),
    ("HKDF-SHA512", hkdf_parser.HKDF_SHA512, ("hkdf_sha512",), "_test.json", "./parsed_vectors/tv_hkdf_sha512.h", None),
    ("PBKDF2-HMAC-SHA1", pbkdf2_hmac_parser.PBKDF2_HMAC_SHA1, ("pbkdf2_hmacsha1",), "_test.json", "./parsed_vectors/tv_pbkdf2_hmac_sha1.h", None),
    ("PBKDF2-HMAC-SHA224", pbkdf2_hmac_parser.PBKDF2_HMAC_SHA224, ("pbkdf2_hmacsha224",), "_test.json", "./parsed_vectors/tv_pbkdf2_hmac_sha224.h", None),
    ("PBKDF2-HMAC-SHA256", pbkdf2_hmac_parser.PBKDF2_HMAC_SHA256, ("pbkdf2_hmacsha256",), "_test.json", "./parsed_vectors/tv_pbkdf2_hmac_sha256.h", None),
    ("PBKDF2-HMAC-SHA384", pbkdf2_hmac_parser.PBKDF2_HMAC_SHA384, ("pbkdf2_hmacsha384",), "_test.json", "./parsed_vectors/tv_pbkdf2_hmac_sha384.h", None),
    ("PBKDF2-HMAC-SHA512", pbkdf2_hmac_parser.PBKDF2_HMAC_SHA512, ("pbkdf2_hmacsha512",), "_test.json", "./parsed_vectors/tv_pbkdf2_hmac_sha512.h", None),
    ("AES-CBC-PKCS5", aes_modes_parser.AES_CBC_PKCS5, ("aes_cbc_pkcs5",), "_test.json", "./parsed_vectors/tv_aes_cbc_pkcs5.h", None),
    ("AES-GCM", aes_modes_parser.AES_GCM, ("aes_gcm",), "_test.json", "./parsed_vectors/tv_aes_gcm.h", None),
    ("ChaCha20-Poly1305", chacha20_poly1305_parser.CHACHA20_POLY1305, ("chacha20_poly1305",), "_test.json", "./parsed_vectors/tv_chacha20_poly1305.h", None),
    ("XChaCha20-Poly1305", chacha20_poly1305_parser.XCHACHA20_POLY1305, ("xchacha20_poly1305",), "_test.json", "./parsed_vectors/tv_xchacha20_poly1305.h", None),
]

def parse_specific_algorithm():
    print("Choose an algorithm to parse:")
    for idx, (name, *_rest) in enumerate(PARSERS, start=1):
        print(f"{idx}. {name}")

    selection = input("Enter the number of the algorithm to parse: ")
    try:
        idx = int(selection) - 1
        name, parser_class, prefixes, suffix, output, exclude = PARSERS[idx]
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        return

    directory_path = "vectors/"
    target_files = get_target_files(directory_path, prefixes, suffix, exclude)
    if not target_files:
        print(f"No matching files found for {name}.")
        return

    parser = parser_class(directory_path=directory_path, output_c_header=output, target_files=target_files)
    print(f"Parsing {name}...")
    parser.parse()
    print(f"Finished parsing {name}. Output written to {output}.")


def parse_all_algorithms():
    directory_path = "vectors/"
    for name, parser_class, prefixes, suffix, output, exclude in PARSERS:
        target_files = get_target_files(directory_path, prefixes, suffix, exclude)
        if not target_files:
            print(f"No files found for {name}, skipping.")
            continue

        parser = parser_class(directory_path=directory_path, output_c_header=output, target_files=target_files)
        print(f"Parsing {name}...")
        parser.parse()
        print(f"Finished parsing {name}. Output written to {output}.")

    print("Finished parsing all algorithms.")


def main():
    print("Welcome to the test vector parser.")
    print("Please choose an option:")
    print("1. Parse specific algorithm")
    print("2. Parse all algorithms")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        parse_specific_algorithm()
    elif choice == "2":
        parse_all_algorithms()
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()