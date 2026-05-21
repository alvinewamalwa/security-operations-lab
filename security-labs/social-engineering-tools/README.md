# Social Engineering (SET & BeEF)

In this lab, I used the Social Engineering Toolkit (SET) and BeEF in a controlled and authorized environment to simulate social engineering attacks. The objective was to understand how attackers exploit human behavior to capture sensitive information such as login credentials.

---

## I) Infectious Media Generator

I used the Infectious Media Generator option in SET to simulate creating malicious media (e.g., USB drives or DVDs) that automatically execute code when inserted into a target system.

**Finding:**
This technique demonstrates how attackers can distribute infected media in public areas, relying on user curiosity to execute malicious payloads.

**Security Insight:**
If configured with a “phone home” feature, the attacker can track how many users executed the payload, providing measurable results of user susceptibility.

---

## II) Website Cloning & Credential Harvester

I used the Credential Harvester attack method in SET to clone a legitimate login page and capture user credentials.

- I selected the **3rd method**, which allows the use of a custom website for the exploit.
- I cloned the DVWA login page using the URL: DVWA.vm/login.php

---

## III) Capturing and Viewing User Credentials

To simulate user interaction and redirection, I implemented the following code:

```html
<html>
<head>
<meta http-equiv="refresh" content="0; url=http://10.6.6.1/" />
</head>
</html>
```
When credentials were entered into the cloned page, the browser redirected to:

http://10.6.6.1/

After login, the user was redirected back to the legitimate site:

DVWA.vm/login.php

Observation:
The user believed they were interacting with the real website, while their credentials were captured by the cloned page.

Captured Information:

Username
Password

Finding:
The cloned webpage successfully harvested user credentials before redirecting the victim to the legitimate site, making the attack less noticeable.

IV) Attack Scenario & Real-World Application

I observed that this technique can be used in phishing attacks by:

Sending emails containing a fake login URL
Directing users to a cloned website that appears legitimate
Capturing credentials when users attempt to log in

Impact:
An attacker could use the harvested credentials to:

Access the real system as a legitimate user
Escalate privileges
Perform further attacks within the network
V) BeEF Integration

I also used BeEF alongside SET to enhance the attack.

SET enabled website cloning and credential harvesting (server-side attack)
BeEF enabled browser exploitation and command execution (client-side attack)

Insight:
Combining SET and BeEF allows attackers to:

Capture credentials
Maintain control over the victim’s browser
Execute further actions after initial compromise
Key Lessons Learned
Human factors are a major vulnerability in cybersecurity
Users can be easily deceived by realistic-looking websites
Social engineering attacks can bypass technical defenses
Mitigation Strategies
Conduct regular security awareness training
Educate users to verify URLs before logging in
Implement multi-factor authentication (MFA)
Disable autorun for removable media
Use email filtering to detect phishing attempts
