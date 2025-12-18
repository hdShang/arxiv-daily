---
layout: default
title: Generative Universal Verifier as Multimodal Meta-Reasoner
---

# Generative Universal Verifier as Multimodal Meta-Reasoner

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13804" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13804v1</a>
  <a href="https://arxiv.org/pdf/2510.13804.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13804v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13804v1', 'Generative Universal Verifier as Multimodal Meta-Reasoner')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinchen Zhang, Xiaoying Zhang, Youbin Wu, Yanbin Cao, Renrui Zhang, Ruihang Chu, Ling Yang, Yujiu Yang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-15

---

## 💡 一句话要点

**提出生成式通用验证器，赋能多模态模型进行视觉结果反思与优化。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉验证` `生成式模型` `测试时优化` `图像生成` `图像编辑` `视觉-语言模型`

## 📋 核心要点

1. 现有视觉-语言模型在多模态推理中，缺乏对视觉结果的可靠验证能力，导致性能受限。
2. 提出生成式通用验证器，通过反思和优化视觉结果，提升多模态推理和生成能力。
3. 构建ViVerBench基准，训练OmniVerifier-7B，并在图像生成和编辑任务上取得显著提升。

## 📝 摘要（中文）

本文提出了一种名为生成式通用验证器（Generative Universal Verifier）的新概念和插件，旨在为视觉-语言模型和统一多模态模型提供下一代多模态推理能力，使其能够在推理和生成过程中对视觉结果进行反思和优化。主要贡献包括：构建了ViVerBench，一个包含16类关键任务的综合基准，用于评估多模态推理中的视觉结果。结果表明，现有VLM在这些任务上表现不佳，与人类水平的视觉验证能力存在显著差距。设计了两种自动流水线来构建大规模视觉验证数据，并训练了OmniVerifier-7B，这是第一个用于通用视觉验证的全能生成式验证器，并在ViVerBench上取得了显著提升（+8.3）。通过训练，识别了视觉验证中的三个原子能力，并展示了它们如何泛化和协同作用。提出了OmniVerifier-TTS，一种顺序测试时缩放范式，利用通用验证器来桥接统一模型中的图像生成和编辑，通过迭代细粒度优化来提高生成能力的上限。除了生成之外，还将通用验证器扩展到更广泛的世界建模交错推理场景。实验表明，OmniVerifier-TTS在T2I-ReasonBench（+3.7）和GenEval++（+4.3）上取得了改进，优于现有的并行测试时缩放方法，如Best-of-N。通过赋予多模态推理可靠的视觉验证能力，OmniVerifier推动了生成过程中可靠的反思和可扩展的测试时优化，标志着朝着更值得信赖和可控的下一代推理系统迈出了一步。

## 🔬 方法详解

**问题定义**：现有的视觉-语言模型（VLM）在进行多模态推理时，往往缺乏对生成或理解的视觉内容进行有效验证的能力。这导致模型容易产生与现实不符或逻辑错误的结论，尤其是在需要精细视觉理解的任务中。现有方法通常依赖于间接的语言监督或简单的视觉特征匹配，难以实现可靠的视觉验证。

**核心思路**：本文的核心思路是引入一个独立的、可学习的“视觉验证器”，该验证器能够像人类一样，对视觉内容进行细致的分析和判断，从而对VLM的推理过程进行反思和优化。通过训练该验证器，使其具备通用的视觉验证能力，可以显著提升VLM在各种多模态任务中的表现。

**技术框架**：OmniVerifier-TTS的整体框架包含以下几个主要模块：1) **视觉验证器（OmniVerifier）**：这是一个预训练的生成式模型，负责接收图像和文本描述，并生成对图像内容是否符合描述的判断。2) **图像生成/编辑模型**：这是需要进行优化的目标模型，例如文本到图像生成模型。3) **测试时缩放（Test-Time Scaling）**：OmniVerifier-TTS采用顺序测试时缩放范式，即迭代地使用视觉验证器对生成/编辑的图像进行评估，并根据评估结果对模型进行微调，从而逐步提升生成质量。

**关键创新**：本文最重要的技术创新点在于提出了“生成式通用验证器”的概念，并设计了相应的训练方法和测试时优化策略。与以往的视觉验证方法相比，OmniVerifier具有更强的通用性和可解释性，能够处理各种复杂的视觉验证任务。此外，OmniVerifier-TTS的顺序测试时缩放范式也优于传统的并行方法，能够更有效地利用验证器的反馈信息。

**关键设计**：在训练OmniVerifier时，采用了两种自动流水线来构建大规模的视觉验证数据集。这些流水线能够生成包含各种视觉错误和逻辑矛盾的图像-文本对，从而使验证器能够学习到鲁棒的视觉验证能力。在OmniVerifier-TTS中，使用了基于梯度的微调方法，根据验证器的输出结果对图像生成/编辑模型的参数进行迭代更新。具体的损失函数设计旨在最大化验证器对生成图像的置信度，并同时保持生成图像与原始文本描述的一致性。

## 📊 实验亮点

实验结果表明，OmniVerifier-7B在ViVerBench基准上取得了显著提升（+8.3），证明了其强大的通用视觉验证能力。OmniVerifier-TTS在T2I-ReasonBench（+3.7）和GenEval++（+4.3）上优于现有的并行测试时缩放方法，表明其能够有效提升图像生成和编辑质量。

## 🎯 应用场景

该研究成果可广泛应用于图像生成、图像编辑、视觉问答、机器人导航等领域。通过赋予AI系统可靠的视觉验证能力，可以提升其在复杂环境中的适应性和决策能力，使其能够更好地服务于人类生活和生产。

## 📄 摘要（原文）

> We introduce Generative Universal Verifier, a novel concept and plugin designed for next-generation multimodal reasoning in vision-language models and unified multimodal models, providing the fundamental capability of reflection and refinement on visual outcomes during the reasoning and generation process. This work makes three main contributions: (1) We build ViVerBench, a comprehensive benchmark spanning 16 categories of critical tasks for evaluating visual outcomes in multimodal reasoning. Results show that existing VLMs consistently underperform across these tasks, underscoring a substantial gap from human-level capability in reliable visual verification. (2) We design two automated pipelines to construct large-scale visual verification data and train OmniVerifier-7B, the first omni-capable generative verifier trained for universal visual verification and achieves notable gains on ViVerBench(+8.3). Through training, we identify three atomic capabilities in visual verification and demonstrate how they generalize and interact synergistically. (3) We propose OmniVerifier-TTS, a sequential test-time scaling paradigm that leverages the universal verifier to bridge image generation and editing within unified models, enhancing the upper bound of generative ability through iterative fine-grained optimization. Beyond generation, we extend universal verifier to broader world-modeling interleaved reasoning scenarios. Empirically, OmniVerifier-TTS achieves improvements on T2I-ReasonBench(+3.7), and GenEval++(+4.3), outperforming existing parallel test-time scaling methods, such as Best-of-N. By endowing multimodal reasoning with reliable visual verification, OmniVerifier advances both reliable reflection during generation and scalable test-time refinement, marking a step toward more trustworthy and controllable next-generation reasoning systems.

