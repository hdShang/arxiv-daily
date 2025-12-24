---
layout: default
title: "Interpretable Multimodal Framework for Human-Centered Street Assessment: Integrating Visual-Language Models for Perceptual Urban Diagnostics"
---

# Interpretable Multimodal Framework for Human-Centered Street Assessment: Integrating Visual-Language Models for Perceptual Urban Diagnostics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05087" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05087v1</a>
  <a href="https://arxiv.org/pdf/2506.05087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05087v1', 'Interpretable Multimodal Framework for Human-Centered Street Assessment: Integrating Visual-Language Models for Perceptual Urban Diagnostics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: HaoTian Lan

**分类**: cs.CV, cs.CL

**发布日期**: 2025-06-05

**备注**: 24 pages, 10 figures

---

## 💡 一句话要点

**提出多模态街道评估框架解决城市设计主观感知不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态评估` `城市设计` `主观感知` `视觉变换器` `语言模型` `可解释性` `社会经济分析`

## 📋 核心要点

1. 现有的城市分析方法主要依赖于客观指标，无法充分反映居民的主观感知，导致城市设计缺乏包容性。
2. 本研究提出的多模态街道评估框架（MSEF）结合视觉变换器和大型语言模型，实现了对街景的可解释双输出评估。
3. 实验结果显示，模型在客观特征上F1分数达到0.84，与居民感知的聚合结果一致性为89.3%，验证了其有效性。

## 📝 摘要（中文）

尽管基于图像或地理信息系统的客观街道指标在城市分析中已成为标准，但仍不足以捕捉包容性城市设计所需的主观感知。本研究提出了一种新颖的多模态街道评估框架（MSEF），将视觉变换器（VisualGLM-6B）与大型语言模型（GPT-4）融合，实现了街景的可解释双输出评估。通过对来自中国哈尔滨的15,000多张标注街景图像进行微调，模型在客观特征上达到了0.84的F1分数，并与居民感知的聚合结果达成了89.3%的一致性，验证了不同社会经济地理的适用性。MSEF不仅关注分类准确性，还捕捉了上下文依赖的矛盾现象，揭示了普遍空间启发式的局限性。该框架通过基于注意力机制生成自然语言推理，将感官数据与社会情感推理相结合，为与可持续发展目标11对齐的透明诊断提供了可能。此研究在城市感知建模方法论上具有创新性，并为寻求将基础设施精确性与生活体验相结合的规划系统提供了实用价值。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有城市分析方法无法捕捉主观感知的问题，导致城市设计缺乏包容性。现有方法通常依赖于客观指标，忽视了居民的真实体验和感受。

**核心思路**：提出的多模态街道评估框架（MSEF）通过结合视觉变换器（VisualGLM-6B）和大型语言模型（GPT-4），实现了对街景的可解释双输出评估，能够同时考虑客观特征和主观感知。

**技术框架**：MSEF的整体架构包括数据收集、模型训练和评估三个主要阶段。首先，收集来自哈尔滨的15,000多张标注街景图像；然后，使用LoRA和P-Tuning v2对模型进行微调；最后，通过生成自然语言推理实现可解释性。

**关键创新**：MSEF的主要创新在于其能够捕捉上下文依赖的矛盾现象，并识别非线性和语义相关的模式，揭示了普遍空间启发式的局限性。这种方法在城市感知建模中具有重要的理论和实践意义。

**关键设计**：在模型训练中，采用了LoRA和P-Tuning v2进行参数高效适配，确保了模型在保持高性能的同时，能够有效处理大规模数据。模型在客观特征上的F1分数为0.84，且与居民感知的聚合结果一致性达到89.3%。

## 📊 实验亮点

实验结果显示，MSEF在客观特征上的F1分数达到0.84，与居民感知的聚合结果一致性为89.3%。此外，框架能够捕捉到上下文依赖的矛盾现象，揭示了建筑透明度在不同区域的感知差异，展示了其在城市感知建模中的创新性和实用性。

## 🎯 应用场景

该研究的多模态街道评估框架（MSEF）具有广泛的应用潜力，特别是在城市规划、交通管理和公共政策制定等领域。通过将客观数据与居民的主观感知相结合，MSEF能够为城市设计提供更全面的视角，促进更具包容性的城市环境的创建。未来，该框架还可能为智能城市建设和可持续发展目标的实现提供支持。

## 📄 摘要（原文）

> While objective street metrics derived from imagery or GIS have become standard in urban analytics, they remain insufficient to capture subjective perceptions essential to inclusive urban design. This study introduces a novel Multimodal Street Evaluation Framework (MSEF) that fuses a vision transformer (VisualGLM-6B) with a large language model (GPT-4), enabling interpretable dual-output assessment of streetscapes. Leveraging over 15,000 annotated street-view images from Harbin, China, we fine-tune the framework using LoRA and P-Tuning v2 for parameter-efficient adaptation. The model achieves an F1 score of 0.84 on objective features and 89.3 percent agreement with aggregated resident perceptions, validated across stratified socioeconomic geographies. Beyond classification accuracy, MSEF captures context-dependent contradictions: for instance, informal commerce boosts perceived vibrancy while simultaneously reducing pedestrian comfort. It also identifies nonlinear and semantically contingent patterns -- such as the divergent perceptual effects of architectural transparency across residential and commercial zones -- revealing the limits of universal spatial heuristics. By generating natural-language rationales grounded in attention mechanisms, the framework bridges sensory data with socio-affective inference, enabling transparent diagnostics aligned with SDG 11. This work offers both methodological innovation in urban perception modeling and practical utility for planning systems seeking to reconcile infrastructural precision with lived experience.

