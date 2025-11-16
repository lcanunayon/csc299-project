create a new tasks4 directory and Python package in your repository using uv as before this is a standalone experiment to try out the OpenAI Chat Completions API, so you do not need to copy over any of your PKMS/task software use the OpenAI Chat Completions API to send a paragraph-length description of a task to ChatGPT-5-mini and have it summarize the task as a short phrase add a loop to your code so that it can summarize multiple paragraph-length descriptions (independently of one another) add at least 2 sample paragraph-length descriptions to your code so that running uv run tasks4 will summarize both descriptions and then print the summaries

how do i test

error: No pyproject.toml found in current directory or any parent directory

but there is no toml file in my repo root

Traceback (most recent call last): File "<frozen runpy>", line 198, in _run_module_as_main File "<frozen runpy>", line 88, in _run_code File "C:\commandline\tasks4\src\tasks4\__main__.py", line 1, in <module> from openai import OpenAI ModuleNotFoundError: No module named 'openai'

Built tasks4 @ file:///C:/commandline/tasks4 Uninstalled 1 package in 1ms Installed 18 packages in 296ms Traceback (most recent call last): File "<frozen runpy>", line 198, in _run_module_as_main File "<frozen runpy>", line 88, in _run_code File "C:\commandline\tasks4\src\tasks4\__main__.py", line 5, in <module> client = OpenAI() File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\_client.py", line 137, in __init__ raise OpenAIError( "The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable" ) openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable

PS C:\commandline\tasks4> uv run python -m tasks4 Summaries: Traceback (most recent call last): File "<frozen runpy>", line 198, in _run_module_as_main File "<frozen runpy>", line 88, in _run_code File "C:\commandline\tasks4\src\tasks4\__main__.py", line 49, in <module> main() ~~~~^^ File "C:\commandline\tasks4\src\tasks4\__main__.py", line 45, in main summary = summarize_task(description) File "C:\commandline\tasks4\src\tasks4\__main__.py", line 25, in summarize_task response = client.chat.completions.create( model=MODEL, ...<10 lines>... max_tokens=20, ) File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper return func(*args, **kwargs) File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1189, in create return self._post( ~~~~~~~~~~^ "/chat/completions", ^^^^^^^^^^^^^^^^^^^^ ...<47 lines>... stream_cls=Stream[ChatCompletionChunk], ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ) ^ File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\_base_client.py", line 1259, in post return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)) ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\_base_client.py", line 1047, in request raise self._make_status_error_from_response(err.response) from None openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Incorrect API key provided: your-key*here. You can find your API key at https://platform.openai.com/account/api-keys.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}}

PS C:\commandline\tasks4> uv run python -m tasks4
Summaries:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\commandline\tasks4\src\tasks4\__main__.py", line 49, in <module>
    main()
    ~~~~^^
  File "C:\commandline\tasks4\src\tasks4\__main__.py", line 45, in main
    summary = summarize_task(description)
  File "C:\commandline\tasks4\src\tasks4\__main__.py", line 25, in summarize_task
    response = client.chat.completions.create(
        model=MODEL,
    ...<10 lines>...
        max_tokens=20,
    )
  File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
  File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1189, in create
    return self._post(
           ~~~~~~~~~~^
        "/chat/completions",
        ^^^^^^^^^^^^^^^^^^^^
    ...<47 lines>...
        stream_cls=Stream[ChatCompletionChunk],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\commandline\tasks4\.venv\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}