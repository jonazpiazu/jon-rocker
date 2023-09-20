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
        print(f'url is {cli_args["ros_git_pkg"][0]}')
        return em.expand(snippet, git_url=cli_args["ros_git_pkg"][0])

    def get_docker_args(self, cli_args):
        return ''

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--ros-git-pkg',
            type=str,
            nargs=1,
            help='create and build a ROS ws from a git repo containing a ROS package')