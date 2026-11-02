# 04. 캐릭터 애니메이션

**목표**: 뼈의 포즈를 시간에 따라 기록한다.

```python
arm = bpy.data.objects.get("Armature")
if arm is None or arm.type != 'ARMATURE':
    raise RuntimeError("Armature 오브젝트가 필요합니다")
bone = arm.pose.bones.get("Bone")
if bone is None:
    raise RuntimeError("Bone 포즈 뼈가 없습니다")
bone.rotation_mode = 'XYZ'
bone.rotation_euler = (0, 0, 0)
bone.keyframe_insert(data_path="rotation_euler", frame=1)
bone.rotation_euler.z = 0.5
bone.keyframe_insert(data_path="rotation_euler", frame=20)
```

걷기 루프: 접지(Contact) → 하강(Down) → 통과(Passing) → 상승(Up) → 다음 접지. 좌우 다리 위상과 골반 이동을 맞추고 발 미끄러짐을 확인한다.

**주의**: 뼈 이름, 로컬 회전축, IK/제약 여부에 따라 결과가 달라진다. 기존 리그에는 별도 검증이 필요하다.
