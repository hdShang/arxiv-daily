---
layout: default
title: Intervene-All-Paths: Unified Mitigation of LVLM Hallucinations across Alignment Formats
---

# Intervene-All-Paths: Unified Mitigation of LVLM Hallucinations across Alignment Formats

**arXiv**: [2511.17254v1](https://arxiv.org/abs/2511.17254) | [PDF](https://arxiv.org/pdf/2511.17254.pdf)

**作者**: Jiaye Qian, Ge Zheng, Yuchen Zhu, Sibei Yang

---

## 💡 一句话要点

**提出统一干预框架以缓解多模态大模型在不同对齐格式下的幻觉问题**

**关键词**: `多模态大模型` `幻觉缓解` `因果路径干预` `对齐格式适应` `Transformer架构`

## 📋 核心要点

1. 核心问题：多模态大模型在图像-文本任务中易产生幻觉，源于多个因果路径的交互作用
2. 方法要点：基于Transformer因果架构，识别并干预关键幻觉头，适应判别式和生成式对齐格式
3. 实验或效果：在多个基准测试中，该方法一致减少不同对齐类型的幻觉

## 📄 摘要（原文）

> Despite their impressive performance across a wide range of tasks, Large Vision-Language Models (LVLMs) remain prone to hallucination. In this study, we propose a comprehensive intervention framework aligned with the transformer's causal architecture in LVLMs, integrating the effects of different intervention paths on hallucination. We find that hallucinations in LVLMs do not arise from a single causal path, but rather from the interplay among image-to-input-text, image-to-output-text, and text-to-text pathways. For the first time, we also find that LVLMs rely on different pathways depending on the question-answer alignment format. Building on these insights, we propose simple yet effective methods to identify and intervene on critical hallucination heads within each pathway, tailored to discriminative and generative formats. Experiments across multiple benchmarks demonstrate that our approach consistently reduces hallucinations across diverse alignment types.

