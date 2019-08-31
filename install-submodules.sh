# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env bash

# Just install the submodules

set -e  # exit when any command fails
set -x

[[ -d "./pybind11" ]] || git clone -b 'v2.2.4' --single-branch --depth 1 https://github.com/pybind/pybind11.git
# TODO: Point to the official  https://github.com/dds-bridge/dds.git
# when pull requests are in
[[ -d open_spiel/games/bridge/double_dummy_solver ]] || \
  git clone -b 'develop' --single-branch --depth 1 https://github.com/jblespiau/dds.git  \
  open_spiel/games/bridge/double_dummy_solver
[[ -d open_spiel/abseil-cpp ]] || \
  git clone -b 'master' --single-branch --depth 1 https://github.com/abseil/abseil-cpp.git \
  open_spiel/abseil-cpp
