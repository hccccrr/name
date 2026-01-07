import os
import time
import asyncio
from prettytable import PrettyTable

try:
    from pyrogram import Client
    from pyrogram.raw.functions.account import ReportPeer
    from pyrogram.raw.types import (
        InputPeerUser, InputPeerChannel, InputPeerChat,
        InputReportReasonSpam, InputReportReasonPornography,
        InputReportReasonViolence, InputReportReasonChildAbuse,
        InputReportReasonOther, InputReportReasonCopyright,
        InputReportReasonFake, InputReportReasonGeoIrrelevant,
        InputReportReasonIllegalDrugs, InputReportReasonPersonalDetails
    )
except ImportError:
    os.system("pip install pyrogram")
    from pyrogram import Client
    from pyrogram.raw.functions.account import ReportPeer
    from pyrogram.raw.types import (
        InputPeerUser, InputPeerChannel, InputPeerChat,
        InputReportReasonSpam, InputReportReasonPornography,
        InputReportReasonViolence, InputReportReasonChildAbuse,
        InputReportReasonOther, InputReportReasonCopyright,
        InputReportReasonFake, InputReportReasonGeoIrrelevant,
        InputReportReasonIllegalDrugs, InputReportReasonPersonalDetails
    )

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'

def clear():
    os.system('clear')

clear()

t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Method{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}Report Spam{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}Report Pornography{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}Report Violence{lrd}'])
t.add_row([f'{lgn}4{lrd}', f'{gn}Report Child Abuse{lrd}'])
t.add_row([f'{lgn}5{lrd}', f'{gn}Report Other{lrd}'])
t.add_row([f'{lgn}6{lrd}', f'{gn}Report Copyright{lrd}'])
t.add_row([f'{lgn}7{lrd}', f'{gn}Report Fake{lrd}'])
t.add_row([f'{lgn}8{lrd}', f'{gn}Report Geo Irrelevant{lrd}'])
t.add_row([f'{lgn}9{lrd}', f'{gn}Report Illegal Drugs{lrd}'])
t.add_row([f'{lgn}10{lrd}', f'{gn}Report Personal Details{lrd}'])

print(f"{lrd}")
print(t)

class TelegramReporter:
    def __init__(self):
        self.api_id = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter API ID: {g}")
        self.api_hash = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter API Hash: {g}")
        self.phone_number = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter phone number (with +country code): {g}")
        self.password = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter 2FA password (leave empty if none): {g}")
        clear()
        print(f"{lrd}")
        print(t)
        self.method = input(f"{lrd}[{lgn}?{lrd}] {gn}Choose a method (1-10): {k}")
        self.target = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter Username or ID of the target (with @ if username): {k}")
        self.number = int(input(f"{lrd}[{lgn}+{lrd}] {gn}Number of reports (be careful, too many may ban your account): {k}"))
        self.message = "Reported for violation"  # Default message
        if self.method == "5":
            self.message = input(f"{lrd}[{lgn}?{lrd}] {gn}Enter report message: {k}")

    def get_reason(self):
        if self.method == "1":
            return InputReportReasonSpam()
        elif self.method == "2":
            return InputReportReasonPornography()
        elif self.method == "3":
            return InputReportReasonViolence()
        elif self.method == "4":
            return InputReportReasonChildAbuse()
        elif self.method == "5":
            return InputReportReasonOther()
        elif self.method == "6":
            return InputReportReasonCopyright()
        elif self.method == "7":
            return InputReportReasonFake()
        elif self.method == "8":
            return InputReportReasonGeoIrrelevant()
        elif self.method == "9":
            return InputReportReasonIllegalDrugs()
        elif self.method == "10":
            return InputReportReasonPersonalDetails()
        else:
            raise ValueError("Invalid method chosen")

    def report(self):
        app = Client("reporter", api_id=self.api_id, api_hash=self.api_hash, phone_number=self.phone_number)
        
        with app:
            try:
                peer = app.resolve_peer(self.target)
            except Exception as e:
                print(f'{lrd}[{rd}!{lrd}] {k}Error resolving peer: {e}')
                return

            reason = self.get_reason()

            for i in range(self.number):
                try:
                    app.invoke(ReportPeer(peer=peer, reason=reason, message=self.message))
                    print(f"{lrd}[{lgn}+{lrd}] {gn}Report sent: {i+1}")
                    time.sleep(2)  # Delay to avoid flood wait errors
                except Exception as e:
                    print(f"{lrd}[{rd}!{lrd}] {k}Error sending report {i+1}: {e}")
                    if "FLOOD_WAIT" in str(e):
                        print(f"{lrd}[{rd}!{lrd}] {k}Flood wait detected. Stopping.")
                        break

        print(f'\n\n{lrd}[{rd}-{lrd}] {k}Reporting finished! Note: Mass reporting from one account may not be effective and could lead to your account being restricted.')

reporter = TelegramReporter()
reporter.report()
