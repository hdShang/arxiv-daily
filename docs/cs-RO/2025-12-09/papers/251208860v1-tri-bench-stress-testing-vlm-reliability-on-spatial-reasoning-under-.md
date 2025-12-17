---
layout: default
title: Tri-Bench: Stress-Testing VLM Reliability on Spatial Reasoning under Camera Tilt and Object Interference
---

# Tri-Bench: Stress-Testing VLM Reliability on Spatial Reasoning under Camera Tilt and Object Interference

**arXiv**: [2512.08860v1](https://arxiv.org/abs/2512.08860) | [PDF](https://arxiv.org/pdf/2512.08860.pdf)

**作者**: Amit Bendkhale

---

## 💡 一句话要点

**提出Tri-Bench基准，测试VLM在相机倾斜和物体干扰下的空间推理可靠性。**

**关键词**: `视觉语言模型` `空间推理` `基准测试` `相机姿态` `几何验证` `物体干扰`

## 📋 核心要点

1. 核心问题：VLM在真实场景变化下几何推理失败，影响可信AI。
2. 方法要点：设计平面三角形问题，隔离相对几何推理，强调相机姿态和物体干扰因素。
3. 实验效果：VLM整体准确率约69%，相机倾斜降低4.1%，物体干扰无显著影响，模型依赖2D图像线索。

## 📄 摘要（原文）

> Verifiable geometric reasoning is a critical component for trustworthy and controllable agentic AI. Despite impressive capabilities, Vision-Language Models (VLMs) often fail under realistic scene changes. We present Tri-Bench, a compact benchmark of planar triangle problems that isolates relative geometric reasoning while stressing two deployment-critical factors: camera pose (planar vs. tilted) and scene context via object interference (10 everyday objects). To test verifiability and control, we evaluate four recent VLMs using a single, fixed prompt whose guardrail explicitly describes a surrounding square border, enabling correct answers via homography. We evaluate six simple tasks over binary and continuous targets, and observe that the overall accuracy with respect to 3D ground truth is modest, ~69% on average (best ~75%, worst ~64%). The same responses align even more closely with 2D projections in the image plane, where mean accuracy is ~72%. All four VLMs consistently fail, with accuracy falling to ~0%, on recognizing minority shape classes (equilateral, isosceles, right-angled triangles). Additionally, overall VLM accuracy degrades by ~4.1% under camera tilt. This demonstrates that models fail to correctly utilize the explicit frame-of-reference hint provided in the prompt and default to 2D image plane cues. Finally, we find that object interference has no significant effect on VLM accuracy.

