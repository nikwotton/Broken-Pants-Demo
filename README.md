This works fine with pipenv:

1. pipenv install --deploy --ignore-pipfile --dev
2. pipenv run pytest -vv test_foobar.py

If you run it through pants though:

1. ./pants test ::

The test written synchronously works fine and the test written async fails due to:

```shell
________________________ ERROR at setup of test_tornado ________________________
file /private/var/folders/lr/8ddj3mvs45vfb5hzrx2nf_xw0000gr/T/pants-sandbox-TzBbMF/test_foobar.py, line 23
  @pytest.mark.gen_test
  async def test_tornado(http_client):
      response = await http_client.fetch('http://www.tornadoweb.org/')
      assert response.code == 200
E       fixture 'http_client' not found
>       available fixtures: app, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, cov, doctest_namespace, monkeypatch, no_cover, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, testrun_uid, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, worker_id
>       use 'pytest --fixtures [testpath]' for help on them.

```