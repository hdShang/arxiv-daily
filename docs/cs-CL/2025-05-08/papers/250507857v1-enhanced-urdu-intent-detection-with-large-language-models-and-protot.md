---
layout: default
title: Enhanced Urdu Intent Detection with Large Language Models and Prototype-Informed Predictive Pipelines
---

# Enhanced Urdu Intent Detection with Large Language Models and Prototype-Informed Predictive Pipelines

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07857" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07857v1</a>
  <a href="https://arxiv.org/pdf/2505.07857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07857v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07857v1', 'Enhanced Urdu Intent Detection with Large Language Models and Prototype-Informed Predictive Pipelines')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Faiza Hassan, Summra Saleem, Kashif Javed, Muhammad Nabeel Asim, Abdur Rehman, Andreas Dengel

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-08

**备注**: 42 pages, 10 figures(including 6 graphs)

---

## 💡 一句话要点

**提出基于大语言模型的原型信息预测管道以提升乌尔都语意图检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `意图检测` `乌尔都语` `对比学习` `大语言模型` `原型信息` `机器学习` `自然语言处理`

## 📋 核心要点

1. 现有的意图检测方法在乌尔都语领域发展不足，缺乏有效的少量学习策略，主要集中于已知类别的预测。
2. 本文提出了一种创新的对比学习方法，通过未标记的乌尔都语数据重新训练预训练语言模型，增强其表示学习能力。
3. 在ATIS和Web Queries两个数据集上，提出的LLMPIA框架在多种实验设置下均取得了显著的F1-Score提升，尤其在Web Queries数据集上超越了现有最优预测器。

## 📝 摘要（中文）

尽管多种意图检测预测器已为英语、中文和法语等语言开发，但乌尔都语作为第十大语言在这一领域仍显不足。现有的意图检测方法主要依赖于少量学习和已知类别的预测，而乌尔都语缺乏基于少量学习的意图检测预测器。为此，本文提出了一种独特的对比学习方法，利用未标记的乌尔都语数据重新训练预训练语言模型，从而增强其在下游意图检测任务中的表示学习能力。最终，结合预训练大语言模型与原型信息注意机制，构建了一个全面的端到端意图检测管道。该框架在两个公共基准数据集上进行了评估，取得了显著的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决乌尔都语意图检测领域的不足，尤其是缺乏基于少量学习的意图检测预测器，现有方法主要集中于已知类别的预测，限制了模型的泛化能力。

**核心思路**：论文提出了一种对比学习的方法，通过利用未标记的乌尔都语数据对预训练语言模型进行再训练，从而提升其在意图检测任务中的表现。该方法旨在通过增强模型的表示能力，克服传统方法的局限性。

**技术框架**：整体架构包括数据预处理、对比学习模块、预训练模型再训练和原型信息注意机制。通过这些模块的协同工作，形成一个端到端的意图检测管道。

**关键创新**：最重要的技术创新在于结合了对比学习与原型信息注意机制，形成了LLMPIA意图检测框架。这一方法与传统的仅依赖于已知类别的预测方法有本质区别，能够有效利用未标记数据。

**关键设计**：在模型训练中，采用了特定的损失函数以优化对比学习过程，并设计了多种相似性计算方法，以增强模型对不同类别的区分能力。

## 📊 实验亮点

在ATIS数据集上，LLMPIA在4-way 1 shot和4-way 5 shot实验设置下分别达到了83.28%和98.25%的F1-Score；在Web Queries数据集上，分别达到了76.23%和84.42%的F1-Score。此外，在Web Queries数据集的同类训练和测试设置下，LLMPIA超越了现有最优预测器53.55%的F1-Score，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能客服系统和多语言交互平台等。通过提升乌尔都语的意图检测能力，可以更好地服务于乌尔都语用户，推动相关技术在多语言环境中的应用与普及，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Multifarious intent detection predictors are developed for different languages, including English, Chinese and French, however, the field remains underdeveloped for Urdu, the 10th most spoken language. In the realm of well-known languages, intent detection predictors utilize the strategy of few-shot learning and prediction of unseen classes based on the model training on seen classes. However, Urdu language lacks few-shot strategy based intent detection predictors and traditional predictors are focused on prediction of the same classes which models have seen in the train set. To empower Urdu language specific intent detection, this introduces a unique contrastive learning approach that leverages unlabeled Urdu data to re-train pre-trained language models. This re-training empowers LLMs representation learning for the downstream intent detection task. Finally, it reaps the combined potential of pre-trained LLMs and the prototype-informed attention mechanism to create a comprehensive end-to-end LLMPIA intent detection pipeline. Under the paradigm of proposed predictive pipeline, it explores the potential of 6 distinct language models and 13 distinct similarity computation methods. The proposed framework is evaluated on 2 public benchmark datasets, namely ATIS encompassing 5836 samples and Web Queries having 8519 samples. Across ATIS dataset under 4-way 1 shot and 4-way 5 shot experimental settings LLMPIA achieved 83.28% and 98.25% F1-Score and on Web Queries dataset produced 76.23% and 84.42% F1-Score, respectively. In an additional case study on the Web Queries dataset under same classes train and test set settings, LLMPIA outperformed state-of-the-art predictor by 53.55% F1-Score.

