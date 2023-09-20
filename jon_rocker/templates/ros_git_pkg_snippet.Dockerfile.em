# TODO: this is only tested ros:noetic image
RUN apt-get update -qq \
 && apt-get install -q -y --no-install-recommends build-essential byobu neovim curl wget git sudo python3-catkin-tools python3-vcstool \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ws/src \
 && cd ws/src \
 && git clone @git_url @(branch_name ? "-b " + branch_name) \
 && cd .. \
 && find . -maxdepth 2 -name '*.rosinstall' -exec sh -c "vcs import < {}" \; \
 && rosdep update  \
 && apt-get update -qq \
 && rosdep install --from-path src -iy \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && catkin init \
 && catkin config --extend /opt/ros/noetic \
 && catkin build
