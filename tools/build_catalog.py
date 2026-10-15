#!/usr/bin/env python3
"""Build the portable catalog from papers.json; Python standard library only."""
from pathlib import Path
from datetime import date
import json
import re

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'papers.json').read_text(encoding='utf-8'))
assert data['schemaVersion'] == 1, 'Unsupported schema version'
assert isinstance(data['papers'], list), 'papers must be a list'
ids = set()
for paper in data['papers']:
    paper_id = paper['id']
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', paper_id), f'Invalid id: {paper_id}'
    assert paper_id not in ids, f'Duplicate paper id: {paper_id}'
    ids.add(paper_id)
    assert paper['href'] == f'papers/{paper_id}/index.html', f'Unexpected path: {paper_id}'
    assert (ROOT / paper['href']).is_file(), f'Missing HTML: {paper_id}'
    for field in ['title', 'subject', 'grade', 'term', 'description', 'scope']:
        assert isinstance(paper[field], str) and paper[field].strip(), f'Missing {field}: {paper_id}'
    date.fromisoformat(paper['addedOn'])
    assert isinstance(paper['unitCount'], int) and paper['unitCount'] > 0
    assert isinstance(paper['exerciseCount'], int) and paper['exerciseCount'] >= 0
    assert isinstance(paper['hasWriting'], bool)
    assert isinstance(paper['tags'], list) and all(isinstance(tag, str) for tag in paper['tags'])

payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
template = (ROOT / 'tools/catalog.template.html').read_text(encoding='utf-8')
assert template.count('__PAPERS_DATA__') == 1
(ROOT / 'index.html').write_text(template.replace('__PAPERS_DATA__', payload), encoding='utf-8')
print(f'Built catalog: {len(ids)} paper(s); all IDs, metadata and local links validated.')
