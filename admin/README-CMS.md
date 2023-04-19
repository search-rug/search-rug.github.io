# RUG-Search CMS

The `/admin` directory contains configuration files for the content management system (CMS) of the RUG-Search website. It allows site admins to manage most content present on the website without having to use Git.

## Deploying CMS

This section outlines how to deploy the CMS.

### CMS on Netlify.com

This approach uses Netlify's identity service and static website hosting to host the CMS. The website administrator can invite users to the CMS and they can sign up through email or using their GitHub account.

1. Create an account at [Netlify.com](https://app.netlify.com/signup)

2. [Deploy the repo](https://docs.netlify.com/get-started/#deploy-a-project-to-netlify) containing the CMS to Netlify.

3. Navigate to `Site Settings > Identity` for the newly deployed site and enable [Netlify Identity](https://docs.netlify.com/visitor-access/identity/) and [Git Gateway](https://docs.netlify.com/visitor-access/git-gateway/#app)

4. Manage Identity settings.

    - To enable CMS users to log in with Github, navigate to `Site Settings > Identity > Registration`, and add Github as an external provider.

    - To only enable invited users to accessing the CMS change registration to invite only.

5. When the page has been successfully deployed you can manage website content by navigating to `/admin` under the netlify deployed site.

> WARNING: If you have any anti-tracking or AD block extensions the netlify login widget might be blocked, and the page won't load. Make sure to whitelist the domain or disable your extension to use the CMS.
