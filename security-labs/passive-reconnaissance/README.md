#Source / Learning Context
This lab was completed as part of the Cisco Networking Academy cybersecurity training program. All activities were performed in a controlled lab environment for educational purposes, following ethical guidelines.

This section demonstrates my hands-on experience with passive reconnaissance techniques used to gather publicly available information without directly interacting with the target.

Tools & Techniques Used

* Recon-ng (module installation, execution, and reporting)
  
a) ![Recon-ng Module Execution](screenshots/recon-ng-module-execution-output..png)
I executed Recon-ng modules from the marketplace to perform OSINT data collection. I ran both the hackertarget and bing modules and in each I found 7 subdomains that had been listed. The results are shown in a tabular form in the screenshot above

b) ![Recon-ng Module Execution](screenshots/recon-ng-interestingfiles.png)

I went ahead and tried to find interesting files following the same method in running the hackertarget and bing modules above. I ran the module as shown and even found that it creates a CSV file in the recon-ng/data folder which makes analysis and presentation of reports easier.


  
* DNS enumeration (nslookup, dig, host)
* WHOIS lookups
* Reverse DNS analysis
* Google dorking
* SpiderFoot (OSINT automation)
* Email harvesting techniques

Key Activities

* Installed and executed Recon-ng marketplace modules to collect OSINT data
* Generated structured reports using Recon-ng reporting features
* Identified publicly exposed files using search-based reconnaissance
* Performed DNS analysis to map domain-to-IP relationships
* Compared outputs across multiple DNS tools for accuracy
* Conducted reverse DNS lookups for infrastructure insight

Evidence

Screenshots of tool execution and results are included in the /screenshots directory.

Outcome

Developed a strong understanding of how attackers gather intelligence during the reconnaissance phase and how publicly available data can expose critical information.


