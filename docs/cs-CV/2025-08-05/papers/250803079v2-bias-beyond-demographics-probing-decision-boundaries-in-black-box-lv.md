---
layout: default
title: "Bias Beyond Demographics: Probing Decision Boundaries in Black-Box LVLMs via Counterfactual VQA"
---

# Bias Beyond Demographics: Probing Decision Boundaries in Black-Box LVLMs via Counterfactual VQA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03079" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03079v2</a>
  <a href="https://arxiv.org/pdf/2508.03079.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03079v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03079v2', 'Bias Beyond Demographics: Probing Decision Boundaries in Black-Box LVLMs via Counterfactual VQA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zaiying Zhao, Toshihiko Yamasaki

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-12-02)

---

## 💡 一句话要点

**提出反事实视觉问答基准以审计黑箱LVLM的决策偏差**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `公平性评估` `视觉语言模型` `反事实推理` `多模态学习` `模型透明性`

## 📋 核心要点

1. 现有方法主要关注人口统计属性，未能全面评估LVLM的公平性，导致对决策偏差的理解不足。
2. 本文提出反事实视觉问答基准，通过控制上下文变化来探测LVLM的决策边界，提供了新的评估视角。
3. 实验结果显示，非人口统计属性对LVLM决策影响更大，且少量人类验证示例能有效改善模型响应的一致性。

## 📝 摘要（中文）

近年来，随着大型视觉语言模型（LVLM）的发展，公平性问题日益受到关注。然而，现有评估主要集中于人口统计属性，常常将公平性与拒绝行为混淆。本文通过引入反事实视觉问答基准，拓宽了公平性的评估范围，能够在控制的上下文变化下探测闭源LVLM的决策边界。每对图像在一个视觉属性上有所不同，该属性被验证为与问题无关，从而实现了无地面真相和拒绝意识的推理稳定性分析。实验结果表明，非人口统计属性（如环境上下文或社会行为）对LVLM决策的扭曲程度大于人口统计属性。此外，基于指令的去偏见方法效果有限，甚至可能加剧这些不对称性，而接触少量经过人类规范验证的示例则能促进更一致和均衡的响应，突显了该基准作为评估框架和理解改进模型行为的潜力。综合这些结果，为审计黑箱LVLM中的上下文偏见提供了实用基础，推动了多模态推理的透明性和公平性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有公平性评估方法局限于人口统计属性的问题，缺乏对非人口统计属性对LVLM决策影响的深入分析。

**核心思路**：通过引入反事实视觉问答基准，论文设计了一种能够在控制上下文变化的情况下探测LVLM决策边界的方法，从而实现对模型推理稳定性的评估。

**技术框架**：整体架构包括数据集构建、反事实图像对生成、模型评估和结果分析四个主要模块。数据集通过验证无关属性的图像对来构建，模型评估则基于这些图像对进行。

**关键创新**：最重要的创新在于引入了反事实视觉问答基准，能够在无地面真相的情况下分析模型的推理稳定性，这与现有方法的单一人口统计属性评估形成鲜明对比。

**关键设计**：在实验中，采用了特定的图像对生成策略，确保每对图像在一个视觉属性上有所不同，同时设计了适应性评估指标，以量化模型在不同上下文下的表现。实验还探讨了指令基于去偏见方法的效果及其局限性。

## 📊 实验亮点

实验结果表明，非人口统计属性对LVLM决策的扭曲程度显著高于人口统计属性，且在少量人类验证示例的影响下，模型响应的一致性和均衡性得到了显著改善。这一发现为模型公平性提供了新的视角，强调了反事实基准的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括公平性审计、模型透明性提升以及多模态推理的优化。通过提供新的评估框架，研究成果可帮助开发更公正的AI系统，减少模型在实际应用中的偏见，推动AI技术的社会责任感。未来，该方法也可扩展到其他类型的模型和任务中，进一步提升AI的公平性与可靠性。

## 📄 摘要（原文）

> Recent advances in large vision-language models (LVLMs) have amplified concerns about fairness, yet existing evaluations remain confined to demographic attributes and often conflate fairness with refusal behavior. This paper broadens the scope of fairness by introducing a counterfactual VQA benchmark that probes the decision boundaries of closed-source LVLMs under controlled context shifts. Each image pair differs in a single visual attribute that has been validated as irrelevant to the question, enabling ground-truth-free and refusal-aware analysis of reasoning stability. Comprehensive experiments reveal that non-demographic attributes, such as environmental context or social behavior, distort LVLM decision-making more strongly than demographic ones. Moreover, instruction-based debiasing shows limited effectiveness and can even amplify these asymmetries, whereas exposure to a small number of human norm validated examples from our benchmark encourages more consistent and balanced responses, highlighting its potential not only as an evaluative framework but also as a means for understanding and improving model behavior. Together, these results provide a practial basis for auditing contextual biases even in black-box LVLMs and contribute to more transparent and equitable multimodal reasoning.

