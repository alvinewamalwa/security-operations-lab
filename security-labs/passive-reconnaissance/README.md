#Source / Learning Context
This lab was completed as part of the Cisco Networking Academy cybersecurity training program. All activities were performed in a controlled lab environment for educational purposes, following ethical guidelines.

This section demonstrates my hands-on experience with passive reconnaissance techniques used to gather publicly available information without directly interacting with the target.

Tools & Techniques Used

* Recon-ng (module installation, execution, and reporting)
  
a) ![Recon-ng Module Execution](screenshots/recon-ng-module-execution-output..png)
I executed Recon-ng modules from the marketplace to perform OSINT data collection. I ran both the hackertarget and bing modules and in each I found 7 subdomains that had been listed. The results of the hosts found are shown in the screenshot above.

b) ![Recon-ng Module Execution](screenshots/recon-ng-interestingfiles.png)

I went ahead and tried to find interesting files following the same method used in running the hackertarget and bing modules in part(a). I ran the module as shown and even found that it creates a CSV file in the recon-ng/data folder which makes analysis and presentation of reports easier.


  
* DNS enumeration (nslookup, dig, host)

  I used nslookup to obtain domain and IP address information by simply running on the terminal (nslookup cisco.com) by default the nslookup command queries A and AAAA records for the target.
  In the case where the local DNS server is unable to resolve an address or resolves the host name to an additional private address and I need to obtain the internet accessible address of the host, I'd simply change the server used to perform lookuop ie; nslookup netacad.com 8.8.8.8 therefore displaying all the record types.
  
* WHOIS lookups
  Whois can also be used to gather information about IP address ranges that are assigned to an organisation ie whois72.163.5.201

* dig

  I used dig to query for DNS servers and I found that Dig queries only the A record type. However I used it to obtain additional information ie: dig cisco.com 8.8.8.8 ns
  
* Reverse DNS analysis
I used dig to perform reverse DNS lookups to obtain the domain name by simply running dig -x 72.163.5.201 and I found that PTR record is returned with the hostname. I went ahead and examined the output returned from the dig command (dig -x 72.163.1.1) and I could deduce that the type of device assigned the 72.163.1.1 address is an HSRP router configuration since the host is named hsrp-72-163-1-1
  
* Google dorking
  
* SpiderFoot (OSINT automation) I also used SpiderFoot to find usernames in email addresses that are associated with a company or domain. I found that SpiderFoot offers the option of choosing scans based on use case, required data.
  
* Email harvesting techniques

Key Activities

* Installed and executed Recon-ng marketplace modules to collect OSINT data
* Generated structured reports using Recon-ng reporting features
* Identified publicly exposed files using search-based reconnaissance
* Performed DNS analysis to map domain-to-IP relationships
* Compared outputs across multiple DNS tools for accuracy
* Conducted reverse DNS lookups for infrastructure insight


Outcome

Developed a strong understanding of how attackers gather intelligence during the reconnaissance phase and how publicly available data can expose critical information.


