# SeaTable Developer's Repository

Welcome to the SeaTable Developer's Repository! 🌊🔍✨

This repository serves as the foundational source for the SeaTable Developer's Manual available at https://developer.seatable.com. The Developer Manual is generated with the help of MkDocs Material and is a comprehensive guide and resource hub for developers aiming to build extensions, scripts, plugins, or custom applications within SeaTable.

## Content

- **Introducion**: Explanation of fundamental approaches and SeaTable basic concepts.
- **Scripting in SeaTable**: Detailed instructions on scripting with a complete function overview and ready-to-use scripts.
- **Plugin Development**: Step-by-step guide to developing your own SeaTable plugin.
- **Client APIs**: List of ready-to-use API clients for various programming languages like JavaScript, Python, and PHP.

## How to participate

Please fell free to participate in the Developer Manual by creating pull requests. Before you do this, please test your changes in a local copy of this manual. Here is how you can do this.

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

### Step 2: Generate your local version of the Developer Manual

We developed a tiny bash script to generate the local copy of the manual.

```bash
sudo ./preview.sh
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

### Step 4: Stop the docker container with your local Developer Manual copy

```bash
./preview.sh -stop
```

## Editing the JavaScript reference

Read this before touching `docs/javascript/`. These pages document **two different APIs** that both call their object `base`, and they are not identical:

- **Script in SeaTable** — runs in the browser, no authentication. `base` is provided by the script environment.
- **External client** — `npm install seatable-api`, runs in Node.js or a frontend app, authenticates with an API token.

Most methods exist in both, but not all. The differences are not obvious and have caused documented methods to be `undefined` for readers in the wrong context. Two kinds of divergence exist:

**Capability** — columns can only be created or modified from the external client. `insertColumn`, `renameColumn`, `modifyColumnType`, `addColumnOptions`, `deleteColumn` and the other write methods do not exist in a script. Scripts have read-only access to columns.

**Naming** — the same method has different names in the two contexts:

| Script in SeaTable | External client |
|---|---|
| `getRows` | `listRows` |
| `updateLinks` | `updateLink` |
| `getColumns` | `listColumns` (works in both) |

### The marker convention

Every method that is limited to one context carries a marker in its `!!! abstract` heading:

```markdown
!!! abstract "getShownColumns :material-tag-outline:{ title='Scripting only' }"
!!! abstract "insertColumn :material-package-variant-closed:{ title='External client only' }"
```

The markers are the authoritative per-method record. **When you add or move a method, determine its context first and mark it** — do not assume parity. A missing marker is read as "works in both".

### How to check a method

The external client is machine-readable:

```bash
npm pack seatable-api && tar xzf seatable-api-*.tgz
grep -oE 'key: "[a-zA-Z0-9_]+"' package/lib/base.js | sed 's/key: //' | tr -d '"' | sort -u
```

The scripting API is not — it lives in the SeaTable frontend, not in a published package. Run [`scripts/dump-script-api.js`](scripts/dump-script-api.js) in any base's script editor to get its current method list.

Note that `dtable-sdk` on npm is **not** a reliable stand-in for the scripting API. The script environment wraps it and adds methods; the SDK contains no link methods at all, for example.

# Feedback and Support

Feel free to raise issues or reach out with any questions, feedback, or suggestions. We're here to support your SeaTable development endeavors! We welcome contributions and feedback from the SeaTable developer community.
