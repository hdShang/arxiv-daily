---
layout: default
title: "AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees"
---

# AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01268" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01268v4</a>
  <a href="https://arxiv.org/pdf/2510.01268.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01268v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01268v4', 'AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyi Zhou, Jin Zhu, Pingfan Su, Kai Ye, Ying Yang, Shakeel A O B Gavioli-Akilagun, Chengchun Shi

**分类**: cs.CL, cs.AI, cs.LG, stat.ML

**发布日期**: 2025-09-29 (更新: 2025-12-07)

**备注**: Accepted by NeurIPS2025

**🔗 代码/项目**: [GITHUB](https://github.com/Mamba413/AdaDetectGPT)

---

## 💡 一句话要点

**AdaDetectGPT：利用统计保证自适应检测LLM生成文本**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM文本检测` `自适应学习` `Witness函数` `统计保证` `自然语言处理`

## 📋 核心要点

1. 现有基于logits的LLM文本检测器仅依赖对数概率，可能无法达到最优的检测效果。
2. AdaDetectGPT通过自适应学习witness函数，增强了基于logits的检测器性能，并提供统计保证。
3. 实验结果表明，AdaDetectGPT在多种数据集和LLM组合中显著优于现有方法，最高提升达37%。

## 📝 摘要（中文）

本文研究了判断一段文本是由人类还是由大型语言模型（LLM）创作的问题。现有的基于logits的最先进检测器利用从给定源LLM评估的观察文本的对数概率导出的统计数据。然而，仅仅依赖对数概率可能并非最优。为此，我们引入了AdaDetectGPT——一种新颖的分类器，它从训练数据中自适应地学习一个witness函数，以提高基于logits的检测器的性能。我们提供了关于其真正率、假正率、真负率和假负率的统计保证。大量的数值研究表明，AdaDetectGPT几乎一致地改进了各种数据集和LLM组合中的最先进方法，改进幅度可达37%。我们的方法的Python实现可在https://github.com/Mamba413/AdaDetectGPT获得。

## 🔬 方法详解

**问题定义**：论文旨在解决区分文本是由人类撰写还是由大型语言模型（LLM）生成的问题。现有方法主要依赖于LLM输出的logits（对数概率）进行判断，但这种方法可能存在局限性，无法充分利用文本中的信息，导致检测准确率不高。

**核心思路**：AdaDetectGPT的核心思路是自适应地学习一个“witness函数”，该函数能够更有效地捕捉人类生成文本和LLM生成文本之间的差异。通过训练，该函数可以增强基于logits的检测器的性能，从而提高区分两种文本的准确性。

**技术框架**：AdaDetectGPT的整体框架包含以下几个主要阶段：1. 使用现有的基于logits的检测器提取文本的特征；2. 利用训练数据，自适应地学习一个witness函数，该函数能够区分人类生成文本和LLM生成文本；3. 将witness函数的输出与基于logits的检测器的输出相结合，形成最终的分类结果。该框架的关键在于witness函数的学习过程。

**关键创新**：AdaDetectGPT的关键创新在于自适应学习witness函数。与直接使用logits相比，witness函数能够从训练数据中学习到更具区分性的特征，从而提高检测的准确性。此外，论文还提供了关于检测器性能（真正率、假正率等）的统计保证，使得该方法在实际应用中更具可靠性。

**关键设计**：关于witness函数的具体形式和学习方法，论文中可能涉及具体的参数设置、损失函数以及网络结构等细节。这些细节的设计旨在最大化witness函数区分人类生成文本和LLM生成文本的能力。具体的技术细节需要在论文原文中查找。

## 📊 实验亮点

实验结果表明，AdaDetectGPT在各种数据集和LLM组合中均优于现有最先进的方法。在某些情况下，AdaDetectGPT的性能提升高达37%。这些结果验证了AdaDetectGPT自适应学习witness函数的有效性，并证明了其在LLM文本检测任务中的优越性。

## 🎯 应用场景

AdaDetectGPT可应用于内容审核、学术诚信检测、虚假信息识别等领域。通过准确区分人类撰写和LLM生成的文本，有助于维护网络内容质量，防止学术不端行为，并减少虚假信息传播。该研究的成果对于构建更安全、可信赖的在线环境具有重要意义。

## 📄 摘要（原文）

> We study the problem of determining whether a piece of text has been authored by a human or by a large language model (LLM). Existing state of the art logits-based detectors make use of statistics derived from the log-probability of the observed text evaluated using the distribution function of a given source LLM. However, relying solely on log probabilities can be sub-optimal. In response, we introduce AdaDetectGPT -- a novel classifier that adaptively learns a witness function from training data to enhance the performance of logits-based detectors. We provide statistical guarantees on its true positive rate, false positive rate, true negative rate and false negative rate. Extensive numerical studies show AdaDetectGPT nearly uniformly improves the state-of-the-art method in various combination of datasets and LLMs, and the improvement can reach up to 37\%. A python implementation of our method is available at https://github.com/Mamba413/AdaDetectGPT.

