# Example project #
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub](https://img.shields.io/github/license/rdurica/example)

Django skeleton for new applications


# Installation #
1. Clone or download repository
2. Update database connection inside <code>./config/settings.py</code>
3. Run initial script <code>make</code>
4. Run development server <code>python ./manage.py runserver</code>

> **_NOTE:_**  Do not forget to change SECRET_KEY before deploy

### Webpack ###
Uncomment this lines in <code>webpack.config.json</code> for image compilation
```js
// new CopyPlugin({
//     patterns: [
//         { from: "./assets/images", to: "images" },
//     ],
// }),
```

### Coding standards ###
To validate standards run command <code>make pre_commit</code>

![Screenshot from 2021-09-19 20-45-04](https://user-images.githubusercontent.com/16089770/158486061-f0ca98af-c14b-4f4e-a4d7-ae84248fa593.png)


For automatic check before commit initialize hook for your repository using <code>pre-commit install</code>

### Folder structure ###
New applications always put into <code>./app</code> folder

```
📦root
 ┣ 📂app
 ┃ ┣ 📂core
 ┣ 📂assets
 ┣ 📂config
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜wsgi.py
 ┣ 📂media
 ┣ 📂static
 ┗ 📜manage.py
```

### Useful links ###
- [django documentation](https://docs.djangoproject.com/)
- [black](https://github.com/psf/black)
- [pre-commit](https://pre-commit.com/)
- [flake8](https://github.com/PyCQA/flake8)
- [isort](https://github.com/PyCQA/isort)