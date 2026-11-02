# 03. 리깅

**목표**: 메시를 Armature에 연결해 뼈대의 움직임으로 변형한다.

1. Armature 추가, Edit Mode에서 뼈 배치.
2. 메시와 Armature의 스케일·회전·위치를 확인.
3. 메시 선택 → Armature 마지막 선택 → `Ctrl+P` → **With Automatic Weights**.
4. Pose Mode에서 뼈 회전, Weight Paint로 영향 범위 수정.

`obj.vertex_groups`는 버텍스 그룹을, `obj.modifiers`의 Armature 모디파이어는 메시 변형 연결을 관리한다.

**흔한 문제**: 자동 가중치 실패는 메시 구조, 중복 버텍스, 비정상 스케일, 복잡한 겹침과 관련될 수 있다. 원본을 보존하고 원인을 순서대로 확인한다.
