---
layout: default
title: Benchmarking the Generality of Vision-Language-Action Models
---

# Benchmarking the Generality of Vision-Language-Action Models

**arXiv**: [2512.11315v1](https://arxiv.org/abs/2512.11315) | [PDF](https://arxiv.org/pdf/2512.11315.pdf)

**作者**: Pranav Guruprasad, Sudipta Chowdhury, Harsh Sikka, Mridul Sharma, Helen Lu, Sean Rivera, Aryan Khurana, Hangliang Ren, Yangyue Wang

---

## 💡 一句话要点

**提出MultiNet v1.0基准以评估视觉语言模型在跨领域通用性中的表现。**

**关键词**: `视觉语言模型评估` `跨领域通用性` `基准测试` `模态对齐` `机器人控制` `多模态智能`

## 📋 核心要点

1. 核心问题：当前评估方法碎片化，难以衡量基础模型在训练分布外的通用性。
2. 方法要点：引入统一基准MultiNet v1.0，覆盖六种能力领域以标准化评估。
3. 实验或效果：评估GPT-5等模型发现通用性不足，存在模态错位和知识退化问题。

## 📄 摘要（原文）

> Generalist multimodal agents are expected to unify perception, language, and control - operating robustly across diverse real world domains. However, current evaluation practices remain fragmented across isolated benchmarks, making it difficult to assess whether today's foundation models truly generalize beyond their training distributions. We introduce MultiNet v1.0, a unified benchmark for measuring the cross domain generality of vision language models (VLMs) and vision language action models (VLAs) across six foundational capability regimes. Visual grounding, spatial reasoning, tool use, physical commonsense, multi agent coordination, and continuous robot control. Evaluating GPT 5, Pi0, and Magma, we find that no model demonstrates consistent generality. All exhibit substantial degradation on unseen domains, unfamiliar modalities, or cross domain task shifts despite strong performance within their training distributions.These failures manifest as modality misalignment, output format instability, and catastrophic knowledge degradation under domain transfer.Our findings reveal a persistent gap between the aspiration of generalist intelligence and the actual capabilities of current foundation models.MultiNet v1.0 provides a standardized evaluation substrate for diagnosing these gaps and guiding the development of future generalist agents.Code, data, and leaderboards are publicly available.

