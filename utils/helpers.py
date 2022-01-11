from pathlib import Path
from brownie import config, project


class DependencyLoader(object):
    dependencies = {}

    @staticmethod
    def load(dependency_name, contract_name):
        if dependency_name not in DependencyLoader.dependencies:
            dependency_index = config["dependencies"].index(dependency_name)
            DependencyLoader.dependencies[dependency_name] = project.load(
                Path.home()
                / ".brownie"
                / "packages"
                / config["dependencies"][dependency_index]
            )
        return getattr(DependencyLoader.dependencies[dependency_name], contract_name)
