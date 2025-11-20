SUMMARY.md Development Process Summary.  

  

The project was created with a test-driven, iterative, and AI-assisted workflow involving several ways of assisting with the coding, including direct ChatGPT dialogues, GitHub Copilot completions, and continuous test feedback. Throughout the implementation of the task manager CLI and the supporting modules, the development process was carried out in terms of planning, structured coding, debugging, CI automation and refinement.  

  

Preliminary Planning and Specification.  

  

I started by explaining the project requirements: a task manager system: design, models, storage, CLI commands, complete test coverage (tasks1, tasks2, tasks3, tasks4, tasks5). I applied ChatGPT in the practice of planning/explaining mode to divide the project into distinct parts: data models, storage interface, task manager logic, features, and CLI UX. ChatGPT was useful in paraphrasing specifications in my language, making anticipated module duties, and where tests would anticipate particular methods or behaviors. 

  

AI Coding Assistance  

  

I have applied two primary types of AI assistance:  

  

ChatGPT (conversational mode)  

  

I used ChatGPT to a large extent to:  

  

Divide assignment PDFs into steps to be taken.  

  

explaining failing tests  

  

store layer, CLI flow, model classes design work  

  

tracing down complicated bugs (e.g., ModuleNotFoundError, path problems, packaging layouts)  

  

runing CI workflow files  

  

checking and recommending the further steps.  

  

This mode was very important in problem solving and errors interpretation.  

  

GitHub Copilot (chat side panel + inline)  

  

I used Copilot mainly for:  

  

producing boilerplate functions  

  

autofilling data-class repetition code.  

  

writing boiler-plate of argparse to the CLI.  

  

implementing test-driven implementations using docstrings.  

  

adding JSON files to store data.  

  

suggesting small refactors  

  

Copilot excelled in accelerating the small things but sometimes failed to provide a clear picture of the larger picture. It occasionally produced faulty rationale or programmes that were not in line with testing expectations. ChatGPT was much more useful in conceptual advice.  

  

Testing and Debugging  

  

I kept on testing through pytest -q in PowerShell. At the beginning, I encountered problems with tests in tasks3 and tasks5 failing because of missing modules or inappropriate directory hierarchy. ChatGPT assisted in diagnosing the missing init.py files, editable installs (pip install -e .) and PYTHONPATH problems. With the increase in the codebase, tests revealed logic errors in add/update/remove task logic, JSON serialization, and CLI command behavior.  

  

Testing became the motivation toward most design choices, particularly in edge cases such as nonexistent task IDs, empty stores, or CLI argument format.  

  

CI and Project Packaging  

  

Toward the end, I added:  

  

a GitHub Actions Ci workflow (install + test)  

  

an adequate layout of the packaging (src/taskmgr)  

  

a tried entry point of the CLI.  

  

ChatGPT has created the original workflow, which I have modified.  

  

What Worked  

  

ChatGPT as an assistant in planning and debugging.  

  

Early problem exposures through test-driven development.  

  

Copilot to accelerate boilerplate and repetitive code.  

  

Subdivision of work (i.e., 001-task-manager).  

  

Fixing module import problems with editable installs.  

  

What Didn't Work / False Starts  

  

Executing pytest prior to configuration of the packaging (resulted in premature confusion)  

  

Attempts to correct tasks3 tests despite tasks5 being the only important ones.  

  

Copilot producing incorrect method signatures that were not spec compliant.  

  

There were several Git conflicts of pushing before pulling.  

  

Improperly configured CI initially because of improper working directory.  

  

Final Reflection  

  

The process of my development turned out to be a combination of human logic, planning with AI assistance, code generation with AI assistance, and following automated tests to the letter. ChatGPT, used with Copilot, and continuous pytest feedback, which was used the most at the final stage of development. This formed a rigorous, iterative development process that enhanced the quality of code and my knowledge of full-stack Pythons project structure.  

 

 
