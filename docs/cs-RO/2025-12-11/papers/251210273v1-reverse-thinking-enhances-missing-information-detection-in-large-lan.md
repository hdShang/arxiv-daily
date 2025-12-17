---
layout: default
title: Reverse Thinking Enhances Missing Information Detection in Large Language Models
---

# Reverse Thinking Enhances Missing Information Detection in Large Language Models

**arXiv**: [2512.10273v1](https://arxiv.org/abs/2512.10273) | [PDF](https://arxiv.org/pdf/2512.10273.pdf)

**作者**: Yuxin Liu, Chaojie Gu, Yihang Zhang, Bin Qian, Shibo He

---

## 💡 一句话要点

**提出反向思维框架以增强大语言模型在缺失信息检测任务中的性能**

**关键词**: `大语言模型` `缺失信息检测` `反向推理` `逻辑完整性` `推理鲁棒性`

## 📋 核心要点

1. 核心问题：大语言模型在缺失信息任务中常出现响应不完整、事实错误和幻觉问题
2. 方法要点：基于反向推理，引导模型通过反向思维识别必要条件和缺失元素
3. 实验或效果：相比传统前向推理方法，显著提升模型准确率，增强逻辑完整性和推理鲁棒性

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities in various reasoning tasks, yet they often struggle with problems involving missing information, exhibiting issues such as incomplete responses, factual errors, and hallucinations. While forward reasoning approaches like Chain-of-Thought (CoT) and Tree-of-Thought (ToT) have shown success in structured problem-solving, they frequently fail to systematically identify and recover omitted information. In this paper, we explore the potential of reverse thinking methodologies to enhance LLMs' performance on missing information detection tasks. Drawing inspiration from recent work on backward reasoning, we propose a novel framework that guides LLMs through reverse thinking to identify necessary conditions and pinpoint missing elements. Our approach transforms the challenging task of missing information identification into a more manageable backward reasoning problem, significantly improving model accuracy. Experimental results demonstrate that our reverse thinking approach achieves substantial performance gains compared to traditional forward reasoning methods, providing a promising direction for enhancing LLMs' logical completeness and reasoning robustness.

