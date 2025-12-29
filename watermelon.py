#!/usr/bin/env python3
import argparse
from core.output import print_banner, info
from modules.param_discovery import run_param_discovery
from modules.sqli_detector import run_sqli_scan
from modules.xss_detector import run_xss_scan
from modules.wordpress import run_wp_scan
from modules.headers import run_header_scan

def main():
    parser = argparse.ArgumentParser(prog="watermelon")
    parser.add_argument("mode", choices=["scan", "param", "wp", "full"])
    parser.add_argument("-u", "--url", required=True)
    args = parser.parse_args()

    print_banner()

    if args.mode == "param":
        run_param_discovery(args.url)

    elif args.mode == "scan":
        run_header_scan(args.url)
        run_sqli_scan(args.url)
        run_xss_scan(args.url)

    elif args.mode == "wp":
        run_wp_scan(args.url)

    elif args.mode == "full":
        run_param_discovery(args.url)
        run_header_scan(args.url)
        run_sqli_scan(args.url)
        run_xss_scan(args.url)
        run_wp_scan(args.url)

    info("Analisis selesai.")

if __name__ == "__main__":
    main()
