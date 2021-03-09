import json
import os

import yaml

from checkov.common.models.enums import CheckResult
from checkov.graph.checks.checks_infra.base_parser import BaseGraphCheckParser
from checkov.graph.checks.checks_infra.resources_types import resources_types
from checkov.graph.graph_builder.graph_components.attribute_names import CustomAttributes
from checkov.graph.graph_builder.graph_components.block_types import BlockType

CHECKS_POSSIBLE_ENDING = [".yaml"]


class Registry:
    def __init__(self, parser=BaseGraphCheckParser()):
        self.checks = []
        self.parser = parser

    def load_checks(self):
        for root, d_names, f_names in os.walk(os.getcwd()):
            for file in f_names:
                file_ending = os.path.splitext(file)[1]
                if file_ending in CHECKS_POSSIBLE_ENDING:
                    with open(file, "r") as f:
                        check_yaml = yaml.safe_load(f)
                        check_json = json.loads(json.dumps(check_yaml))
                        check = self.parser.parse_raw_check(check_json, resources_types=self._get_resource_types(check_json))

                        self.checks.append(check)

    def run_checks(self, graph_connector):
        check_results = {}
        for check in self.checks:
            passed, failed = check.run(graph_connector)
            check_result = self._process_check_result(passed, [], CheckResult.PASSED)
            check_result = self._process_check_result(failed, check_result, CheckResult.FAILED)
            check_results[check.id] = check_result
        return check_results

    @staticmethod
    def _process_check_result(results, processed_results, result):
        for vertex in results:
            if vertex.get(CustomAttributes.BLOCK_TYPE.value) == BlockType.CUSTOM.value:
                continue
            processed_results.append({'result': result, 'entity': vertex})
        return processed_results

    @staticmethod
    def _get_resource_types(check_json):
        provider = check_json.get("scope", {}).get("provider", "").lower()
        return resources_types.get(provider)
