# -*- coding: utf-8 -*-

TRIGGER_PREFIX = "HM-"

TRIGGER_EVENT_STATUS = dict(
    new="NEW",
    expired="EXPIRED"
)

# NOTE(tianhuan) Don't change this map, some codes depend on it.
ZBX_SEVERITY_MAP = {
    'Disaster':       'critical',
    'High':           'major',
    'Average':        'minor',
    'Warning':        'warning',
    'Information':    'informational',
    'Not classified': 'unknown',
}

# NOTE(tianhuan) Don't change this value, some codes depend on it.
UNBIND_AUTOFIX_SCRIPT_ACTION = "cancel"

AUTOFIX_STATUS = dict(
    success="SUCCESS",
    fixing="FIXING",
    failed="FAILED"
)
