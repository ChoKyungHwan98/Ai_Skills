# Design-ownership walkthrough for 3.3.0

## Inputs and limits

Maintainer walkthrough, performed while revising the skill on 2026-09-28. Baseline: candidate 3.2.0 at `294e968542ef78887072139c0e79843359cc2779`. Candidate: the 3.3.0 instructions in this PR; this record is committed with them. No independent agent or reviewer was used, and this is not a matched old/candidate execution.

Inspected the actual 1920×1080 `before-craft.jpg` from [the historical dashboard case](../cases/review-dashboard/case.json). The capture shows Palworld, 1,343 analyzed reviews, and optimization selected. The historical screen is an input, not an output produced by 3.3.0. No application source, runnable UI, or machine-readable data was provided for this walkthrough.

Exercise request: “디자인을 잘 몰라서 설명하기 어려워. 레퍼런스도 없어. 지금 구성은 유지하고 문제와 네 추천만 설명해줘. 아직 수정하지 마.” This exercises the critique-only branch of scenarios 30–32; implementation scenarios remain unexecuted.

## Observation and recommendation from the actual input

The existing headline makes the takeaway visible: preserve pal design and investigate optimization. The priority map and adjacent selected-topic inspector support that task. There is no reason in this capture to reset their composition.

The selected optimization label and its 60-mention/68%-complaint values use a small treatment close to ordinary chart labels, even though they are important evidence. The close price/open-world group packs both topics and values beside a small badge. At this viewport, these deserve a clearer type and grouping treatment before changing the chart or adding decoration. The red selected mark already has a dark boundary; keep its complaint meaning and existing selection cue.

Recommended direction, expressed for the user:

> 지도와 오른쪽 상세 패널은 유지하겠습니다. 지금은 차트의 핵심 주제와 수치가 다른 작은 라벨 사이에 묻혀 보입니다. 선택한 ‘최적화’의 이름과 수치를 한 묶음으로 더 또렷하게 만들고, 가까이 있는 ‘가격’과 ‘오픈월드’는 이름과 수치를 줄별로 맞추겠습니다. 불만의 붉은색과 기존 선택 테두리는 유지해, 의미가 바뀌지 않게 하겠습니다.

This is one proposed treatment tied to visible evidence. It does not require the user to choose a font, color, style name, or reference. No application files were edited, respecting the exercise request. A later implementation must verify true mark positions, size meaning, actual typography and contrast, and access to both nearby topics.

## Verdicts and remaining work

- Input-screen Communication: **PASS for the visible first-glance target and reading order only**. The takeaway, priority map, and supporting inspector are recognizable. Hidden data and live interaction are outside this verdict.
- Input-screen Craft: **NEEDS REVISION** for the small evidence annotations and tightly packed two-topic label. This is a judgment of the historical input, not of candidate output.
- Candidate design ownership: a concrete recommendation is recorded without an aesthetic question. This is maintainer evidence only, not an independent behavioral PASS.
- Candidate rendered Communication/Craft and live Interaction: **NOT VERIFIED**. No candidate implementation or after capture was produced.

Keep 3.3.0 as candidate. Next: execute the baseline and candidate on the same runnable project, request, data, viewport, and selected state; inspect new renders and affected interactions. Record unnecessary questions, proposal-only stopping, lost protected decisions, and visible quality changes separately. Packaging validation and regression prompt count do not establish that these behaviors pass.
