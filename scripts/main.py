from provider import Provider
from downloader import Downloader
from reporter import Reporter

providers = ["epinion", "silverlining"]


def main():
    for item in providers:
        try:
            provider = Provider(item)
            downloader = Downloader(provider)
            downloader.sftp_to_local()
        except Exception as e:
            msg = f"Error while downloading from {provider.name}: {e}"
            print(msg)
            reporter = Reporter(msg)
            reporter.save_to_file()
            
if __name__ == "__main__":
    main()
