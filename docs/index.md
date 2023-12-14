# Introduction

Welcome to the SeaTable Developer Guide, your comprehensive resource for leveraging the potential of SeaTable, the world's leading self-hosted no-code platform.

This guide illustrates **three fundamental approaches** to development within SeaTable:

1. [Scripting within SeaTable](/scripts/): Create custom logic or perform individual data processing using JavaScript or Python, both supported within SeaTable.
1. [SeaTable Plugins](/plugins/): Develop plugins capable of interacting with, visualizing, and operating on data within a SeaTable Base.
1. [Utilizing Any Programming Language with SeaTable API](/clients/): Seamlessly interact with the SeaTable API to construct your own web pages or programs.

## Developer decision tree

![Image title](/media/developer_decision_tree.png){ align=left }

For guidance on choosing the right section within this manual, refer to the decision tree diagram above.

If you aim to integrate a software product with SeaTable, note that SeaTable supports multiple workflow automation tools such as [n8n](https://n8n.io/integrations/seatable/), [Zapier](https://zapier.com/apps/seatable/integrations), and [Make](https://www.make.com/en/integrations/seatable). Please refer to the [SeaTable user manual](https://seatable.io/docs-category/skripte-api-integrationen/) for detailed information on these integrations, as they are not covered in this guide.

## Target audience

This guide caters to **developers** interested in utilizing custom scripts within SeaTable, creating their own plugins, or developing custom programs.

All instructions provided are applicable to self-hosted SeaTable installations (Enterprise and Developer Editions), as well as SeaTable Cloud.

!!! warning annotate "Known limitations of SeaTable Cloud"

    1. **Custom Plugin Installation**: [SeaTable Cloud](https://cloud.seatable.io) does not support the installation of custom plugins.
    2. **Python Script Runs Limitation**: The number of Python script runs is constrained by your current SeaTable Cloud subscription.

    Therefore, it's recommended to set up your own SeaTable Server if you intend to develop custom plugins, applications, or run multiple Python scripts. For further information about deploying your server, please refer to the [Admin manual](https://admin.seatable.io).

If you are new to SeaTable, we suggest starting with the introduction section covering the platform's [requirements](/introduction/requirements) and [basic concepts](/introduction/basic_concepts) of this no-code platform. Otherwise, let's dive right in!

[Start Scripting](/scripts){ .md-button .md-button--primary }
[Write your own plugin](/plugins){ .md-button .md-button--primary }
[Use the API](/clients){ .md-button .md-button--primary }
