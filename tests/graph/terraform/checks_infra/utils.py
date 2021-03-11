def verify_report(report, expected_results):
    for check_id in expected_results:
        found = False
        for resource in expected_results[check_id]['should_pass']:
            for record in report.passed_checks:
                if record.check_id == check_id and record.resource == resource:
                    found = True
                    break
            if not found:
                return f"expected resource {resource} to pass in check {check_id}"
        found = False
        for resource in expected_results[check_id]['should_fail']:
            for record in report.failed_checks:
                if record.check_id == check_id and record.resource == resource:
                    found = True
                    break
            if not found:
                return f"expected resource {resource} to fail in check {check_id}"

    return None
