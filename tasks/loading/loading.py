from selinon import SelinonTask


class LoadingTask(SelinonTask):

     def run(self, node_args):
        return {"payload": {"time_series": "some_stuff"}}
