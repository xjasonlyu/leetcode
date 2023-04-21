import os
import requests
from jinja2 import Template


def main():

    with requests.get('https://raw.githubusercontent.com/bunnyxt/lcid/main/problems_all.json') as r:
        r.raise_for_status()
        problems = r.json()

    with open('template.md', encoding='utf-8') as f:
        template = Template(f.read())

    solutions = {}

    for filename in os.listdir('./solutions'):
        name, ext = os.path.splitext(filename)
        pid = filename.split('.', maxsplit=1)[0]
        title = '{pid}. {title}'.\
            format(pid=pid, title=problems[pid]['title'])
        url = 'https://leetcode.com/problems/{slug}/'\
            .format(slug=problems[pid]['titleSlug'])

        with open(f'./solutions/{filename}', encoding='utf-8') as f:
            code = f.read()

        with open(f'./docs/{name}.md', 'w', encoding='utf-8') as f:
            f.write(template.render(
                title=title, 
                url=url,
                lang=ext.lstrip('.'),
                code=code.rstrip()))

        stat = os.stat(f'./solutions/{filename}')
        os.utime(f'./docs/{name}.md', ns=(stat.st_atime_ns, stat.st_mtime_ns))

        solutions[int(pid)] = (title, f'{name}.md')

    solutions_list = []
    for k, v in sorted(solutions.items(), key=lambda x: x[0]):
        solutions_list.append(' ' * 4 + f'- {v[0]}: {v[1]}')

    with open('mkdocs.yml', 'r', encoding='utf-8') as f:
        mkdocs_origin = f.read()
    with open('mkdocs.yml', 'w', encoding='utf-8') as f:
        f.write(mkdocs_origin.replace('#$solutions_list', '\n'.join(solutions_list)))


if __name__ == '__main__':
    main()
