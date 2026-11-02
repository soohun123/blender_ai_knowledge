# 01. 기본 개념

**목표**: 애니메이션 생성 전 씬 상태를 파악한다.

- `bpy.data.objects`: 현재 파일에 존재하는 오브젝트 데이터 집합.
- `bpy.context.scene`: 현재 씬. `scene.frame_current`는 현재 프레임.
- `obj.location`, `obj.rotation_euler`, `obj.scale`: 변환 값.
- Object Mode: 오브젝트 단위 작업. Edit Mode: 메시·뼈대 구조 수정. Pose Mode: Armature 포즈 조작.
- `scene.render.fps`: 프레임레이트. 실제 재생 시간은 프레임 수 / fps.

```python
import bpy
scene = bpy.context.scene
print(scene.frame_start, scene.frame_end, scene.render.fps)
for obj in scene.objects:
    print(obj.name, obj.type)
```

**주의**: 활성 오브젝트와 선택된 오브젝트는 다르다. 모드 의존 오퍼레이터 실행 전에 둘을 확인한다.
