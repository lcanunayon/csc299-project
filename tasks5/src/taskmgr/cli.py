import argparse
import json
from typing import Optional
from .store import FileStore


def _print(obj, json_mode: bool = False):
    if json_mode:
        print(json.dumps(obj, ensure_ascii=False))
    else:
        if isinstance(obj, list):
            if not obj:
                print("No tasks")
                return
            for o in obj:
                print(f"[{o.get('id')}] {o.get('title')} (completed={o.get('completed')})")
        elif isinstance(obj, dict):
            for k, v in obj.items():
                print(f"{k}: {v}")
        else:
            print(obj)


def main(argv: Optional[list] = None):
    parser = argparse.ArgumentParser(prog="task")
    sub = parser.add_subparsers(dest="cmd")

    add_p = sub.add_parser("add", help="Create a new task")
    # support both `--title` (legacy/explicit) and a positional `title`
    add_p.add_argument("--title", dest="title")
    add_p.add_argument("title", nargs="?")
    add_p.add_argument("--description")
    add_p.add_argument("--json", action="store_true")

    done_p = sub.add_parser("done", help="Mark a task completed")
    done_p.add_argument("id", type=int)
    done_p.add_argument("--json", action="store_true")

    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument("--completed", choices=["true", "false"], required=False)
    list_p.add_argument("--json", action="store_true")

    show_p = sub.add_parser("show", help="Show a task")
    show_p.add_argument("id", type=int)
    show_p.add_argument("--json", action="store_true")

    update_p = sub.add_parser("update", help="Update a task")
    update_p.add_argument("id", type=int)
    update_p.add_argument("--title")
    update_p.add_argument("--description")
    update_p.add_argument("--completed", choices=["true", "false"])
    update_p.add_argument("--json", action="store_true")

    delete_p = sub.add_parser("delete", help="Delete a task")
    delete_p.add_argument("id", type=int)
    delete_p.add_argument("--force", action="store_true")

    args = parser.parse_args(argv)
    store = FileStore()

    if args.cmd == "add":
        # fallback: if argparse didn't populate title (e.g., when invoked via -m),
        # attempt to read --title from raw argv for compatibility
        if not args.title:
            import sys as _sys

            raw = list(argv) if argv is not None else _sys.argv[1:]
            if "--title" in raw:
                i = raw.index("--title")
                if i + 1 < len(raw):
                    args.title = raw[i + 1]

        task = store.create(args.title, args.description)
        _print(task.to_dict(), json_mode=args.json)
        return 0

    if args.cmd == "list":
        completed = None
        if args.completed == "true":
            completed = True
        elif args.completed == "false":
            completed = False
        tasks = [t.to_dict() for t in store.list(completed=completed)]
        _print(tasks, json_mode=args.json)
        return 0

    if args.cmd == "show":
        task = store.get(args.id)
        if not task:
            print("Task not found", flush=True)
            return 2
        _print(task.to_dict(), json_mode=args.json)
        return 0

    if args.cmd == "update":
        fields = {}
        if args.title:
            fields["title"] = args.title
        if args.description is not None:
            fields["description"] = args.description
        if args.completed is not None:
            fields["completed"] = args.completed == "true"
        updated = store.update(args.id, **fields)
        if not updated:
            print("Task not found", flush=True)
            return 2
        _print(updated.to_dict(), json_mode=args.json)
        return 0

    if args.cmd == "done":
        updated = store.update(args.id, completed=True)
        if not updated:
            print("Task not found", flush=True)
            return 2
        _print(updated.to_dict(), json_mode=args.json)
        return 0

    if args.cmd == "delete":
        if not args.force:
            confirm = input(f"Delete task {args.id}? [y/N]: ")
            if confirm.lower() != "y":
                print("Aborted")
                return 1
        ok = store.delete(args.id)
        if not ok:
            print("Task not found")
            return 2
        print("Deleted")
        return 0

    parser.print_help()
    return 0
