# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPreCommitHooks(PythonPackage):
    """A collection of useful pre-commit hooks."""

    homepage = "https://github.com/pre-commit/pre-commit-hooks"
    url = "https://github.com/pre-commit/pre-commit-hooks/archive/refs/tags/v4.5.0.tar.gz"

    maintainers("cedricchevalier19", "claireguilbaud")

    license("MIT")

    version("6.0.0", sha256="5236d2daff61aed8d882ec81463cf27786f6a1f449f05d8c6c3882c3cf2810bb")
    version("5.0.0", sha256="b2fcd00243b7e61b43a3a26d226e295e0a07611f3436818f64846c067a1679d5")
    version("4.6.0", sha256="ebf493781b27929294ff1262763cfd877af1fd33c21fc9d7cd684fdf40204b27")
    version("4.5.0", sha256="1d6040a22a1c2a9216b4f439dfc5c626c214587e372a57b603079d9c88d2d425")
    version("4.4.0", sha256="ecaa3c38e81000115f7e42a2c53dde3785fe2bcc9be7a5c7a2d8f103423b9b16")
    version("4.3.0", sha256="d65f376bbb525e6269daffc63f6cecb5b83bcfe016633882fdeb8deb87f523b9")
    version("4.2.0", sha256="04cd4d328ac79be634776ec27e8800b56abacce27dfb5fa2cd9b617a81bddf27")
    version("4.1.0", sha256="cc7a9ed56f2044ddcfccd15ad65ce0a967b9f11b3210ada05f742ad87d702b40")
    version("4.0.1", sha256="25c039a33c77aebcc1500df93125388ed4b96444c39766c42721812a96e44093")
    version("4.0.0", sha256="2ca6da2636b8d6f3afc9f0e6fe7cf36607ae0f116eb4b0f12f76d52a87336c7d")

    # Dépendances Python minimales
    depends_on("py-setuptools", type="build")
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-tomli", type=("build", "run"), when="^python@:3.10")

    # Optionnel : utilisé par certains hooks YAML
    depends_on("py-ruamel-yaml", type=("build", "run"), when="@4.5.0:")
