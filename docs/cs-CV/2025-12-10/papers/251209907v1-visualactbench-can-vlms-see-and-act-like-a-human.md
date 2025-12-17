---
layout: default
title: VisualActBench: Can VLMs See and Act like a Human?
---

# VisualActBench: Can VLMs See and Act like a Human?

**arXiv**: [2512.09907v1](https://arxiv.org/abs/2512.09907) | [PDF](https://arxiv.org/pdf/2512.09907.pdf)

**作者**: Daoan Zhang, Pai Liu, Xiaofei Zhou, Yuan Ge, Guangchen Lan, Jing Bi, Christopher Brinton, Ehsan Hoque, Jiebo Luo

---

## 💡 一句话要点

**提出VisualActBench基准以评估视觉语言模型在无文本提示下的主动视觉动作推理能力**

**关键词**: `视觉动作推理` `视觉语言模型评估` `主动视觉理解` `人类对齐基准` `视频动作标注`

## 📋 核心要点

1. 核心问题：视觉语言模型在仅凭视觉输入进行主动推理和行动的能力尚未充分探索
2. 方法要点：引入视觉动作推理任务，构建包含1074个视频和3733个人工标注动作的大规模基准
3. 实验或效果：评估29个模型，发现前沿模型表现相对较强，但与人类推理水平仍有显著差距

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have achieved impressive progress in perceiving and describing visual environments. However, their ability to proactively reason and act based solely on visual inputs, without explicit textual prompts, remains underexplored. We introduce a new task, Visual Action Reasoning, and propose VisualActBench, a large-scale benchmark comprising 1,074 videos and 3,733 human-annotated actions across four real-world scenarios. Each action is labeled with an Action Prioritization Level (APL) and a proactive-reactive type to assess models' human-aligned reasoning and value sensitivity. We evaluate 29 VLMs on VisualActBench and find that while frontier models like GPT4o demonstrate relatively strong performance, a significant gap remains compared to human-level reasoning, particularly in generating proactive, high-priority actions. Our results highlight limitations in current VLMs' ability to interpret complex context, anticipate outcomes, and align with human decision-making frameworks. VisualActBench establishes a comprehensive foundation for assessing and improving the real-world readiness of proactive, vision-centric AI agents.

