try:
    from urlparse import urlparse
except:
    from urllib.parse import urlparse

from metaflow.decorators import StepDecorator
from metaflow.environment import InvalidEnvironmentException

try:
    unicode
except NameError:
    unicode = str
    basestring = str

class PipenvStepDecorator(StepDecorator):
    """
    TODO: Add documentation
    """
    name = 'pipenv'
    defaults = {'libraries': {},
                'python': None,
                'disabled': None}

    pipenv = None
    environments = None

    def _get_base_attributes(self):
        return self.defaults

    def step_init(self, flow, graph, step_name, decorators, environment, datastore, logger):
        if environment.TYPE != 'pipenv':
            raise InvalidEnvironmentException('The *@pipenv* decorator requires '
                                              '--environment=pipenv')
        self.base_attributes = self._get_base_attributes()

    def package_init(self, flow, step_name, environment):
        """
        Called to determine package components
        """
        pass

    def step_task_retry_count(self):
        """
        Called to determine the number of times this task should be retried.
        Returns a tuple of (user_code_retries, error_retries). Error retries
        are attempts to run the process after the user code has failed all
        its retries.
        """
        return 0, 0

    def runtime_init(self, flow, graph, package, run_id):
        """
        Top-level initialization before anything gets run in the runtime
        context.
        """
        pass

    def runtime_task_created(self,
                             datastore,
                             task_id,
                             split_index,
                             input_paths,
                             is_cloned):
        """
        Called when the runtime has created a task related to this step.
        """
        pass

    def runtime_finished(self, exception):
        """
        Called when the runtime created task finishes or encounters an interrupt/exception.
        """
        print(self.attributes)
        pass

    def runtime_step_cli(self, cli_args, retry_count, max_user_code_retries):
        """
        Access the command line for a step execution in the runtime context.
        """
        pass

    def task_pre_step(self,
                      step_name,
                      datastore,
                      metadata,
                      run_id,
                      task_id,
                      flow,
                      graph,
                      retry_count,
                      max_user_code_retries):
        """
        Run before the step function in the task context.
        """
        pass

    def task_decorate(self,
                      step_func,
                      flow,
                      graph,
                      retry_count,
                      max_user_code_retries):
        return step_func

    def task_post_step(self,
                       step_name,
                       flow,
                       graph,
                       retry_count,
                       max_user_code_retries):
        """
        Run after the step function has finished successfully in the task
        context.
        """
        pass

    def task_exception(self,
                       exception,
                       step_name,
                       flow,
                       graph,
                       retry_count,
                       max_user_code_retries):
        """
        Run if the step function raised an exception in the task context.

        If this method returns True, it is assumed that the exception has
        been taken care of and the flow may continue.
        """
        pass

    def task_finished(self,
                      step_name,
                      flow,
                      graph,
                      is_task_ok,
                      retry_count,
                      max_user_code_retries):
        """
        Run after the task context has been finalized.

        is_task_ok is set to False if the user code raised an exception that
        was not handled by any decorator.

        Note that you can't create or modify data artifacts in this method
        since the task has been finalized by the time this method
        is called. Also note that the task may fail after this method has been
        called, so this method may get called multiple times for a task over
        multiple attempts, similar to all task_ methods.
        """
        pass