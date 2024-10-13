def write_markdown(
    log, issql=False, header=False, last_in_group=False, new_log_file=False
):
    log = log.strip()
    with open("Query_results.md", "w" if new_log_file else "a") as file:
        if issql:
            file.write(f"\n```sql\n{log}\n```\n\n")
        elif header:
            file.write(f"### {log} ### \n")
        elif last_in_group:
            file.write(f"\n{log}\n\n<br /><br />\n\n")
        else:
            file.write(f"{log}<br />")
