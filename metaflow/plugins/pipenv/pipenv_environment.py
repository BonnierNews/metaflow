from metaflow.environment import MetaflowEnvironment


class PipenvEnvironment(MetaflowEnvironment):
    TYPE = 'pipenv'

    def __init__(self, flow):
        pass

    def init_environment(self, logger):
        """
        Run before any step decorators are initialized.
        """
        pass

    def validate_environment(self, logger):
        """
        Run before any command to validate that we are operating in
        a desired environment.
        """
        pass

    def decospecs(self):
        """
        Environment may insert decorators, equivalent to setting --with
        options on the command line.
        """
        return ()

    def bootstrap_commands(self, step_name):
        """
        A list of shell commands to bootstrap this environment in a remote runtime.
        """
        return []

    def add_to_package(self):
        """
        A list of tuples (file, arcname) to add to the job package.
        `arcname` is an alterative name for the file in the job package.
        """
        return []

    def pylint_config(self):
        """
        Environment may override pylint config.
        """
        return []

    @classmethod
    def get_client_info(cls, flow_name, metadata):
        """
        Environment may customize the information returned to the client about the environment

        Parameters
        ----------
        flow_name : str
            Name of the flow
        metadata : dict
            Metadata information regarding the task

        Returns
        -------
        str : Information printed and returned to the user
        """
        return "Local environment"

    def get_package_commands(self, code_package_url):
        cmds = ["set -e",
                "echo \'Setting up task environment.\'",
                "%s -m pip install awscli click requests boto3 \
                    --user -qqq" % self._python(),
                "mkdir metaflow",
                "cd metaflow",
                "i=0; while [ $i -le 5 ]; do "
                    "echo \'Downloading code package.\'; "
                    "%s -m awscli s3 cp %s job.tar >/dev/null && \
                        echo \'Code package downloaded.\' && break; "
                    "sleep 10; i=$((i+1));"
                "done " % (self._python(), code_package_url),
                "tar xf job.tar"
                ]
        return cmds

    def executable(self, step_name):
        return self._python()

    def _python(self):
        return "python"
