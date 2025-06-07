# x365 ai automation using python script
Automating the x365.ai Token Claim Process explained in this [video](https://www.youtube.com/watch?v=X8zRZQ_YMwI)

<a href="https://www.youtube.com/watch?v=X8zRZQ_YMwI&t=9s" target="_blank">
  <img width="556" alt="x365Automate-c-sharp" src="https://github.com/user-attachments/assets/5441888e-3719-4ec8-af19-0974872d9149" />
</a>

After downloading these files, navigate to the downloaded folder and type 'cmd' in file explorer address bar and press enter. This will open the command prompt and enter the command 'python automate.py'.

Before launching running this script, make sure to configure the user login details in the 'appsettings.json' file, as shown below.

```
{
    "AppSettings": {
      "LoginUrl": "https://x365.ai/login",
      "ActionUrl": "https://x365.ai/quantum",
      "email": "Testuser@gmail.com",
      "password": "Testuser@12345",
      "intervalInMinutes": "10",
      "closePopups": "false"
    }
  }
```
  
'intervalInMinutes' - defines how often the flow should run continuously, with the interval specified in minutes using this parameter.

'closePopups' - Some times it display popups that can interfere with button clicks. If you notice any popup appearing on the page, set this option to true. It will automatically close the popup, allowing the button click to work properly.

### Prerequisites

1. Install the [python](https://www.python.org/downloads/)
2. Ensure an active internet connection
3. Have your x365 account credentials ready
4. Use a Windows machine

While running this script if you face any issue python module installation, run the below commands to install those modules
```
> pip install selenium
> pip install webdriver_manager
```


