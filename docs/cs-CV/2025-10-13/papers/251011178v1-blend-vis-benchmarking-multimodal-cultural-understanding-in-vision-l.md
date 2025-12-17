---
layout: default
title: BLEnD-Vis: Benchmarking Multimodal Cultural Understanding in Vision Language Models
---

# BLEnD-Vis: Benchmarking Multimodal Cultural Understanding in Vision Language Models

**arXiv**: [2510.11178v1](https://arxiv.org/abs/2510.11178) | [PDF](https://arxiv.org/pdf/2510.11178.pdf)

**作者**: Bryan Chen Zhengyu Tan, Zheng Weihua, Zhengyuan Liu, Nancy F. Chen, Hwaran Lee, Kenny Tsu Wei Choo, Roy Ka-Wei Lee

---

## 💡 一句话要点

**提出BLEnD-Vis基准以评估视觉语言模型的多模态文化理解鲁棒性**

**关键词**: `视觉语言模型` `文化理解基准` `多模态评估` `鲁棒性分析` `跨模态一致性`

## 📋 核心要点

1. 现有评估忽视视觉语言模型的文化理解鲁棒性和可迁移性
2. 构建多模态多文化基准，涵盖文本重述和视觉模态的313个问题模板
3. 实验显示模型在语言重述下性能下降，视觉线索帮助但跨模态一致性低

## 📄 摘要（原文）

> As vision-language models (VLMs) are deployed globally, their ability to
> understand culturally situated knowledge becomes essential. Yet, existing
> evaluations largely assess static recall or isolated visual grounding, leaving
> unanswered whether VLMs possess robust and transferable cultural understanding.
> We introduce BLEnD-Vis, a multimodal, multicultural benchmark designed to
> evaluate the robustness of everyday cultural knowledge in VLMs across
> linguistic rephrasings and visual modalities. Building on the BLEnD dataset,
> BLEnD-Vis constructs 313 culturally grounded question templates spanning 16
> regions and generates three aligned multiple-choice formats: (i) a text-only
> baseline querying from Region $\to$ Entity, (ii) an inverted text-only variant
> (Entity $\to$ Region), and (iii) a VQA-style version of (ii) with generated
> images. The resulting benchmark comprises 4,916 images and over 21,000
> multiple-choice question (MCQ) instances, validated through human annotation.
> BLEnD-Vis reveals significant fragility in current VLM cultural knowledge;
> models exhibit performance drops under linguistic rephrasing and, whilst visual
> cues often aid performance, low cross-modal consistency highlights challenges
> in robustly integrating textual and visual understanding, particularly for
> lower-resource regions. BLEnD-Vis thus provides a crucial testbed for
> systematically analysing cultural robustness and multimodal grounding, exposing
> limitations and guiding the development of more culturally competent VLMs.

