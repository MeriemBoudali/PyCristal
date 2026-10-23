import pycristal as pc

def sync_project():
    pc.title("PyCristal Demo")
    pc.info("Application started successfully.")
    pc.success("Project build completed.")
    pc.warning("A few files were skipped.")
    pc.error("Something went wrong.")
    pc.debug("Debug mode enabled.")
    pc.question("Would you like to continue?")
    pc.header("Status Report", width=42, color=pc.GREEN)
    pc.box("Everything is running smoothly.", title="Summary", color=pc.RED)


if __name__ == "__main__":
    sync_project()