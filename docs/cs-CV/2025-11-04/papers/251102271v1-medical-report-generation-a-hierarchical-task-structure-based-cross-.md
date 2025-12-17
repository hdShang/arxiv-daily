---
layout: default
title: Medical Report Generation: A Hierarchical Task Structure-Based Cross-Modal Causal Intervention Framework
---

# Medical Report Generation: A Hierarchical Task Structure-Based Cross-Modal Causal Intervention Framework

**arXiv**: [2511.02271v1](https://arxiv.org/abs/2511.02271) | [PDF](https://arxiv.org/pdf/2511.02271.pdf)

**作者**: Yucheng Song, Yifan Ge, Junhao Li, Zhining Liao, Zhifang Liao

---

## 💡 一句话要点

**提出分层任务结构跨模态因果干预框架以解决医学报告生成中的多挑战问题**

**关键词**: `医学报告生成` `跨模态对齐` `因果干预` `分层任务分解` `视觉语言模型`

## 📋 核心要点

1. 核心问题：医学报告生成面临领域知识不足、模态对齐差和虚假相关三大挑战
2. 方法要点：通过低中高层次任务分解，结合实体对齐、互指导和因果干预
3. 实验或效果：在实验中显著优于现有方法，代码将公开

## 📄 摘要（原文）

> Medical Report Generation (MRG) is a key part of modern medical diagnostics,
> as it automatically generates reports from radiological images to reduce
> radiologists' burden. However, reliable MRG models for lesion description face
> three main challenges: insufficient domain knowledge understanding, poor
> text-visual entity embedding alignment, and spurious correlations from
> cross-modal biases. Previous work only addresses single challenges, while this
> paper tackles all three via a novel hierarchical task decomposition approach,
> proposing the HTSC-CIF framework. HTSC-CIF classifies the three challenges into
> low-, mid-, and high-level tasks: 1) Low-level: align medical entity features
> with spatial locations to enhance domain knowledge for visual encoders; 2)
> Mid-level: use Prefix Language Modeling (text) and Masked Image Modeling
> (images) to boost cross-modal alignment via mutual guidance; 3) High-level: a
> cross-modal causal intervention module (via front-door intervention) to reduce
> confounders and improve interpretability. Extensive experiments confirm
> HTSC-CIF's effectiveness, significantly outperforming state-of-the-art (SOTA)
> MRG methods. Code will be made public upon paper acceptance.

