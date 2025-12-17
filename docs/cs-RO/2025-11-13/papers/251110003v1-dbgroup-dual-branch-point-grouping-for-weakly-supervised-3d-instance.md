---
layout: default
title: DBGroup: Dual-Branch Point Grouping for Weakly Supervised 3D Instance Segmentation
---

# DBGroup: Dual-Branch Point Grouping for Weakly Supervised 3D Instance Segmentation

**arXiv**: [2511.10003v1](https://arxiv.org/abs/2511.10003) | [PDF](https://arxiv.org/pdf/2511.10003.pdf)

**作者**: Xuexun Liu, Xiaoxu Xu, Qiudan Zhang, Lin Ma, Xu Wang

---

## 💡 一句话要点

**提出DBGroup双分支点分组框架，利用场景级标注解决弱监督3D实例分割问题**

**关键词**: `弱监督学习` `3D实例分割` `点云处理` `伪标签生成` `场景级标注`

## 📋 核心要点

1. 核心问题：弱监督3D实例分割标注成本高，现有方法依赖点击或边界框，效率低
2. 方法要点：双分支点分组生成伪标签，结合语义和掩码线索，并采用细化策略提升质量
3. 实验或效果：在实验中性能优于稀疏点级监督方法，超越场景级监督语义分割方法

## 📄 摘要（原文）

> Weakly supervised 3D instance segmentation is essential for 3D scene understanding, especially as the growing scale of data and high annotation costs associated with fully supervised approaches. Existing methods primarily rely on two forms of weak supervision: one-thing-one-click annotations and bounding box annotations, both of which aim to reduce labeling efforts. However, these approaches still encounter limitations, including labor-intensive annotation processes, high complexity, and reliance on expert annotators. To address these challenges, we propose \textbf{DBGroup}, a two-stage weakly supervised 3D instance segmentation framework that leverages scene-level annotations as a more efficient and scalable alternative. In the first stage, we introduce a Dual-Branch Point Grouping module to generate pseudo labels guided by semantic and mask cues extracted from multi-view images. To further improve label quality, we develop two refinement strategies: Granularity-Aware Instance Merging and Semantic Selection and Propagation. The second stage involves multi-round self-training on an end-to-end instance segmentation network using the refined pseudo-labels. Additionally, we introduce an Instance Mask Filter strategy to address inconsistencies within the pseudo labels. Extensive experiments demonstrate that DBGroup achieves competitive performance compared to sparse-point-level supervised 3D instance segmentation methods, while surpassing state-of-the-art scene-level supervised 3D semantic segmentation approaches. Code is available at https://github.com/liuxuexun/DBGroup.

