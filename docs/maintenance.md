# Codex 스킬 유지보수

## 원본과 설치본

- 원본: `https://github.com/ChoKyungHwan98/Ai_Skills`.
- 개발: 원본을 영구 위치에 clone하고 브랜치에서 변경합니다.
- 설치: 커밋된 스킬 폴더 전체를 설치합니다. `references`도 함께 갱신합니다.
- 추적: 설치 폴더의 `.codex-skill-install.json`에 저장소, 버전, 채널, 커밋, 파일별 SHA-256을 기록합니다.

새 환경에서는 `$skill-installer`에게 `skills/game-tool-visual-director` 설치를 요청할 수 있습니다. 이후 이 저장소의 관리 스크립트로 전환하려면 첫 갱신에 `--adopt`를 명시합니다.

기본 설치 위치는 기존 `$CODEX_HOME/skills` 또는 `~/.codex/skills`의 설치본을 우선 재사용합니다. 새 설치는 `~/.agents/skills`를 사용합니다. 별도 경로는 `--dest`로 스킬들을 담는 상위 폴더를 지정합니다. 같은 이름을 여러 탐색 경로에 중복 설치하지 않습니다. Python 3.10 이상과 Git만 필요합니다.

## 사용·업데이트·복구

저장소 체크아웃에서 실행합니다.

```powershell
python scripts/check_skills.py
python -m unittest discover -s tests -v
python scripts/manage_skills.py status

# 현재 미병합 후보 브랜치를 가져와 시험
git fetch origin refs/heads/codex/skill-maintenance:refs/remotes/origin/codex/skill-maintenance
python scripts/manage_skills.py sync --ref origin/codex/skill-maintenance --allow-candidate

# 비관리 설치본의 첫 전환에만 --adopt 추가: 전체 백업 후 교체
python scripts/manage_skills.py sync --ref origin/codex/skill-maintenance --allow-candidate --adopt

# 유지보수 manifest와 stable 버전이 main에 반영된 이후
python scripts/manage_skills.py sync --ref origin/main --fetch

# sync가 출력한 backup bundle의 경로 사용
python scripts/manage_skills.py rollback --backup "C:/path/to/backup-bundle"
```

`sync`는 지정한 ref를 커밋으로 고정하고 검사한 뒤 설치합니다. 작업 중인 미커밋 파일을 설치하지 않습니다. 후보는 `--allow-candidate` 없이는 설치되지 않습니다. `--fetch`는 원본 main만 가져오며 앱 종료나 checkout 변경을 하지 않습니다. private 저장소에는 사용자의 Git 인증이 필요합니다. 자격 증명은 설치 기록에 저장하지 않습니다.

현재 main은 유지보수 manifest 도입 이전의 baseline입니다. 후보 시험은 위 개발 브랜치 명령을 사용합니다. 로컬 브랜치의 커밋을 시험하려면 `--ref HEAD --allow-candidate`를 지정할 수 있습니다.

업데이트 전에 설치본의 실제 파일 해시와 기록을 비교합니다. 직접 수정되거나 파일이 추가/삭제된 관리 설치본은 중단하고 변경 목록을 보여줍니다. 수정 내용을 원본 브랜치에 반영하거나 별도로 보존한 뒤 진행하세요. `--adopt`는 비관리 설치본 전환에만 쓰이며 수정된 관리 설치본을 강제 덮어쓰지 않습니다.

기본 백업 위치는 `~/.codex/skill-backups/<skill>/<timestamp>/`입니다. `payload`는 기존 설치본 전체이고 `receipt.json`은 대상과 해시입니다. 복구는 백업 무결성과 현재 설치본을 확인한 뒤 진행하고, 복구 직전 설치본도 다시 백업합니다. 백업은 자동 삭제하지 않습니다.

첫 전환 이전의 비관리 설치본으로 복구하면 상태도 `unmanaged`로 돌아갑니다. 다시 관리 설치로 전환할 때 `--adopt`를 명시하세요.

새 파일은 다음 턴에서 사용할 수 있습니다. 스킬이 나타나지 않으면 Codex를 재시작하세요. GitHub 변경을 자동 설치하거나 모델이 대화에서 자동 학습한다고 가정하지 않습니다.

## 발전 루프

1. 실제 실패를 기록: 요청, 보호할 결정, 관찰된 문제, 화면과 데이터/선택/viewport 조건.
2. 작은 수정: `SKILL.md`에는 판단을 바꾸는 핵심 지침만; 상세 기준은 관련 reference에 유지.
3. 회귀 사례 추가: 스킬 폴더의 `evals/evals.json`에 프롬프트와 관찰할 행동을 기록. 필요한 실제 화면은 저장소 루트 `evals/cases`에 두고 스킬 설치본에는 복제하지 않음.
4. 패키지 검사 및 updater 테스트. 통과는 링크, 버전, 배포 안정성에 대한 근거임.
5. 행동 평가: 사례별 실제 요청을 수행하고 결과·도구 사용·화면을 기록. 화면이 없으면 Craft를 검증했다고 쓰지 않음. 사용자 반응과 평가자의 근거를 구분.
6. 관련 행동/시각적 평가가 통과하면 PR에 근거를 첨부하고 `channel`을 stable로 승격. 승인된 원본 커밋을 설치.

새 버전에는 `SKILL.md`의 `metadata.version`, `releases.json`, `CHANGELOG.md`를 함께 갱신합니다. 포장 검사만 통과한 버전은 candidate를 유지합니다. 문제 발생 시 rollback하고 실패를 다음 회귀 사례로 남깁니다.

## 도구 선택

명시한 스킬을 우선 사용하고, 현재 작업에 도움이 될 때만 다른 스킬을 보조로 사용합니다. 사용자의 금지·허용은 그 작업과 명시한 범위에 적용합니다. 한 번의 결과를 근거로 Impeccable 등 특정 스킬의 영구 금지 규칙을 만들지 않습니다.

## 평가 기록

각 실행은 `.eval-runs/<date>/<case-id>/`에 기록할 수 있습니다. 아래 항목을 남기세요.

- 스킬 버전과 커밋, 평가 프롬프트, 사용자 제약
- 입력 자료와 실제 캡처 환경 (viewport, 데이터, 선택 상태, 캡처 방식)
- 실제 수행한 도구·변경·검증, before/after 경로
- Communication: PASS / NEEDS REVISION / NOT VERIFIED, 관찰 근거
- Craft: PASS / NEEDS REVISION / NOT VERIFIED, 관찰 근거
- 데이터 무결성 및 중요한 상호작용 검증, 남은 문제
- 사용자 피드백, 다음 가설과 수정

동일 조건의 before/after가 없으면 비교 한계를 명시합니다. 사례 목록이 존재한다는 사실이나 자동 검사 성공을 행동 평가 완료로 보고하지 마세요.
