Monorepo support built around `git subtree`.

Installation
============

    pip install git_monorepo

Usage
=====

Simply create a mapping file called `gerepo.yml`:

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

To pull the repos (including initial setup), use:

    git mono pull

To push the repos do:

    git mono push

This takes into account the current branch name, so pushes can happen
also with branches.
