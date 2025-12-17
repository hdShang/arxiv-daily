---
layout: default
title: Evaluating Gemini LLM in Food Image-Based Recipe and Nutrition Description with EfficientNet-B4 Visual Backbone
---

# Evaluating Gemini LLM in Food Image-Based Recipe and Nutrition Description with EfficientNet-B4 Visual Backbone

**arXiv**: [2511.08215v1](https://arxiv.org/abs/2511.08215) | [PDF](https://arxiv.org/pdf/2511.08215.pdf)

**作者**: Rizal Khoirul Anam

---

## 💡 一句话要点

**评估基于EfficientNet-B4和Gemini LLM的多模态系统在食物图像识别与生成中的性能平衡**

**关键词**: `食物图像识别` `多模态系统` `语义错误传播` `EfficientNet-B4` `Gemini LLM` `营养分析`

## 📋 核心要点

1. 核心问题：自动化食物营养分析和食谱生成中视觉分类精度与生成质量的权衡。
2. 方法要点：结合EfficientNet-B4视觉骨干和Gemini LLM，分析语义错误传播。
3. 实验或效果：在自定义数据集上，EfficientNet-B4准确率89.0%，Gemini事实准确率9.2/10。

## 📄 摘要（原文）

> The proliferation of digital food applications necessitates robust methods for automated nutritional analysis and culinary guidance. This paper presents a comprehensive comparative evaluation of a decoupled, multimodal pipeline for food recognition. We evaluate a system integrating a specialized visual backbone (EfficientNet-B4) with a powerful generative large language model (Google's Gemini LLM). The core objective is to evaluate the trade-offs between visual classification accuracy, model efficiency, and the quality of generative output (nutritional data and recipes). We benchmark this pipeline against alternative vision backbones (VGG-16, ResNet-50, YOLOv8) and a lightweight LLM (Gemma). We introduce a formalization for "Semantic Error Propagation" (SEP) to analyze how classification inaccuracies from the visual module cascade into the generative output. Our analysis is grounded in a new Custom Chinese Food Dataset (CCFD) developed to address cultural bias in public datasets. Experimental results demonstrate that while EfficientNet-B4 (89.0\% Top-1 Acc.) provides the best balance of accuracy and efficiency, and Gemini (9.2/10 Factual Accuracy) provides superior generative quality, the system's overall utility is fundamentally bottlenecked by the visual front-end's perceptive accuracy. We conduct a detailed per-class analysis, identifying high semantic similarity as the most critical failure mode.

