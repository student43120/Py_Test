cmake_minimum_required(VERSION 3.10)

project(MyTest)

set(CMAKE_CXX_STANDARD 11)


./ext4/MyTest


find_package(GTest REQUIRED)
target_link_libraries(GTest::GTest GTest::Main)