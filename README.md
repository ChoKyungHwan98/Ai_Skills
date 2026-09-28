# Ai_Skills

## game-tool-visual-director

정보가 많은 게임 기획 도구, 분석 대시보드, 에디터, 포트폴리오 도구, AI 생산성 도구의 화면을 진단하고 재설계·폴리싱하는 스킬입니다. 디자인 용어를 모르거나 레퍼런스가 없어도 사용할 수 있습니다. 현재 화면과 사용 목적을 바탕으로 스킬이 문제를 찾고, 구체적인 디자인 방향을 추천하며, 요청한 범위에서 구현과 실제 화면 검증까지 진행합니다.

사용 예시:

- “이 화면 뭔가 이상해. game-tool-visual-director 기준으로 진단해줘.”
- “현재 UI를 game-tool-visual-director로 분석하고 Visual Intent까지만 작성해. 구현하지 마.”
- “이 dashboard를 분석하고 재설계한 뒤 screenshot critique loop까지 수행해.”
- “디자인을 잘 몰라서 설명하기 어려워. 레퍼런스도 없어. 지금 구성은 유지하고 네가 보기 좋게 다듬어줘.”

색상·폰트·스타일을 먼저 고를 필요는 없습니다. 스킬이 눈에 보이는 변화와 이유를 쉽게 설명합니다. 사용 목적이나 데이터 의미처럼 결과를 좌우하는 사실이 확인되지 않을 때만 필요한 질문을 합니다. “문제만 설명해줘”라고 하면 구현하지 않습니다.

## Codex에서 사용하기

GitHub 원본 → 검증한 커밋 → Codex 설치본 순서로 관리합니다. 전체 운영 절차는 [유지보수 안내](docs/maintenance.md)에 있습니다.

```text
game-tool-visual-director를 사용해줘.
현재 구성은 유지하고 시각적 완성도를 개선해.
실제 화면을 확인하고 구현 후 rendered screenshot으로 검증해.
```

사용할 도구나 보존할 구성은 작업마다 지정할 수 있습니다. 특정 디자인 스킬을 일괄 금지하거나 필수로 요구하지 않습니다.

```powershell
# 원본 저장소의 체크아웃에서 실행 (Python 3.10+, Git)
python scripts/check_skills.py
python scripts/manage_skills.py status

# 아직 main에 합치지 않은 후보 브랜치를 가져와 명시적으로 시험
git fetch origin refs/heads/codex/skill-maintenance:refs/remotes/origin/codex/skill-maintenance
python scripts/manage_skills.py sync --ref origin/codex/skill-maintenance --allow-candidate
```

현재 PR의 `3.3.0`은 candidate이며 main에는 아직 유지보수 manifest가 없습니다. 위 명령은 후보를 시험할 때 사용합니다. 기존 비관리 설치본을 처음 전환할 때만 `--adopt`를 추가하며, 원본 설치본 전체를 백업합니다. 관리된 설치본의 직접 수정은 덮어쓰지 않습니다. 안정 버전이 main에 반영된 뒤에는 `sync --ref origin/main --fetch`로 갱신할 수 있습니다.

시각화 지침에는 [색상·타이포·차트 표현](skills/game-tool-visual-director/references/visualization-craft.md), [이전/후보 버전 결과 평가](skills/game-tool-visual-director/references/visual-evaluation.md), [선별한 GitHub 출처와 적용 범위](skills/game-tool-visual-director/references/upstream-sources.md)가 포함됩니다.

검증 종류: CI는 패키지와 업데이트/복구 동작만 검사합니다. 디자인 품질은 [실제 화면 사례](evals/cases/review-dashboard/case.json)와 Communication/Craft 리뷰로 확인합니다.
