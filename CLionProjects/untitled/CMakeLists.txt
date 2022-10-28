cmake_minimum_required(VERSION 3.21)
project(untitled C)

set(CMAKE_C_STANDARD 99)

add_executable(untitled main.c)
set_target_properties(untitled PROPERTIES COMPILE_FLAGS "-m32" LINK_FLAGS "-m32")
