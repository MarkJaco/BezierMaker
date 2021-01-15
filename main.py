"""
main module, calls other modules

about this project:
This project will help creating bezier curves for describing outlines of pictures

creator: Mark Jacobsen
"""
import application


if __name__ == "__main__":
    app = application.Application(1000, 800)
    app.run()
