---
title: Mike Maynard | School Data Integration and Authentication Case Study - Account Creation
---
## [School Data Integration and Authentication Case Study](./)

### Account Creation Findings


| Product | Manual | Manual CSV | Automated CSV | Intra-vendor Integration | Other Provisioning Integrations | API |
| ------- | ------ | ----------- | ------- | ------ | ----------- | ------- |
| [Blackboard WCM](https://www.blackboard.com/engage-your-community/websites-branding/web-community-manager) | [Yes - Users Workspace](https://help.blackboard.com/Web_Community_Manager/Administrator/Users_and_Groups/Users/Edit_Users) | [Yes](https://help.blackboard.com/Web_Community_Manager/Administrator/Users_and_Groups/Users#import) | [Connector](https://help.blackboard.com/Web_Community_Manager/Administrator/Data_Integration_And_Automation/Universal_Connector) | Community Engagement |  | [Note](#Notes) |
| [Blackboard Mass Communication](https://www.blackboard.com/engage-your-community/communications/mass-notifications-for-k-12)| [Yes - Communications HQ](https://help.blackboard.com/Community_Engagement/Administrator/Community_Settings/Account_Management)  | [Yes](https://help.blackboard.com/Community_Engagement/Administrator/Community_Settings/Account_Management/Manage_User_Accounts/Upload_Accounts_from_Files) | [DataLink](https://help.blackboard.com/Community_Engagement/Administrator/Data_Imports) | WCM | | |
| [Clever Admin](https://support.clever.com/hc/s/articles/360026950471) | [Yes - Support Tools](https://support.clever.com/hc/s/articles/360026950471?language=en_US) | [Yes](https://support.clever.com/hc/s/articles/229253547?language=en_US) | [Yes](https://support.clever.com/hc/s/articles/229253547?language=en_US) | | [SIS Auto-sync](https://support.clever.com/hc/s/articles/202042973) | [Yes](https://dev.clever.com/) |
| [Freshservice](https://freshservice.com/) | [Yes - Admin](https://support.freshservice.com/support/solutions/articles/154762-adding-requesters-in-freshservice) | [Yes](https://support.freshservice.com/support/solutions/articles/154763-importing-requesters-from-a-csv-file) | [User Importer](https://www.freshworks.com/apps/freshservice/user_importer/) | [Freshworks Organization](https://support.freshservice.com/support/solutions/articles/50000002932-introducing-freshworks-organization) | [Google Workspace](https://support.google.com/a/answer/7364833?hl=en) &#124;<BR> [Azure AD](https://www.freshworks.com/apps/freshservice/azure_active_directory_provisioning_scim) | [Yes](https://api.freshservice.com/) |
| [Google Apps/Workspace for Education](https://edu.google.com/why-google/k-12-solutions/)| [Yes - Admin Console](https://support.google.com/a/answer/9970788?hl=en) | [Yes](https://support.google.com/a/answer/9970788?hl=en) | [Google SDS - EOL'd 2022](https://support.google.com/a/topic/6039552) | | [Clever IDM](https://clever.com/appstore/clever-idm) &#124;<BR> [Google Cloud Directory Sync - LDAP](https://support.google.com/a/answer/106368?hl=en)  | [Directory API](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users) |




Glossary:

* Manual - Entering data by hand in a console provided by the vendor
* Manual CSV - Uploading a file in the [comma separated value](https://en.wikipedia.org/wiki/Comma-separated_values) format using a console. Select the file and initiate the transfer.
* Automatic CSV - Transferring a file programmatically typically with the [SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) protocol.
* Intra-vendor Integration - Integrates data between two or more products from the same vendor.
* Other Provisioning Integrations - Third party partners that facilitate user creation integrations. Also can be through other data stores maintained by the school such as an LDAP server, SIS system or HR system.
* API - [Application programming interface](https://en.wikipedia.org/wiki/API)


##### Notes
Blackboard has a published [API](https://developer.blackboard.com/portal/displayApi) but appears to be specific to their 'Learn' products.


#### Next... [End-user Authentication Findings](authentication_findings.html)



---
[School Project Home](./) | [Summary](summary.html)

Created by **Mike Maynard**<BR>
Project Implemented in **Google Docs, Google Sheets, Markdown**<BR>
Last updated:  **2021-11-09**
