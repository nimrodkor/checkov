from checkov.common.models.enums import CheckResult


class BaseRegistry:
    def __init__(self, parser):
        self.checks = []
        self.parser = parser

    def load_checks(self):
        raise NotImplementedError

    def run_checks(self, graph_connector, runner_filter):
        check_results = {}
        filtered_checks = self.checks
        if runner_filter.checks:
            filtered_checks = [check for check in self.checks if check.id in runner_filter.checks]
        for check in filtered_checks:
            passed, failed = check.run(graph_connector)
            check_result = self._process_check_result(passed, [], CheckResult.PASSED)
            check_result = self._process_check_result(failed, check_result, CheckResult.FAILED)
            check_results[check.id] = check_result
        return check_results

    @staticmethod
    def _process_check_result(results, processed_results, result):
        for vertex in results:
            processed_results.append({'result': result, 'entity': vertex})
        return processed_results
