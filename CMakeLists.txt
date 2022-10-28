cmake_minimum_required(VERSION 3.10)
project(TimeOptimalTrajectory)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -pthread")

#glog
set(glog_INCLUDE_DIRS "/usr/include")
set(glog_LIBRARY_DIRS "/usr/lib/x86_64-linux-gnu")
set(glog_LIBS "glog")
INCLUDE_DIRECTORIES(${glog_INCLUDE_DIRS})

#eigen
# find_library(Eigen3 REQUIRED)
set(EIGEN3_INCLUDE_DIRS "/usr/include/eigen3")
message(STATUS "EIGEN3_INCLUDE_DIRS: " ${EIGEN3_INCLUDE_DIRS})
include_directories(${EIGEN3_INCLUDE_DIRS})

include_directories(src)
file(GLOB SRC_LIST src/*.h src/*.cpp)
message(STATUS "SRC_LIST: " ${SRC_LIST})

add_executable(example Example.cpp ${SRC_LIST})
target_link_libraries(example ${glog_LIBS})
add_executable(test Test.cpp ${SRC_LIST})
target_link_libraries(test ${glog_LIBS})
