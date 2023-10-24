from provider import Provider
from downloader import Downloader
from reporter import Reporter

providers = ["epinion", "silverlining"]


def main():
    report: str = ""
    for name in providers:
        provider = Provider(name)
        downloader = Downloader(provider)
        report += downloader.sftp_to_local()
    handle_reporting(report)


def handle_reporting(report):
    reporter = Reporter(report)
    reporter.save_to_file()
    if "Error" in report:
        reporter.send_as_email()


if __name__ == "__main__":
    main()
