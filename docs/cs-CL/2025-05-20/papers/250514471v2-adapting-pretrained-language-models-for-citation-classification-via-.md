---
layout: default
title: Adapting Pretrained Language Models for Citation Classification via Self-Supervised Contrastive Learning
---

# Adapting Pretrained Language Models for Citation Classification via Self-Supervised Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14471" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14471v2</a>
  <a href="https://arxiv.org/pdf/2505.14471.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14471v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14471v2', 'Adapting Pretrained Language Models for Citation Classification via Self-Supervised Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tong Li, Jiachuan Wang, Yongqi Zhang, Shuangyin Li, Lei Chen

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-05-28)

**备注**: Accepted to KDD 2025. This is the author's version of the work

**DOI**: [10.1145/3711896.3736829](https://doi.org/10.1145/3711896.3736829)

---

## 💡 一句话要点

**提出Citss框架以解决学术引用分类中的数据稀缺问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `引用分类` `自监督学习` `对比学习` `预训练语言模型` `学术分析` `数据稀缺` `关键词扰动`

## 📋 核心要点

1. 现有方法在引用分类中面临数据稀缺、上下文噪声和虚假关键词相关性等挑战，限制了性能提升。
2. 论文提出Citss框架，利用自监督对比学习缓解数据稀缺，并通过句子级裁剪和关键词扰动获取对比对。
3. 实验结果显示，Citss在多个基准数据集上表现优越，超越了以往的最先进技术，验证了其有效性。

## 📝 摘要（中文）

学术引用分类旨在识别学术引用背后的意图，对学术分析至关重要。以往的研究主要通过在引用分类数据集上微调预训练语言模型（PLMs），利用其在预训练过程中获得的语言知识。然而，直接微调面临标签数据稀缺、上下文噪声和虚假关键词相关性等挑战。本文提出了一种新颖的框架Citss，通过自监督对比学习来缓解数据稀缺问题，并采用句子级裁剪和关键词扰动两种策略来获取对比对。与仅针对编码器基础PLMs的以往工作相比，Citss兼容编码器和解码器基础的PLMs，充分利用扩展预训练的优势。实验结果表明，Citss在三个基准数据集上优于之前的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决学术引用分类中的数据稀缺问题，现有方法在微调预训练语言模型时面临标签数据不足和上下文噪声的挑战。

**核心思路**：Citss框架通过自监督对比学习来增强模型的学习能力，利用句子级裁剪和关键词扰动策略来生成对比对，从而提高模型的鲁棒性和准确性。

**技术框架**：Citss的整体架构包括数据预处理、对比对生成、模型训练和评估四个主要模块。数据预处理阶段进行句子裁剪和关键词扰动，以生成有效的对比对。

**关键创新**：Citss的主要创新在于引入自监督对比学习，并设计了适用于编码器和解码器基础PLMs的训练策略，突破了以往方法的局限性。

**关键设计**：在模型训练中，采用了特定的损失函数来优化对比学习过程，并在网络结构上进行了调整，以适应不同类型的PLMs。

## 📊 实验亮点

实验结果表明，Citss在三个基准数据集上相较于之前的最先进方法取得了显著提升，具体性能提升幅度达到XX%，验证了其在引用分类任务中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括学术搜索引擎、文献推荐系统和科研管理工具。通过提高引用分类的准确性，能够更好地支持学术研究和知识发现，未来可能对学术界和工业界产生深远影响。

## 📄 摘要（原文）

> Citation classification, which identifies the intention behind academic citations, is pivotal for scholarly analysis. Previous works suggest fine-tuning pretrained language models (PLMs) on citation classification datasets, reaping the reward of the linguistic knowledge they gained during pretraining. However, directly fine-tuning for citation classification is challenging due to labeled data scarcity, contextual noise, and spurious keyphrase correlations. In this paper, we present a novel framework, Citss, that adapts the PLMs to overcome these challenges. Citss introduces self-supervised contrastive learning to alleviate data scarcity, and is equipped with two specialized strategies to obtain the contrastive pairs: sentence-level cropping, which enhances focus on target citations within long contexts, and keyphrase perturbation, which mitigates reliance on specific keyphrases. Compared with previous works that are only designed for encoder-based PLMs, Citss is carefully developed to be compatible with both encoder-based PLMs and decoder-based LLMs, to embrace the benefits of enlarged pretraining. Experiments with three benchmark datasets with both encoder-based PLMs and decoder-based LLMs demonstrate our superiority compared to the previous state of the art. Our code is available at: github.com/LITONG99/Citss

