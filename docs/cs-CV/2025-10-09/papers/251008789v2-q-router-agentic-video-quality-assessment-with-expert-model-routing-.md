---
layout: default
title: Q-Router: Agentic Video Quality Assessment with Expert Model Routing and Artifact Localization
---

# Q-Router: Agentic Video Quality Assessment with Expert Model Routing and Artifact Localization

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08789" target="_blank" class="toolbar-btn">arXiv: 2510.08789v2</a>
    <a href="https://arxiv.org/pdf/2510.08789.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08789v2" 
            onclick="toggleFavorite(this, '2510.08789v2', 'Q-Router: Agentic Video Quality Assessment with Expert Model Routing and Artifact Localization')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Shuo Xing, Soumik Dey, Mingyang Wu, Ashirbad Mishra, Naveen Ravipati, Binbin Li, Hansi Wu, Zhengzhong Tu

**分类**: cs.CV

**发布日期**: 2025-10-09 (更新: 2025-10-13)

---

## 💡 一句话要点

**Q-Router：基于专家模型路由和伪影定位的Agentic视频质量评估**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频质量评估` `Agentic框架` `视觉-语言模型` `模型路由` `伪影定位`

## 📋 核心要点

1. 现有VQA模型在不同视频内容和任务上泛化性差，可解释性有限，且难以扩展到新的应用场景。
2. Q-Router利用视觉-语言模型作为路由器，动态选择并集成不同的专家模型，以适应不同的视频内容和任务。
3. 实验表明，Q-Router在多个VQA基准测试中达到或超过了SOTA水平，并显著提升了泛化性和可解释性。

## 📝 摘要（中文）

视频质量评估（VQA）是一项基础的计算机视觉任务，旨在预测给定视频的感知质量，使其与人类的判断相符。现有的VQA模型虽然性能良好，但通常通过直接的分数监督进行训练，存在以下问题：（1）在用户生成内容（UGC）、短视频和AI生成内容（AIGC）等不同内容和任务上的泛化能力较差；（2）可解释性有限；（3）难以扩展到新的用例或内容类型。我们提出了Q-Router，一个用于通用VQA的agentic框架，具有多层模型路由系统。Q-Router集成了各种专家模型，并采用视觉-语言模型（VLM）作为实时路由器，动态推理并集成最合适的专家，这取决于输入视频的语义。我们构建了一个基于计算预算的多层路由系统，其中最重的层涉及特定的时空伪影定位，以提高可解释性。这种agentic设计使Q-Router能够结合专业专家的互补优势，在跨异构视频源和任务中实现灵活性和鲁棒性，从而提供一致的性能。大量的实验表明，Q-Router在各种基准测试中与最先进的VQA模型相匹配或超越，同时大大提高了泛化性和可解释性。此外，Q-Router在基于质量的问答基准测试Q-Bench-Video上表现出色，突显了其作为下一代VQA系统基础的潜力。最后，我们展示了Q-Router能够定位时空伪影，显示出作为后训练视频生成模型奖励函数的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决现有视频质量评估（VQA）模型在泛化性、可解释性和可扩展性方面的不足。现有模型通常难以适应用户生成内容、短视频和AI生成内容等多样化的视频类型，并且缺乏对模型决策过程的解释，限制了其在新的应用场景中的应用。

**核心思路**：论文的核心思路是构建一个agentic的VQA框架，该框架能够根据输入视频的语义动态地选择和集成不同的专家模型。通过引入视觉-语言模型（VLM）作为路由器，Q-Router能够实时推理并选择最适合当前视频内容的专家模型，从而提高泛化能力和性能。

**技术框架**：Q-Router的整体架构包含一个多层模型路由系统。第一层根据计算预算选择不同的路由策略。最高层级的路由策略会利用VLM进行时空伪影定位，以提高可解释性。不同的专家模型负责处理不同类型的视频质量问题。VLM路由器根据输入视频的语义信息，动态地选择并集成这些专家模型的输出，最终得到视频质量评估结果。

**关键创新**：Q-Router的关键创新在于其agentic设计和多层模型路由系统。通过将VLM作为路由器，Q-Router能够根据视频内容动态地选择合适的专家模型，从而提高了模型的泛化能力和适应性。此外，时空伪影定位模块提高了模型的可解释性，使其能够识别视频中存在的质量问题。

**关键设计**：Q-Router的关键设计包括VLM路由器的选择和训练、专家模型的构建和集成、以及多层路由系统的设计。VLM路由器需要能够准确地理解视频内容并选择合适的专家模型。专家模型需要覆盖各种视频质量问题，并能够提供准确的评估结果。多层路由系统需要根据计算预算和性能要求进行优化。

## 📊 实验亮点

Q-Router在多个VQA基准测试中取得了与SOTA模型相当或更优的性能，同时显著提高了泛化性和可解释性。在Q-Bench-Video基准测试中表现出色，验证了其在质量问答方面的潜力。此外，Q-Router能够有效地定位视频中的时空伪影，为视频质量分析提供了新的手段。

## 🎯 应用场景

Q-Router可应用于视频监控、视频会议、在线视频平台等领域，用于评估视频质量、优化视频编码和传输策略，并提高用户体验。此外，Q-Router还可以作为视频生成模型的奖励函数，用于指导生成更高质量的视频内容。该研究有望推动下一代VQA系统的发展。

## 📄 摘要（原文）

> Video quality assessment (VQA) is a fundamental computer vision task that aims to predict the perceptual quality of a given video in alignment with human judgments. Existing performant VQA models trained with direct score supervision suffer from (1) poor generalization across diverse content and tasks, ranging from user-generated content (UGC), short-form videos, to AI-generated content (AIGC), (2) limited interpretability, and (3) lack of extensibility to novel use cases or content types. We propose Q-Router, an agentic framework for universal VQA with a multi-tier model routing system. Q-Router integrates a diverse set of expert models and employs vision--language models (VLMs) as real-time routers that dynamically reason and then ensemble the most appropriate experts conditioned on the input video semantics. We build a multi-tiered routing system based on the computing budget, with the heaviest tier involving a specific spatiotemporal artifacts localization for interpretability. This agentic design enables Q-Router to combine the complementary strengths of specialized experts, achieving both flexibility and robustness in delivering consistent performance across heterogeneous video sources and tasks. Extensive experiments demonstrate that Q-Router matches or surpasses state-of-the-art VQA models on a variety of benchmarks, while substantially improving generalization and interpretability. Moreover, Q-Router excels on the quality-based question answering benchmark, Q-Bench-Video, highlighting its promise as a foundation for next-generation VQA systems. Finally, we show that Q-Router capably localizes spatiotemporal artifacts, showing potential as a reward function for post-training video generation models.

