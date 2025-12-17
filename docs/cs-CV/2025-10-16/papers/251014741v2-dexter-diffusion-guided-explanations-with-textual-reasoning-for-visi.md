---
layout: default
title: DEXTER: Diffusion-Guided EXplanations with TExtual Reasoning for Vision Models
---

# DEXTER: Diffusion-Guided EXplanations with TExtual Reasoning for Vision Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14741" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14741v2</a>
  <a href="https://arxiv.org/pdf/2510.14741.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14741v2" onclick="toggleFavorite(this, '2510.14741v2', 'DEXTER: Diffusion-Guided EXplanations with TExtual Reasoning for Vision Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simone Carnemolla, Matteo Pennisi, Sarinda Samarasinghe, Giovanni Bellitto, Simone Palazzo, Daniela Giordano, Mubarak Shah, Concetto Spampinato

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-16 (更新: 2025-11-16)

**备注**: Accepted to NeurIPS 2025 (spotlight)

**🔗 代码/项目**: [GITHUB](https://github.com/perceivelab/dexter)

---

## 💡 一句话要点

**DEXTER：利用扩散模型和文本推理实现视觉模型的可解释性，无需数据。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可解释性` `扩散模型` `大型语言模型` `视觉模型` `偏差检测` `数据无关` `模型调试`

## 📋 核心要点

1. 现有模型可解释性方法依赖大量数据和标签，DEXTER旨在解决在缺乏数据的情况下，理解视觉分类器决策过程的难题。
2. DEXTER的核心思想是利用扩散模型生成能激活分类器的图像，再用大语言模型根据这些图像生成自然语言解释。
3. 实验表明，DEXTER在ImageNet等数据集上，能够有效发现并解释分类器的偏差，优于现有方法，且无需真实数据。

## 📝 摘要（中文）

为了构建透明且值得信赖的AI系统，理解和解释机器学习模型的行为至关重要。我们提出了DEXTER，一个无需数据的框架，它利用扩散模型和大型语言模型来生成视觉分类器的全局文本解释。DEXTER通过优化文本提示来合成类条件图像，这些图像能够强烈激活目标分类器。然后，这些合成样本被用于生成详细的自然语言报告，描述类特定的决策模式和偏差。与先前的工作不同，DEXTER无需访问训练数据或真实标签即可实现关于分类器决策过程的自然语言解释。我们通过激活最大化、切片发现和去偏置以及偏差解释这三个任务展示了DEXTER的灵活性，每个任务都说明了其发现视觉分类器内部机制的能力。定量和定性评估（包括用户研究）表明，DEXTER产生准确、可解释的输出。在ImageNet、Waterbirds、CelebA和FairFaces上的实验证实，DEXTER在全局模型解释和类级别偏差报告方面优于现有方法。

## 🔬 方法详解

**问题定义**：现有视觉模型的可解释性方法通常需要访问大量的训练数据和ground-truth标签，这在数据受限或隐私敏感的场景下是不可行的。此外，现有方法在揭示模型潜在偏差和决策模式方面存在局限性。因此，如何无需数据即可理解和解释视觉分类器的行为，并发现其潜在偏差，是一个重要的研究问题。

**核心思路**：DEXTER的核心思路是利用扩散模型生成能够最大程度激活目标分类器的合成图像，然后利用大型语言模型对这些合成图像进行分析，生成自然语言解释。通过优化文本提示来引导扩散模型生成特定类别的图像，这些图像能够揭示分类器对该类别的关键特征的关注点。这种方法避免了对真实数据的依赖，并且能够提供全局性的模型解释。

**技术框架**：DEXTER框架主要包含两个阶段：图像合成阶段和文本解释阶段。在图像合成阶段，通过优化文本提示，使用扩散模型生成类条件图像，这些图像能够最大化目标分类器的激活值。在文本解释阶段，将生成的合成图像输入到大型语言模型中，利用其强大的文本生成能力，生成关于分类器决策模式和偏差的自然语言报告。整个流程无需访问训练数据或ground-truth标签。

**关键创新**：DEXTER的关键创新在于其数据无关性以及利用扩散模型和大型语言模型进行模型解释的结合。与传统的依赖数据的可解释性方法不同，DEXTER无需访问训练数据，从而解决了数据受限场景下的可解释性问题。此外，DEXTER利用扩散模型生成具有代表性的合成图像，并利用大型语言模型生成自然语言解释，从而提供了更全面和易于理解的模型解释。

**关键设计**：在图像合成阶段，使用CLIP模型来衡量生成图像与目标文本提示之间的相似度，并使用分类器的输出作为优化目标，以确保生成的图像能够最大程度地激活分类器。在文本解释阶段，使用预训练的大型语言模型（如GPT-3）来生成自然语言报告，并使用prompt engineering技术来引导语言模型生成更准确和有用的解释。

## 📊 实验亮点

DEXTER在ImageNet、Waterbirds、CelebA和FairFaces等数据集上进行了评估，结果表明DEXTER在全局模型解释和类级别偏差报告方面优于现有方法。用户研究表明，DEXTER生成的解释更准确、更易于理解。例如，在Waterbirds数据集上，DEXTER能够准确地识别出模型对背景（水）的依赖，从而解释了模型在区分鸟类时的偏差。

## 🎯 应用场景

DEXTER可应用于多个领域，包括模型调试、安全关键系统和公平性评估。它可以帮助开发者理解模型的决策过程，发现潜在的偏差和漏洞，从而改进模型的设计和性能。在医疗诊断、自动驾驶等安全关键系统中，DEXTER可以提供可信的解释，增强用户对AI系统的信任。此外，DEXTER还可以用于评估模型的公平性，发现并减轻模型对特定人群的歧视。

## 📄 摘要（原文）

> Understanding and explaining the behavior of machine learning models is essential for building transparent and trustworthy AI systems. We introduce DEXTER, a data-free framework that employs diffusion models and large language models to generate global, textual explanations of visual classifiers. DEXTER operates by optimizing text prompts to synthesize class-conditional images that strongly activate a target classifier. These synthetic samples are then used to elicit detailed natural language reports that describe class-specific decision patterns and biases. Unlike prior work, DEXTER enables natural language explanation about a classifier's decision process without access to training data or ground-truth labels. We demonstrate DEXTER's flexibility across three tasks-activation maximization, slice discovery and debiasing, and bias explanation-each illustrating its ability to uncover the internal mechanisms of visual classifiers. Quantitative and qualitative evaluations, including a user study, show that DEXTER produces accurate, interpretable outputs. Experiments on ImageNet, Waterbirds, CelebA, and FairFaces confirm that DEXTER outperforms existing approaches in global model explanation and class-level bias reporting. Code is available at https://github.com/perceivelab/dexter.

