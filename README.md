# README

## Required Packages:
- selenium
- schedule
- time
- pause

## Setup
1. set password and username 
```
browser.find_element_by_id("okta-signin-username").send_keys("")
browser.find_element_by_id ("okta-signin-password").send_keys("")
```

2. set cookie location
```
options.add_argument("user-data-dir=/Users/clemens/Library/Application Support/Google/Chrome/selenium")
```

3. set time when you want to gym (this script tries to register for last session on the registration website, e.g. 15:59:58 will most likely result in a 4pm booking)
```
schedule.every().day.at("15:59:58").do(register_latest)
```

# Note
The first time you run it, it will fail due to two-factor auth. However continue manually and click don't challenge me on this device for 30 days. Then it'll work for the next 30 days.
