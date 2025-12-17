---
layout: default
title: RULER-Bench: Probing Rule-based Reasoning Abilities of Next-level Video Generation Models for Vision Foundation Intelligence
---

# RULER-Bench: Probing Rule-based Reasoning Abilities of Next-level Video Generation Models for Vision Foundation Intelligence

**arXiv**: [2512.02622v1](https://arxiv.org/abs/2512.02622) | [PDF](https://arxiv.org/pdf/2512.02622.pdf)

**作者**: Xuming He, Zehao Fan, Hengjia Li, Fan Zhuo, Hankun Xu, Senlin Cheng, Di Weng, Haifeng Liu, Can Ye, Boxi Wu

---

## 💡 一句话要点

**提出RULER-Bench基准以评估视频生成模型的规则推理能力，推动视觉基础智能发展。**

**关键词**: `视频生成基准` `规则推理评估` `视觉基础模型` `认知规则` `GPT-o3评分`

## 📋 核心要点

1. 现有基准主要关注视觉感知，视频生成模型的规则推理能力评估不足。
2. RULER-Bench基于文本到视频和图像到视频范式，覆盖6类规则40个任务。
3. 实验显示当前最佳模型规则一致性得分仅48.87%，推理能力有显著提升空间。

## 📄 摘要（原文）

> Recent advances in video generation have enabled the synthesis of videos with strong temporal consistency and impressive visual quality, marking a crucial step toward vision foundation models. To evaluate these video generation models, existing benchmarks primarily focus on factors related to visual perception and understanding, like visual aesthetics, instruction adherence, and temporal coherence. However, the rule-based reasoning capabilities of video generation models remain largely unexplored. Although recent studies have carried out preliminary explorations into whether video models can serve as zero-shot learners, they still lack a fine-grained decomposition of reasoning capabilities and a comprehensive evaluation protocol. To address this gap, we introduce RULER-Bench, a benchmark designed to evaluate the reasoning ability of video generation models from the perspective of cognitive rules. Built upon two fundamental paradigms: text-to-video and image-to-video, RULER-Bench covers 40 representative tasks spanning six rule categories with 622 high-quality annotated instances. For the evaluation of each generated video, we construct a checklist covering four metrics and leverage GPT-o3 to assign scores to each question, achieving 85% alignment with human judgements. Extensive experiments show that the state-of-the-art model achieves only 48.87% on the rule coherence metric, highlighting significant room for improvement in the reasoning capability of next-level video models. We expect that the insight obtained from RULER-Bench will facilitate further development of reasoning-aware video generation, advancing video generation models toward vision foundation intelligence.

