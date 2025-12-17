---
layout: default
title: VOPE: Revisiting Hallucination of Vision-Language Models in Voluntary Imagination Task
---

# VOPE: Revisiting Hallucination of Vision-Language Models in Voluntary Imagination Task

**arXiv**: [2511.13420v1](https://arxiv.org/abs/2511.13420) | [PDF](https://arxiv.org/pdf/2511.13420.pdf)

**作者**: Xingming Long, Jie Zhang, Shiguang Shan, Xilin Chen

---

## 💡 一句话要点

**提出VOPE方法以评估大视觉语言模型在自愿想象任务中的幻觉问题**

**关键词**: `大视觉语言模型` `幻觉评估` `自愿想象任务` `存在评估` `重检查问题`

## 📋 核心要点

1. 核心问题：现有研究忽视大视觉语言模型在自愿想象任务中的幻觉，如故事写作
2. 方法要点：VOPE通过重检查问题评估模型对想象对象存在的解释一致性
3. 实验或效果：多数模型在自愿想象中幻觉严重，现有缓解方法效果有限

## 📄 摘要（原文）

> Most research on hallucinations in Large Vision-Language Models (LVLMs) focuses on factual description tasks that prohibit any output absent from the image. However, little attention has been paid to hallucinations in voluntary imagination tasks, e.g., story writing, where the models are expected to generate novel content beyond the given image. In these tasks, it is inappropriate to simply regard such imagined novel content as hallucinations. To address this limitation, we introduce Voluntary-imagined Object Presence Evaluation (VOPE)-a novel method to assess LVLMs' hallucinations in voluntary imagination tasks via presence evaluation. Specifically, VOPE poses recheck-based questions to evaluate how an LVLM interprets the presence of the imagined objects in its own response. The consistency between the model's interpretation and the object's presence in the image is then used to determine whether the model hallucinates when generating the response. We apply VOPE to several mainstream LVLMs and hallucination mitigation methods, revealing two key findings: (1) most LVLMs hallucinate heavily during voluntary imagination, and their performance in presence evaluation is notably poor on imagined objects; (2) existing hallucination mitigation methods show limited effect in voluntary imagination tasks, making this an important direction for future research.

