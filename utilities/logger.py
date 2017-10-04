import logging


def log(msga, msgb):
    logging.basicConfig(
        format='%(asctime)s --- %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )
    logging.info('%s --- %s', msga, msgb)
