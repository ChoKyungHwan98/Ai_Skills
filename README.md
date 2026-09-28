# Ai_Skills

## game-tool-visual-director

정보가 많은 게임 기획 도구, 분석 대시보드, 에디터, 포트폴리오 도구, AI 생산성 도구의 화면을 진단하고 재설계하는 스킬입니다. 막연한 피드백을 정보 구조, 시각화, 시각적 위계, 상호작용의 구체적인 문제로 바꾸고, 구현 전 Visual Intent를 정합니다.

사용 예시:

- “이 화면 뭔가 이상해. game-tool-visual-director 기준으로 진단해줘.”
- “현재 UI를 game-tool-visual-director로 분석하고 Visual Intent까지만 작성해. 구현하지 마.”
- “이 dashboard를 분석하고 재설계한 뒤 screenshot critique loop까지 수행해.”

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

# GitHub main을 가져오고 안정 버전을 설치/업데이트
python scripts/manage_skills.py sync --ref origin/main --fetch
```

현재 `3.2.0`은 candidate입니다. 이를 시험하려면 `--allow-candidate`를 명시합니다. 기존 비관리 설치본을 처음 전환할 때는 `--adopt`를 사용하며, 원본 설치본 전체를 백업합니다. 관리된 설치본의 직접 수정은 덮어쓰지 않습니다.

시각화 지침에는 [색상·타이포·차트 표현](skills/game-tool-visual-director/references/visualization-craft.md), [이전/후보 버전 결과 평가](skills/game-tool-visual-director/references/visual-evaluation.md), [선별한 GitHub 출처와 적용 범위](skills/game-tool-visual-director/references/upstream-sources.md)가 포함됩니다.

검증 종류: CI는 패키지와 업데이트/복구 동작만 검사합니다. 디자인 품질은 [실제 화면 사례](evals/cases/review-dashboard/case.json)와 Communication/Craft 리뷰로 확인합니다.
