---
layout: default
title: MV-TAP: Tracking Any Point in Multi-View Videos
---

# MV-TAP: Tracking Any Point in Multi-View Videos

**arXiv**: [2512.02006v1](https://arxiv.org/abs/2512.02006) | [PDF](https://arxiv.org/pdf/2512.02006.pdf)

**作者**: Jahyeok Koo, Inès Hyeonsu Kim, Mungyeom Kim, Junghyun Park, Seohyun Park, Jaeyeong Kim, Jung Yi, Seokju Cho, Seungryong Kim

---

## 💡 一句话要点

**提出MV-TAP以解决多视角视频中动态场景点跟踪问题**

**关键词**: `多视角视频` `点跟踪` `跨视角注意力` `相机几何` `合成数据集`

## 📋 核心要点

1. 核心问题：多视角视频中动态对象的点跟踪，需跨视角整合信息以提高轨迹完整性和可靠性。
2. 方法要点：利用相机几何和跨视角注意力机制聚合时空信息，增强跟踪性能。
3. 实验或效果：构建大规模合成训练数据集和真实评估集，在挑战性基准上优于现有方法。

## 📄 摘要（原文）

> Multi-view camera systems enable rich observations of complex real-world scenes, and understanding dynamic objects in multi-view settings has become central to various applications. In this work, we present MV-TAP, a novel point tracker that tracks points across multi-view videos of dynamic scenes by leveraging cross-view information. MV-TAP utilizes camera geometry and a cross-view attention mechanism to aggregate spatio-temporal information across views, enabling more complete and reliable trajectory estimation in multi-view videos. To support this task, we construct a large-scale synthetic training dataset and real-world evaluation sets tailored for multi-view tracking. Extensive experiments demonstrate that MV-TAP outperforms existing point-tracking methods on challenging benchmarks, establishing an effective baseline for advancing research in multi-view point tracking.

