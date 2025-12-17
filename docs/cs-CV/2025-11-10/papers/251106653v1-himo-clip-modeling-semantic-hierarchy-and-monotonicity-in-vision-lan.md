---
layout: default
title: HiMo-CLIP: Modeling Semantic Hierarchy and Monotonicity in Vision-Language Alignment
---

# HiMo-CLIP: Modeling Semantic Hierarchy and Monotonicity in Vision-Language Alignment

**arXiv**: [2511.06653v1](https://arxiv.org/abs/2511.06653) | [PDF](https://arxiv.org/pdf/2511.06653.pdf)

**作者**: Ruijia Wu, Ping Chen, Fei Shen, Shaoan Zhao, Qiang Hui, Huanlin Gao, Ting Lu, Zhaoxiang Liu, Fang Zhao, Kai Wang, Shiguo Lian

---

## 💡 一句话要点

**提出HiMo-CLIP以增强CLIP模型处理复杂文本描述的能力**

**关键词**: `视觉语言对齐` `语义层次建模` `对比学习` `图像文本检索` `长文本处理`

## 📋 核心要点

1. CLIP模型处理复杂文本时忽略语义层次和单调性，导致对齐效果不佳
2. 引入HiDe模块分解语义和MoLo损失函数，强化多粒度对齐和语义顺序
3. 在图像-文本检索基准上表现优异，尤其在长文本和组合描述场景

## 📄 摘要（原文）

> Contrastive vision-language models like CLIP have achieved impressive results
> in image-text retrieval by aligning image and text representations in a shared
> embedding space. However, these models often treat text as flat sequences,
> limiting their ability to handle complex, compositional, and long-form
> descriptions. In particular, they fail to capture two essential properties of
> language: semantic hierarchy, which reflects the multi-level compositional
> structure of text, and semantic monotonicity, where richer descriptions should
> result in stronger alignment with visual content.To address these limitations,
> we propose HiMo-CLIP, a representation-level framework that enhances CLIP-style
> models without modifying the encoder architecture. HiMo-CLIP introduces two key
> components: a hierarchical decomposition (HiDe) module that extracts latent
> semantic components from long-form text via in-batch PCA, enabling flexible,
> batch-aware alignment across different semantic granularities, and a
> monotonicity-aware contrastive loss (MoLo) that jointly aligns global and
> component-level representations, encouraging the model to internalize semantic
> ordering and alignment strength as a function of textual completeness.These
> components work in concert to produce structured, cognitively-aligned
> cross-modal representations. Experiments on multiple image-text retrieval
> benchmarks show that HiMo-CLIP consistently outperforms strong baselines,
> particularly under long or compositional descriptions. The code is available at
> https://github.com/UnicomAI/HiMo-CLIP.

