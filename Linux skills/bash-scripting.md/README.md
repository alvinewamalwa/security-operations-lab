Bash scripting is used in Linux to automate repetitive tasks, manage system operations, and improve efficiency in command-line workflows. In this section, I practiced writing simple scripts to demonstrate automation and basic logic in Linux.

---

## I) Basic Script Structure

I learned that every Bash script starts with a shebang line that tells the system which interpreter to use:

```bash
#!/bin/bash
```
I then created scripts that execute Linux commands in sequence.
II) Simple Automation Script

I wrote a basic script to automate system information display:

#!/bin/bash

echo "System Information"
uname -a
echo "Current User:"
whoami
echo "Current Directory:"
pwd
III) Variables in Bash

I used variables to store and reuse values:

#!/bin/bash

name="Kali User"
echo "Hello, $name"
IV) Conditional Statements

I practiced basic decision-making using if-else statements:

#!/bin/bash

echo "Enter a number:"
read num

if [ $num -gt 10 ]
then
  echo "Number is greater than 10"
else
  echo "Number is 10 or less"
fi
V) Loops

I used loops to repeat tasks automatically:

#!/bin/bash

for i in 1 2 3 4 5
do
  echo "Iteration $i"
done
VI) Practical Use in Cybersecurity

Bash scripting is useful in cybersecurity for:

Automating reconnaissance tasks
Running repetitive scans
Parsing log files
Managing system monitoring tasks
Automating basic penetration testing workflows
