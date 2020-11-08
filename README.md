Monorepo support built around `git subtree`.

Installation
============

    pip install git_monorepo

Usage
=====

Simply create a mapping file called `monorepo.yml` in the root of your
git directory:

    mappings:
      adhesive: git@github.com:germaniumhq/adhesive.git
      oaas:
        oaas: git@github.com:germaniumhq/oaas.git
        grpc-compiler: git@github.com:germaniumhq/oaas-grpc-compiler.git
        registry-api: git@github.com:germaniumhq/oaas-registry-api.git
        registry: git@github.com:germaniumhq/oaas-registry.git
        grpc: git@github.com:germaniumhq/oaas-grpc.git
        simple: git@github.com:germaniumhq/oaas-simple.git
      tools:
        git-monorepo: git@github.com:bmustiata/git-monorepo.git

pull
----

To pull the repos (including initial setup), use:

    git mono pull

push
----

To push the repos do:

    git mono push

This takes into account the current branch name, so pushes can happen
also with branches.

At the end of the operation, if something was pushed, a new file to
track the status named `.monorepo.sync` is created and committed
automatically. This file holds a list of commits that were pushed, so
your merges can also be dealed with correctly, by adding both entries
when solving a potential conflict for a project.

mv
--

WARN: this is not yet implemented.

    git mv old/path new/path
    git subtree split --rejoin --prefix=new/path HEAD
    git subtree pull --squash --prefix=new/path giturl branch
