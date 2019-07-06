from book_models.stores.user_file_store import UserFileStore


def test_really_happy_flow_for_user_file_store_interaction():
    file_name = 'test_user_store.txt'
    file_store = UserFileStore(file_name)

    row1 = 'Adrian 3mperor Parola'
    row2 = 'Denis M. Taolen Secret'

    file_store.insert(row1)
    file_store.insert(row2)

    file_store.update(row1, "Adrian M. 3mperor Parola")
    file_store.delete(row2)

    assert len(file_store.read()) == 25

    # really awful way to clean up after ourselves.
    import os
    os.remove(file_name)
