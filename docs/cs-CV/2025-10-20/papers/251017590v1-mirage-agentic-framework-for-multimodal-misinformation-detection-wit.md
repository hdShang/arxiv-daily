---
layout: default
title: MIRAGE: Agentic Framework for Multimodal Misinformation Detection with Web-Grounded Reasoning
---

# MIRAGE: Agentic Framework for Multimodal Misinformation Detection with Web-Grounded Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17590" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17590v1</a>
  <a href="https://arxiv.org/pdf/2510.17590.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17590v1" onclick="toggleFavorite(this, '2510.17590v1', 'MIRAGE: Agentic Framework for Multimodal Misinformation Detection with Web-Grounded Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mir Nafis Sharear Shopnil, Sharad Duwal, Abhishek Tyagi, Adiba Mahbub Proma

**分类**: cs.AI, cs.CL, cs.CV, cs.CY, cs.LG

**发布日期**: 2025-10-20

**备注**: 16 pages, 3 tables, 1 figure

---

## 💡 一句话要点

**MIRAGE：利用Web检索推理的多模态信息检测Agent框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态信息检测` `Agent框架` `Web检索` `视觉真实性评估` `跨模态一致性` `事实核查` `零样本学习`

## 📋 核心要点

1. 现有监督模型依赖特定领域数据，难以泛化到各种信息操纵手段，限制了多模态信息检测的有效性。
2. MIRAGE框架通过分解多模态验证流程，结合视觉真实性评估、跨模态一致性分析和检索增强的事实核查，实现更准确的判断。
3. 实验表明，MIRAGE在MMFakeBench数据集上显著优于现有零样本基线，并在测试集上保持了良好的泛化能力。

## 📝 摘要（中文）

针对网络平台海量多模态（文本和图像）信息传播，人工核查能力不足的问题，论文提出了MIRAGE，一个推理时可插拔的Agent框架。该框架将多模态验证分解为四个顺序模块：视觉真实性评估（检测AI生成图像）、跨模态一致性分析（识别不相关的图像挪用）、检索增强的事实核查（通过迭代问题生成从Web证据中验证声明）以及校准判断模块（整合所有信号）。MIRAGE协调视觉-语言模型推理和有针对性的Web检索，输出结构化且带有引用的理由。在MMFakeBench验证集上，MIRAGE结合GPT-4o-mini实现了81.65%的F1值和75.1%的准确率，优于最强的零样本基线（GPT-4V with MMD-Agent，F1值为74.0%）。测试集结果也验证了其泛化能力，F1值为81.44%，准确率为75.08%。消融实验表明，视觉验证贡献了5.18的F1值，检索增强推理贡献了2.97的F1值。结果表明，分解的Agent推理与Web检索可以匹配监督检测器的性能，而无需特定领域的训练数据，从而能够在缺乏标记数据的模态中进行信息检测。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态信息检测问题，即判断包含文本和图像的网络帖子是否包含虚假信息。现有监督模型需要大量特定领域标注数据进行训练，难以泛化到新的信息操纵手段和领域。零样本方法虽然不需要训练数据，但性能往往不如监督模型，且缺乏可解释性。

**核心思路**：论文的核心思路是将多模态信息检测任务分解为多个可解释的子任务，并利用Agent框架协调各个子任务的执行。通过结合视觉真实性评估、跨模态一致性分析和检索增强的事实核查，可以更全面地评估信息的真实性，并提供可解释的推理过程。

**技术框架**：MIRAGE框架包含四个主要模块：1) 视觉真实性评估：检测图像是否为AI生成；2) 跨模态一致性分析：判断文本和图像是否相关，是否存在挪用情况；3) 检索增强的事实核查：通过迭代问题生成，从Web检索相关证据，验证文本声明的真实性；4) 校准判断模块：整合前三个模块的输出，给出最终的判断结果。整个流程由一个Agent协调，负责任务分解、模块调用和结果整合。

**关键创新**：MIRAGE的关键创新在于将多模态信息检测任务分解为多个可解释的子任务，并利用Agent框架协调这些子任务的执行。这种分解的方式使得模型更易于理解和调试，同时也提高了模型的泛化能力。此外，MIRAGE还引入了检索增强的事实核查模块，利用Web检索来获取外部知识，从而提高了事实核查的准确性。

**关键设计**：视觉真实性评估模块使用了现有的AI生成图像检测模型。跨模态一致性分析模块使用了CLIP等视觉-语言模型来计算文本和图像之间的相似度。检索增强的事实核查模块使用了迭代问题生成技术，即根据文本声明生成多个问题，然后利用这些问题从Web检索相关证据。校准判断模块使用了一个简单的线性模型来整合各个模块的输出。

## 📊 实验亮点

MIRAGE在MMFakeBench验证集上实现了81.65%的F1值和75.1%的准确率，显著优于最强的零样本基线GPT-4V with MMD-Agent (F1值为74.0%)。消融实验表明，视觉验证和检索增强推理分别贡献了5.18和2.97的F1值，证明了各个模块的有效性。测试集结果也验证了MIRAGE的泛化能力，F1值为81.44%，准确率为75.08%。

## 🎯 应用场景

MIRAGE框架可应用于社交媒体平台、新闻网站等场景，自动检测和标记虚假信息，帮助用户识别和避免受到误导。该研究有助于提高网络信息的可信度，减少虚假信息传播带来的负面影响，并为未来的多模态信息检测研究提供新的思路。

## 📄 摘要（原文）

> Misinformation spreads across web platforms through billions of daily multimodal posts that combine text and images, overwhelming manual fact-checking capacity. Supervised detection models require domain-specific training data and fail to generalize across diverse manipulation tactics. We present MIRAGE, an inference-time, model-pluggable agentic framework that decomposes multimodal verification into four sequential modules: visual veracity assessment detects AI-generated images, cross-modal consistency analysis identifies out-of-context repurposing, retrieval-augmented factual checking grounds claims in web evidence through iterative question generation, and a calibrated judgment module integrates all signals. MIRAGE orchestrates vision-language model reasoning with targeted web retrieval, outputs structured and citation-linked rationales. On MMFakeBench validation set (1,000 samples), MIRAGE with GPT-4o-mini achieves 81.65% F1 and 75.1% accuracy, outperforming the strongest zero-shot baseline (GPT-4V with MMD-Agent at 74.0% F1) by 7.65 points while maintaining 34.3% false positive rate versus 97.3% for a judge-only baseline. Test set results (5,000 samples) confirm generalization with 81.44% F1 and 75.08% accuracy. Ablation studies show visual verification contributes 5.18 F1 points and retrieval-augmented reasoning contributes 2.97 points. Our results demonstrate that decomposed agentic reasoning with web retrieval can match supervised detector performance without domain-specific training, enabling misinformation detection across modalities where labeled data remains scarce.

