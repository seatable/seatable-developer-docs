# Introduction

Welcome to the SeaTable Developer Guide. This guide describes all possibilities to build extensions for SeaTable, the world leading self-hosted no-code platform.

This guide explains basically three approaches to develop with SeaTable:

1. Write **Scripts** inside SeaTable to create custom logic or individual data processing. SeaTable supports Javascript and Python as scripting language. 
1. Or write a SeaTable **Plugin** that can interact, visualize and operate with the data of a SeaTable Base
1. Or use any programm language you want and interact with the **SeaTable API** to build your own web page or programm.

## Target audience

This guide is for **developers**, who want to use custom scripts inside SeaTable, build their own plugins or their own programms.

All instructions are valid for self-hosted Seatable installations (Enterprise and Developer Edition) as well as for the SeaTable Cloud.

!!! warning "Known limitations of SeaTable Cloud"

    Currently it is not possible to install custom plugins at SeaTable Cloud. Also the number of python-script runs is determined by your current SeaTable Cloud subscription.
    Therefore we recomment that you install your own SeaTable Server if you want to developer custom plugins, applications or multiple python scripts. 
    Please check the [Admin Manual](https://admin.seatable.io) how to install your own SeaTable Server.

Let's get started. We start with some general basics and then the development of your own scripts, plugins or applications can begin.

---

## More documentations

Next to this developer guide there are more documentations available. To learn more about the SeaTable API, the installation of your own server or the usage or SeaTable, please refer to their respective manuals:

- [SeaTable User Manual](https://docs.seatable.io/?lang=auto)
- [SeaTable Admin Manual](https://admin.seatable.io)
- [SeaTable API Reference](https://api.seatable.io)

See the [official SeaTable channel](https://youtube.com/seatable) on YouTube for tutorials, guides and overviews. Visit [our blog](https://seatable.io/blog/?lang=auto) for latest news and to learn more about what is going on in and around SeaTable.

At any time you could have a look at the SeaTable [Community Forum](https://forum.seatable.io) to share your experience with other users or report issues or bugs.

!!! note "Enterprise support"

    If you're using SeaTable in your organization and need
    assistance, e.g., to __digitalization of processes__, __develop custom solutions__ or __improve efficiency__,
    [__get in touch__](mailto:sales@seatable.io) to discuss our __enterprise support__ offerings. We're happy to help!
