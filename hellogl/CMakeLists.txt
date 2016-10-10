cmake_minimum_required(VERSION 3.5)

project(hellogl LANGUAGES C)
find_package(OpenGL REQUIRED)
find_package(GLUT REQUIRED)
add_executable(hellogl hellogl.c)
target_link_libraries(hellogl ${OPENGL_LIBRARIES} ${GLUT_LIBRARY})
install(TARGETS hellogl DESTINATION bin)

# FIXME: remove opengl-launch once base wrappers set LIBGL_DRIVERS_PATH
# See https://bugs.launchpad.net/snappy/+bug/1584178
install(PROGRAMS opengl-launch DESTINATION bin)
