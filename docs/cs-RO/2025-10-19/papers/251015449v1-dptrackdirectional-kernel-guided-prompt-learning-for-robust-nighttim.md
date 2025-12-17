---
layout: default
title: DPTrack:Directional Kernel-Guided Prompt Learning for Robust Nighttime Aerial Tracking
---

# DPTrack:Directional Kernel-Guided Prompt Learning for Robust Nighttime Aerial Tracking

**arXiv**: [2510.15449v1](https://arxiv.org/abs/2510.15449) | [PDF](https://arxiv.org/pdf/2510.15449.pdf)

**作者**: Zhiqiang Zhu, Xinbo Gao, Wen Lu, Jie Li, Zhaoyang Wang, Mingqian Ge

---

## 💡 一句话要点

**提出DPTrack，通过方向性核引导提示学习解决夜间空中跟踪中提示模糊问题**

**关键词**: `夜间空中跟踪` `提示学习` `方向性核` `拓扑结构` `视觉仿生` `目标跟踪`

## 📋 核心要点

1. 现有夜间空中跟踪器仅依赖空间定位监督，导致提示模糊，难以聚焦目标特征
2. DPTrack利用拓扑结构编码方向性核，生成精确提示，增强特征表示和定位能力
3. 在标准基准测试中表现优异，代码已开源

## 📄 摘要（原文）

> Existing nighttime aerial trackers based on prompt learning rely solely on
> spatial localization supervision, which fails to provide fine-grained cues that
> point to target features and inevitably produces vague prompts. This limitation
> impairs the tracker's ability to accurately focus on the object features and
> results in trackers still performing poorly. To address this issue, we propose
> DPTrack, a prompt-based aerial tracker designed for nighttime scenarios by
> encoding the given object's attribute features into the directional kernel
> enriched with fine-grained cues to generate precise prompts. Specifically,
> drawing inspiration from visual bionics, DPTrack first hierarchically captures
> the object's topological structure, leveraging topological attributes to enrich
> the feature representation. Subsequently, an encoder condenses these
> topology-aware features into the directional kernel, which serves as the core
> guidance signal that explicitly encapsulates the object's fine-grained
> attribute cues. Finally, a kernel-guided prompt module built on
> channel-category correspondence attributes propagates the kernel across the
> features of the search region to pinpoint the positions of target features and
> convert them into precise prompts, integrating spatial gating for robust
> nighttime tracking. Extensive evaluations on established benchmarks demonstrate
> DPTrack's superior performance. Our code will be available at
> https://github.com/zzq-vipsl/DPTrack.

