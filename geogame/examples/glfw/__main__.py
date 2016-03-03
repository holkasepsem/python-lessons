import sys
import glfw
# import OpenGL


def main():
    if not glfw.init(): 
        sys.exit("Library cannot be initialized!")
   
    # Create a windowed mode window and its OpenGL context.
    window = glfw.create_window(640, 480, "GLFW Example", None, None)
    if not window:
        glfw.terminate()
        sys.exit("Window cannot be created!")

    # Make the window's context current.
    glfw.make_context_current(window)

    # Loop until the user closes the window.
    while not glfw.window_should_close(window):
        # XXX ... some processing ...
        # Swap front and back buffers.
        glfw.swap_buffers(window)
        # Poll for and process events.
        glfw.poll_events()

    glfw.terminate()
    sys.exit(0)

if __name__ == "__main__":
    main()
