---
layout: default
title: TubeRMC: Tube-conditioned Reconstruction with Mutual Constraints for Weakly-supervised Spatio-Temporal Video Grounding
---

# TubeRMC: Tube-conditioned Reconstruction with Mutual Constraints for Weakly-supervised Spatio-Temporal Video Grounding

**arXiv**: [2511.10241v1](https://arxiv.org/abs/2511.10241) | [PDF](https://arxiv.org/pdf/2511.10241.pdf)

**作者**: Jinxuan Li, Yi Zhang, Jian-Fang Hu, Chaolei Tan, Tianming Liang, Beihao Xia

---

## 💡 一句话要点

**提出TubeRMC框架以解决弱监督时空视频定位中的目标识别与跟踪不一致问题**

**关键词**: `时空视频定位` `弱监督学习` `管状重建` `视觉语言理解` `时空约束`

## 📋 核心要点

1. 核心问题：弱监督STVG中，独立生成管状区域易导致目标识别失败和跟踪不一致
2. 方法要点：使用文本条件管状重建与时空约束，通过三个重构策略增强管-文本对应
3. 实验或效果：在VidSTG和HCSTVG基准上优于现有方法，可视化显示有效缓解错误

## 📄 摘要（原文）

> Spatio-Temporal Video Grounding (STVG) aims to localize a spatio-temporal tube that corresponds to a given language query in an untrimmed video. This is a challenging task since it involves complex vision-language understanding and spatiotemporal reasoning. Recent works have explored weakly-supervised setting in STVG to eliminate reliance on fine-grained annotations like bounding boxes or temporal stamps. However, they typically follow a simple late-fusion manner, which generates tubes independent of the text description, often resulting in failed target identification and inconsistent target tracking. To address this limitation, we propose a Tube-conditioned Reconstruction with Mutual Constraints (\textbf{TubeRMC}) framework that generates text-conditioned candidate tubes with pre-trained visual grounding models and further refine them via tube-conditioned reconstruction with spatio-temporal constraints. Specifically, we design three reconstruction strategies from temporal, spatial, and spatio-temporal perspectives to comprehensively capture rich tube-text correspondences. Each strategy is equipped with a Tube-conditioned Reconstructor, utilizing spatio-temporal tubes as condition to reconstruct the key clues in the query. We further introduce mutual constraints between spatial and temporal proposals to enhance their quality for reconstruction. TubeRMC outperforms existing methods on two public benchmarks VidSTG and HCSTVG. Further visualization shows that TubeRMC effectively mitigates both target identification errors and inconsistent tracking.

