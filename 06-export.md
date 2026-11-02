# 06. Unity와 파일 내보내기

- 일반적으로 Unity용 애니메이션 모델은 FBX로 내보낼 수 있다.
- 내보내기 전 Armature, 메시, 액션, 스케일, 좌표축, 애니메이션 포함 옵션을 확인한다.
- Blender의 FBX Export UI에서 선택 오브젝트만 내보낼지, Bake Animation을 사용할지 결정한다.
- Unity에서 FBX 임포트 후 Rig 탭의 Animation Type, Animation 탭의 클립과 루프를 확인한다.
- glTF/GLB도 선택지이지만 대상 엔진·플러그인의 애니메이션 지원 범위를 확인해야 한다.

**검증**: Unity에서 1) 본 구조, 2) 크기, 3) 방향, 4) 루프, 5) 루트 모션을 테스트한다.
