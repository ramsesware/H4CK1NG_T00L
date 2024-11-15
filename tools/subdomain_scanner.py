import requests
from concurrent.futures import ThreadPoolExecutor
from tkinter import messagebox
import tkinter as tk
import dns.resolver
import dns.zone
import dns.query
import re

stop_scan = False

def automatic_subdomain_scan(domain, result_text, progress_bar):
    global stop_scan
    stop_scan = False

    progress_bar["value"] = 0
    progress_bar["maximum"] = calculate_total_tasks(domain)

    getNSRecord(domain, result_text, progress_bar)
    getMXRecord(domain, result_text, progress_bar)
    getTXTRecord(domain, result_text, progress_bar)
    getCNAMERecord(domain, result_text, progress_bar)




def getMXRecord(domain, result_text, progress_bar):
    try:

        mx_records = dns.resolver.resolve(domain, 'MX')
        for mx in mx_records:
            mx_target = mx.exchange.to_text().strip('.')
            result_text.insert(tk.END, f"Found MX record: {mx_target}\n")
            progress_bar["value"] += 1
            progress_bar.update_idletasks()
    except dns.resolver.NoAnswer:
        result_text.insert(tk.END,f"No MX records found for {domain}.\n")
    except dns.exception.Timeout:
        result_text.insert(tk.END,"DNS query timed out.\n")
    except Exception as e:
        result_text.insert(tk.END,f"Error scanning subdomains: {e}\n")

def getTXTRecord(domain, result_text, progress_bar):
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        for txt in txt_records:
            txt_data = txt.to_text()
            potential_domains = re.findall(r'[a-zA-Z0-9._\-~!$&()*+,;=]+\.' + re.escape(domain), txt_data)
            for pd in potential_domains:
                if pd != "":
                    result_text.insert(tk.END, f"Found TXT record: {potential_domains}\n")
                progress_bar["value"] += 1
                progress_bar.update_idletasks()

    except dns.resolver.NoAnswer:
        result_text.insert(tk.END,f"No TXT records found for {domain}.\n")
    except dns.exception.Timeout:
        result_text.insert(tk.END,"DNS query timed out.\n")
    except Exception as e:
        result_text.insert(tk.END,f"Error scanning subdomains: {e}\n")
    
        

def getCNAMERecord(domain, result_text, progress_bar):
    try:
        cname_records = dns.resolver.resolve(domain, 'CNAME')
        for cname in cname_records:
            cname_target = cname.target.to_text().strip('.')
            result_text.insert(tk.END,f"Found CNAME record: {cname_target}")
            progress_bar["value"] += 1
            progress_bar.update_idletasks()
    except dns.resolver.NoAnswer:
        result_text.insert(tk.END,f"No CNAME records found for {domain}.\n")
    except dns.exception.Timeout:
        result_text.insert(tk.END,"DNS query timed out.\n")
    except Exception as e:
        result_text.insert(tk.END,f"Error scanning subdomains: {e}\n")

def getNSRecord(domain, result_text, progress_bar):
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        name_servers = [ns.target.to_text() for ns in ns_records]
        result_text.insert(tk.END, f"Name servers for {domain}:\n")
        for ns in name_servers:
            result_text.insert(tk.END, f"NS: {ns}\n")
            progress_bar["value"] += 1
            progress_bar.update_idletasks()
    except dns.resolver.NoAnswer:
        result_text.insert(tk.END,f"No NS records found for {domain}.\n")
    except dns.exception.Timeout:
        result_text.insert(tk.END,"DNS query timed out.\n")
    except Exception as e:
        result_text.insert(tk.END,f"Error scanning subdomains: {e}\n")

def start_automatic_subdomain_scan(domain_entry, result_text, progress_bar):

    result_text.delete(1.0, tk.END)
    if not domain_entry:
        messagebox.showinfo("Error", "Please enter a domain.")
        return

    automatic_subdomain_scan(domain_entry, result_text, progress_bar)

    result_text.insert(tk.END, "\nScan completed.\n")
    progress_bar["value"] = progress_bar["maximum"]

def stop_analysis():
    global stop_scan
    stop_scan = True
    messagebox.showinfo("Scan stoped", "The directory scan has been stoped.")

def calculate_total_tasks(domain):

    total_tasks = 0

    try:
        total_tasks += len(dns.resolver.resolve(domain, 'NS'))
    except Exception:
        pass

    try:
        total_tasks += len(dns.resolver.resolve(domain, 'MX'))
    except Exception:
        pass

    try:
        total_tasks += len(dns.resolver.resolve(domain, 'TXT'))
    except Exception:
        pass

    try:
        total_tasks += len(dns.resolver.resolve(domain, 'CNAME'))
    except Exception:
        pass

    return total_tasks