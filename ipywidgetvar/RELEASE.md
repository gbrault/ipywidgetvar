- To release a new version of ipywidgetvar on PyPI:

Change version in

- example.py
- package.json
- _version.py
- example.js

Update _version.py (set release version, remove 'dev')
git add the _version.py file and git commit
`python setup.py sdist`
`python setup.py bdist_wheel`
`git tag -a X.X.X -m 'comment'`
`twine upload dist/*`
Update _version.py (add 'dev' and increment minor)
git add and git commit
git push
`git push --tags`

- To release a new version of ipywidgetvar on NPM:

Update `js/package.json` with new npm package version

# clean out the `dist` and `node_modules` directories in js subdirectory
`git clean -fdx`
`npm install`
`npm publish`
