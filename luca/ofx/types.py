"""Classes representing OFX data."""

class Application(object):
    def __init__(self, name, appid, appver):
        self.name = name
        self.appid = appid
        self.appver = appver

class FinancialInstitution(object):
    def __init__(self, name, url, org, fid, version):
        self.name = name
        self.url = url
        self.org = org
        self.fid = fid
        self.version = version

class Account(object):
    def __init__(self, bankid, acctid, accttype):
        self.bankid = bankid
        self.acctid = acctid
        self.accttype = accttype
        self.key = (bankid, acctid, accttype)

class Transaction(object):
    def __init__(self, trntype, dtposted, trnamt, fitid, checknum, name):
        self.trntype = trntype
        self.dtposted = dtposted
        self.trnamt = trnamt
        self.fitid = fitid
        self.checknum = checknum
        self.name = name
