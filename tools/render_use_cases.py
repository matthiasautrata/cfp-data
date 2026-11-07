# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""Render docs/data/use-cases.yaml into the generated section of the use-case doc.

Usage:
  uv run tools/render_use_cases.py           # validate and write
  uv run tools/render_use_cases.py --check   # validate; exit 1 if the doc is stale
"""
import os
import posixpath
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "docs/data/use-cases.yaml"
DOC = "docs/problem/02-stakeholders-use-cases.md"
BEGIN = "<!-- BEGIN GENERATED: tools/render_use_cases.py from docs/data/use-cases.yaml. Do not edit. -->"
END = "<!-- END GENERATED -->"
FACT_DIMENSIONS = {"valid_time", "record_time", "modality", "oracle_authority", "source_authority", "provenance"}
ANSWER_REQUIREMENTS = {"dependencies", "freshness"}
STATUSES = {"candidate", "validated"}


def fail(msg):
    sys.exit(f"error: {msg}")


def validate(data, doc_text):
    activities = set(re.findall(r"^\| (AC-\d+) \|", doc_text, flags=re.M))
    uc_ids, cq_ids = set(), set()
    for uc in data["use_cases"]:
        if uc["id"] in uc_ids:
            fail(f"duplicate {uc['id']}")
        uc_ids.add(uc["id"])
        if uc["activity"] not in activities:
            fail(f"{uc['id']}: unknown activity {uc['activity']}")
        if not uc.get("questions"):
            fail(f"{uc['id']}: no competency questions")
        for q in uc["questions"]:
            if q["id"] in cq_ids:
                fail(f"duplicate {q['id']}")
            cq_ids.add(q["id"])
            bad = set(q["fact_dimensions"]) - FACT_DIMENSIONS
            if bad:
                fail(f"{q['id']}: unknown fact dimensions {sorted(bad)}")
            bad = set(q.get("answer_requirements", [])) - ANSWER_REQUIREMENTS
            if bad:
                fail(f"{q['id']}: unknown answer requirements {sorted(bad)}")
            if q["status"] not in STATUSES:
                fail(f"{q['id']}: unknown status {q['status']}")
    unused = activities - {uc["activity"] for uc in data["use_cases"]}
    if unused:
        fail(f"activities without a use case: {sorted(unused)}")


def code(text):
    return re.sub(r"<([^>]+)>", r"`<\1>`", text)


def words(items):
    return ", ".join(i.replace("_", " ") for i in items) or "—"


def link(driver):
    path, _, anchor = driver["link"].partition("#")
    rel = posixpath.relpath(path, posixpath.dirname(DOC))
    return f"[{driver['label']}]({rel}{'#' + anchor if anchor else ''})"


def render(data):
    out = ["### Use Cases", "",
           "| ID | Activity | Actor | Need | Questions | Driver | Status |",
           "|---|---|---|---|---|---|---|"]
    for uc in data["use_cases"]:
        qs = ", ".join(q["id"] for q in uc["questions"])
        status = "validated" if all(q["status"] == "validated" for q in uc["questions"]) else "candidate"
        out.append(f"| {uc['id']} | {uc['activity']} | {uc['actor']} | {uc['need']} | {qs} | {link(uc['driver'])} | {status} |")
    out += ["", "### Competency Questions", "",
            "| ID | Use case | Question | Entities | Fact dimensions | Answer requirements | Expected answer | Status |",
            "|---|---|---|---|---|---|---|---|"]
    for uc in data["use_cases"]:
        for q in uc["questions"]:
            ents = words(q["entities"])
            if q.get("attributes"):
                ents += "; attributes: " + words(q["attributes"])
            out.append(f"| {q['id']} | {uc['id']} | {code(q['question'])} | {ents} | "
                       f"{words(q['fact_dimensions'])} | {words(q.get('answer_requirements', []))} | "
                       f"{q['answer']} | {q['status']} |")
    return "\n".join(out)


def main():
    os.chdir(ROOT)
    data = yaml.safe_load(open(SRC))
    doc = open(DOC).read()
    if BEGIN not in doc or END not in doc:
        fail(f"markers missing in {DOC}")
    validate(data, doc)
    head, rest = doc.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{BEGIN}\n{render(data)}\n{END}{tail}"
    if "--check" in sys.argv:
        if new != doc:
            fail(f"{DOC} is stale; run: uv run tools/render_use_cases.py")
        print("ok")
        return
    if new != doc:
        open(DOC, "w").write(new)
    n = sum(len(uc["questions"]) for uc in data["use_cases"])
    print(f"rendered {len(data['use_cases'])} use cases, {n} questions")


if __name__ == "__main__":
    main()
