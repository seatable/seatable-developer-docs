# Coding for beginners

## What to learn?

The Developer Manual is divided into three major sections ([scripts](../scripts/index.md), [plugins](../plugins/index.md), or [API client](../clients/index.md)) depending on what you want to do with SeaTable. Your development requirements will naturally vary based on your intended project. Below is an outline of the skills you might need:

=== "Scripts"

    Scripts inside SeaTable can only be written with either JavaScript or Python. Therefore you will only require one of these programming languages.

=== "Plugins"

    The development of a custom plugin for your own SeaTable Server requires profound knowledge of JavaScript and React.

    Even if the `SeaTable plugin templates` offers some reusable components, you will need some experience with React to build the interface of your plugin.

=== "Client API's"

    Due to the publicly available and well documented API documentation, you can theoretically interact with SeaTable using any programming language.

## Learn the fundamentals

If you're relatively new to development, diving into general tutorials can lay a strong foundation for your SeaTable development journey.

While numerous free online tutorials cover various programming languages, investing in a comprehensive online course or a well-structured book can be invaluable. While free resources are available, a structured course or book often offers a more cohesive and thorough learning experience.

These paid resources, though requiring a small investment, often provide:

- **Structured Learning**: A step-by-step approach ensuring a coherent understanding.
- **Comprehensive Content**: In-depth coverage of essential concepts and practical applications.
- **Consistency**: Ensuring continuity and coherence in learning.

Remember, while free tutorials are abundant, investing in a structured resource can significantly expedite your learning process and provide a solid understanding of programming fundamentals essential for SeaTable development.

!!! info "This are personal recommendations"

    The following sources does not contain any affiliate links and we do not earn any money from these recommendations. These are just good sources that we have used ourselves in the past.

=== "JavaScript"

    **Free online course**

    :   A solid and __free online__ course is available from codecademy.com. The course [Learn JavaScript](https://www.codecademy.com/learn/introduction-to-javascript) requires a registration but is free and teaches you in approx. 20 hours all necessary skills.

    **Best online course**

    :   The best __online course__ on javascript comes from [Mosh Hamedani](https://codewithmosh.com/). Mosh manages to explain all the important basics for programming with JavaScript in his course [The Ultimate JavaScript Series](https://codewithmosh.com/p/ultimate-javascript-series). Once you have completed this course, you should be able to write your first scripts with ease. A monthly subscription costs just $29.

    **Book for Beginners**

    :   If you prefer a __book__, then we can recommend [JavaScript from Beginner to Professional](https://www.amazon.de/JavaScript-Beginner-Professional-building-interactive/dp/1800562527/). It gives you all the basics for your first steps with JavaScript.

=== "Python"

    **Free online course**

    :   An easy to follow beginner guide comes from Google. At [https://developers.google.com/edu/python](https://developers.google.com/edu/python) you can find this well balanced course to learn how to do your first steps.

    **Best online course**

    :   The best __online course__ on Python comes from [Mosh Hamedani](https://codewithmosh.com/). Mosh manages to explain all the important basics for programming with Python in his course [Complete Python Mastery](https://codewithmosh.com/p/python-programming-course-beginners). Once you have completed this course, you should be able to write your first scripts with ease. A monthly subscription costs just $29.

    **Book for Beginners**

    :   Our recommended book for beginners is called [Learn Python in One Day and Learn It Well](https://www.amazon.de/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ) and as far as we can tell it keeps his promise. Most of our working students have read this book if they want to learn more about Python.

=== "React"

    **Free online course**

    :   This free online course comes to you from [Scrimba](https://scrimba.com/). Scrimba is a coding bootcamp with mainly paid courses and a high amount of interactive screencasts. The React course [Learn React](https://scrimba.com/learn/learnreact) is fortunately free of charge.

    **Best online course**

    :   The best __online course__ on React comes from [Mosh Hamedani](https://codewithmosh.com/). Mosh will guide and teach you React until and will build a complete Video Game Discovery App. The course is called [React Course for Beginners](https://codewithmosh.com/p/ultimate-react-part1).

## Learning by doing

Some of us are more comfortable with learning by doing. The principle is simple: dissect a working example, understand it, and finally modify it so that it achieves what we want.

Here are **three examples**, one for each approach described in this manual:

### Python script to get the structure of a base

You can take the following python code and copy&paste it to SeaTable. It will return the complete metastructure of your base. Easy or not? If you need some more information about this script, please refer to [this step-by-step presentation](https://seatable.com/help/python-beispiel-die-metastruktur-einer-base-auslesen/).

=== "Python code"

    ```python
    from seatable_api import Base, context
    base = Base(context.api_token, context.server_url)
    base.auth()

    metadata = base.get_metadata()

    print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
    for table in metadata['tables']:
        print('.')
        print("Table: "+table['name']+" (ID: "+table['_id']+")")
    for column in table['columns']:
        link_target = ""
        if column['type'] == "link":
            link_target = " --> "+column['data']['other_table_id']
            if column['data']['other_table_id'] == table['_id']:
                link_target = " --> "+column['data']['table_id']
        print("  --> "+column['name']+" ("+column['type']+link_target+")")
    ```

=== "Output example"

    ```
    --- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---
    .
    Table: Opportunities (ID: 9g8f)
    --> Name (text)
    --> Status (single-select)
    --> Prio (single-select)
    --> Owner (collaborator)
    --> Customer (link --> deGa)
    --> Estimated value (number)
    --> Proposal deadline (date)
    --> Contacts (link --> lYb8)
    --> Interactions (link --> 0000)
    .
    Table: Interactions (ID: 0000)
    --> Interaction ID (auto-number)
    --> Opportunity (link --> 9g8f)
    --> Type (single-select)
    --> Interaction (formula)
    --> Opportunity status (formula)
    --> Date and time (date)
    --> Contact (link --> lYb8)
    --> Notes (long-text)#
    ```

Feel free to check the other [JavaScript](../scripts/javascript/examples/index.md) and [Python](../scripts/python/examples/index.md) examples.

### Existing plugins

SeaTable provides some plugins to visualize your data, for example the [Gallery](https://seatable.com/help/anleitung-zum-galerie-plugin/), [Timeline](https://seatable.com/help/anleitung-zum-timeline-plugin/), [Kanban](https://seatable.com/help/anleitung-zum-kanban-plugin/) and so on, but it also offers everything you need to you build your own plugin. There are no limits to the imagination, it just requires some time and React skills. 

For each existing plugin, you can find a corresponding [Github repository](https://github.com/orgs/seatable/repositories?q=seatable-plugin) that will allow you to fork/clone the code and try by yourself (you will probably need some basic git skills too). Please note that this is probably the one of the three approaches ([scripts](../scripts/index.md), [plugins](../plugins/index.md), or [API client](../clients/index.md)) that **requires the most skills**.

### Using SeaTable APIs: the SeaTable ideas custom app example

There are multiple API classes available for various programming languages. This enables you to build any app or website you want.

Our feature request tool [SeaTable Ideas](https://ideas.seatable.com) is an example for such a website. It uses SeaTable as database and the frontend is build completely with PHP and the [slim framework](https://www.slimframework.com/).

![Screenshot of ideas.seatable.com](/media/ideas.png).

Do not hesitate to consult this [pretty detailed article](https://seatable.com/seatable-app-frontend-php/) about the logic behind this app.

Of course, the [SeaTable API Reference](https://api.seatable.com) is another good place to start as it allows you to experiment with most queries, see the responses, and get the corresponding source code for all supported languages.