---
layout: default
title: Mitigating Object and Action Hallucinations in Multimodal LLMs via Self-Augmented Contrastive Alignment
---

# Mitigating Object and Action Hallucinations in Multimodal LLMs via Self-Augmented Contrastive Alignment

**arXiv**: [2512.04356v1](https://arxiv.org/abs/2512.04356) | [PDF](https://arxiv.org/pdf/2512.04356.pdf)

**作者**: Kai-Po Chang, Wei-Yuan Cheng, Chi-Pin Huang, Fu-En Yang, Yu-Chiang Frank Wang

---

## 💡 一句话要点

**提出SANTA框架以缓解多模态大语言模型在视频描述中的对象和动作幻觉问题**

**关键词**: `多模态大语言模型` `视频描述生成` `幻觉缓解` `对比学习` `自增强训练` `轨迹-短语对齐`

## 📋 核心要点

1. 核心问题：多模态大语言模型在视频描述生成中存在对象和动作的事实性幻觉，动态视频的联合缓解是未解挑战。
2. 方法要点：采用自增强对比对齐，通过幻觉自增强生成负样本，并利用轨迹-短语对比对齐匹配视觉和时序事实。
3. 实验或效果：在幻觉检测基准上优于现有方法，有效减轻对象和动作幻觉，提升描述准确性。

## 📄 摘要（原文）

> Recent advancement in multimodal LLMs (MLLMs) has demonstrated their remarkable capability to generate descriptive captions for input videos. However, these models suffer from factual inaccuracies in the generated descriptions, causing severe hallucination issues. While prior works have explored alleviating hallucinations for static images, jointly mitigating visual object and temporal action hallucinations for dynamic videos remains a challenging and unsolved task. To tackle this challenge, we propose a Self-Augmented Contrastive Alignment (SANTA) framework for enabling object and action faithfulness by exempting the spurious correlations and enforcing the emphasis on visual facts. SANTA employs a hallucinative self-augmentation scheme to identify the potential hallucinations that lie in the MLLM and transform the original captions to the contrasted negatives. Furthermore, we develop a tracklet-phrase contrastive alignment to match the regional objects and relation-guided actions with their corresponding visual and temporal phrases. Extensive experiments demonstrate that SANTA outperforms existing methods in alleviating object and action hallucinations, yielding superior performance on the hallucination examination benchmarks.

