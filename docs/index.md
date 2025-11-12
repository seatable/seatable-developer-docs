# Introduction

You've decided to venture into developing your own script, plugin, or custom application: excellent choice! This guide is designed to cover all aspects of this journey. While some descriptions might seem obvious to seasoned professionals, this manual is crafted to assist novice developers who are just starting out.

## Who is this manual for?

The Developer Manual caters to **developers** interested in utilizing custom scripts within SeaTable, creating their own plugins, or developing custom programs. Both minimal programming skills and knowledge of SeaTable are therefore recommended to take full advantage of this manual.

!!! info "Tips for beginners"

    You don't feel familiar enough with coding or with SeaTable? Depending on your actual skills, knowledge and aims, here are some suggested starting points: 

    - You would like to get started but currently have no programming knowledge? We invite you to consult the [Coding for beginners page](/introduction/coding_for_beginnners)

    - You are new to SeaTable? Do not hesitate to consult [SeaTable's user manual](https://seatable.com/help/) to get more familiar with it.

## Scope of this manual

This guide illustrates **three fundamental approaches** to development within SeaTable:

1. [Scripting within SeaTable](/scripts/): Create custom logic or perform individual data processing using JavaScript or Python, both supported within SeaTable.
2. [SeaTable plugins](/plugins/): Develop plugins capable of interacting with, visualizing, and operating on data within a SeaTable Base.
3. [Utilizing any programming language with SeaTable's API](/clients/): Seamlessly interact with the SeaTable API to construct your own web pages or programs.

!!! info "JavaScript or Python scripts?"

    Differences between JavaScript and Python (in terms of abilities and requirements) are mentioned in the [Scripting introduction page](./scripts/index.md) to help you make the right choice depending on your needs

All instructions provided are applicable to self-hosted SeaTable installations (Enterprise and Developer Editions), as well as to SeaTable Cloud.

### Where to start?

For guidance on choosing the right section within this manual, refer to the decision tree diagram below.

![Image title](/media/developer_decision_tree.png){ align=left }

If you aim to integrate a software product with SeaTable, note that SeaTable supports multiple workflow automation tools such as [n8n](https://n8n.io/integrations/seatable/), [Zapier](https://zapier.com/apps/seatable/integrations), and [Make](https://www.make.com/en/integrations/seatable). Please refer to the [SeaTable User Manual](https://seatable.com/help/integrations/) for detailed information on these integrations, as they are not covered here.

## Requirements

### Development system

To begin your development journey with SeaTable, you'll need a SeaTable system. If you're planning to create short scripts, [SeaTable Cloud](https://seatable.com/prices/) could be a suitable option. However, for more in-depth development or when creating plugins, it's highly recommended to set up your own SeaTable Server. Refer to the [Admin manual](https://admin.seatable.com) for installation instructions.

!!! warning annotate "Known limitations of SeaTable Cloud"

    1. **Custom Plugin Installation**: [SeaTable Cloud](https://cloud.seatable.io) does not support the installation of custom plugins.
    2. **Python Script Runs Limitation**: The number of Python script runs is constrained by your current SeaTable Cloud subscription.

    Therefore, it's recommended to set up your own SeaTable Server if you intend to develop custom plugins, applications, or run multiple Python scripts. For further information about deploying your server, please refer to the [Admin Manual](https://admin.seatable.com).

### Authentication

The actual authentication depends on the development approach one chooses.

=== "Scripts"

    JavaScript scripts does not require any authentication at all because these scripts are executed in the browser of the user and the user has to be authenticated already.

    Python scripts require an authentication to get data from the base, but the `context` objects contains everything for an easy authentication.

=== "Plugins"

    Plugins interact with the data of one base. SeaTable provides all required functions for easy authentication.

=== "Client APIs"

    If you want to build your own application you always have to authenticate with a base token against the base (learn more about the different tokens used by SeaTable in the [API Reference](https://api.seatable.com/reference/authentication)).

## Data model

{%
    include-markdown "includes.md"
    start="<!--datamodel-start-->"
    end="<!--datamodel-end-->"
%}