import urllib.request
import os
import hashlib
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(
        prog="HIBP checker",
        description="Check if a password (hash) is present in the HIBP database",
        allow_abbrev=True
    )
    parser.add_argument("-f", "--file", dest="filepath", required=True, help="File path to password list")
    parser.add_argument("-s", "--sha1", dest="ishash", required=False, action="store_const", const=True, default=False,
                        help="Provided password are already (SHA1) hashed? (default: False)")

    args = parser.parse_args()

    checkfile(args.filepath, args.ishash)


def checkfile(filepath, ishash=False):
    if not os.path.isfile(filepath):
        logging.error("File path {} does not exist. Exiting...".format(filepath))
        raise FileNotFoundError("File path {} does not exist. Exiting...".format(filepath))

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()

            logging.debug("Checking '{}'".format(line))

            pwhash = hash_sha1(line, ishash)

            logging.debug(" > Checking hash '{}'".format(pwhash))

            found, occ = check_hibp(pwhash)
            if found:
                print(" - Found matching entry on HIBP for '{}'. It has occurred {} times.".format(line, occ))
            else:
                print(" + Found no matching entry found on HIBP for '{}'".format(line))


def hash_sha1(password, ishash=False):
    if ishash:
        logging.debug(" - Already a SHA1 hash '{}'".format(password))
        return password
    else:
        hash = hashlib.sha1(password.encode()).hexdigest().upper()
        logging.debug(" - Hash for '{}' is '{}'".format(password, hash))
        return hash


def check_hibp(pwhash):
    prefix = pwhash[:5]
    suffix = pwhash[5:]

    logging.debug(" - Requesting list based on prefix '{}'".format(prefix))

    with urllib.request.urlopen("https://api.pwnedpasswords.com/range/{}".format(prefix)) as resp:
        for line in resp:
            line = line.decode('utf-8').strip()
            if line.split(":")[0] == suffix:
                occ = line.split(":")[1]
                logging.debug(" - hash found: '{}'".format(pwhash))
                logging.debug(" - password occurrence: {}".format(occ))
                return True, occ
    return False, None


if __name__ == "__main__":
    main()
