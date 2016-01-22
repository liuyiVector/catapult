# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
import os
import tempfile

from perf_insights.mre import trace_handle


class InMemoryTraceHandle(trace_handle.TraceHandle):
  def __init__(self, url, display_name, metadata, data):
    super(InMemoryTraceHandle, self).__init__(url, display_name, metadata)
    self.data = data

  def Open(self):
    f = tempfile.NamedTemporaryFile()
    f.write(self.data)
    f.flush()
    f.seek(0)
    return f
