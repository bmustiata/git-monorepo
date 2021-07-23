python_binary(
  name="git-monorepo",
  main="git_monorepo/__main__.py",
  srcs=glob([
    "git_monorepo/**/*.py",
  ], exclude=[
    "git_monorepo/__main__.py",
  ]),
  deps=[
    "//build/thirdparty/python:click",
    "//build/thirdparty/python:PyYAML",

    "//tools/termcolor-util:termcolor-util-lib",
  ],
)
