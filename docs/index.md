# Introduction

Welcome to the SeaTable Developer Guide. This guide describes all possibilities to build extensions for SeaTable, the world leading self-hosted no-code platform.

This guide explains basically three approaches to develop with SeaTable:

1. Write **Scripts** inside SeaTable to create custom logic or individual data processing. SeaTable supports Javascript and Python as scripting language. 
1. Or write a SeaTable **Plugin** that can interact, visualize and operate with the data of a SeaTable Base
1. Or use any programm language you want and interact with the **SeaTable API** to build your own web page or programm.

## Target audience

This guide is for **developers**, who want to use custom scripts inside SeaTable, build their own plugins or their own programms.

All instructions are valid for self-hosted Seatable installations (Enterprise and Developer Edition) as well as for the SeaTable Cloud.

!!! warning annotate "Known limitations of SeaTable Cloud"

    1. It is not possible to install custom plugins at [SeaTable Cloud](https://cloud.seatable.io). 
    2. The number of python-script runs is limited by your current SeaTable Cloud subscription.
 
    Therefore we recomment that you install your own SeaTable Server if you want to developer custom plugins, applications or multiple python scripts. More info about your own server in the [Admin Manual](https://admin.seatable.io).

Ok. Let's get started. 

If you are new to SeaTable, we recommend that you go on with the reading of the introduction part. In the next articles you will learn more about the [requirements](/introduction/requirements) or the [basic concepts](/introduction/basic_concepts) of the no-code platform SeaTable.
