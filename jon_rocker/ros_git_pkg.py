import em
import pkgutil
from rocker.extensions import RockerExtension


class RosGitPkg(RockerExtension):

    name = 'ros_git_pkg'

    @classmethod
    def get_name(cls):
        return cls.name

    def precondition_environment(self, cli_args):
        pass

    def validate_environment(self, cli_args):
        pass

    def get_preamble(self, cli_args):
        return ''

    def get_snippet(self, cli_args):
        snippet = pkgutil.get_data(
            'jon_rocker',
            'templates/ros_git_pkg_snippet.Dockerfile.em').decode('utf-8')
        branch_name = None
        branch_name = self.extractsuffix(self.removeprefix(cli_args["ros_git_pkg"][0], 'git@'))
        git_url = cli_args["ros_git_pkg"][0]
        if branch_name is not None:
            git_url = self.removesuffix(cli_args["ros_git_pkg"][0], '@' + branch_name)
        return em.expand(snippet, git_url = git_url, branch_name = branch_name)

    def get_docker_args(self, cli_args):
        return ''

    # only available for python 3.9+
    def removeprefix(self, text, prefix):
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def extractsuffix(self, text):
        if "@" in text:
            suffix_start = text.index("@") + 1
            return text[suffix_start:]
        else:
            return None

    def removesuffix(self,text, suffix):
        if text.endswith(suffix):
            return text[:len(text) - len(suffix)]
        return text

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--ros-git-pkg',
            type=str,
            nargs=1,
            help='create and build a ROS ws from a git repo containing a ROS package')
