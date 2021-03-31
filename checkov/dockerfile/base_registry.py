from checkov.common.checks.base_check_registry import BaseCheckRegistry
from checkov.common.models.enums import CheckResult


class Registry(BaseCheckRegistry):
    def __init__(self):
        super().__init__()

    def extract_entity_details(self, entity):
        if isinstance(entity, list) and entity:
            instruction = entity[0]['instruction']
            return instruction, instruction, entity

    def scan(self, scanned_file, entity, skipped_checks, runner_filter):

        # (entity_type, entity_name, entity_configuration) = self.extract_entity_details(entity)

        results = {}
        if not entity:
            return results
        for instruction, checks in self.checks.items():
            skip_info = {}

            for check in checks:
                if check.id in [x['id'] for x in skipped_checks]:
                    skip_info = [x for x in skipped_checks if x['id'] == check.id][0]

                if runner_filter.should_run_check(check.id):
                    entity_name = instruction
                    entity_type = instruction
                    entity_configuration = entity[instruction]
                    result = self.run_check(check, entity_configuration, entity_name, entity_type, scanned_file,
                                            skip_info)
                    results[check] = {}
                    if result['result'] == CheckResult.SKIPPED:
                        results[check]['result'] = result['result']
                        results[check]['suppress_comment'] = result['suppress_comment']
                        results[check]['results_configuration'] = None
                    else:
                        results[check]['result'] = result['result'][0]
                        results[check]['results_configuration'] = result['result'][1]

        for check in self.wildcard_checks["*"]:
            if skipped_checks:
                if check.id in [x['id'] for x in skipped_checks]:
                    skip_info = [x for x in skipped_checks if x['id'] == check.id][0]

            if runner_filter.should_run_check(check.id):
                entity_name = scanned_file
                entity_type = "*"
                entity_configuration = entity
                result = self.run_check(check, entity_configuration, entity_name, entity_type, scanned_file,
                                        skip_info)
                results[check] = {}
                if result['result'] == CheckResult.SKIPPED:
                    results[check]['result'] = result['result']
                    results[check]['suppress_comment'] = result['suppress_comment']
                    results[check]['results_configuration'] = None
                else:
                    results[check]['result'] = result['result'][0]
                    results[check]['results_configuration'] = result['result'][1]
        return results
