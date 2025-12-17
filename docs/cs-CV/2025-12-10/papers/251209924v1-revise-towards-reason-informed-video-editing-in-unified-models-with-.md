---
layout: default
title: ReViSE: Towards Reason-Informed Video Editing in Unified Models with Self-Reflective Learning
---

# ReViSE: Towards Reason-Informed Video Editing in Unified Models with Self-Reflective Learning

**arXiv**: [2512.09924v1](https://arxiv.org/abs/2512.09924) | [PDF](https://arxiv.org/pdf/2512.09924.pdf)

**作者**: Xinyu Liu, Hangjie Yuan, Yujie Wei, Jiazheng Xing, Yujin Han, Jiahao Pan, Yanbiao Ma, Chi-Min Chan, Kang Zhao, Shiwei Zhang, Wenhan Luo, Yike Guo

---

## 💡 一句话要点

**提出ReViSE框架以解决统一模型中推理感知视频编辑的难题**

**关键词**: `推理感知视频编辑` `自反式学习` `统一模型` `视频生成基准` `视觉语言模型`

## 📋 核心要点

1. 核心问题：现有统一模型在推理感知视频编辑中存在能力脱节，缺乏合适数据集
2. 方法要点：引入RVE任务和RVE-Bench基准，提出自反式推理框架统一生成与评估
3. 实验或效果：在RVE-Bench上显著提升编辑准确性和视觉保真度，总体得分提高32%

## 📄 摘要（原文）

> Video unified models exhibit strong capabilities in understanding and generation, yet they struggle with reason-informed visual editing even when equipped with powerful internal vision-language models (VLMs). We attribute this gap to two factors: 1) existing datasets are inadequate for training and evaluating reasoning-aware video editing, and 2) an inherent disconnect between the models' reasoning and editing capabilities, which prevents the rich understanding from effectively instructing the editing process. Bridging this gap requires an integrated framework that connects reasoning with visual transformation. To address this gap, we introduce the Reason-Informed Video Editing (RVE) task, which requires reasoning about physical plausibility and causal dynamics during editing. To support systematic evaluation, we construct RVE-Bench, a comprehensive benchmark with two complementary subsets: Reasoning-Informed Video Editing and In-Context Video Generation. These subsets cover diverse reasoning dimensions and real-world editing scenarios. Building upon this foundation, we propose the ReViSE, a Self-Reflective Reasoning (SRF) framework that unifies generation and evaluation within a single architecture. The model's internal VLM provides intrinsic feedback by assessing whether the edited video logically satisfies the given instruction. The differential feedback that refines the generator's reasoning behavior during training. Extensive experiments on RVE-Bench demonstrate that ReViSE significantly enhances editing accuracy and visual fidelity, achieving a 32% improvement of the Overall score in the reasoning-informed video editing subset over state-of-the-art methods.

