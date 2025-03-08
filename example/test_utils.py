import os
from typing import List
from crimson.tracer.tracer import TraceEvent

def normalize_filename(filename: str, keep_last: int) -> str:
    """
    Normalize a file path by keeping only the last `keep_last` segments.

    For example, if filename is '/home/user/project/module/script.py' and 
    keep_last=2, the function returns 'module/script.py'.
    """
    parts = filename.split(os.sep)
    return os.path.join(*parts[-keep_last:]) if len(parts) >= keep_last else filename

def normalize_trace_result_filenames(trace_result: List[TraceEvent], keep_last: int = 3) -> List[TraceEvent]:
    """
    Returns a new list of TraceEvent objects with normalized 'filename' fields,
    keeping only the last `keep_last` segments of the file path.

    Args:
        trace_result (List[TraceEvent]): The original trace events.
        keep_last (int): Number of trailing segments of the file path to keep.

    Returns:
        List[TraceEvent]: The trace events with normalized filenames.
    """
    normalized_trace = []
    for event in trace_result:
        event_dict = event.dict()
        event_dict['filename'] = normalize_filename(event_dict['filename'], keep_last)
        normalized_trace.append(TraceEvent(**event_dict))
    return normalized_trace
