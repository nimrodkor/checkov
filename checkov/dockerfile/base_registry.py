from checkov.common.checks.base_check_registry import BaseCheckRegistry


class Registry(BaseCheckRegistry):
    def __init__(self):
        super().__init__()

    def extract_entity_details(self, entity):
        if isinstance(entity,list) and entity:
            instruction = entity[0]['instruction']
            return instruction,instruction, entity

    def scan(self, scanned_file, entity, skipped_checks, runner_filter):

        (entity_type, entity_name, entity_configuration) = self.extract_entity_details(entity)

        results = {}

        checks = self.get_checks(entity_type)
        for check in checks:
            skip_info = {}
            if skipped_checks:
                if check.id in [x['id'] for x in skipped_checks]:
                    skip_info = [x for x in skipped_checks if x['id'] == check.id][0]

            if runner_filter.should_run_check(check.id):
                result = self.run_check(check, entity_configuration, entity_name, entity_type, scanned_file, skip_info)
                results[check] = {}
                results[check]['results_configuration'] = result['result'][1]
                results[check]['result'] = result['result'][0]
        return results
