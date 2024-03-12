from src.save_to_json import SaveToJSON

some_saver = SaveToJSON('some_path', 'some_data')


def test_init():
    assert some_saver.data_to_save == 'some_data'
    assert some_saver.file_path == 'some_path'