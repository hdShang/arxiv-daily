---
layout: default
title: Harmonious Parameter Adaptation in Continual Visual Instruction Tuning for Safety-Aligned MLLMs
---

# Harmonious Parameter Adaptation in Continual Visual Instruction Tuning for Safety-Aligned MLLMs

**arXiv**: [2511.20158v1](https://arxiv.org/abs/2511.20158) | [PDF](https://arxiv.org/pdf/2511.20158.pdf)

**作者**: Ziqi Wang, Chang Che, Qi Wang, Hui Ma, Zenglin Shi, Cees G. M. Snoek, Meng Wang

---

## 💡 一句话要点

**提出和谐参数适应以解决安全对齐多模态大模型在持续视觉指令调优中的安全与任务平衡问题**

**关键词**: `持续视觉指令调优` `安全对齐多模态大模型` `参数适应` `灾难性遗忘` `正交约束` `安全评估`

## 📋 核心要点

1. 核心问题：持续视觉指令调优中，安全对齐多模态大模型出现任务遗忘和安全性能退化。
2. 方法要点：基于聚焦的参数划分、和谐平衡参数选择和正交参数调整，以缓解灾难性遗忘。
3. 实验或效果：在CVIT基准和安全评估数据集上，HPA优于基线，保持高安全性和减轻遗忘。

## 📄 摘要（原文）

> While continual visual instruction tuning (CVIT) has shown promise in adapting multimodal large language models (MLLMs), existing studies predominantly focus on models without safety alignment. This critical oversight ignores the fact that real-world MLLMs inherently require such mechanisms to mitigate potential risks. In this work, we shift our focus to CVIT for safety-aligned MLLMs and observe that during continual adaptation, the model not only suffers from task forgetting but also exhibits degradation in its safety. Achieving a harmonious balance between safety and task performance remains a crucial challenge. To address this, we propose Harmonious Parameter Adaptation (HPA), a post-training framework composed of focusing-based parameter partition, harmoniously balanced parameter selection, and orthogonal parameter adjustment. Specifically, HPA partitions parameters into two types based on their focus on safety or task performance, and selects the focused ones to preserve from a balanced perspective. In addition, HPA imposes orthogonality constraints on parameter updates to further alleviate catastrophic forgetting. Extensive experiments on the CVIT benchmark and safety evaluation datasets demonstrate that HPA better maintains high safety and mitigates forgetting than existing baselines.

