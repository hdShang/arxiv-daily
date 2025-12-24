---
layout: default
title: "CoCoTen: Detecting Adversarial Inputs to Large Language Models through Latent Space Features of Contextual Co-occurrence Tensors"
---

# CoCoTen: Detecting Adversarial Inputs to Large Language Models through Latent Space Features of Contextual Co-occurrence Tensors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02997" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02997v3</a>
  <a href="https://arxiv.org/pdf/2508.02997.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02997v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02997v3', 'CoCoTen: Detecting Adversarial Inputs to Large Language Models through Latent Space Features of Contextual Co-occurrence Tensors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sri Durga Sai Sowmya Kadali, Evangelos E. Papalexakis

**分类**: cs.CL

**发布日期**: 2025-08-05 (更新: 2025-08-27)

**DOI**: [10.1145/3746252.3760886](https://doi.org/10.1145/3746252.3760886)

---

## 💡 一句话要点

**提出CoCoTen以检测大型语言模型的对抗输入**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗性输入` `大型语言模型` `上下文共现矩阵` `安全性检测` `机器学习` `潜在空间特征` `数据稀缺环境`

## 📋 核心要点

1. 现有大型语言模型在复杂性和不透明性上存在不足，易受到越狱攻击，导致安全隐患。
2. 本文提出了一种基于上下文共现矩阵潜在空间特征的新方法，旨在有效识别对抗性输入。
3. 实验结果显示，该方法在使用极少标记数据的情况下，F1分数达到0.83，显著提升检测性能。

## 📝 摘要（中文）

大型语言模型（LLMs）的广泛应用标志着研究和实践的重大进展。然而，其复杂性和难以理解的特性使其容易受到攻击，尤其是旨在产生有害响应的越狱攻击。为应对这些威胁，开发强大的检测方法对于LLMs的安全可靠使用至关重要。本文研究了这一检测问题，利用上下文共现矩阵的潜在空间特征，提出了一种新方法，有效识别对抗性和越狱提示。评估结果显示，该方法在仅使用0.5%的标记提示的情况下，获得了0.83的F1分数，比基线提高了96.6%。这一结果突显了我们学习模式的强大，尤其是在标记数据稀缺的情况下。我们的检测方法还显著加快了速度，相较于基线模型提升幅度在2.3到128.4倍之间。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型对抗输入的检测问题。现有方法在数据稀缺环境下表现不佳，难以有效识别对抗性提示。

**核心思路**：我们提出利用上下文共现矩阵的潜在空间特征，通过学习数据的共现模式来识别对抗性输入，特别是在标记数据稀缺的情况下。

**技术框架**：整体架构包括数据预处理、上下文共现矩阵构建、潜在空间特征提取和对抗输入检测四个主要模块。数据预处理阶段负责清洗和准备输入数据，构建共现矩阵后提取潜在特征，最后进行分类以识别对抗性输入。

**关键创新**：本研究的主要创新在于利用上下文共现矩阵的潜在空间特征进行对抗输入检测，这一方法在数据稀缺情况下表现优异，与传统方法相比具有本质区别。

**关键设计**：我们在模型中设置了特定的超参数，以优化共现矩阵的构建和特征提取过程，采用了适应性损失函数以提高模型的鲁棒性，确保在不同数据条件下的有效性。

## 📊 实验亮点

实验结果表明，所提出的CoCoTen方法在仅使用0.5%的标记提示的情况下，达到了0.83的F1分数，相较于基线模型提高了96.6%。此外，该方法的速度提升显著，检测速度比基线快2.3到128.4倍，展示了其高效性和实用性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在安全性要求高的领域，如金融、医疗和社交媒体等。通过有效检测对抗性输入，可以显著提升大型语言模型的安全性和可靠性，防止潜在的恶意攻击，保护用户和系统的安全。未来，该方法还可扩展至其他类型的模型和应用场景，进一步推动人工智能的安全发展。

## 📄 摘要（原文）

> The widespread use of Large Language Models (LLMs) in many applications marks a significant advance in research and practice. However, their complexity and hard-to-understand nature make them vulnerable to attacks, especially jailbreaks designed to produce harmful responses. To counter these threats, developing strong detection methods is essential for the safe and reliable use of LLMs. This paper studies this detection problem using the Contextual Co-occurrence Matrix, a structure recognized for its efficacy in data-scarce environments. We propose a novel method leveraging the latent space characteristics of Contextual Co-occurrence Matrices and Tensors for the effective identification of adversarial and jailbreak prompts. Our evaluations show that this approach achieves a notable F1 score of 0.83 using only 0.5% of labeled prompts, which is a 96.6% improvement over baselines. This result highlights the strength of our learned patterns, especially when labeled data is scarce. Our method is also significantly faster, speedup ranging from 2.3 to 128.4 times compared to the baseline models.

