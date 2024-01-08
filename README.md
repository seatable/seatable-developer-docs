# SeaTable Developer's Repository

Welcome to the SeaTable Developer's Repository! 🌊🔍✨

This repository serves as the foundational source for the SeaTable Developer's Manual available at https://developer.seatable.io. The developer manual is generated with the help of MkDocs Material and is a comprehensive guide and resource hub for developers aiming to build extensions, scripts, plugins, or custom applications within SeaTable.

## Content

- **Introducion**: Explanation of fundamental approaches and SeaTable basic concepts.
- **Scripting in SeaTable**: Detailed instructions on scripting with a complete function overview and ready-to-use scripts.
- **Plugin Development**: Step-by-step guide to developing your own SeaTable plugin.
- **Client API's**: List of ready-to-use API clients for various programming languages like JavaScript, Python, and PHP.

## How to participate

Please fell free to particiate in the developer manual by creating pull requests. Before you do this, please test your changes in a local copy of this manual. Here is how you can do this.

> :warning: Docker is required
>
> We use Docker to create this local manual copy. You have to install docker first, if you don't have it already on your local machine. Use this one line command to easily install it on a linux machine:
>
> `curl -fsSL get.docker.com | bash`

### Step 1: Clone this repository and checkout a new branch

```bash
git clone https://github.com/seatable/seatable-developer-docs
cd seatable-developer-docs
git checkout -b <new_branch>
# please replace <new_branch> with something short like "add_python_example"
```

### Step 2: Generate your local version of the developer manual

We developed a tiny bash script to generate the local copy of the manual.

```bash
./preview.sh
```

Initiate your browser and access http://127.0.0.1:8000 to view a local copy of the manual. Any modifications made locally will be instantly reflected in this version. You don't even have to restart docker or reload the page.

The manual can be found within the `docs` folder. For comprehensive guidance on utilizing [MKDocs](https://www.mkdocs.org/user-guide/) or [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), refer to their respective manuals for detailed instructions.

### Step 3: Create a pull request

The last step is to create a pull request will your proposed changes.

```bash
git add .
git commit -m "<commit_message>"
git push
```

### Step 4: Stop the docker container with your local admin manual copy

```bash
./preview.sh -stop
```

# Feedback and Support

Feel free to raise issues or reach out with any questions, feedback, or suggestions. We're here to support your SeaTable development endeavors! We welcome contributions and feedback from the SeaTable developer community.
