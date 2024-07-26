# rename.py Documentation

The `rename.py` script is a command-line tool designed to automatically rename EPUB files based on their metadata. It is particularly useful for organizing large collections of EPUB files.

## Installation

To use `rename.py`, you need to set up a Python virtual environment. Here's how you can do it:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create your virtual environment.
3. Run the following command to create a new virtual environment:

    ```shell
    python3 -m venv myenv
    ```

    Replace `myenv` with the desired name for your virtual environment.

4. Activate the virtual environment by running the appropriate command for your operating system:

    - **Windows**:

      ```shell
      myenv\Scripts\activate
      ```

    - **MacOS/Linux**:

      ```shell
      source myenv/bin/activate
      ```

5. Once the virtual environment is activated, you can proceed with the installation.

## Usage

To use `rename.py`, follow these steps:

1. Activate your Python virtual environment as described in the installation section.

2. Navigate to the directory where your EPUB files are located.

3. Run the following command to execute the `rename.py` script:

    ```shell
    python rename.py
    ```

    The script will automatically scan the directory for EPUB files and rename them based on their metadata.

    **Note:** The script uses the EPUB's title metadata to generate the new file name. If the EPUB file does not have a title, it will be skipped.

4. After the script finishes, you will find the renamed EPUB files in the same directory.

That's it! You have successfully used `rename.py` to automatically rename your EPUB files.
