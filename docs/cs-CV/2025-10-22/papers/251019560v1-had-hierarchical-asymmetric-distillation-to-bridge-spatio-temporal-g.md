---
layout: default
title: HAD: Hierarchical Asymmetric Distillation to Bridge Spatio-Temporal Gaps in Event-Based Object Tracking
---

# HAD: Hierarchical Asymmetric Distillation to Bridge Spatio-Temporal Gaps in Event-Based Object Tracking

**arXiv**: [2510.19560v1](https://arxiv.org/abs/2510.19560) | [PDF](https://arxiv.org/pdf/2510.19560.pdf)

**作者**: Yao Deng, Xian Zhong, Wenxuan Liu, Zhaofei Yu, Jingling Yuan, Tiejun Huang

---

## 💡 一句话要点

**提出分层非对称蒸馏以解决事件相机与RGB相机时空不对称问题**

**关键词**: `事件相机跟踪` `多模态知识蒸馏` `时空不对称` `分层对齐` `目标跟踪`

## 📋 核心要点

1. 核心问题：事件相机与RGB相机成像机制不同导致时空不对称，阻碍多模态融合。
2. 方法要点：设计分层对齐策略，减少信息损失，保持学生网络高效与紧凑。
3. 实验或效果：在高速运动、HDR等场景下优于现有方法，消融实验验证组件有效性。

## 📄 摘要（原文）

> RGB cameras excel at capturing rich texture details with high spatial
> resolution, whereas event cameras offer exceptional temporal resolution and a
> high dynamic range (HDR). Leveraging their complementary strengths can
> substantially enhance object tracking under challenging conditions, such as
> high-speed motion, HDR environments, and dynamic background interference.
> However, a significant spatio-temporal asymmetry exists between these two
> modalities due to their fundamentally different imaging mechanisms, hindering
> effective multi-modal integration. To address this issue, we propose
> {Hierarchical Asymmetric Distillation} (HAD), a multi-modal knowledge
> distillation framework that explicitly models and mitigates spatio-temporal
> asymmetries. Specifically, HAD proposes a hierarchical alignment strategy that
> minimizes information loss while maintaining the student network's
> computational efficiency and parameter compactness. Extensive experiments
> demonstrate that HAD consistently outperforms state-of-the-art methods, and
> comprehensive ablation studies further validate the effectiveness and necessity
> of each designed component. The code will be released soon.

