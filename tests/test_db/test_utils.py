import os
import pytest
from utils.db_utils import remove_directory

def test_always_pass():
    assert True
    
@pytest.fixture
def setup_db(tmp_path):
    return tmp_path

# # @pytest.fixture
def test_remove_directory_success(setup_db):
    """
    Test the behavior of the remove_directory function when attempting to 
    remove a directory that does exist.

    This test verifies that the `remove_directory` function correctly removes
    the specified directory and all its contents. It sets up a test database
    path, creates a subdirectory within it, and then calls the function to
    remove the directory. The test asserts that the directory no longer exists
    after the removal operation.

    Args:
        setup_db: A fixture that provides the path to the test database.

    Raises:
        AssertionError: If the directory still exists after removal.
    """
    # Arrange
    test_db_path = setup_db
    os.makedirs(os.path.join(test_db_path, "subdir"), exist_ok=True)  # Create a subdirectory

    # Act
    remove_directory(test_db_path)

    # Assert
    assert not os.path.exists(test_db_path)  # Check if the directory was removed

def test_remove_directory_non_existent(setup_db):
    """
    Test the behavior of the remove_directory function when attempting to 
    remove a directory that does not exist.

    This test verifies that calling remove_directory with a non-existent 
    directory path does not raise any errors and that the directory 
    still does not exist after the function call.

    Args:
        setup_db (function): A fixture that sets up the database for testing.
    """
    # Arrange
    non_existent_path = "non_existent_directory"

    # Act
    remove_directory(non_existent_path)  # Should not raise an error
    
    # Assert
    assert not os.path.exists(non_existent_path)  # Confirm it still doesn't exist
