cmake_minimum_required(VERSION 3.23)
project(CDLab C)

set(CMAKE_C_STANDARD 11)

add_executable(CDLab
        Test/firstprog.c TEMP/test.c TEMP/test.cpp)
