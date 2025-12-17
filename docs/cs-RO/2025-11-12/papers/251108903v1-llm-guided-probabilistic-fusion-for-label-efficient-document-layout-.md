---
layout: default
title: LLM-Guided Probabilistic Fusion for Label-Efficient Document Layout Analysis
---

# LLM-Guided Probabilistic Fusion for Label-Efficient Document Layout Analysis

**arXiv**: [2511.08903v1](https://arxiv.org/abs/2511.08903) | [PDF](https://arxiv.org/pdf/2511.08903.pdf)

**作者**: Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma

---

## 💡 一句话要点

**提出LLM引导的概率融合方法，以解决文档布局分析中标签效率低的问题。**

**关键词**: `文档布局分析` `半监督学习` `概率融合` `LLM先验` `伪标签生成` `轻量级骨干网络`

## 📋 核心要点

1. 文档布局理解依赖大量标注数据，半监督学习仍不足。
2. 融合视觉检测与LLM结构先验，通过概率加权生成伪标签。
3. 在PubLayNet上，使用5%标签达到88.2 AP，超越基线方法。

## 📄 摘要（原文）

> Document layout understanding remains data-intensive despite advances in semi-supervised learning. We present a framework that enhances semi-supervised detection by fusing visual predictions with structural priors from text-pretrained LLMs via principled probabilistic weighting. Given unlabeled documents, an OCR-LLM pipeline infers hierarchical regions which are combined with teacher detector outputs through inverse-variance fusion to generate refined pseudo-labels.Our method demonstrates consistent gains across model scales. With a lightweight SwiftFormer backbone (26M params), we achieve 88.2$\pm$0.3 AP using only 5\% labels on PubLayNet. When applied to document-pretrained LayoutLMv3 (133M params), our fusion framework reaches 89.7$\pm$0.4 AP, surpassing both LayoutLMv3 with standard semi-supervised learning (89.1$\pm$0.4 AP, p=0.02) and matching UDOP~\cite{udop} (89.8 AP) which requires 100M+ pages of multimodal pretraining. This demonstrates that LLM structural priors are complementary to both lightweight and pretrained architectures. Key findings include: (1) learned instance-adaptive gating improves over fixed weights by +0.9 AP with data-dependent PAC bounds correctly predicting convergence; (2) open-source LLMs enable privacy-preserving deployment with minimal loss (Llama-3-70B: 87.1 AP lightweight, 89.4 AP with LayoutLMv3); (3) LLMs provide targeted semantic disambiguation (18.7\% of cases, +3.8 AP gain) beyond simple text heuristics.Total system cost includes \$12 for GPT-4o-mini API or 17 GPU-hours for local Llama-3-70B per 50K pages, amortized across training runs.

