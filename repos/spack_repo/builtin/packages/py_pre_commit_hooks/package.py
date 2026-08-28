# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPreCommitHooks(PythonPackage):
    """A collection of useful pre-commit hooks."""

    homepage = "https://github.com/pre-commit/pre-commit-hooks"
    pypi = "pre-commit-hooks/pre-commit-hook-4.5.0.tar.gz"

    maintainers("cedricchevalier19", "claireguilbaud")

    license("MIT")

    version("4.5.0", sha256="1d6040a22a1c2a9216b4f439dfc5c626c214587e372a57b603079d9c88d2d425")

    # Dépendances Python minimales
    depends_on("py-setuptools", type="build")
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-tomli", type=("build", "run"), when="^python@:3.10")

    # Optionnel : utilisé par certains hooks YAML
    depends_on("py-ruamel-yaml", type=("build", "run"), when="@4.5.0:")
