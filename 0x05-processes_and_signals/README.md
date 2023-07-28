# 0x05. Processes and signals

## Tasks

### 0. What is my PID

Write a Bash script that displays its own PID.


### 1. List your processes

Write a Bash script that displays a list of currently running processes.

-   Must show all processes, for all users, including those which might not have a TTY
-   Display in a user-oriented format
-   Show process hierarchy


### 2. Show your Bash PID


Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.


-   You cannot use `pgrep`
-   The third line of your script must be `# shellcheck disable=SC2009` 
### 3. Show your Bash PID made easy


Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

-   You cannot use `ps`


### 4. To infinity and beyond


Write a Bash script that displays `To infinity and beyond` indefinitely.


-   In between each iteration of the loop, add a `sleep 2`

### 5. Don't stop me now!


Write a Bash script that stops `4-to_infinity_and_beyond` process.


-   You must use `kill`


### 6. Stop me if you can


Write a Bash script that stops `4-to_infinity_and_beyond` process.



-   You cannot use `kill` or `killall`



### 7. Highlander

Write a Bash script that displays:

-   `To infinity and beyond` indefinitely
-   With a `sleep 2` in between each iteration
-   `I am invincible!!!` when receiving a `SIGTERM` signal


### 8. Beheaded process


Write a Bash script that kills the process `7-highlander`.

