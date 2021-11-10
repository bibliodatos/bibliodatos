---
title: Mike Maynard | School Data Integration and Authentication Case Study - Classroom Rostering
---
## [School Data Integration and Authentication Case Study](./)

### Classroom Findings


| Product | Manual | Manual CSV | Automated CSV | Intra-vendor Integration | Other Integrations | API |
| ------- | ------ | ----------- | ------- | ------ | ----------- | ------- |
| [Blackboard WCM](https://www.blackboard.com/engage-your-community/websites-branding/web-community-manager) | [Yes - Users Workspace](https://help.blackboard.com/Web_Community_Manager/Administrator/Users_and_Groups/Users/Edit_Users) | [Yes](https://help.blackboard.com/Web_Community_Manager/Administrator/Users_and_Groups/Users#import) | [Connector](https://help.blackboard.com/Web_Community_Manager/Administrator/Data_Integration_And_Automation/Universal_Connector) | Community Engagement |  | |
| [Blackboard Mass Communication](https://www.blackboard.com/engage-your-community/communications/mass-notifications-for-k-12)| [Yes - Communications HQ](https://help.blackboard.com/Community_Engagement/Administrator/Community_Settings/Account_Management)  | [Yes](https://help.blackboard.com/Community_Engagement/Administrator/Community_Settings/Account_Management/Manage_User_Accounts/Upload_Accounts_from_Files) | [DataLink](https://help.blackboard.com/Community_Engagement/Administrator/Data_Imports) | WCM | | |
| [Clever Admin](https://support.clever.com/hc/s/articles/360026950471) | [Yes - Support Tools](https://support.clever.com/hc/s/articles/360026950471?language=en_US) | [Yes](https://support.clever.com/hc/s/articles/229253547?language=en_US) | [Yes](https://support.clever.com/hc/s/articles/229253547?language=en_US) | | [SIS Auto-sync](https://support.clever.com/hc/s/articles/202042973) | [Yes](https://dev.clever.com/) |
| [Google Apps/Workspace](https://edu.google.com/why-google/k-12-solutions/)| [Yes - Admin Console](https://support.google.com/a/answer/9970788?hl=en) | [Yes](https://support.google.com/a/answer/9970788?hl=en) | [Integromat SFTP](https://www.integromat.com/en/integrations/google-g-suite/sftp) | | [Clever IDM](https://clever.com/appstore/clever-idm) &#124;<BR> [Google Cloud Directory Sync - LDAP](https://support.google.com/a/answer/106368?hl=en) &#124;<BR>[Google SDS - EOL'd 2022](https://support.google.com/a/topic/6039552) | [Directory API](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users) |

Glossary:

* Manual - Entering data by hand in a console provided by the vendor
* Manual CSV - Uploading a file in the [comma separated value](https://en.wikipedia.org/wiki/Comma-separated_values) format using a console. Select the file and initiate the transfer.
* Automatic CSV - Transferring a file programmatically typically with the [SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) protocol.


#### Next... [Data Integration Findings](integration_findings.html)



---
[School Project Home](./) | [Authentication Findings](authentication_findings.html)

Created by **Mike Maynard**<BR>
Project Implemented in **Google Docs, Google Sheets, Markdown**<BR>
Last updated:  **2021-11-09**
