import re

with open("list.txt", "r") as f:
    content = f.read()

# Match IP, hostname, and credential status
entries = re.findall(
    r'(\d{1,3}(?:\.\d{1,3}){3})\n\n(.*?) OS Credentials:\n\n(.*?)(?=\n\n\d{1,3}|\Z)',
    content,
    re.DOTALL
)

# Markdown table header
md = "| IP Address       | Hostname | Credentials         |\n"
md += "|------------------|----------|---------------------|\n"

# Prepare IP list for spray
iplist = []

for ip, hostname, creds in entries:
    creds = creds.strip()
    display_creds = "" if "No credentials" in creds else creds
    md += f"| {ip:<16} | {hostname:<8} | {display_creds:<19} |\n"
    iplist.append(ip)

# Save Markdown table
with open("ip.md", "w") as f:
    f.write(md)

# Save flat IP list
with open("ips.txt", "w") as f:
    f.write("\n".join(iplist))

print("[+] Markdown table saved to ip.md")
print("[+] IP list saved to ips.txt")
