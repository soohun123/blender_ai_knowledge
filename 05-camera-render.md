# 05. 카메라와 렌더

카메라 오브젝트도 `location`, `rotation_euler` 키프레임으로 움직인다. 렌더 카메라는 `scene.camera`로 지정한다.

```python
import bpy
scene = bpy.context.scene
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100
scene.render.fps = 30
scene.frame_start = 1
scene.frame_end = 90
```

영상 출력은 Output Properties에서 FFmpeg Video / MPEG-4 / H.264를 설정할 수 있다(빌드의 코덱 지원 확인). 긴 렌더는 PNG 시퀀스를 먼저 출력하는 것이 중단 복구에 유리하다.

**주의**: 저장 경로에 쓰기 권한이 있는지 확인하고 기존 출력물을 덮어쓰지 않도록 한다.
