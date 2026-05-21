# Linux File Permissions Analysis Lab

## Objective
To understand how Linux file permissions control access to files and directories.

## Tools Used
- ls -l
- chmod
- whoami

## Process
- Listed file permissions using `ls -l`
- Identified read, write, execute permissions
- Modified permissions using `chmod`
- Tested access changes with different permission settings

## Observations / Findings
- Files with 777 permissions are fully accessible to all users
- Restrictive permissions like 600 limit access to owner only

## Security Insight
Improper file permissions can expose sensitive data or allow unauthorized modification of system files.
