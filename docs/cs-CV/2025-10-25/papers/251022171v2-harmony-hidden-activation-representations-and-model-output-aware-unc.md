---
layout: default
title: HARMONY: Hidden Activation Representations and Model Output-Aware Uncertainty Estimation for Vision-Language Models
---

# HARMONY: Hidden Activation Representations and Model Output-Aware Uncertainty Estimation for Vision-Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22171" target="_blank" class="toolbar-btn">arXiv: 2510.22171v2</a>
    <a href="https://arxiv.org/pdf/2510.22171.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22171v2" 
            onclick="toggleFavorite(this, '2510.22171v2', 'HARMONY: Hidden Activation Representations and Model Output-Aware Uncertainty Estimation for Vision-Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Erum Mushtaq, Zalan Fabian, Yavuz Faruk Bakman, Anil Ramakrishna, Mahdi Soltanolkotabi, Salman Avestimehr

**分类**: cs.CV

**发布日期**: 2025-10-25 (更新: 2025-11-28)

---

## 💡 一句话要点

**提出HARMONY，利用隐层激活和模型输出来提升视觉-语言模型的不确定性估计。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `不确定性估计` `视觉-语言模型` `隐层激活表示` `多模态融合` `VQA` `可靠性` `深度学习`

## 📋 核心要点

1. 现有基于概率的UE方法难以捕捉token间复杂关系，且易受语言先验影响，导致不确定性估计不准确。
2. HARMONY整合文本、输出不确定性及隐层视觉理解置信度，通过输入映射和架构设计有效利用多模态对齐信号。
3. 实验表明，HARMONY在多个VQA基准和VLM上优于现有方法，AUROC提升高达5%，PRR提升高达9%。

## 📝 摘要（中文）

不确定性估计（UE）在量化模型输出的可靠性以及通过选择性预测减少不安全生成方面起着核心作用。目前，大多数基于概率的UE方法依赖于预定义的函数，使用诸如长度归一化等启发式方法将token概率聚合为单个UE分数。然而，这些方法通常无法捕捉到生成的token之间复杂的关系，并且难以识别受语言先验影响的偏差概率。另一项研究使用模型的隐藏表示，并训练简单的MLP架构来预测不确定性。但是，这样的函数通常会丢失复杂的token间依赖关系。虽然先前的工作表明隐藏表示编码了多模态对齐信号，但我们的工作表明，这些信号的处理方式对UE性能有重大影响。为了有效地利用这些信号来识别token间依赖关系以及视觉-文本对齐，我们提出HARMONY（隐层激活表示和模型输出感知的不确定性估计），这是一种新颖的UE框架，它通过适当的输入映射设计和合适的架构选择，在token级别整合生成的token（“文本”）、模型在输出端的不确定性得分（“MaxProb”）及其对图像视觉理解和生成token的内部置信度（由“隐藏表示”捕获）。我们在两个开放式VQA基准测试（A-OKVQA和VizWiz）以及四个最先进的VLM（LLaVA-7B、LLaVA-13B、InstructBLIP和Qwen-VL）上的实验表明，HARMONY始终与现有方法相匹配或超越，在AUROC中实现了高达5％的改进，在PRR中实现了9％的改进。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言模型（VLM）中不确定性估计（UE）不准确的问题。现有方法，如基于概率的方法和基于隐层表示的方法，都存在局限性。基于概率的方法无法捕捉token间的复杂依赖关系，且易受语言先验的影响。基于隐层表示的方法则容易丢失token间的细粒度信息。这些问题导致VLM在实际应用中可靠性降低，尤其是在需要高置信度的场景下。

**核心思路**：HARMONY的核心思路是将模型的输出不确定性、生成的文本信息以及模型内部对视觉理解的置信度进行整合，从而更全面地评估模型的不确定性。通过分析隐层激活表示，捕捉token间的依赖关系和视觉-文本对齐信息，克服现有方法的局限性。这种多维度信息融合的方式能够更准确地反映模型对答案的真实置信水平。

**技术框架**：HARMONY框架主要包含以下几个模块：1) **输入映射模块**：将生成的文本token、模型输出的概率（MaxProb）以及隐层激活表示进行映射，形成统一的输入表示。2) **不确定性预测模块**：使用一个神经网络（例如，MLP或Transformer）来处理输入表示，预测每个token的不确定性得分。3) **聚合模块**：将每个token的不确定性得分聚合为一个整体的不确定性度量，用于评估模型输出的可靠性。整体流程是，给定一个视觉-语言输入，VLM生成文本输出，同时提取隐层激活表示和输出概率，然后通过HARMONY框架预测不确定性。

**关键创新**：HARMONY的关键创新在于其综合利用了模型输出、生成文本和隐层激活表示。与仅依赖于输出概率或隐层表示的方法不同，HARMONY能够更全面地捕捉模型的不确定性来源。此外，HARMONY通过精心设计的输入映射和网络结构，有效地利用了隐层激活表示中蕴含的视觉-文本对齐信息和token间依赖关系。

**关键设计**：HARMONY的关键设计包括：1) **输入映射**：如何将文本token、MaxProb和隐层激活表示有效地融合为一个输入向量是关键。论文可能采用了拼接、加权平均或其他更复杂的映射方法。2) **网络结构**：用于预测不确定性的神经网络结构的选择也很重要。论文可能尝试了不同的网络结构，如MLP、Transformer等，并根据实验结果选择了最优的结构。3) **损失函数**：用于训练不确定性预测模型的损失函数的设计也很重要。论文可能采用了二元交叉熵损失或其他适用于不确定性估计的损失函数。

## 📊 实验亮点

实验结果表明，HARMONY在A-OKVQA和VizWiz两个VQA基准测试上，以及LLaVA-7B、LLaVA-13B、InstructBLIP和Qwen-VL四个VLM上均取得了显著的性能提升。具体而言，HARMONY在AUROC指标上实现了高达5%的改进，在PRR指标上实现了高达9%的改进，证明了其在不确定性估计方面的有效性。

## 🎯 应用场景

HARMONY可应用于各种需要高可靠性的视觉-语言任务，例如自动驾驶、医疗诊断和智能客服。通过提供可靠的不确定性估计，HARMONY可以帮助系统识别潜在的错误预测，从而避免安全风险和提高决策质量。未来，HARMONY可以进一步扩展到其他多模态任务和模型，提升AI系统的整体可靠性和安全性。

## 📄 摘要（原文）

> Uncertainty Estimation (UE) plays a central role in quantifying the reliability of model outputs and reducing unsafe generations via selective prediction. In this regard, most existing probability-based UE approaches rely on predefined functions, aggregating token probabilities into a single UE score using heuristics such as length-normalization. However, these methods often fail to capture the complex relationships between generated tokens and struggle to identify biased probabilities often influenced by \textbf{language priors}. Another line of research uses hidden representations of the model and trains simple MLP architectures to predict uncertainty. However, such functions often lose the intricate \textbf{ inter-token dependencies}. While prior works show that hidden representations encode multimodal alignment signals, our work demonstrates that how these signals are processed has a significant impact on the UE performance. To effectively leverage these signals to identify inter-token dependencies, and vision-text alignment, we propose \textbf{HARMONY} (Hidden Activation Representations and Model Output-Aware Uncertainty Estimation for Vision-Language Models), a novel UE framework that integrates generated tokens ('text'), model's uncertainty score at the output ('MaxProb'), and its internal belief on the visual understanding of the image and the generated token (captured by 'hidden representations') at token level via appropriate input mapping design and suitable architecture choice. Our experimental experiments across two open-ended VQA benchmarks (A-OKVQA, and VizWiz) and four state-of-the-art VLMs (LLaVA-7B, LLaVA-13B, InstructBLIP, and Qwen-VL) show that HARMONY consistently matches or surpasses existing approaches, achieving up to 5\% improvement in AUROC and 9\% in PRR.

